import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools import extrair_rco as rco

P = 'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"'
A = 'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"'
R = 'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'
W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
REL = 'xmlns="http://schemas.openxmlformats.org/package/2006/relationships"'
T_SLIDE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide"
T_NOTES = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/notesSlide"


def _sp(textos, ph=None, lvl=0):
    ph_xml = f'<p:ph type="{ph}"/>' if ph else ""
    pars = "".join(f'<a:p><a:pPr lvl="{lvl}"/><a:r><a:t>{t}</a:t></a:r></a:p>' for t in textos)
    return (f"<p:sp><p:nvSpPr><p:cNvPr id=\"1\" name=\"s\"/><p:cNvSpPr/><p:nvPr>{ph_xml}</p:nvPr></p:nvSpPr>"
            f"<p:txBody>{pars}</p:txBody></p:sp>")


def _slide(shapes, show=True):
    attr = "" if show else ' show="0"'
    return f'<p:sld {P} {A} {R}{attr}><p:cSld><p:spTree>{shapes}</p:spTree></p:cSld></p:sld>'


def fazer_pptx(caminho: Path):
    """Dois slides; a ordem de apresentacao e a inversa do nome dos arquivos."""
    capa = _sp(["Curso Técnico"], ph="ctrTitle") + _sp(
        ["ANÁLISE E MÉTODO PARA SISTEMAS", "1ª Série", "Engenharia de Software", "Aula 01"], ph="subTitle")
    tabela = ('<p:graphicFrame><a:graphic><a:graphicData><a:tbl>'
              '<a:tr><a:tc><a:txBody><a:p><a:r><a:t>Fase</a:t></a:r></a:p></a:txBody></a:tc>'
              '<a:tc><a:txBody><a:p><a:r><a:t>Saída</a:t></a:r></a:p></a:txBody></a:tc></a:tr>'
              '<a:tr><a:tc><a:txBody><a:p><a:r><a:t>Requisitos</a:t></a:r></a:p></a:txBody></a:tc>'
              '<a:tc><a:txBody><a:p><a:r><a:t>a|b</a:t></a:r></a:p></a:txBody></a:tc></a:tr>'
              '</a:tbl></a:graphicData></a:graphic></p:graphicFrame>')
    conteudo = _sp(["Definição"], ph="title") + "<p:grpSp>" + _sp(["Nível zero", "Nível um"], lvl=0) + "</p:grpSp>" + tabela + "<p:pic/>"
    notas = f'<p:notes {P} {A}><p:cSld><p:spTree>{_sp(["Fale do SWEBOK"])}{_sp(["2"], ph="sldNum")}</p:spTree></p:cSld></p:notes>'
    with zipfile.ZipFile(caminho, "w") as z:
        z.writestr("ppt/presentation.xml",
                   f'<p:presentation {P} {R}><p:sldIdLst><p:sldId id="256" r:id="rId9"/>'
                   f'<p:sldId id="257" r:id="rId8"/></p:sldIdLst></p:presentation>')
        z.writestr("ppt/_rels/presentation.xml.rels",
                   f'<Relationships {REL}><Relationship Id="rId8" Type="{T_SLIDE}" Target="slides/slide1.xml"/>'
                   f'<Relationship Id="rId9" Type="{T_SLIDE}" Target="slides/slide2.xml"/></Relationships>')
        z.writestr("ppt/slides/slide2.xml", _slide(capa))
        z.writestr("ppt/slides/slide1.xml", _slide(conteudo, show=False))
        z.writestr("ppt/slides/_rels/slide1.xml.rels",
                   f'<Relationships {REL}><Relationship Id="rId1" Type="{T_NOTES}" Target="../notesSlides/notesSlide1.xml"/></Relationships>')
        z.writestr("ppt/notesSlides/notesSlide1.xml", notas)


def fazer_docx(caminho: Path, titulo: str):
    corpo = (f'<w:p><w:pPr><w:pStyle w:val="Heading2"/></w:pPr><w:r><w:t>{titulo}</w:t></w:r></w:p>'
             '<w:p><w:r><w:t>Questão 1</w:t></w:r></w:p>'
             '<w:p><w:pPr><w:numPr/></w:pPr><w:r><w:t>Canva</w:t></w:r></w:p>'
             '<w:tbl><w:tr><w:tc><w:p><w:r><w:t>A</w:t></w:r></w:p></w:tc>'
             '<w:tc><w:p><w:r><w:t>B</w:t></w:r></w:p></w:tc></w:tr></w:tbl>')
    with zipfile.ZipFile(caminho, "w") as z:
        z.writestr("word/document.xml", f"<w:document {W}><w:body>{corpo}</w:body></w:document>")


class ExtrairRcoTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self._orig = (rco.ROOT, rco.LAKE)
        rco.ROOT, rco.LAKE = self.root, self.root / "lake"
        # o export do Drive espalha a mesma aula em duas raizes
        self.r1 = self.root / "lake" / "AULAS_RCO-x-001" / "AULAS_RCO"
        self.r2 = self.root / "lake" / "AULAS_RCO-x-002" / "AULAS_RCO"
        aula1 = self.r1 / "AMS" / "1TRI" / "1-engenharia-de-software"
        aula2 = self.r2 / "AMS" / "1TRI" / "1-engenharia-de-software"
        aula1.mkdir(parents=True)
        aula2.mkdir(parents=True)
        fazer_pptx(aula1 / "1-engenharia-de-software.pptx")
        fazer_docx(aula2 / "AULA 01_ATIVIDADE_ANÁLISE.docx", "Atividade")
        fazer_docx(aula2 / "AULA 01_PRÁTICA_ANÁLISE.docx", "Objetivo da Aula Prática")
        (self.r1 / "Template.docx").write_bytes(b"x")
        (self.r1 / "XYZ" / "1TRI" / "1-a").mkdir(parents=True)
        (self.r1 / "XYZ" / "1TRI" / "1-a" / "a.pptx").write_bytes(b"x")

    def tearDown(self):
        rco.ROOT, rco.LAKE = self._orig
        self._tmp.cleanup()

    def test_descobrir_une_raizes_e_ignora_fora_do_padrao(self):
        aulas, ignorados = rco.descobrir([self.r1, self.r2])
        self.assertEqual(len(aulas), 1)
        self.assertEqual(len(aulas[0].arquivos), 3)
        self.assertEqual({p.name for p in ignorados}, {"Template.docx", "a.pptx"})

    def test_slides_seguem_ordem_de_apresentacao(self):
        slides = rco.ler_pptx(self.r1 / "AMS" / "1TRI" / "1-engenharia-de-software" / "1-engenharia-de-software.pptx")
        self.assertEqual([s.titulo for s in slides], ["Curso Técnico", "Definição"])
        self.assertFalse(slides[0].oculto)
        self.assertTrue(slides[1].oculto)
        self.assertEqual(slides[1].notas, "Fale do SWEBOK")
        self.assertEqual(slides[1].imagens, 1)

    def test_renderiza_frontmatter_e_corpo(self):
        aulas, _ = rco.descobrir([self.r1, self.r2])
        md = rco.renderizar(aulas[0])
        self.assertIn('titulo: "Engenharia de Software"', md)
        self.assertIn("disciplina: analise-e-metodos-para-sistemas", md)
        self.assertIn("serie: 1\n", md)
        self.assertIn('aula_rco: "Aula 01"', md)
        self.assertIn("tem_atividade: true", md)
        self.assertIn("tem_pratica: true", md)
        self.assertIn("status: bruto", md)
        self.assertIn("### Slide 2 — Definição (oculto)", md)
        self.assertIn("- Nível zero", md)
        self.assertIn("| Requisitos | a\\|b |", md)
        self.assertIn("> **Notas do apresentador:** Fale do SWEBOK", md)
        self.assertNotIn("Notas do apresentador:** Fale do SWEBOK 2", md)
        self.assertIn("## Atividade", md)
        self.assertIn("## Prática", md)
        self.assertIn("##### Objetivo da Aula Prática", md)
        self.assertIn("- Canva", md)
        self.assertLess(md.index("## Atividade"), md.index("## Prática"))

    def test_main_escreve_e_check_fica_limpo(self):
        raizes = ["--raiz", str(self.r1), "--raiz", str(self.r2)]
        self.assertEqual(rco.main(raizes + ["--check"]), 1)
        self.assertEqual(rco.main(raizes), 0)
        destino = self.root / "lake" / "analise-e-metodos-para-sistemas" / "rco" / "1tri" / "1-engenharia-de-software.md"
        self.assertTrue(destino.exists())
        self.assertEqual(rco.main(raizes + ["--check"]), 0)


if __name__ == "__main__":
    unittest.main()
