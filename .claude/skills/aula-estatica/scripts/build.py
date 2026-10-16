#!/usr/bin/env python3
"""Finaliza uma apostila da skill aula-estatica.

Uso:
    python scripts/build.py entrada.html saida.html
    python scripts/build.py entrada.html --check      # só valida, não grava

O que faz:
1. Troca o bloco entre <!-- FONTES:INICIO --> e <!-- FONTES:FIM --> pelas fontes
   Archivo e JetBrains Mono embutidas em base64 (o arquivo passa a abrir 100%
   offline, como o portal, que também hospeda as próprias fontes).
2. Embute as imagens locais (<img src="img/...">) como data URI, convertendo PNG/JPG
   para WebP com ffmpeg quando ele existir (arquivo bem menor, mesma nitidez).
3. Roda o checklist da skill e aponta cada problema com o motivo.

Só usa a biblioteca padrão do Python.
"""
import base64
import mimetypes
import re
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
FONTS = SKILL / 'assets' / 'fonts'
CALLOUT_KINDS = {'conceito', 'atencao', 'dica', 'exemplo', 'importante', 'curiosidade', 'objetivo', 'erro'}
VOID = {'meta', 'link', 'br', 'img', 'input', 'hr', 'path', 'circle', 'rect', 'source', 'col', 'wbr'}


def embed_fonts(html):
    start, end = '<!-- FONTES:INICIO', '<!-- FONTES:FIM -->'
    if start not in html:
        return html, False
    a = html.index(start)
    b = html.index(end, a) + len(end)

    def face(family, file, weight):
        data = base64.b64encode((FONTS / file).read_bytes()).decode('ascii')
        return (f"@font-face {{ font-family: '{family}'; font-style: normal; font-weight: {weight}; "
                f"font-display: swap; src: url(data:font/woff2;base64,{data}) format('woff2'); }}")

    block = ('<!-- FONTES: embutidas por scripts/build.py (Archivo + JetBrains Mono, self-host como no portal) -->\n'
             '  <style>\n'
             f"  {face('Archivo', 'archivo-latin.woff2', '400 900')}\n"
             f"  {face('JetBrains Mono', 'jetbrains-mono-latin.woff2', '400 700')}\n"
             '  </style>')
    return html[:a] + block + html[b:], True


def embed_images(html, base_dir):
    """Troca <img src="caminho/local"> por data URI. Devolve (html, quantas, kb)."""
    ffmpeg = shutil.which('ffmpeg')
    count, total = 0, 0

    def repl(m):
        nonlocal count, total
        src = m.group(2)
        if src.startswith(('data:', 'http:', 'https:', '//')):
            return m.group(0)
        path = (base_dir / src).resolve()
        if not path.is_file():
            return m.group(0)                       # o checklist avisa depois
        data, mime = path.read_bytes(), mimetypes.guess_type(path.name)[0] or 'image/png'
        if ffmpeg and path.suffix.lower() in ('.png', '.jpg', '.jpeg'):
            with tempfile.TemporaryDirectory() as tmp:
                out = Path(tmp) / 'img.webp'
                r = subprocess.run([ffmpeg, '-loglevel', 'error', '-y', '-i', str(path),
                                    '-vf', "scale='min(1600,iw)':-2", '-c:v', 'libwebp',
                                    '-quality', '82', str(out)], capture_output=True)
                if r.returncode == 0 and out.stat().st_size < len(data):
                    data, mime = out.read_bytes(), 'image/webp'
        count += 1
        total += len(data)
        return f'{m.group(1)}data:{mime};base64,{base64.b64encode(data).decode("ascii")}{m.group(3)}'

    html = re.sub(r'(<img\b[^>]*?\bsrc=")([^"]+)(")', repl, html)
    return html, count, total // 1024


class TagBalance(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.errors = [], []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        # <p> e <li> podem fechar implicitamente; tolera desde que exista na pilha
        while self.stack and self.stack[-1][0] in ('p', 'li') and self.stack[-1][0] != tag:
            self.stack.pop()
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            self.errors.append(f'</{tag}> na linha {self.getpos()[0]} não fecha nada aberto')


def check(html, base_dir=None):
    problems = []
    body = html[html.find('<body'):]

    if '[EDIT' in html:
        problems.append('Ainda há marcadores [EDIT...] no arquivo.')
    if body.count('<h1') != 1:
        problems.append(f'Deve haver exatamente um <h1> (achei {body.count("<h1")}).')
    if re.search(r'class="[^"]*\b(accent|c-primary|c-secondary|c-tertiary|c-warning|c-error|code-shell|demo-wrap|hero-title|apostila-shell)\b', body):
        problems.append('Há classes do template v2 (accent, c-*, code-shell, demo-wrap...). Use os componentes do BLOCOS.md v3.')
    if re.search(r'linear-gradient\([^)]*(#10b981|#8b5cf6|#06b6d4)', html):
        problems.append('Degradê multicolorido do design antigo detectado: banido no Volta Atelier.')

    ids = re.findall(r'<section class="section[^"]*" id="([^"]+)"', body)
    toc = re.search(r'<nav class="toc".*?</nav>', body, re.S)
    hrefs = re.findall(r'href="#([^"]+)"', toc.group(0)) if toc else []
    if not ids:
        problems.append('Nenhuma <section class="section" id="..."> encontrada.')
    if hrefs != ids:
        problems.append(f'Sumário e seções não batem.\n    sumário: {hrefs}\n    seções:  {ids}')
    sections = re.findall(r'<section class="(section[^"]*)"', body)
    if sections and 'section--close' not in sections[-1]:
        problems.append('A última seção precisa ter class="section section--close".')

    for block in re.findall(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', body, re.S):
        bare = re.sub(r'</?span( class="tok-[kasnc]")?>', '', block)
        if '<' in bare or '>' in bare:
            problems.append('Há < ou > sem escapar dentro de <pre><code>: ' + bare.strip()[:60])

    for kind in re.findall(r'<aside class="callout ([^"]+)"', body):
        if kind.strip() not in CALLOUT_KINDS:
            problems.append(f'Callout desconhecido: "{kind}". Tipos válidos: {", ".join(sorted(CALLOUT_KINDS))}.')

    for q in re.finditer(r'<li class="lesson-quiz-question"([^>]*)>(.*?)</li>\s*(?=<li class="lesson-quiz-question"|</ol>)', body, re.S):
        attrs, inner = q.group(1), q.group(2)
        m = re.search(r'data-correct="([a-e])"', attrs)
        letters = re.findall(r'<span class="quiz-option-letter">([a-e])</span>', inner)
        title = re.sub(r'<[^>]+>', '', inner)[:50].strip()
        if letters and not m:
            problems.append(f'Questão com alternativas mas sem data-correct (a–e): "{title}"')
        elif m and m.group(1) not in letters:
            problems.append(f'data-correct="{m.group(1)}" não existe entre as alternativas: "{title}"')
        if 'class="quiz-answer"' not in inner:
            problems.append(f'Questão sem gabarito comentado (<details class="quiz-answer">): "{title}"')

    for c in re.findall(r'<!--(.*?)-->', html, re.S):
        if '<!--' in c:
            problems.append('Comentário HTML aninhado: o primeiro --> fecha o comentário e o resto vaza para a página.')

    for img in re.findall(r'<img\b[^>]*>', body):
        if not re.search(r'\balt="[^"]+"', img):
            problems.append('Imagem sem texto alternativo (alt): ' + img[:70])
        src = re.search(r'\bsrc="([^"]+)"', img)
        if src and not src.group(1).startswith(('data:', 'http')) and base_dir and not (base_dir / src.group(1)).is_file():
            problems.append(f'Imagem não encontrada: {src.group(1)}')

    parser = TagBalance()
    parser.feed(html)
    problems += parser.errors[:5]
    leftovers = [t for t, _ in parser.stack if t not in ('p', 'li', 'html', 'body')]
    if leftovers:
        problems.append(f'Tags abertas sem fechamento: {leftovers[:6]}')
    return problems


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    src = Path(argv[1])
    html = src.read_text(encoding='utf-8')
    only_check = '--check' in argv
    problems = check(html, src.parent)
    if not only_check:
        if len(argv) < 3 or argv[2].startswith('--'):
            print('Informe o arquivo de saída (ou use --check).')
            return 2
        html, embedded = embed_fonts(html)
        html, n_img, kb_img = embed_images(html, src.parent)
        Path(argv[2]).write_text(html, encoding='utf-8')
        size = len(html.encode('utf-8')) // 1024
        extra = f' · {n_img} imagem(ns) embutida(s), {kb_img} KB' if n_img else ''
        print(f'Gravado {argv[2]} ({size} KB){" · fontes embutidas" if embedded else " · fontes já estavam embutidas"}{extra}')
    if problems:
        print(f'\n{len(problems)} problema(s):')
        for p in problems:
            print('  ✗ ' + p)
        return 1
    print('Checklist OK ✓')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
