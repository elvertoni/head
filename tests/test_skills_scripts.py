"""Testes dos scripts das skills em .claude/skills (stdlib only).

Cobre o que cada script promete no próprio docstring:
- aula-estatica/scripts/build.py: checklist da apostila.
- aula-estatica/scripts/migrar_v2.py: questão sem gabarito não ganha data-correct chutado.
- gerar-imagem-aula/scripts/montar_prompt.py: monta os dois perfis sem lacuna e recusa brief ruim.
- gerar-imagem-aula/scripts/inspecionar_png.py: mede proporção pelo header IHDR.
"""
import importlib.util
import struct
import tempfile
import unittest
import zlib
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SKILLS = RAIZ / '.claude' / 'skills'


def carregar(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


build = carregar('build', SKILLS / 'aula-estatica' / 'scripts' / 'build.py')
migrar = carregar('migrar_v2', SKILLS / 'aula-estatica' / 'scripts' / 'migrar_v2.py')
montar = carregar('montar_prompt', SKILLS / 'gerar-imagem-aula' / 'scripts' / 'montar_prompt.py')
inspecionar = carregar('inspecionar_png', SKILLS / 'gerar-imagem-aula' / 'scripts' / 'inspecionar_png.py')


class TestBuild(unittest.TestCase):
    def test_exemplo_passa_no_checklist(self):
        exemplo = SKILLS / 'aula-estatica' / 'exemplo-aula-01-formularios.html'
        self.assertEqual(build.check(exemplo.read_text(encoding='utf-8'), exemplo.parent), [])

    def test_template_cru_acusa_marcadores(self):
        tpl = (SKILLS / 'aula-estatica' / 'template.html').read_text(encoding='utf-8')
        self.assertTrue(any('[EDIT' in p for p in build.check(tpl)))

    def test_questao_sem_data_correct_e_letras_ate_h(self):
        html = ('<body><h1>x</h1><nav class="toc"><a href="#sec-1">a</a></nav>'
                '<section class="section section--close" id="sec-1"><ol>'
                '<li class="lesson-quiz-question"><div class="quiz-options">'
                '<span class="quiz-option-letter">a</span><span class="quiz-option-letter">f</span>'
                '</div><details class="quiz-answer"></details></li></ol></section></body>')
        problemas = build.check(html)
        self.assertTrue(any('sem data-correct' in p for p in problemas), problemas)
        ok = html.replace('<li class="lesson-quiz-question">', '<li class="lesson-quiz-question" data-correct="f">')
        self.assertFalse(any('data-correct' in p for p in build.check(ok)))


class TestMigrarV2(unittest.TestCase):
    V2 = ('<p><strong>Questão 1.</strong> Quanto é 2+2?</p><ol type="a"><li>3</li><li>4{marca}</li></ol>'
          '<aside class="callout conceito"><div class="ic" aria-hidden="true"></div><div class="ct">'
          '<b>Resposta</b><p>É quatro.</p></div></aside>')

    def test_sem_gabarito_nao_chuta(self):
        saida = migrar.convert_questions(self.V2.format(marca=''))
        self.assertIn('class="lesson-quiz-question">', saida)
        self.assertNotIn('data-correct', saida)

    def test_com_marca_correta(self):
        saida = migrar.convert_questions(self.V2.format(marca=' <strong>(correta)</strong>'))
        self.assertIn('data-correct="b"', saida)
        self.assertNotIn('(correta)', saida)


class TestMontarPrompt(unittest.TestCase):
    INFO = {'perfil': 'infografico', 'aula': 'Aula X', 'titulo': 'Ciclo de instrução',
            'palavra_chave': 'instrução', 'conceito': 'c', 'mensagem_3s': 'm',
            'composicao': '3-5 step cycle',
            'blocos': [{'rotulo': 'BUSCAR', 'cor': 'signal'}, {'rotulo': 'EXECUTAR', 'cor': 'volt'}]}
    CAPA = {'perfil': 'capa', 'aula': 'Aula X', 'titulo': 'Ciclo de instrução', 'palavra_chave': 'instrução',
            'objetivo': 'o', 'estrutura': '(a)', 'subtitulo': 's', 'faixa_rotulo': 'EM RESUMO',
            'faixa_frase': 'f', 'blocos': [{'rotulo': r, 'texto': 't'} for r in 'ABCD']}

    def test_monta_os_dois_perfis_sem_lacuna(self):
        for brief in (self.INFO, self.CAPA):
            texto = montar.montar(brief)
            self.assertNotRegex(texto, r'\[(insert|choose one|for each block)')
            self.assertIn('Ciclo de instrução', texto)

    def test_recusa_brief_fora_do_perfil(self):
        ruim = dict(self.INFO, blocos=[dict(b, texto='parágrafo') for b in self.INFO['blocos']])
        with self.assertRaises(SystemExit):
            montar.montar(ruim)
        with self.assertRaises(SystemExit):
            montar.montar(dict(self.INFO, palavra_chave='fora'))
        with self.assertRaises(SystemExit):
            montar.montar(dict(self.CAPA, blocos=self.CAPA['blocos'][:2]))


def png_minimo(largura, altura):
    def chunk(tipo, dados):
        return struct.pack('>I', len(dados)) + tipo + dados + struct.pack('>I', zlib.crc32(tipo + dados))
    ihdr = struct.pack('>IIBBBBB', largura, altura, 8, 2, 0, 0, 0)
    return b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', ihdr) + chunk(b'IEND', b'')


class TestInspecionarPng(unittest.TestCase):
    def test_mede_e_classifica(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'a.png'
            p.write_bytes(png_minimo(1536, 1024))
            self.assertEqual(inspecionar.dimensoes(p), (1536, 1024))
        ok, *_ = inspecionar.avaliar('capa', 1536, 1024)
        self.assertTrue(ok)
        ok, *_ = inspecionar.avaliar('infografico', 1536, 1024)
        self.assertFalse(ok)
        self.assertEqual(inspecionar.perfil_provavel(1672 / 941), 'infografico')


if __name__ == '__main__':
    unittest.main()
