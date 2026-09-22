#!/usr/bin/env python3
"""Extrai o texto das aulas RCO (SEED-PR) para Markdown bruto no lake.

Entrada: pastas exportadas do Drive `lake/AULAS_RCO-*/AULAS_RCO/{SIGLA}/{N}TRI/{aula}/`,
cada aula com um `.pptx` de slides e ate dois `.docx` (ATIVIDADE e PRATICA). O
export do Drive quebra o lote em varios zips, entao a mesma aula pode ter arquivos
espalhados em mais de uma raiz: as raizes sao unidas pelo caminho relativo.

Saida: lake/{disciplina}/rco/{n}tri/{aula}.md  (conteudo BRUTO, status: bruto)

Deterministico e sem LLM: le o XML dos arquivos Office com a stdlib, preserva a
ordem de apresentacao dos slides, tabelas e notas do apresentador. Os originais
nunca sao alterados. Rodar de novo so reescreve o que mudou.

Uso:
    python tools/extrair_rco.py                  # extrai tudo
    python tools/extrair_rco.py --sigla AMS      # so uma disciplina
    python tools/extrair_rco.py --check          # exit != 0 se algo estiver desatualizado
"""
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Dict, List, Optional, Tuple
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
LAKE = ROOT / "lake"

# Sigla do RCO -> slug de disciplina do acervo.
SIGLAS: Dict[str, str] = {
    "AMS": "analise-e-metodos-para-sistemas",
    "APS": "analise-e-projeto-de-sistemas",
    "IAC": "introducao-a-computacao",
    "ITE": "inovacao-tecnologia-e-empreendedorismo",
    "PDS": "programacao-no-desenvolvimento-de-sistemas",
    "PFE": "programacao-front-end",
}

NS_P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
NS_A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
NS_R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
NS_REL = "{http://schemas.openxmlformats.org/package/2006/relationships}"
NS_W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
NS_MC = "{http://schemas.openxmlformats.org/markup-compatibility/2006}"

TITLE_PH = {"title", "ctrTitle"}
SKIP_NOTE_PH = {"sldNum", "sldImg", "hdr", "ftr", "dt"}
RE_TRI = re.compile(r"^(\d)TRI$", re.IGNORECASE)
RE_SERIE = re.compile(r"(\d)\s*[ªº°]?\s*s[ée]rie", re.IGNORECASE)
RE_AULA = re.compile(r"^aula\b", re.IGNORECASE)
RE_HEADING = re.compile(r"^(?:heading|t[ií]?tulo)\s*(\d)$", re.IGNORECASE)


# --------------------------------------------------------------------------- texto


def _clean(texto: str) -> str:
    return re.sub(r"\s+", " ", texto.replace(" ", " ")).strip()


def _para_text_a(par: ET.Element) -> str:
    """Texto de um <a:p> (DrawingML), com <a:br> virando espaco."""
    partes: List[str] = []
    for el in par.iter():
        if el.tag == NS_A + "t":
            partes.append(el.text or "")
        elif el.tag == NS_A + "br":
            partes.append(" ")
    return _clean("".join(partes))


def _md_table(linhas: List[List[str]]) -> List[str]:
    linhas = [l for l in linhas if any(c for c in l)]
    if not linhas:
        return []
    largura = max(len(l) for l in linhas)
    linhas = [l + [""] * (largura - len(l)) for l in linhas]
    esc = lambda c: c.replace("|", "\\|")
    out = ["| " + " | ".join(esc(c) for c in linhas[0]) + " |"]
    out.append("|" + " --- |" * largura)
    out += ["| " + " | ".join(esc(c) for c in l) + " |" for l in linhas[1:]]
    return out


# --------------------------------------------------------------------------- pptx


@dataclass
class Slide:
    numero: int
    oculto: bool
    titulo: str = ""
    linhas: List[str] = field(default_factory=list)
    notas: str = ""
    imagens: int = 0
    subtitulo: List[str] = field(default_factory=list)


def _rels(z: zipfile.ZipFile, part: str) -> Dict[str, Tuple[str, str]]:
    """Id -> (tipo, alvo absoluto no zip) para as relacoes de uma parte."""
    p = PurePosixPath(part)
    rels_path = str(p.parent / "_rels" / (p.name + ".rels"))
    if rels_path not in z.namelist():
        return {}
    out: Dict[str, Tuple[str, str]] = {}
    for rel in ET.fromstring(z.read(rels_path)).iter(NS_REL + "Relationship"):
        alvo = rel.get("Target", "")
        if rel.get("TargetMode") == "External":
            continue
        partes: List[str] = []
        for seg in (p.parent / alvo).parts:
            if seg == "..":
                if partes:
                    partes.pop()
            elif seg != ".":
                partes.append(seg)
        out[rel.get("Id", "")] = (rel.get("Type", "").rsplit("/", 1)[-1], "/".join(partes))
    return out


def _ordem_slides(z: zipfile.ZipFile) -> List[str]:
    """Partes dos slides na ordem de apresentacao (sldIdLst), nao na do nome do arquivo."""
    pres = ET.fromstring(z.read("ppt/presentation.xml"))
    rels = _rels(z, "ppt/presentation.xml")
    ordem = []
    for sld in pres.iter(NS_P + "sldId"):
        rid = sld.get(NS_R + "id")
        if rid in rels:
            ordem.append(rels[rid][1])
    return ordem


def _walk_shapes(el: ET.Element, slide: Slide, e_notas: bool = False, acc: Optional[List[str]] = None) -> None:
    for filho in el:
        tag = filho.tag
        if tag == NS_P + "sp":
            ph = filho.find(f"{NS_P}nvSpPr/{NS_P}nvPr/{NS_P}ph")
            ph_tipo = ph.get("type", "body") if ph is not None else None
            body = filho.find(NS_P + "txBody")
            if body is None:
                continue
            pars = [(p, _para_text_a(p)) for p in body.iter(NS_A + "p")]
            pars = [(p, t) for p, t in pars if t]
            if not pars:
                continue
            if e_notas:
                if ph_tipo in SKIP_NOTE_PH:
                    continue
                acc.extend(t for _, t in pars)
            elif ph_tipo in TITLE_PH and not slide.titulo:
                slide.titulo = " ".join(t for _, t in pars)
            else:
                if ph_tipo == "subTitle":
                    slide.subtitulo.extend(t for _, t in pars)
                for p, t in pars:
                    ppr = p.find(NS_A + "pPr")
                    nivel = int(ppr.get("lvl", "0")) if ppr is not None else 0
                    slide.linhas.append("  " * nivel + "- " + t)
        elif tag == NS_P + "grpSp":
            _walk_shapes(filho, slide, e_notas, acc)
        elif tag == NS_P + "graphicFrame" and not e_notas:
            tbl = filho.find(f".//{NS_A}tbl")
            if tbl is not None:
                linhas = [
                    [" ".join(_para_text_a(p) for p in tc.iter(NS_A + "p")).strip() for tc in tr.findall(NS_A + "tc")]
                    for tr in tbl.findall(NS_A + "tr")
                ]
                tabela = _md_table(linhas)
                if tabela:
                    slide.linhas += [""] + tabela + [""]
        elif tag == NS_P + "pic":
            slide.imagens += 1
        elif tag == NS_MC + "AlternateContent":
            escolha = filho.find(NS_MC + "Choice")
            if escolha is not None:
                _walk_shapes(escolha, slide, e_notas, acc)


def ler_pptx(caminho: Path) -> List[Slide]:
    slides: List[Slide] = []
    with zipfile.ZipFile(caminho) as z:
        for i, part in enumerate(_ordem_slides(z), start=1):
            root = ET.fromstring(z.read(part))
            slide = Slide(numero=i, oculto=root.get("show") == "0")
            tree = root.find(f"{NS_P}cSld/{NS_P}spTree")
            if tree is not None:
                _walk_shapes(tree, slide)
            for tipo, alvo in _rels(z, part).values():
                if tipo == "notesSlide" and alvo in z.namelist():
                    notas: List[str] = []
                    ntree = ET.fromstring(z.read(alvo)).find(f"{NS_P}cSld/{NS_P}spTree")
                    if ntree is not None:
                        _walk_shapes(ntree, slide, e_notas=True, acc=notas)
                    slide.notas = " ".join(notas)
            slides.append(slide)
    return slides


# --------------------------------------------------------------------------- docx


def _para_text_w(par: ET.Element) -> str:
    partes: List[str] = []
    for el in par.iter():
        if el.tag == NS_W + "t":
            partes.append(el.text or "")
        elif el.tag in (NS_W + "tab", NS_W + "br", NS_W + "cr"):
            partes.append(" ")
    return _clean("".join(partes))


def _docx_blocos(el: ET.Element, out: List[str]) -> None:
    for filho in el:
        if filho.tag == NS_W + "p":
            texto = _para_text_w(filho)
            if not texto:
                continue
            ppr = filho.find(NS_W + "pPr")
            estilo = ppr.find(NS_W + "pStyle") if ppr is not None else None
            m = RE_HEADING.match(estilo.get(NS_W + "val", "")) if estilo is not None else None
            if m:
                nivel = min(int(m.group(1)) + 3, 6)  # docx H1 -> ####, abaixo de "## Atividade"
                out += ["", "#" * nivel + " " + texto, ""]
            elif ppr is not None and ppr.find(NS_W + "numPr") is not None:
                out.append("- " + texto)
            else:
                out += [texto, ""]
        elif filho.tag == NS_W + "tbl":
            linhas = [
                [" ".join(_para_text_w(p) for p in tc.iter(NS_W + "p")).strip() for tc in tr.findall(NS_W + "tc")]
                for tr in filho.findall(NS_W + "tr")
            ]
            tabela = _md_table(linhas)
            if tabela:
                out += [""] + tabela + [""]
        elif filho.tag == NS_W + "sdt":
            conteudo = filho.find(NS_W + "sdtContent")
            if conteudo is not None:
                _docx_blocos(conteudo, out)


def ler_docx(caminho: Path) -> List[str]:
    with zipfile.ZipFile(caminho) as z:
        body = ET.fromstring(z.read("word/document.xml")).find(NS_W + "body")
    out: List[str] = []
    if body is not None:
        _docx_blocos(body, out)
    # colapsa linhas em branco repetidas
    limpo: List[str] = []
    for linha in out:
        if linha == "" and (not limpo or limpo[-1] == ""):
            continue
        limpo.append(linha)
    return limpo


# --------------------------------------------------------------------------- aula


@dataclass
class AulaRCO:
    sigla: str
    tri: int
    pasta: str  # nome da pasta da aula, ex. "1-engenharia-de-software"
    arquivos: List[Path] = field(default_factory=list)

    @property
    def disciplina(self) -> str:
        return SIGLAS[self.sigla]

    @property
    def destino(self) -> Path:
        return LAKE / self.disciplina / "rco" / f"{self.tri}tri" / f"{self.pasta}.md"


def descobrir(raizes: List[Path]) -> Tuple[List[AulaRCO], List[Path]]:
    """Une as raizes pelo caminho relativo SIGLA/NTRI/aula. Devolve (aulas, ignorados)."""
    aulas: Dict[Tuple[str, int, str], AulaRCO] = {}
    ignorados: List[Path] = []
    for raiz in raizes:
        for arq in sorted(p for p in raiz.rglob("*") if p.is_file()):
            partes = arq.relative_to(raiz).parts
            m = RE_TRI.match(partes[1]) if len(partes) == 4 else None
            if not m or partes[0] not in SIGLAS or arq.suffix.lower() not in (".pptx", ".docx"):
                ignorados.append(arq)
                continue
            chave = (partes[0], int(m.group(1)), partes[2])
            aulas.setdefault(chave, AulaRCO(*chave)).arquivos.append(arq)
    return [aulas[k] for k in sorted(aulas, key=lambda k: (k[0], k[1], _ordem_pasta(k[2]), k[2]))], ignorados


def _ordem_pasta(pasta: str) -> int:
    m = re.match(r"^(\d+)", pasta)
    return int(m.group(1)) if m else 10**6


def _tipo_docx(nome: str) -> str:
    n = nome.upper()
    if "PRÁTICA" in n or "PRATICA" in n:
        return "pratica"
    if "ATIVIDADE" in n:
        return "atividade"
    return "outro"


def _cabecalho(slides: List[Slide], pasta: str) -> Tuple[str, str, str]:
    """(titulo, serie, aula) a partir do subtitulo do slide 1; cai para o nome da pasta."""
    sub = slides[0].subtitulo if slides else []
    serie = aula = ""
    resto: List[str] = []
    for linha in sub:
        m = RE_SERIE.search(linha)
        if m and not serie:
            serie = m.group(1)
        elif RE_AULA.match(linha) and not aula:
            aula = linha
        else:
            resto.append(linha)
    # a primeira linha restante e o nome da disciplina (caixa alta); o titulo e a ultima
    candidatos = [l for l in resto if not (l.isupper() and len(resto) > 1)]
    titulo = candidatos[-1] if candidatos else ""
    if not titulo:
        titulo = re.sub(r"^\d+-", "", pasta).replace("-", " ").capitalize()
    return titulo, serie, aula


def _yaml(valor: str) -> str:
    return '"' + valor.replace("\\", "\\\\").replace('"', '\\"') + '"'


def renderizar(aula: AulaRCO) -> str:
    pptx = sorted(a for a in aula.arquivos if a.suffix.lower() == ".pptx")
    docx = sorted(a for a in aula.arquivos if a.suffix.lower() == ".docx")
    slides: List[Slide] = []
    for arq in pptx:
        slides += ler_pptx(arq)
    titulo, serie, aula_rotulo = _cabecalho(slides, aula.pasta)

    fm = [
        "---",
        f"titulo: {_yaml(titulo)}",
        "tipo: rco-seed",
        f"disciplina: {aula.disciplina}",
        f"sigla_rco: {aula.sigla}",
        f"trimestre: {aula.tri}",
        f"ordem_rco: {_ordem_pasta(aula.pasta)}",
    ]
    if serie:
        fm.append(f"serie: {serie}")
    if aula_rotulo:
        fm.append(f"aula_rco: {_yaml(aula_rotulo)}")
    fm += [
        f"slides: {len(slides)}",
        f"tem_atividade: {'true' if any(_tipo_docx(d.name) == 'atividade' for d in docx) else 'false'}",
        f"tem_pratica: {'true' if any(_tipo_docx(d.name) == 'pratica' for d in docx) else 'false'}",
        "fontes:",
    ]
    fm += [f"  - {_yaml(a.relative_to(ROOT).as_posix())}" for a in pptx + docx]
    fm += ["extrator: tools/extrair_rco.py", "status: bruto", "---", ""]

    corpo = [
        f"# {titulo}",
        "",
        "> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. "
        "Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.",
        "",
        "## Slides",
        "",
    ]
    for s in slides:
        cab = f"### Slide {s.numero}"
        if s.titulo:
            cab += f" — {s.titulo}"
        if s.oculto:
            cab += " (oculto)"
        corpo.append(cab)
        corpo.append("")
        corpo += s.linhas or ["_(sem texto)_"]
        if s.imagens:
            corpo += ["", f"_{s.imagens} imagem(ns) no slide._"]
        if s.notas:
            corpo += ["", f"> **Notas do apresentador:** {s.notas}"]
        corpo.append("")

    for tipo, rotulo in (("atividade", "Atividade"), ("pratica", "Prática"), ("outro", "Outros documentos")):
        docs = [d for d in docx if _tipo_docx(d.name) == tipo]
        for d in docs:
            corpo += [f"## {rotulo}", "", f"_Fonte: {d.name}_", ""]
            corpo += ler_docx(d)
            corpo.append("")

    texto = "\n".join(fm + corpo)
    texto = re.sub(r"\n{3,}", "\n\n", texto).rstrip() + "\n"
    return texto


# --------------------------------------------------------------------------- cli


def main(argv: Optional[List[str]] = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--raiz", action="append", type=Path,
                    help="raiz AULAS_RCO (repetivel). Padrao: lake/AULAS_RCO-*/AULAS_RCO")
    ap.add_argument("--sigla", action="append", choices=sorted(SIGLAS), help="filtra disciplina(s)")
    ap.add_argument("--check", action="store_true", help="nao escreve; exit 1 se algo mudaria")
    args = ap.parse_args(argv)

    raizes = args.raiz or sorted(LAKE.glob("AULAS_RCO-*/AULAS_RCO"))
    if not raizes:
        print("nenhuma raiz AULAS_RCO encontrada em lake/", file=sys.stderr)
        return 2
    aulas, ignorados = descobrir(raizes)
    if args.sigla:
        aulas = [a for a in aulas if a.sigla in args.sigla]

    novos = alterados = iguais = erros = 0
    for aula in aulas:
        try:
            texto = renderizar(aula)
        except (zipfile.BadZipFile, KeyError, ET.ParseError) as exc:
            erros += 1
            print(f"ERRO {aula.sigla}/{aula.tri}TRI/{aula.pasta}: {exc}", file=sys.stderr)
            continue
        atual = aula.destino.read_text(encoding="utf-8") if aula.destino.exists() else None
        if atual == texto:
            iguais += 1
            continue
        if atual is None:
            novos += 1
        else:
            alterados += 1
        if args.check:
            print(f"desatualizado: {aula.destino.relative_to(ROOT).as_posix()}")
        else:
            aula.destino.parent.mkdir(parents=True, exist_ok=True)
            aula.destino.write_text(texto, encoding="utf-8", newline="\n")

    print(f"[rco] {len(aulas)} aulas | novas {novos} | alteradas {alterados} | "
          f"iguais {iguais} | erros {erros} | ignorados {len(ignorados)}")
    for arq in ignorados:
        print(f"  ignorado: {arq.relative_to(ROOT).as_posix()}")
    if erros:
        return 1
    return 1 if args.check and (novos or alterados) else 0


if __name__ == "__main__":
    sys.exit(main())
