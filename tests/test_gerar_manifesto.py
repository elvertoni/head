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


if __name__ == "__main__":
    unittest.main()
