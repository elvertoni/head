#!/usr/bin/env python3
"""Gerador do manifesto.json — contrato de import do ProfessorDash.

Varre `aulas/{disciplina}/{trilha}/{NN-slug}/canonica.md`, extrai o frontmatter
e emite `manifesto.json` no schema EXATO que o portal espera (ver AGENTS.md
"Contrato de import do portal"):

  disciplinas[]: { slug, label, serie, status, trilhas: [ {slug, label} ], ... }
  lessons[]:     { disciplina, trilha, ordem, slug, titulo, status: "aprovada", ... }

Regras:
  - SÓ entram em lessons[] aulas com `status: aprovada` no frontmatter.
  - A identidade (disciplina/trilha/ordem/slug) vem do CAMINHO; o frontmatter
    é validado contra ele.
  - Sem dependências externas (stdlib only). Frontmatter é YAML de chaves
    escalares no topo — parser mínimo abaixo basta para os campos do contrato.

Uso:
    python tools/gerar_manifesto.py          # valida + reescreve manifesto.json
    python tools/gerar_manifesto.py --check  # só valida, NÃO escreve (exit!=0 se divergência)

Saída: lista de divergências em stderr; exit code 1 se houver divergência crítica.
"""
from __future__ import annotations

import datetime as _dt
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DIR_AULAS = RAIZ / "aulas"
MANIFESTO = RAIZ / "manifesto.json"

# Campos escalares do frontmatter que o gerador lê.
CAMPOS = ("titulo", "tema", "disciplina", "trilha", "ordem", "slug",
          "status", "versao", "atualizado_em")

# Campos do frontmatter exigidos pelo contrato (mínimo inviolável).
OBRIGATORIOS = ("titulo", "disciplina", "trilha", "ordem", "slug",
                "status", "versao", "atualizado_em")


def parse_frontmatter(texto: str) -> dict:
    """Extrai chaves escalares do bloco YAML entre os dois primeiros '---'.

    Ignora listas/blocos aninhados (linhas indentadas ou iniciadas por '-').
    Suficiente para os campos escalares do contrato.
    """
    linhas = texto.splitlines()
    if not linhas or linhas[0].strip() != "---":
        return {}
    fm: dict[str, str] = {}
    for linha in linhas[1:]:
        if linha.strip() == "---":
            break
        if not linha or linha[0] in " \t-":  # aninhado ou item de lista
            continue
        m = re.match(r"^([A-Za-z_][\w]*):\s*(.*)$", linha)
        if not m:
            continue
        chave, valor = m.group(1), m.group(2).strip()
        if chave in CAMPOS:
            fm[chave] = valor.strip().strip('"').strip("'")
    return fm


def coletar() -> tuple[list[dict], list[str]]:
    """Retorna (aulas, divergencias). Cada aula é um dict com identidade + frontmatter."""
    divergencias: list[str] = []
    aulas: list[dict] = []
    vistos_slug: dict[str, str] = {}  # slug -> caminho (unicidade global, p/ wikilinks)

    for canonica in sorted(DIR_AULAS.glob("*/*/*/canonica.md")):
        rel = canonica.relative_to(RAIZ).as_posix()
        pasta = canonica.parent.name           # NN-slug
        trilha_dir = canonica.parent.parent.name
        disc_dir = canonica.parent.parent.parent.name

        m = re.match(r"^(\d{2,})-(.+)$", pasta)
        if not m:
            divergencias.append(f"[caminho] {rel}: pasta '{pasta}' fora do padrao NN-slug")
            continue
        ordem_path = int(m.group(1))
        slug_path = m.group(2)

        fm = parse_frontmatter(canonica.read_text(encoding="utf-8"))
        status = fm.get("status", "")

        # Só publica aprovada; rascunho/publicada ignoradas em lessons[].
        if status != "aprovada":
            continue

        # Frontmatter obrigatório completo.
        faltando = [c for c in OBRIGATORIOS if not fm.get(c)]
        if faltando:
            divergencias.append(
                f"[frontmatter] {rel}: campos obrigatorios ausentes: {', '.join(faltando)}")

        # Caminho TEM que casar com frontmatter.
        if fm.get("disciplina") and fm["disciplina"] != disc_dir:
            divergencias.append(
                f"[mismatch] {rel}: disciplina frontmatter '{fm['disciplina']}' != caminho '{disc_dir}'")
        if fm.get("trilha") and fm["trilha"] != trilha_dir:
            divergencias.append(
                f"[mismatch] {rel}: trilha frontmatter '{fm['trilha']}' != caminho '{trilha_dir}'")
        if fm.get("ordem") and fm["ordem"] != str(ordem_path):
            divergencias.append(
                f"[mismatch] {rel}: ordem frontmatter '{fm['ordem']}' != caminho '{ordem_path:02d}'")
        if fm.get("slug") and fm["slug"] != slug_path:
            divergencias.append(
                f"[mismatch] {rel}: slug frontmatter '{fm['slug']}' != caminho '{slug_path}'")

        # Slug único global (resolução de wikilinks + chave do portal).
        if slug_path in vistos_slug:
            divergencias.append(
                f"[slug-duplicado] '{slug_path}': {rel} e {vistos_slug[slug_path]}")
        else:
            vistos_slug[slug_path] = rel

        aulas.append({
            "disciplina": disc_dir,
            "trilha": trilha_dir,
            "ordem": ordem_path,
            "slug": slug_path,
            "titulo": fm.get("titulo", slug_path),
            "tema": fm.get("tema", ""),
            "status": "aprovada",
        })

    return aulas, divergencias


def label_de_slug(slug: str) -> str:
    return slug.replace("-", " ").title()


def construir_manifesto(aulas: list[dict]) -> dict:
    """Mescla metadados curados (manifesto atual) com aulas descobertas no FS."""
    base = json.loads(MANIFESTO.read_text(encoding="utf-8")) if MANIFESTO.exists() else {}

    # Índice de ordem das disciplinas (preserva a curadoria do manifesto atual).
    disc_meta = {d["slug"]: d for d in base.get("disciplinas", [])}
    ordem_disc = list(disc_meta.keys())

    # Trilhas descobertas por disciplina: slug -> label (do `tema`, fallback título).
    trilhas_por_disc: dict[str, dict[str, str]] = {}
    contagem: dict[str, int] = {}
    for a in aulas:
        d, t = a["disciplina"], a["trilha"]
        trilhas_por_disc.setdefault(d, {})
        if t not in trilhas_por_disc[d]:
            trilhas_por_disc[d][t] = a.get("tema") or label_de_slug(t)
        contagem[d] = contagem.get(d, 0) + 1

    disciplinas = []
    for slug in ordem_disc:
        meta = disc_meta[slug]
        trilhas = [{"slug": ts, "label": tl}
                   for ts, tl in trilhas_por_disc.get(slug, {}).items()]
        disciplinas.append({
            "slug": slug,
            "label": meta.get("label", label_de_slug(slug)),
            "serie": meta.get("serie", ""),
            "status": meta.get("status", "planejada"),
            "lake": meta.get("lake", f"lake/{slug}"),
            "warehouse": meta.get("warehouse", f"aulas/{slug}"),
            "total_aulas": contagem.get(slug, 0),
            "trilhas": trilhas,
        })

    # Ordena lessons por disciplina (ordem do manifesto), trilha, ordem.
    idx = {s: i for i, s in enumerate(ordem_disc)}
    aulas_ord = sorted(aulas, key=lambda a: (idx.get(a["disciplina"], 999),
                                             a["trilha"], a["ordem"]))
    lessons = [{
        "disciplina": a["disciplina"],
        "trilha": a["trilha"],
        "ordem": a["ordem"],
        "slug": a["slug"],
        "titulo": a["titulo"],
        "status": "aprovada",
    } for a in aulas_ord]

    return {
        "version": base.get("version", 1),
        "vault": base.get("vault", "PROF-TONI"),
        "descricao": base.get("descricao", ""),
        "atualizado_em": _dt.date.today().isoformat(),
        "arquitetura": base.get("arquitetura", {}),
        "series": base.get("series", []),
        "disciplinas": disciplinas,
        "lessons": lessons,
    }


def main() -> int:
    check = "--check" in sys.argv
    aulas, divergencias = coletar()

    for d in divergencias:
        print("DIVERGENCIA " + d, file=sys.stderr)

    manifesto = construir_manifesto(aulas)

    if check:
        print(f"[check] {len(aulas)} aulas aprovadas, "
              f"{len(divergencias)} divergencias.", file=sys.stderr)
        return 1 if divergencias else 0

    MANIFESTO.write_text(
        json.dumps(manifesto, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"manifesto.json gerado: {len(manifesto['lessons'])} lessons, "
          f"{len(manifesto['disciplinas'])} disciplinas, "
          f"{len(divergencias)} divergencias.")
    return 1 if divergencias else 0


if __name__ == "__main__":
    raise SystemExit(main())
