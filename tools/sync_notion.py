#!/usr/bin/env python3
"""Sincroniza o índice de aulas canônicas para a base "Aulas" do Notion.

Espelho SOMENTE-LEITURA do acervo: a fonte de verdade continua sendo
`canonica.md` (invariante 1 do CLAUDE.md). O Notion nunca escreve de volta —
este script é one-way, repo -> Notion.

O que sobe: uma linha por aula aprovada, com metadados + link que abre a aula no
ProfessorDash. O corpo da aula NÃO vai para o Notion (o conhecimento longo fica
no vault; o Notion é camada operacional). O caminho do arquivo no repo fica na
propriedade `Caminho`.

Chave de sincronização: a propriedade `Caminho` (caminho relativo do
canonica.md). Aula que some do manifesto vira órfã e só é arquivada com
`--prune`.

Pré-requisitos:
  1. Criar uma integração interna em https://www.notion.so/my-integrations
  2. Compartilhar as bases "Aulas" e "Projetos" com ela
     (menu ••• da base -> Connections -> nome da integração)
  3. Exportar o token: $env:NOTION_TOKEN = "ntn_..."

Uso:
    python tools/sync_notion.py --dry-run   # mostra o plano, não escreve
    python tools/sync_notion.py --check     # só valida (exit!=0 se divergente)
    python tools/sync_notion.py             # aplica (cria/atualiza)
    python tools/sync_notion.py --prune     # aplica + arquiva órfãs

Exit code 1 se houver divergência em `--check` ou erro na aplicação.
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gerar_manifesto import parse_frontmatter  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
MANIFESTO = RAIZ / "manifesto.json"

API = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

# Bases do workspace "Toni's Brain".
DB_AULAS = "3c28d390f4624692ac1b596621bb3474"
DB_PROJETOS = "74a9a672da854f0eaf176505f9b8db1d"

# Link de cada aula no ProfessorDash. A rota por slug (catalog:aula_detail_slug)
# redireciona para a URL canônica de pk — assim o endereço sai do manifesto sem
# precisar conhecer o banco do portal. Exige login no portal.
PORTAL_BASE = "https://prof.tonicoimbra.com/catalogo/aulas/s/"

# Disciplina do acervo -> nome do projeto na base Projetos.
# Disciplina ausente aqui sobe sem relação (a aula ainda é criada).
PROJETO_DE_DISCIPLINA = {
    "introducao-a-computacao": "1º A — Introdução à computação",
    "analise-e-metodos-para-sistemas": "1º A — Análise e métodos para sistemas",
    "programacao-front-end": "2º A — Programação Front-End",
    "inovacao-tecnologia-e-empreendedorismo": "2º A — Inovação tecnológica e empreendedorismo",
    "analise-e-projeto-de-sistemas": "3º A — Análise e projeto de sistemas",
    "programacao-no-desenvolvimento-de-sistemas": "3º A — Programação no desenvolvimento de sistemas",
    "tcc": "3º A — TCC",
    "inteligencia-artificial": "Inteligência Artificial — acervo",
}

# Pausa entre escritas: a API do Notion limita a ~3 req/s.
PAUSA = 0.35


# --------------------------------------------------------------------------- #
# HTTP
# --------------------------------------------------------------------------- #

def _token() -> str:
    tok = os.environ.get("NOTION_TOKEN", "").strip()
    if not tok:
        raise SystemExit(
            "NOTION_TOKEN ausente. Crie a integracao em "
            "https://www.notion.so/my-integrations, compartilhe as bases "
            "'Aulas' e 'Projetos' com ela e exporte o token."
        )
    return tok


def chamar(metodo: str, caminho: str, corpo: dict | None = None) -> dict:
    """Faz uma chamada à API do Notion e devolve o JSON da resposta."""
    dados = json.dumps(corpo).encode("utf-8") if corpo is not None else None
    req = urllib.request.Request(API + caminho, data=dados, method=metodo)
    req.add_header("Authorization", "Bearer " + _token())
    req.add_header("Notion-Version", NOTION_VERSION)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detalhe = e.read().decode("utf-8", "replace")[:400]
        raise SystemExit(f"[notion {e.code}] {metodo} {caminho}: {detalhe}") from None


def consultar_base(db_id: str) -> list[dict]:
    """Devolve todas as páginas de uma base, paginando até o fim."""
    paginas: list[dict] = []
    cursor = None
    while True:
        corpo = {"page_size": 100}
        if cursor:
            corpo["start_cursor"] = cursor
        resp = chamar("POST", f"/databases/{db_id}/query", corpo)
        paginas.extend(resp.get("results", []))
        if not resp.get("has_more"):
            return paginas
        cursor = resp.get("next_cursor")


# --------------------------------------------------------------------------- #
# Leitura de propriedades do Notion
# --------------------------------------------------------------------------- #

def ler_prop(prop: dict | None):
    """Normaliza uma propriedade do Notion para um valor Python comparável."""
    if not prop:
        return None
    tipo = prop.get("type")
    if tipo in ("title", "rich_text"):
        return "".join(p.get("plain_text", "") for p in prop[tipo]) or None
    if tipo == "number":
        return prop["number"]
    if tipo == "select":
        return prop["select"]["name"] if prop["select"] else None
    if tipo == "date":
        return prop["date"]["start"] if prop["date"] else None
    if tipo == "url":
        return prop["url"]
    if tipo == "relation":
        return [r["id"].replace("-", "") for r in prop["relation"]]
    return None


# --------------------------------------------------------------------------- #
# Estado desejado (repo)
# --------------------------------------------------------------------------- #

def coletar_aulas() -> tuple[list[dict], list[str]]:
    """Lê o manifesto + frontmatters e devolve (aulas, divergencias)."""
    if not MANIFESTO.exists():
        raise SystemExit("manifesto.json nao encontrado. Rode gerar_manifesto.py antes.")

    manifesto = json.loads(MANIFESTO.read_text(encoding="utf-8"))
    serie_de = {d["slug"]: d.get("serie", "") for d in manifesto.get("disciplinas", [])}

    divergencias: list[str] = []
    aulas: list[dict] = []

    for lesson in manifesto.get("lessons", []):
        disc, trilha = lesson["disciplina"], lesson["trilha"]
        pasta = f"{lesson['ordem']:02d}-{lesson['slug']}"
        caminho = f"aulas/{disc}/{trilha}/{pasta}/canonica.md"

        arquivo = RAIZ / caminho
        if not arquivo.exists():
            divergencias.append(f"[ausente] {caminho}: no manifesto mas nao no disco")
            continue

        fm = parse_frontmatter(arquivo.read_text(encoding="utf-8"))
        try:
            versao = int(fm.get("versao", "") or 0) or None
        except ValueError:
            versao = None
            divergencias.append(f"[versao] {caminho}: '{fm.get('versao')}' nao e inteiro")

        aulas.append({
            "caminho": caminho,
            "titulo": lesson["titulo"],
            "disciplina": disc,
            "trilha": trilha,
            "ordem": lesson["ordem"],
            "slug": lesson["slug"],
            "serie": serie_de.get(disc, ""),
            "tema": fm.get("tema", ""),
            "status": lesson["status"],
            "versao": versao,
            "atualizado_em": fm.get("atualizado_em", ""),
            "link": f"{PORTAL_BASE}{lesson['slug']}/",
        })

    return aulas, divergencias


def montar_props(aula: dict, projeto_id: str | None) -> dict:
    """Monta o payload de propriedades da API a partir de uma aula."""
    props: dict = {
        "Name": {"title": [{"text": {"content": aula["titulo"]}}]},
        "Trilha": {"select": {"name": aula["trilha"]}},
        "Ordem": {"number": aula["ordem"]},
        "Status": {"select": {"name": aula["status"]}},
        "Slug": {"rich_text": [{"text": {"content": aula["slug"]}}]},
        "Caminho": {"rich_text": [{"text": {"content": aula["caminho"]}}]},
        "Link": {"url": aula["link"]},
        "Tema": {"rich_text": ([{"text": {"content": aula["tema"]}}] if aula["tema"] else [])},
        "Série": {"select": {"name": aula["serie"]}} if aula["serie"] else {"select": None},
        "Versão": {"number": aula["versao"]},
        "Atualizado em": ({"date": {"start": aula["atualizado_em"]}}
                          if aula["atualizado_em"] else {"date": None}),
        "Disciplina": {"relation": ([{"id": projeto_id}] if projeto_id else [])},
    }
    return props


def valores_desejados(aula: dict, projeto_id: str | None) -> dict:
    """Mesma informação de montar_props, no formato normalizado de ler_prop."""
    return {
        "Name": aula["titulo"],
        "Trilha": aula["trilha"],
        "Ordem": aula["ordem"],
        "Status": aula["status"],
        "Slug": aula["slug"],
        "Caminho": aula["caminho"],
        "Link": aula["link"],
        "Tema": aula["tema"] or None,
        "Série": aula["serie"] or None,
        "Versão": aula["versao"],
        "Atualizado em": aula["atualizado_em"] or None,
        "Disciplina": [projeto_id.replace("-", "")] if projeto_id else [],
    }


# --------------------------------------------------------------------------- #
# Diff + aplicação
# --------------------------------------------------------------------------- #

def planejar(aulas: list[dict]) -> tuple[list, list, list, list[str]]:
    """Compara repo x Notion. Devolve (criar, atualizar, orfas, avisos)."""
    avisos: list[str] = []

    projetos = {}
    for pg in consultar_base(DB_PROJETOS):
        nome = ler_prop(pg["properties"].get("Name"))
        if nome:
            projetos[nome] = pg["id"]

    existentes = {}
    for pg in consultar_base(DB_AULAS):
        chave = ler_prop(pg["properties"].get("Caminho"))
        if chave:
            existentes[chave] = pg

    criar, atualizar = [], []
    for aula in aulas:
        nome_projeto = PROJETO_DE_DISCIPLINA.get(aula["disciplina"])
        projeto_id = projetos.get(nome_projeto) if nome_projeto else None
        if nome_projeto and not projeto_id:
            avisos.append(
                f"[projeto] '{nome_projeto}' nao existe na base Projetos; "
                f"aula '{aula['slug']}' sobe sem disciplina vinculada")

        pagina = existentes.pop(aula["caminho"], None)
        if pagina is None:
            criar.append((aula, projeto_id))
            continue

        desejado = valores_desejados(aula, projeto_id)
        atual = {k: ler_prop(pagina["properties"].get(k)) for k in desejado}
        mudou = [k for k in desejado if desejado[k] != atual[k]]
        if mudou:
            atualizar.append((aula, projeto_id, pagina["id"], mudou))

    orfas = [(c, pg["id"]) for c, pg in existentes.items()]
    return criar, atualizar, orfas, avisos


def aplicar(criar, atualizar, orfas, prune: bool) -> None:
    for aula, projeto_id in criar:
        chamar("POST", "/pages", {
            "parent": {"database_id": DB_AULAS},
            "properties": montar_props(aula, projeto_id),
        })
        print(f"  + {aula['caminho']}")
        time.sleep(PAUSA)

    for aula, projeto_id, page_id, _mudou in atualizar:
        chamar("PATCH", f"/pages/{page_id}",
               {"properties": montar_props(aula, projeto_id)})
        print(f"  ~ {aula['caminho']}")
        time.sleep(PAUSA)

    if prune:
        for caminho, page_id in orfas:
            chamar("PATCH", f"/pages/{page_id}", {"archived": True})
            print(f"  - {caminho}")
            time.sleep(PAUSA)


def main() -> int:
    dry = "--dry-run" in sys.argv
    check = "--check" in sys.argv
    prune = "--prune" in sys.argv

    aulas, divergencias = coletar_aulas()
    for d in divergencias:
        print("DIVERGENCIA " + d, file=sys.stderr)

    criar, atualizar, orfas, avisos = planejar(aulas)
    for a in avisos:
        print("AVISO " + a, file=sys.stderr)

    print(f"{len(aulas)} aulas no manifesto | "
          f"criar {len(criar)} | atualizar {len(atualizar)} | orfas {len(orfas)}")

    for aula, _ in criar:
        print(f"  + {aula['caminho']}")
    for aula, _pid, _id, mudou in atualizar:
        print(f"  ~ {aula['caminho']} ({', '.join(mudou)})")
    for caminho, _ in orfas:
        print(f"  ? {caminho} (orfa; use --prune para arquivar)")

    if check:
        pendente = len(criar) + len(atualizar) + (len(orfas) if prune else 0)
        return 1 if (pendente or divergencias) else 0

    if dry:
        print("[dry-run] nada foi escrito no Notion.")
        return 1 if divergencias else 0

    aplicar(criar, atualizar, orfas, prune)
    print("sync concluido.")
    return 1 if divergencias else 0


if __name__ == "__main__":
    raise SystemExit(main())
