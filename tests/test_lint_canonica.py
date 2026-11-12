"""Testes do tools/lint_canonica.py (stdlib only)."""
import tempfile
import unittest
from pathlib import Path

from tools.lint_canonica import lint

FRONT = """---
titulo: Aula teste
disciplina: d
trilha: t
ordem: 1
slug: aula-teste
status: {status}
versao: 1
atualizado_em: 2026-11-12
---

"""

OK = """Gancho da aula com [[conceito-x|rótulo]].

## Objetivos

- Fazer algo.

## Prática

1. Passo.

:::dica Atalho
Texto.
:::

```quiz
- pergunta: Quanto é 2+2?
  alternativas:
    - texto: "3"
    - texto: "4"
      correta: true
  feedback: Porque sim.
```

```diagrama-progressivo
titulo: Fluxo
camadas:
  - rotulo: Navegador
    conteudo: Monta a requisição.
```

```python
# isto é comentário de código, não título
print(":::qualquer")
```
"""


def codigos(corpo, status="aprovada", todas=False):
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        pasta = root / "aulas" / "d" / "t" / "01-aula-teste"
        pasta.mkdir(parents=True)
        (pasta / "canonica.md").write_text(FRONT.format(status=status) + corpo, encoding="utf-8")
        return sorted(d.code for d in lint(root, todas))


class TestLintCanonica(unittest.TestCase):
    def test_aula_conforme_nao_tem_achado(self):
        self.assertEqual(codigos(OK), [])

    def test_rotulo_numerado(self):
        self.assertEqual(codigos(OK.replace("rotulo: Navegador", "rotulo: 1. Navegador")), ["rotulo-numerado"])

    def test_wikilink_sem_rotulo(self):
        self.assertEqual(codigos(OK.replace("[[conceito-x|rótulo]]", "[[conceito-x]]")), ["wikilink-sem-rotulo"])

    def test_quiz_sem_ou_com_duas_corretas(self):
        sem = OK.replace("      correta: true\n", "")
        self.assertEqual(codigos(sem), ["quiz-correta"])
        duas = OK.replace('    - texto: "3"\n', '    - texto: "3"\n      correta: true\n')
        self.assertEqual(codigos(duas), ["quiz-correta"])

    def test_bloco_fora_do_catalogo_e_nao_fechado(self):
        self.assertIn("bloco-desconhecido", codigos(OK.replace(":::dica Atalho", ":::definicao Atalho")))
        self.assertEqual(codigos(OK.replace("Texto.\n:::\n", "Texto.\n")), ["bloco-nao-fechado"])

    def test_h1_no_corpo_e_secao_de_layout(self):
        self.assertEqual(codigos("# Título\n\n" + OK), ["corpo-com-h1"])
        self.assertEqual(codigos(OK.replace("## Prática", "## Mão na massa")), ["secao-ausente"])

    def test_markdown_em_campo_yaml(self):
        self.assertEqual(codigos(OK.replace("Quanto é 2+2?", "Quanto vale `x`?")), ["yaml-com-markdown"])

    def test_caminho_explicito_ignora_status(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pasta = root / "aulas" / "d" / "t" / "01-aula-teste"
            pasta.mkdir(parents=True)
            arq = pasta / "canonica.md"
            arq.write_text(FRONT.format(status="rascunho") + "# Título\n\n" + OK, encoding="utf-8")
            self.assertEqual([d.code for d in lint(root, caminhos=[arq])], ["corpo-com-h1"])

    def test_so_aprovadas_por_padrao(self):
        ruim = "# Título\n\n" + OK
        self.assertEqual(codigos(ruim, status="rascunho"), [])
        self.assertEqual(codigos(ruim, status="rascunho", todas=True), ["corpo-com-h1"])


if __name__ == "__main__":
    unittest.main()
