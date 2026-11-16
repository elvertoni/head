import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.gerar_manifesto import LABELS_TRILHA, divergencias_do_manifesto


class ManifestoComparisonTests(unittest.TestCase):
    def test_all_published_tracks_have_curated_labels(self):
        expected = {
            "controle-de-versao-git-github": "Controle de Versão com Git e GitHub",
            "fundamentos-html-css": "Fundamentos de HTML e CSS",
            "landing-page-mvp": "Landing Page e MVP",
            "analise-de-requisitos": "Análise de Requisitos",
            "arquitetura-e-fluxo-de-sistemas": "Arquitetura e Fluxo de Sistemas",
        }
        for slug, label in expected.items():
            self.assertEqual(LABELS_TRILHA.get(slug), label)

    def test_global_generation_date_is_ignored(self):
        actual = {"atualizado_em": "2026-09-20", "lessons": [{"slug": "a"}]}
        expected = {"atualizado_em": "2026-09-21", "lessons": [{"slug": "a"}]}
        self.assertEqual(divergencias_do_manifesto(actual, expected), [])

    def test_content_drift_is_reported(self):
        actual = {"atualizado_em": "2026-09-20", "lessons": [{"slug": "a"}]}
        expected = {"atualizado_em": "2026-09-21", "lessons": [{"slug": "b"}]}
        self.assertEqual(len(divergencias_do_manifesto(actual, expected)), 1)


class TestRaizEArgumentos(unittest.TestCase):
    def test_argumento_desconhecido_aborta_sem_escrever(self):
        from tools import gerar_manifesto as gm
        with self.assertRaises(SystemExit):
            gm.main(["--hlep"])

    def test_raiz_externa_gera_manifesto_dela(self):
        import json
        import tempfile
        from tools import gerar_manifesto as gm
        originais = (gm.RAIZ, gm.DIR_AULAS, gm.MANIFESTO)
        try:
            with tempfile.TemporaryDirectory() as tmp:
                raiz = Path(tmp)
                pasta = raiz / "aulas" / "estudo" / "trilha-x" / "01-aula-a"
                pasta.mkdir(parents=True)
                (pasta / "canonica.md").write_text(
                    "---\ntitulo: Aula A\ndisciplina: estudo\ntrilha: trilha-x\nordem: 1\n"
                    "slug: aula-a\nstatus: aprovada\nversao: 1\natualizado_em: 2026-11-15\n---\n\nTexto.\n",
                    encoding="utf-8",
                )
                (raiz / "manifesto.json").write_text(json.dumps({
                    "disciplinas": [{"slug": "estudo", "label": "Estudo", "trilhas": []}],
                }), encoding="utf-8")
                self.assertEqual(gm.main(["--raiz", str(raiz)]), 0)
                gerado = json.loads((raiz / "manifesto.json").read_text(encoding="utf-8"))
                self.assertEqual([l["slug"] for l in gerado["lessons"]], ["aula-a"])
                self.assertEqual(gerado["disciplinas"][0]["label"], "Estudo")
                self.assertEqual(gm.main(["--raiz", str(raiz), "--check"]), 0)
        finally:
            gm.RAIZ, gm.DIR_AULAS, gm.MANIFESTO = originais


if __name__ == "__main__":
    unittest.main()
