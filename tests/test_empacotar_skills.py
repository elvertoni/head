"""Testes do tools/empacotar_skills.py (stdlib only)."""
import tempfile
import unittest
import zipfile
from pathlib import Path

from tools import empacotar_skills as emp


def skill(raiz, nome, desc='Faz algo útil.', extra=None):
    pasta = Path(raiz) / nome
    (pasta / 'scripts' / '__pycache__').mkdir(parents=True)
    (pasta / 'SKILL.md').write_text(f'---\nname: {nome}\ndescription: {desc}\n---\n\n# {nome}\n', encoding='utf-8')
    (pasta / 'scripts' / 'a.py').write_text('print(1)\n', encoding='utf-8')
    (pasta / 'scripts' / '__pycache__' / 'a.cpython-314.pyc').write_bytes(b'x')
    (pasta / 'capa.proposta.png').write_bytes(b'x')
    return pasta


class TestValidar(unittest.TestCase):
    def test_skills_do_repo_passam(self):
        for s in emp.skills(emp.SKILLS):
            self.assertEqual(emp.validar(s), [], s.name)

    def test_recusa_nome_divergente_descricao_longa_e_tags(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertTrue(emp.validar(skill(tmp, 'boa')) == [])
            p = skill(tmp, 'longa', desc='x' * 1025)
            self.assertTrue(any('1024' in m for m in emp.validar(p)))
            p = skill(tmp, 'tag', desc='usa <b>negrito</b>')
            self.assertTrue(any('< ou >' in m for m in emp.validar(p)))
            p = skill(tmp, 'outra')
            (p / 'SKILL.md').write_text('---\nname: diferente\ndescription: d\n---\n', encoding='utf-8')
            self.assertTrue(any('diferente do nome da pasta' in m for m in emp.validar(p)))


class TestEmpacotar(unittest.TestCase):
    def test_zip_com_pasta_na_raiz_sem_cache_nem_proposta(self):
        with tempfile.TemporaryDirectory() as tmp:
            z = emp.empacotar(skill(tmp, 'demo'), Path(tmp) / 'out')
            nomes = zipfile.ZipFile(z).namelist()
            self.assertIn('demo/SKILL.md', nomes)
            self.assertIn('demo/scripts/a.py', nomes)
            self.assertFalse(any('__pycache__' in n or n.endswith('.proposta.png') for n in nomes))

    def test_gerar_imagem_leva_o_prompt_xml(self):
        with tempfile.TemporaryDirectory() as tmp:
            z = emp.empacotar(emp.SKILLS / 'gerar-imagem-aula', Path(tmp))
            self.assertIn('gerar-imagem-aula/references/prompt.xml', zipfile.ZipFile(z).namelist())


if __name__ == '__main__':
    unittest.main()
