# -*- coding: utf-8 -*-
"""Renderiza cada *.blueprint.json em HTML standalone no design system tonicoimbra.
Reusa head/CSS/SVG/JS do template.html da skill aula-estatica.
"""
import io, os, re, json, glob, unicodedata, html

TPL = r"C:\PROJETOS\PROF-TONI\.claude\skills\aula-estatica\template.html"
OUT = "render"

SECOES = [
    "Problema e Contexto",
    "Público-Alvo",
    "Solução Proposta",
    "Requisitos Funcionais",
    "Requisitos Não Funcionais",
    "Arquitetura e Tecnologias",
    "Fluxo Principal do Usuário",
    "Autoavaliação do Escopo",
]
STOP = {"de","da","do","das","dos","e","a","o","as","os","um","uma","the","of"}


def read(p):
    return io.open(p, encoding="utf-8").read()


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s or "sem-titulo"


def esc(t):
    return html.escape(t, quote=False)


def accent_title(titulo):
    """Envolve a primeira palavra-chave significativa em <span class='accent'>."""
    palavras = titulo.split()
    for i, w in enumerate(palavras):
        nu = re.sub(r"[^\wçáéíóúâêôãõà-]", "", w, flags=re.I)
        if len(nu) > 3 and nu.lower() not in STOP:
            palavras[i] = '<span class="accent">%s</span>' % esc(w)
            return " ".join(esc(p) if '<span' not in p else p for p in palavras)
    # nenhuma -> primeira palavra inteira
    if palavras:
        palavras[0] = '<span class="accent">%s</span>' % esc(palavras[0])
    return " ".join(p if '<span' in p else esc(p) for p in palavras)


def render_corpo(texto):
    """Converte o texto cru de uma seção em HTML (<p>, <ul>, <ol>)."""
    linhas = [ln.rstrip() for ln in texto.split("\n")]
    out, buf_ul, buf_ol = [], [], []

    def flush_ul():
        if buf_ul:
            out.append('<ul class="lista">\n' + "\n".join(buf_ul) + "\n</ul>")
            buf_ul.clear()

    def flush_ol():
        if buf_ol:
            out.append('<ol class="lista">\n' + "\n".join(buf_ol) + "\n</ol>")
            buf_ol.clear()

    for ln in linhas:
        s = ln.strip()
        if not s:
            flush_ul(); flush_ol()
            continue
        # RF01 — ... / RNF02 — ...
        m = re.match(r"^(RN?F\d+)\s*[—\-:]\s*(.+)$", s)
        if m:
            flush_ol()
            buf_ul.append("<li><strong>%s</strong> — %s</li>" % (esc(m.group(1)), esc(m.group(2))))
            continue
        # numerada: "1. ..." ou "1) ..."
        m = re.match(r"^(\d+)\s*[.)]\s*(.+)$", s)
        if m:
            flush_ul()
            buf_ol.append("<li>%s</li>" % esc(m.group(2)))
            continue
        # bullet "- ..."
        m = re.match(r"^-\s*(.+)$", s)
        if m:
            flush_ol()
            item = m.group(1)
            mt = re.match(r"^([^:]{1,40}):\s*(.+)$", item)
            if mt:
                buf_ul.append("<li><strong>%s:</strong> %s</li>" % (esc(mt.group(1)), esc(mt.group(2))))
            else:
                buf_ul.append("<li>%s</li>" % esc(item))
            continue
        # parágrafo
        flush_ul(); flush_ol()
        out.append("<p>%s</p>" % esc(s))
    flush_ul(); flush_ol()
    return "\n      ".join(out)


def build(tpl, d):
    head = tpl.split("</head>")[0] + "</head>\n"
    # script final (reuso integral)
    script = "<script>" + tpl.split("<script>")[1]

    # SVG logo + topbar topo (reuso): pega do <header class="topbar"> até </header>
    topbar = re.search(r'(<header class="topbar">.*?</header>)', tpl, re.S).group(1)
    topbar = topbar.replace("Apostila · <!-- [EDIT-DISCIPLINA] -->",
                            "Blueprint de Software · TCC")

    titulo = d.get("capa_titulo", "Blueprint")
    aluno = d.get("capa_aluno", "")
    tipo = d.get("capa_tipo", "")

    # sumário
    sumario = "\n".join(
        '        <li><a href="#sec-%d"><span class="sumario-num">%02d</span><span>%s</span></a></li>'
        % (i + 1, i + 1, esc(SECOES[i])) for i in range(8))

    # seções
    secs = []
    for i in range(8):
        n = i + 1
        corpo = render_corpo(d.get("sec%d_texto" % n, "").strip() or "—")
        cls = "section section-close" if n == 8 else "section"
        idx = "Autoavaliação" if n == 8 else "Seção %02d" % n
        secs.append(
            '    <section class="%s" id="sec-%d">\n'
            '      <header class="section-head">\n'
            '        <span class="section-index">%s</span>\n'
            '        <h2>%s</h2>\n'
            '      </header>\n'
            '      %s\n'
            '%s'
            '    </section>' % (
                cls, n, idx, esc(SECOES[i]), corpo,
                ('      <p class="footer-note">\n'
                 '        Blueprint de TCC · Prof. Toni Coimbra · '
                 '<span class="mono">aulas.tonicoimbra.com</span>\n'
                 '      </p>\n') if n == 8 else ""))

    body = (
        '<body class="apostila-shell">\n\n'
        + topbar +
        '\n\n  <main class="shell">\n\n'
        '    <section class="hero">\n'
        '      <div class="hero-gradient" aria-hidden="true"></div>\n'
        '      <div class="hero-inner">\n'
        '        <div class="eyebrow">\n'
        '          <span class="eyebrow-line"></span>\n'
        '          Blueprint de Software · TCC\n'
        '        </div>\n'
        '        <h1 class="hero-title">\n          %s\n        </h1>\n'
        '        <p class="hero-lead">%s</p>\n\n'
        '        <dl class="meta-grid">\n'
        '          <div class="meta-card"><dt>Aluno(a)</dt><dd>%s</dd></div>\n'
        '          <div class="meta-card"><dt>Tipo de sistema</dt><dd>%s</dd></div>\n'
        '          <div class="meta-card"><dt>Disciplina</dt><dd>Programação / Desenvolvimento de Sistemas</dd></div>\n'
        '          <div class="meta-card"><dt>Entrega</dt><dd>Blueprint de TCC</dd></div>\n'
        '        </dl>\n'
        '      </div>\n'
        '    </section>\n\n'
        '    <nav class="sumario" id="sumario" aria-label="Sumário do blueprint">\n'
        '      <p class="sumario-title">Neste blueprint</p>\n'
        '      <ol class="sumario-list">\n%s\n      </ol>\n'
        '    </nav>\n\n'
        '%s\n\n'
        '  </main>\n\n'
        '  <footer class="page-foot">\n'
        '    <div class="page-foot-inner">\n'
        '      <span>© <span id="year"></span> Prof Toni Coimbra</span>\n'
        '      <span class="dotsep">·</span>\n'
        '      <span>Blueprint de TCC · %s</span>\n'
        '      <span class="dotsep">·</span>\n'
        '      <a href="https://aulas.tonicoimbra.com" target="_blank" rel="noopener">aulas.tonicoimbra.com</a>\n'
        '    </div>\n'
        '  </footer>\n\n'
        '  %s\n</body>'
    ) % (accent_title(titulo), esc(tipo + (" · " + aluno if aluno else "")),
         esc(aluno or "—"), esc(tipo or "—"), sumario,
         "\n\n".join(secs), esc(titulo), script)

    # <title>
    head = re.sub(r"<title>.*?</title>",
                  "<title>Blueprint · %s · Prof Toni Coimbra</title>" % esc(titulo),
                  head, flags=re.S)
    return head + body + "\n</html>\n"


def main():
    tpl = read(TPL)
    os.makedirs(OUT, exist_ok=True)
    for jf in sorted(glob.glob("*.blueprint.json")):
        d = json.load(io.open(jf, encoding="utf-8"))
        out_html = build(tpl, d)
        name = "%s/blueprint-%s-%s.html" % (OUT, slug(d.get("capa_aluno", jf)),
                                            slug(d.get("capa_titulo", "")))
        io.open(name, "w", encoding="utf-8").write(out_html)
        print("wrote", name)
    print("DONE")


if __name__ == "__main__":
    main()
