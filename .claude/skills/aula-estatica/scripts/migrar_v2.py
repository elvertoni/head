#!/usr/bin/env python3
"""Migra uma apostila do template v2 (gradientes, Geist, logo C ciano) para o v3 Volta Atelier.

Uso:
    python scripts/migrar_v2.py antiga.html nova.html [--capitulos] [--manter-tema-escuro]

Lê o conteúdo da apostila v2 (capa, sumário, seções, callouts, code-shells, tabelas,
questões de fixação, roteiros), traduz cada componente para o equivalente do BLOCOS.md v3
e encaixa tudo no template.html atual. O conteúdo e a voz não mudam: só a roupa.

Depois rode scripts/build.py no resultado para embutir as fontes e validar.
"""
import html as htmllib
import re
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
TEMPLATE = SKILL / 'template.html'

# v2 → v3: callout por cor/marca
KIND_BY_CLASS = {
    'c-primary': 'objetivo',
    'c-secondary': 'importante',
    'c-tertiary': 'conceito',
    'c-warning': 'atencao',
    'c-error': 'erro',
}
LABELS = {'conceito': 'Conceito', 'atencao': 'Atenção', 'dica': 'Dica', 'exemplo': 'Exemplo',
          'importante': 'Importante', 'curiosidade': 'Curiosidade', 'objetivo': 'Objetivo', 'erro': 'Erro'}
TOKEN_CLASS = {'tag': 'tok-k', 'attr': 'tok-a', 'prop': 'tok-a', 'str': 'tok-s', 'num': 'tok-n', 'com': 'tok-c'}


def strip_comments(s):
    return re.sub(r'<!--.*?-->', '', s, flags=re.S)


# ── componentes ─────────────────────────────────────────────────────────────
def convert_code_shells(s):
    def repl(m):
        block = m.group(0)
        lang = re.search(r'<span class="code-lang">(.*?)</span>', block, re.S)
        code = re.search(r'<pre><code>(.*?)</code></pre>', block, re.S)
        if not code:
            return block
        body = code.group(1)
        body = re.sub(r'<span class="(tag|attr|prop|str|num|com)">',
                      lambda t: f'<span class="{TOKEN_CLASS[t.group(1)]}">', body)
        lang_attr = f' data-lang="{lang.group(1).strip()}"' if lang else ''
        return f'<pre{lang_attr}><code>{body}</code></pre>'
    return re.sub(r'<div class="code-shell">.*?</pre>\s*</div>', repl, s, flags=re.S)


def convert_callouts(s):
    def repl(m):
        classes, mark, body = m.group(1), m.group(2).strip(), m.group(3)
        variant = next((c for c in classes.split() if c.startswith('c-')), 'c-tertiary')
        kind = KIND_BY_CLASS.get(variant, 'conceito')
        if variant == 'c-tertiary' and mark == '✦':
            kind = 'curiosidade'
        if variant == 'c-secondary' and mark == '★':
            kind = 'importante'
        title = re.search(r'<p class="callout-title">(.*?)</p>', body, re.S)
        texts = re.findall(r'<p class="callout-text">(.*?)</p>', body, re.S)
        rest = re.sub(r'<p class="callout-(title|text)">.*?</p>', '', body, flags=re.S).strip()
        label = LABELS[kind]
        t = title.group(1).strip() if title else ''
        if re.match(r'(Gabarito|Resposta)', t) or t.lower().startswith(label.lower()):
            b = t                              # gabarito vira quiz; rótulo já tipado fica como está
        else:
            b = f'{label} · {t}' if t else label
        parts = [f'<b>{b}</b>']
        parts += [f'<p>{t.strip()}</p>' for t in texts]
        if rest:
            parts.append(rest)
        return (f'<aside class="callout {kind}">\n'
                f'  <div class="ic" aria-hidden="true"></div>\n'
                f'  <div class="ct">\n    ' + '\n    '.join(parts) + '\n  </div>\n</aside>')
    pattern = (r'<aside class="callout ([^"]+)">\s*<div class="callout-mark"[^>]*>(.*?)</div>\s*'
               r'<div class="callout-body">(.*?)</div>\s*</aside>')
    return re.sub(pattern, repl, s, flags=re.S)


def balanced_div_end(s, start):
    """Índice logo após o </div> que fecha a <div> aberta em `start`."""
    depth = 0
    for t in re.finditer(r'<div\b|</div>', s[start:]):
        depth += 1 if t.group(0) == '<div' else -1
        if depth == 0:
            return start + t.end()
    return -1


def demo_to_v3(label, body):
    show_label = label and label.lower() != 'renderizado no navegador'
    only_tables = re.sub(r'<table class="demo">.*?</table>|<br\s*/?>|\s', '', body, flags=re.S) == ''
    if only_tables and '<table class="demo">' in body:
        out = []
        for i, t in enumerate(re.findall(r'<table class="demo">.*?</table>', body, re.S)):
            cap = f'\n  <caption>{label}</caption>' if (i == 0 and show_label) else ''
            out.append(t.replace('<table class="demo">', '<table>' + cap, 1))
        return '\n'.join(out)
    return (f'<div class="demo">\n  <p class="demo-label">{label or "Renderizado no navegador"}</p>\n'
            f'  <div class="demo-body">\n{body}\n  </div>\n</div>')


def convert_demos(s):
    out, pos = [], 0
    for m in re.finditer(r'<div class="demo-wrap">', s):
        if m.start() < pos:
            continue
        end = balanced_div_end(s, m.start())
        if end == -1:
            continue
        chunk = s[m.start():end]
        lab = re.search(r'<div class="demo-label">(.*?)</div>', chunk, re.S)
        b0 = chunk.find('<div class="demo-body">')
        if b0 == -1:
            continue
        b1 = balanced_div_end(chunk, b0)
        body = chunk[b0 + len('<div class="demo-body">'):b1 - len('</div>')].strip()
        out.append(s[pos:m.start()])
        out.append(demo_to_v3(lab.group(1).strip() if lab else '', body))
        pos = end
    out.append(s[pos:])
    return ''.join(out)


def convert_roteiros(s):
    return re.sub(
        r'<aside class="roteiro">\s*<header class="roteiro-head">\s*<span class="roteiro-chip">(.*?)</span>\s*</header>',
        r'<aside class="roteiro">\n  <p class="roteiro-label">\1</p>', s, flags=re.S)


def convert_tags(s):
    def repl(m):
        items = re.findall(r'<li>(.*?)</li>', m.group(1), re.S)
        return '<ul class="chips">' + ''.join(f'<li class="chip">{i.strip()}</li>' for i in items) + '</ul>'
    return re.sub(r'<ul class="tags">(.*?)</ul>', repl, s, flags=re.S)


def convert_questions(s):
    """<ol type="a"> + callout de gabarito/resposta → questão interativa do quiz."""
    q_re = re.compile(
        r'<ol type="a">(?P<opts>.*?)</ol>\s*'
        r'<aside class="callout (?P<k>[^"]+)">\s*<div class="ic" aria-hidden="true"></div>\s*<div class="ct">\s*'
        r'<b>(?P<title>(?:Gabarito|Resposta)[^<]*)</b>(?P<body>.*?)</div>\s*</aside>', re.S)
    out, pos, questions = [], 0, []
    for m in q_re.finditer(s):
        before = s[pos:m.start()]
        # enunciado: do último "<p><strong>Questão" ou "<h3>Questão" antes das alternativas
        cut = max(before.rfind('<p><strong>Questão'), before.rfind('<h3>Questão'))
        if cut == -1:
            cut = before.rfind('<p>')
        statement = before[cut:] if cut != -1 else ''
        lead = before[:cut] if cut != -1 else before
        opts = re.findall(r'<li>(.*?)</li>', m.group('opts'), re.S)
        correct = None
        letters = 'abcdefgh'
        clean = []
        for i, o in enumerate(opts):
            if '(correta)' in o:
                correct = letters[i]
            clean.append(re.sub(r'\s*<strong>\(correta\)</strong>', '', o).strip())
        tm = re.search(r'([a-e])\)', m.group('title'))
        if tm:
            correct = tm.group(1)
        statement = re.sub(r'<h3>Questão[^<]*</h3>\s*', '', statement)
        options = '\n'.join(
            f'      <button type="button" class="quiz-option"><span class="quiz-option-letter">{letters[i]}</span>'
            f'<span class="quiz-option-text">{o}</span><span class="quiz-option-icon" aria-hidden="true"></span></button>'
            for i, o in enumerate(clean))
        answer_body = m.group('body').strip()
        label = f'Resposta: {correct})' if correct else 'Resposta'
        answer_body = re.sub(r'^<p>', f'<p><strong>{label}</strong> ', answer_body, count=1)
        item = (f'  <li class="lesson-quiz-question" data-correct="{correct or "a"}">\n'
                f'    {statement.strip()}\n'
                f'    <div class="quiz-options">\n{options}\n    </div>\n'
                f'    <p class="quiz-feedback" hidden></p>\n'
                f'    <details class="quiz-answer"><summary>Gabarito comentado</summary>{answer_body}</details>\n'
                f'  </li>')
        if questions and lead.strip() == '':
            questions.append(item)            # questão colada na anterior: mesmo bloco
        else:
            if questions:
                out.append(wrap_quiz(questions))
                questions = []
            out.append(lead)
            questions = [item]
        pos = m.end()
    if questions:
        out.append(wrap_quiz(questions))
    out.append(s[pos:])
    return ''.join(out)


def wrap_quiz(items, title='Questões', count_label=None):
    n = len(items)
    count_label = count_label or (f'{n} questão' if n == 1 else f'{n} questões')
    return ('<section class="lesson-quiz">\n'
            f'  <div class="lesson-quiz-head"><strong>{title}</strong><span>{count_label}</span></div>\n'
            '  <ol class="lesson-quiz-list">\n' + '\n'.join(items) + '\n  </ol>\n'
            '  <p class="quiz-result" hidden></p>\n</section>')


def convert_body(s):
    s = strip_comments(s)
    s = convert_code_shells(s)
    s = convert_callouts(s)
    s = convert_demos(s)
    s = convert_roteiros(s)
    s = convert_tags(s)
    s = convert_questions(s)
    return s


# ── documento inteiro ──────────────────────────────────────────────────────
def parse_v2(doc):
    get = lambda pat: (re.search(pat, doc, re.S).group(1).strip() if re.search(pat, doc, re.S) else '')
    data = {
        'title': get(r'<title>(.*?)</title>'),
        'disciplina': strip_comments(get(r'<small>\s*Apostila\s*·\s*(.*?)</small>')),
        'eyebrow': re.sub(r'<span class="eyebrow-line"></span>', '', get(r'<div class="eyebrow">(.*?)</div>')).strip(),
        'h1': get(r'<h1 class="hero-title">(.*?)</h1>'),
        'lead': get(r'<p class="hero-lead">(.*?)</p>'),
        'meta': re.findall(r'<div class="meta-card"><dt>(.*?)</dt><dd>(.*?)</dd></div>', doc, re.S),
        'footer': strip_comments(get(r'Apostila estática\s*·\s*(.*?)</span>')),
    }
    data['h1'] = re.sub(r'<span class="accent">(.*?)</span>', r'<em>\1</em>', data['h1'], flags=re.S)
    main = get(r'<main class="shell">(.*?)</main>')
    sections = []
    for m in re.finditer(r'<section class="section( section-close)?" id="([^"]+)">(.*?)</section>', main, re.S):
        close, sid, content = bool(m.group(1)), m.group(2), m.group(3)
        idx = re.search(r'<span class="section-index">(.*?)</span>', content, re.S)
        h2 = re.search(r'<h2>(.*?)</h2>', content, re.S)
        content = re.sub(r'<header class="section-head">.*?</header>', '', content, count=1, flags=re.S)
        sections.append({'id': sid, 'close': close, 'index': idx.group(1).strip() if idx else '',
                         'h2': h2.group(1).strip() if h2 else '', 'content': content.strip()})
    toc = re.findall(r'<a href="#([^"]+)"><span class="sumario-num">(.*?)</span><span>(.*?)</span></a>', main, re.S)
    data['sections'], data['toc'] = sections, toc
    data['toc_title'] = get(r'<p class="sumario-title">(.*?)</p>') or 'Nesta aula'
    return data


def render_v3(data, capitulos=False):
    tpl = TEMPLATE.read_text(encoding='utf-8')
    head, rest = tpl.split('<main class="shell" id="conteudo">', 1)
    _, tail = rest.split('</main>', 1)

    title_text = re.sub(r'\s*·\s*Prof\.? Toni Coimbra\s*$', '', htmllib.unescape(data['title'])) or 'Apostila'
    head = re.sub(r'<title>.*?</title>', f'<title>{htmllib.escape(title_text)} · Prof. Toni Coimbra</title>', head, flags=re.S)
    head = head.replace('<!-- [EDIT-DISCIPLINA] -->', data['disciplina'] or 'Prof. Toni Coimbra')
    if capitulos:
        head = head.replace('<body>', '<body data-print="capitulos">', 1)
    tail = tail.replace('<!-- [EDIT-AULA-FOOTER] -->', data['footer'] or title_text)

    disciplina_chip = next((dd for dt, dd in data['meta'] if 'disciplina' in dt.lower()), data['disciplina'])
    meta = '\n'.join(f'        <div><dt>{dt}</dt><dd>{dd}</dd></div>' for dt, dd in data['meta'])
    chips = f'        <li class="chip">{disciplina_chip}</li>' if disciplina_chip else ''
    header = f'''
    <header class="lesson-header" id="topo">
      <p class="eyebrow">{data["eyebrow"]}</p>
      <ul class="chips">
{chips}
      </ul>
      <h1>{data["h1"]}</h1>
      <p class="dek">{data["lead"]}</p>
      <dl class="meta">
{meta}
      </dl>
    </header>
'''
    toc_items = '\n'.join(
        f'        <li><a href="#{sid}"><span class="toc-num">{num}</span><span>{label}</span></a></li>'
        for sid, num, label in data['toc'])
    toc = f'''
    <nav class="toc" id="sumario" aria-label="Sumário">
      <p class="eyebrow">{data["toc_title"]}</p>
      <ol class="toc-list">
{toc_items}
      </ol>
    </nav>
'''
    blocks = []
    for sec in data['sections']:
        cls = 'section section--close' if sec['close'] else 'section'
        blocks.append(f'''
    <section class="{cls}" id="{sec["id"]}">
      <header class="section-heading">
        <p class="eyebrow">{sec["index"]}</p>
        <h2>{sec["h2"]}</h2>
      </header>
{convert_body(sec["content"])}
    </section>
''')
    return head + '<main class="shell" id="conteudo">\n' + header + toc + ''.join(blocks) + '\n  </main>' + tail


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    doc = Path(argv[1]).read_text(encoding='utf-8')
    if 'apostila-shell' not in doc:
        print('Este arquivo não parece ser uma apostila v2 (sem class="apostila-shell").')
        return 1
    out = render_v3(parse_v2(doc), capitulos='--capitulos' in argv)
    if '--manter-tema-escuro' in argv:
        out = out.replace('<html lang="pt-BR" data-theme="light">', '<html lang="pt-BR" data-theme="dark">', 1)
    Path(argv[2]).write_text(out, encoding='utf-8')
    print(f'Migrado: {argv[2]}  (agora rode: python scripts/build.py {argv[2]} <final.html>)')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
