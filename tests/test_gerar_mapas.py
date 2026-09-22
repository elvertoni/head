import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.gerar_mapas import renderizar, renderizar_indice, rotulo_aula

POS = "lake/Pos-X/Módulo I - Base/Matéria A"


def conceito(slug, nome, fontes, status="rascunho", tipo="conceito"):
    return {"slug": slug, "nome": nome, "status": status, "tipo": tipo,
            "caminho": f"conceitos/pos-x/{slug}", "fontes": fontes}


class GerarMapasTests(unittest.TestCase):
    def test_rotulo_aula_limpa_numeracao_e_sufixo(self):
        self.assertEqual(rotulo_aula("03 - Aula 3 - IOT e 5G - Apostila (Slides).pdf"), "Aula 3 — IOT e 5G")
        self.assertEqual(rotulo_aula("03 - Aula 3 - IOT e 5G - Resumo (Aula em PDF).pdf"), "Aula 3 — IOT e 5G")
        self.assertEqual(rotulo_aula("Git--para--iniciantes.pdf"), "Git--para--iniciantes")

    def test_agrupa_por_modulo_materia_e_aula(self):
        md = renderizar("pos-x", [
            conceito("b", "Beta", [f"{POS}/10 - Aula 10 - Fim - Apostila (Slides).pdf"]),
            conceito("a", "Alfa", [f"{POS}/02 - Aula 2 - Início - Apostila (Slides).pdf",
                                   f"{POS}/02 - Aula 2 - Início - Resumo (Aula em PDF).pdf",
                                   f"{POS}/10 - Aula 10 - Fim - Apostila (Slides).pdf"], status="vivo"),
            conceito("c", "Gama", ["https://example.com"], tipo="sintese"),
        ])
        self.assertIn("## Módulo I - Base", md)
        self.assertIn("### Matéria A", md)
        # aula 2 antes da aula 10 (ordem numerica, nao alfabetica)
        self.assertLess(md.index("#### Aula 2 — Início"), md.index("#### Aula 10 — Fim"))
        # apostila e resumo da mesma aula viram uma entrada so
        self.assertEqual(md.count("[[conceitos/pos-x/a|Alfa]]"), 2)
        self.assertIn("- [[conceitos/pos-x/b|Beta]] · _rascunho_", md)
        self.assertIn("- [[conceitos/pos-x/a|Alfa]]\n", md)
        # fonte fora do lake cai em "Outras fontes", que fecha o mapa
        self.assertTrue(md.rstrip().endswith("- [[conceitos/pos-x/c|Gama]] · _rascunho_ · síntese"))
        self.assertIn("3 conceitos · 1 vivos · 2 rascunhos", md)

    def test_indice_lista_mapas_do_maior_para_o_menor(self):
        md = renderizar_indice({"pequena": [conceito("a", "A", [])],
                                "grande": [conceito("b", "B", []), conceito("c", "C", [])]})
        self.assertLess(md.index("[[mapas/grande|"), md.index("[[mapas/pequena|"))
        self.assertIn("[[mapas/conceitos.base|", md)


if __name__ == "__main__":
    unittest.main()
