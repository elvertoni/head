import io
import json
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools import jev
from tools.triar_rco import carregar, mesmo_titulo, normalizar_titulo, perguntas

AULA = """---
titulo: "Cerimônias do Scrum"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
trimestre: 1
ordem_rco: 21
status: bruto
---

# Cerimônias do Scrum

## Slides

### Slide 1 — Curso Técnico

- ANÁLISE E MÉTODO PARA SISTEMAS
- Aula 21

### Slide 2

- ORGANIZAÇÃO CURRICULAR EPT 2026
- texto de matriz que não interessa

### Slide 3

- Nesta aula, vamos:
- Compreender as cerimônias do Scrum
- Baixe o aplicativo da Alura na Google Play

### Slide 4

- A Sprint Review mostra o incremento.
- Fonte: Wikipedia

### Slide 5

- A Sprint Review mostra o incremento.

| Cerimônia | Duração |
| --- | --- |
| Daily | 15 min |

### Slide 6

- Referências
- SCHWABER, Ken. Scrum Guide. 2020.

## Atividade

- Questão sobre outra coisa
"""


class _Resp(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class TriarRcoTests(unittest.TestCase):
    def test_carregar_tira_template_e_separa_objetivos(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "21-cerimonias.md"
            p.write_text(AULA, encoding="utf-8")
            aula = carregar(p)
        self.assertEqual(aula.titulo, "Cerimônias do Scrum")
        self.assertEqual((aula.trimestre, aula.ordem_rco), (1, 21))
        self.assertEqual(aula.objetivos, ["Compreender as cerimônias do Scrum"])
        # capa, slide de matriz, linhas de template, duplicata e docx ficam de fora
        # tabela entra como "celula; celula"; slide de referencias sai inteiro
        self.assertEqual(aula.conteudo.splitlines(),
                         ["A Sprint Review mostra o incremento.", "Cerimônia; Duração", "Daily; 15 min"])

    def test_perguntas_so_incluem_equivalencia_quando_ha_aula_aprovada(self):
        self.assertEqual(set(perguntas([])), {"natureza", "densidade"})
        q = perguntas([{"slug": "introducao-ao-scrum", "titulo": "Introdução ao Scrum",
                        "trilha": "metodologias-ageis", "ordem": 34}])
        self.assertEqual(set(q["aula_aprovada"]["criteria"]), {"introducao-ao-scrum", "nenhuma"})
        self.assertEqual(q["aula_aprovada"]["criteria"]["introducao-ao-scrum"]["objetivos"], [])
        self.assertEqual(q["densidade"]["type"], "score")

    def test_titulo_identico_decide_sem_modelo(self):
        aula = mock.Mock(titulo="Análises de Resultados")
        aprovadas = [{"slug": "analise-de-resultados", "titulo": "Análises de resultados"},
                     {"slug": "outra", "titulo": "Planejamento de Marketing"}]
        self.assertEqual(mesmo_titulo(aula, aprovadas), "analise-de-resultados")
        # dois titulos iguais no acervo: ambiguo, fica com o Jev
        self.assertIsNone(mesmo_titulo(aula, aprovadas + [{"slug": "dup", "titulo": "ANALISES DE RESULTADOS!"}]))
        self.assertEqual(normalizar_titulo("  Introdução à UML — Parte I "), "introducao a uml parte i")


class JevClientTests(unittest.TestCase):
    def test_retenta_em_429_e_devolve_json(self):
        ok = _Resp(json.dumps({"model": "jev-1.13.0", "answers": {}}).encode())
        erro = urllib.error.HTTPError(jev.API_URL, 429, "too many", {"retry-after": "0"}, io.BytesIO(b"{}"))
        with mock.patch.dict("os.environ", {"TYPESAFE_API_KEY": "k"}), \
                mock.patch("urllib.request.urlopen", side_effect=[erro, ok]) as urlopen, \
                mock.patch("time.sleep"):
            r = jev.system_one("s", {"q": jev.noul("?")})
        self.assertEqual(r["model"], "jev-1.13.0")
        self.assertEqual(urlopen.call_count, 2)
        corpo = json.loads(urlopen.call_args.args[0].data)
        self.assertEqual(corpo["questions"]["q"], {"type": "noul", "instructions": "?"})

    def test_erro_nao_retentavel_sobe_na_hora(self):
        erro = urllib.error.HTTPError(jev.API_URL, 400, "bad", {}, io.BytesIO(b'{"error":"x"}'))
        with mock.patch.dict("os.environ", {"TYPESAFE_API_KEY": "k"}), \
                mock.patch("urllib.request.urlopen", side_effect=[erro]):
            with self.assertRaises(jev.JevError) as ctx:
                jev.system_one("s", {"q": jev.noul("?")})
        self.assertEqual(ctx.exception.status, 400)

    def test_validacao_dos_primitivos(self):
        with self.assertRaises(ValueError):
            jev.choice("?", {"so-uma": None})
        with self.assertRaises(ValueError):
            jev.score("?", ["um"])


if __name__ == "__main__":
    unittest.main()
