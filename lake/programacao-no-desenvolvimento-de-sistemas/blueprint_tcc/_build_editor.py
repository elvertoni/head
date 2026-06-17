# -*- coding: utf-8 -*-
"""Gera blueprint-template.html (EDITOR interativo do aluno) no design system
tonicoimbra (aula-estatica): reusa head/CSS/SVG/theme-toggle/theme-script do
template.html da skill e injeta os componentes de edicao (capa editavel, guia,
textarea, checklist, barra de progresso, import/export, autosave localStorage).

Data-keys identicos aos *.blueprint.json -> import/export 100% compativel.
"""
import io, re

TPL = r"C:\PROJETOS\PROF-TONI\.claude\skills\aula-estatica\template.html"
OUT = "blueprint-template.html"


def read(p):
    return io.open(p, encoding="utf-8").read()


tpl = read(TPL)

# ---- pedacos reaproveitados do design system ----
head = tpl.split("</head>")[0]                       # inclui </style>
svg_brand = re.search(r'<span class="brand-mark".*?</span>', tpl, re.S).group(0)
theme_btn = re.search(r'<button class="btn btn-secondary" id="theme-toggle".*?</button>', tpl, re.S).group(0)
theme_js = re.search(r'<script>(.*?)</script>', tpl, re.S).group(1)

# ---- CSS dos componentes do editor (usa os tokens --shell-* do design) ----
EXTRA_CSS = r"""
/* ===================== EDITOR DE BLUEPRINT (TCC) ===================== */
.topbar-inner { gap: 14px; flex-wrap: wrap; }
.tb-progress { display: flex; align-items: center; gap: 10px; flex: 1; min-width: 130px; }
.tb-bar { flex: 1; height: 8px; border-radius: 999px; background: var(--shell-border-strong); overflow: hidden; min-width: 70px; }
.tb-bar-fill { height: 100%; width: 0%; background: linear-gradient(90deg, var(--shell-primary), var(--shell-tertiary)); transition: width .35s ease; }
.tb-pct { font-size: 12px; font-weight: 800; color: var(--shell-text); min-width: 38px; }
.tb-save-state { font-size: 11px; color: var(--shell-text-soft); min-width: 64px; white-space: nowrap; }
@media (max-width: 760px) { .tb-progress { order: 5; flex-basis: 100%; } }

/* capa editavel (hero) */
.hero-title.field-edit { outline: none; }
.hero-title.field-edit:empty::before { content: attr(data-placeholder); color: var(--shell-text-soft); -webkit-text-fill-color: var(--shell-text-soft); }
.hero-title.field-edit:focus { box-shadow: inset 0 -2px 0 var(--shell-tertiary); }
.meta-card textarea {
  width: 100%; border: 0; background: transparent; resize: none; overflow: hidden;
  font-family: inherit; font-size: .98rem; font-weight: 600; line-height: 1.5;
  color: var(--shell-text); outline: none; padding: 0; min-height: 0;
}
.meta-card textarea::placeholder { color: var(--shell-text-soft); font-weight: 500; }
.meta-card:focus-within { border-color: var(--shell-tertiary); }

/* guia (o que escrever aqui) */
.bp-guide {
  display: flex; gap: 12px; align-items: flex-start; margin: 2px 0 16px;
  padding: 13px 15px; border-radius: var(--shell-radius-md);
  border: 1px solid color-mix(in srgb, var(--shell-tertiary) 32%, transparent);
  border-left: 4px solid var(--shell-tertiary);
  background: color-mix(in srgb, var(--shell-tertiary) 9%, transparent);
}
.bp-guide-icon {
  width: 30px; height: 30px; border-radius: 8px; flex-shrink: 0; display: grid; place-items: center;
  background: color-mix(in srgb, var(--shell-tertiary) 16%, transparent); color: var(--shell-tertiary-200); font-size: 1rem;
}
.bp-guide-title { font-size: 10px; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; color: var(--shell-tertiary-200); margin-bottom: 4px; }
.bp-guide-text { color: var(--shell-text-muted); font-size: .9rem; line-height: 1.66; }
.bp-guide-text em { color: var(--shell-tertiary-200); font-style: normal; font-weight: 700; }

/* campo de resposta */
.bp-field-label { font-size: 10px; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; color: var(--shell-text-soft); margin-bottom: 6px; display: block; }
textarea.bp-field {
  width: 100%; min-height: 120px; resize: vertical;
  background: var(--shell-surface-soft); border: 1px solid var(--shell-border-strong);
  border-radius: var(--shell-radius-md); padding: 13px 15px;
  font-family: inherit; font-size: .96rem; line-height: 1.74; color: var(--shell-text); outline: none;
  transition: border-color .15s ease, box-shadow .15s ease;
}
textarea.bp-field:focus { border-color: var(--shell-tertiary); box-shadow: 0 0 0 3px color-mix(in srgb, var(--shell-tertiary) 18%, transparent); }
textarea.bp-field::placeholder { color: var(--shell-text-soft); }

/* checklist (criterios de aceite) */
.bp-checklist { margin-top: 14px; padding-top: 12px; border-top: 1px dashed var(--shell-border-strong); }
.bp-checklist-title { font-size: 10px; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; color: var(--shell-primary-200); margin-bottom: 8px; display: flex; align-items: center; gap: 7px; }
.bp-check { display: flex; gap: 10px; align-items: flex-start; padding: 6px 0; font-size: .9rem; color: var(--shell-text-muted); cursor: pointer; }
.bp-check input { width: 17px; height: 17px; margin-top: 2px; accent-color: var(--shell-primary); cursor: pointer; flex-shrink: 0; }
.bp-check input:checked + span { color: var(--shell-text-soft); text-decoration: line-through; }

/* tag de progresso por secao + estado done */
.sec-tag { margin-left: auto; font-size: 9px; font-weight: 800; letter-spacing: .06em; padding: 3px 9px; border-radius: 999px; background: var(--shell-border); color: var(--shell-text-soft); }
.section.done { border-color: color-mix(in srgb, var(--shell-primary) 45%, transparent); }
.section.done .section-index { color: var(--shell-primary-200); }
.section.done .sec-tag { background: color-mix(in srgb, var(--shell-primary) 16%, transparent); color: var(--shell-primary-200); }
.section-head { display: flex; align-items: center; gap: 12px; }

/* caixa de ajuda */
.bp-help { background: var(--shell-surface-soft); border: 1px solid var(--shell-border); border-radius: var(--shell-radius-lg); padding: 18px 20px; margin-bottom: 22px; font-size: .9rem; color: var(--shell-text-muted); line-height: 1.7; }
.bp-help strong { color: var(--shell-text); }
.bp-help ul { margin: 8px 0 0 18px; }
.bp-help li { margin-bottom: 4px; }
.bp-help code { font-size: .85em; padding: 1px 5px; border-radius: 5px; background: var(--shell-border); }

@media print {
  .topbar, .bp-guide, .bp-help, .no-print { display: none !important; }
  textarea.bp-field, .meta-card textarea { border: 0 !important; background: transparent !important; padding: 0 !important; resize: none; overflow: hidden; min-height: 0; box-shadow: none !important; }
  .bp-checklist { border-top: 1px solid var(--shell-border); }
}
"""

head = head.replace("</style>", EXTRA_CSS + "\n</style>")
head = re.sub(r"<title>.*?</title>", "<title>Blueprint de Software · Template do TCC · Prof Toni Coimbra</title>", head, flags=re.S)

# ---- topbar (logo + progresso + acoes) ----
topbar = '''  <header class="topbar">
    <div class="topbar-inner">
      <a class="brand" href="#">
        %s
        <span class="brand-text">
          <strong>Prof Toni Coimbra</strong>
          <small>Blueprint de Software · TCC</small>
        </span>
      </a>
      <div class="tb-progress">
        <div class="tb-bar"><div class="tb-bar-fill" id="barFill"></div></div>
        <span class="tb-pct" id="barPct">0%%</span>
        <span class="tb-save-state" id="saveState">—</span>
      </div>
      <nav class="toolbar">
        <button class="btn btn-secondary" type="button" onclick="exportJSON()" title="Baixa um .json com tudo que você preencheu — backup / entrega ao professor">💾 Salvar</button>
        <button class="btn btn-secondary" type="button" onclick="document.getElementById('importFile').click()" title="Carrega um .json salvo antes">📂 Abrir</button>
        %s
        <button class="btn btn-primary" type="button" onclick="window.print()">🖨️ PDF</button>
        <input type="file" id="importFile" accept=".json,application/json" style="display:none" onchange="importJSON(event)" />
      </nav>
    </div>
  </header>''' % (svg_brand, theme_btn)

# ---- hero (capa editavel) ----
hero = '''    <section class="hero">
      <div class="hero-gradient" aria-hidden="true"></div>
      <div class="hero-inner">
        <div class="eyebrow">
          <span class="eyebrow-line"></span>
          Curso Técnico em Desenvolvimento de Sistemas · TCC
        </div>
        <h1 class="hero-title field-edit accent" data-key="capa_titulo" contenteditable="true" data-placeholder="Nome do seu projeto"></h1>
        <p class="hero-lead">Blueprint de Software — documento vivo. Preencha as 8 seções no seu ritmo; tudo salva sozinho neste navegador.</p>
        <dl class="meta-grid">
          <div class="meta-card"><dt>Aluno(a)</dt><dd><textarea data-key="capa_aluno" rows="1" placeholder="Seu nome completo"></textarea></dd></div>
          <div class="meta-card"><dt>Tipo de sistema</dt><dd><textarea data-key="capa_tipo" rows="1" placeholder="Web / Mobile / Desktop / API…"></textarea></dd></div>
          <div class="meta-card"><dt>Documento</dt><dd>Blueprint de TCC</dd></div>
          <div class="meta-card"><dt>Última edição</dt><dd id="lastEdit">—</dd></div>
        </dl>
      </div>
    </section>'''

help_box = '''    <div class="bp-help no-print">
      <strong>Como usar este documento</strong>
      <ul>
        <li>Preencha cada uma das 8 seções no seu ritmo. <strong>Tudo salva sozinho</strong> neste navegador, neste computador.</li>
        <li>Marque os <strong>critérios de aceite</strong> conforme cada parte fica pronta — a barra no topo mostra seu progresso.</li>
        <li><strong>💾 Salvar</strong> baixa um <code>.json</code> com tudo (backup / entrega). <strong>📂 Abrir</strong> retoma de onde parou em outro computador.</li>
        <li>No fim, <strong>🖨️ PDF</strong> exporta em A4 (barra, dicas e guias somem no PDF).</li>
      </ul>
    </div>'''

body = '''<body class="apostila-shell">

%s

  <main class="shell">

%s

%s

    <div id="sections"></div>

    <p class="footer-note" style="text-align:center;margin-top:24px">
      Blueprint de Software · TCC · Curso Técnico em Desenvolvimento de Sistemas · documento vivo — atualize conforme o projeto evoluir.
    </p>

  </main>

  <footer class="page-foot no-print">
    <div class="page-foot-inner">
      <span>© <span id="year"></span> Prof Toni Coimbra</span>
      <span class="dotsep">·</span>
      <a href="https://aulas.tonicoimbra.com" target="_blank" rel="noopener">aulas.tonicoimbra.com</a>
    </div>
  </footer>

''' % (topbar, hero, help_box)

# ---- script do editor (8 secoes + logica) + script de tema do design ----
EDITOR_JS = r'''
/* ===== 8 seções: guia + critérios de aceite ===== */
const SECTIONS = [
  { n:1, title:"Problema e Contexto",
    guide:"Que <em>dor real</em> seu sistema resolve? Quem sofre com ela? Como é resolvido hoje — e por que essa forma falha? Traga ao menos <em>um dado ou número</em> que mostre o tamanho do problema.",
    placeholder:"Descreva o problema: a dor, quem sofre, como é resolvido hoje e por que isso falha. Feche com o que o seu sistema vai resolver.",
    checks:["Descrevi a dor concreta (não genérica)","Disse quem sofre com o problema","Mostrei como é resolvido hoje e por que falha","Incluí pelo menos 1 dado, número ou fato","Fechei dizendo o que o sistema resolve"] },
  { n:2, title:"Público-alvo",
    guide:"Quem vai <em>usar</em> o sistema? Defina de 2 a 4 perfis de usuário diferentes. Para cada um, diga o que ele faz dentro do sistema.",
    placeholder:"Perfil 1 — quem é e o que faz no sistema.\nPerfil 2 — …\nPerfil 3 — …",
    checks:["Defini de 2 a 4 perfis de usuário","Cada perfil diz o que faz no sistema","Os perfis são distintos entre si"] },
  { n:3, title:"Solução Proposta",
    guide:"Em <em>uma frase</em>, o que o sistema é. Qual o <em>tipo</em> (web, mobile, desktop, API). Quais os <em>módulos/funções principais</em>. Qual o diferencial.",
    placeholder:"Em uma frase: o sistema é…\nTipo: …\nMódulos principais: …\nDiferencial: o que ele faz que as soluções de hoje não fazem.",
    checks:["Tenho uma frase única que define o sistema","Defini o tipo de sistema","Listei os módulos/funções principais","Deixei claro o diferencial"] },
  { n:4, title:"Requisitos Funcionais (o que o sistema FAZ)",
    guide:"Liste o que o sistema <em>deve fazer</em>. Cada requisito começa com verbo (\"O sistema deve…\") e tem um <em>critério de aceite mensurável</em>. Mínimo de 8. Devem cobrir os módulos da Seção 3.",
    placeholder:"RF01 — O sistema deve permitir… (critério: …)\nRF02 — O sistema deve… (critério: …)\nRF03 — …",
    checks:["Listei pelo menos 8 requisitos funcionais","Cada RF começa com verbo (\"o sistema deve…\")","Cada RF tem critério mensurável/verificável","Os RF cobrem os módulos da Seção 3"] },
  { n:5, title:"Requisitos Não Funcionais (COMO o sistema se comporta)",
    guide:"Qualidades do sistema: <em>desempenho, segurança, usabilidade, disponibilidade</em>. Mínimo de 4. Devem ser mensuráveis (ter número ou limite).",
    placeholder:"RNF01 — Desempenho: … (ex.: responder em até 2s)\nRNF02 — Segurança: …\nRNF03 — Usabilidade: …\nRNF04 — …",
    checks:["Listei pelo menos 4 requisitos não funcionais","Cobri ao menos desempenho e segurança","São mensuráveis (têm número ou limite)","Não repetem os requisitos funcionais"] },
  { n:6, title:"Arquitetura e Tecnologias",
    guide:"Qual a <em>stack</em>: front-end, back-end, banco de dados, infra/autenticação. Qual o <em>padrão arquitetural</em>. <em>Justifique cada escolha</em>. A stack precisa caber no prazo do TCC.",
    placeholder:"Front-end: … (por quê?)\nBack-end: … (por quê?)\nBanco de dados: … (por quê?)\nInfra/Auth: … (por quê?)\nPadrão arquitetural: …",
    checks:["Defini o front-end","Defini back-end e/ou banco de dados","Citei o padrão arquitetural","Cada tecnologia tem justificativa","A stack é viável para o prazo do TCC"] },
  { n:7, title:"Fluxo Principal de Uso",
    guide:"Conte o <em>passo a passo</em> do uso central do sistema, do início ao fim, numerado. Começa na entrada e termina num resultado entregue.",
    placeholder:"1. O usuário faz login / onboarding…\n2. …\n3. …\nN. O sistema entrega o resultado X.",
    checks:["O fluxo está numerado, passo a passo","Começa na entrada (login/onboarding/abertura)","Termina num resultado ou valor entregue","Cada passo é uma ação clara","Cobre o caso de uso central do sistema"] },
  { n:8, title:"Autoavaliação do Escopo",
    guide:"O projeto <em>cabe no prazo</em> do TCC? Por quê? O que é <em>MVP</em> (essencial) e o que é extra? Quais os <em>riscos</em> e como mitigá-los?",
    placeholder:"Viabilidade: o projeto cabe no prazo porque…\nMVP (essencial): …\nExtras (se sobrar tempo): …\nRiscos e mitigação: …",
    checks:["Justifiquei a viabilidade no prazo","Separei o MVP do que é opcional","Citei ao menos 1 risco e como mitigar","Os critérios de avaliação são verificáveis"] }
];

const STORAGE_KEY = "blueprint_tcc_v1";
const sectionsEl = document.getElementById("sections");
SECTIONS.forEach(s => {
  const sec = document.createElement("section");
  sec.className = "section";
  sec.id = "sec" + s.n;
  sec.innerHTML = `
    <header class="section-head">
      <span class="section-index">Seção ${String(s.n).padStart(2,"0")}</span>
      <h2>${s.title}</h2>
      <span class="sec-tag" id="tag${s.n}">0/${s.checks.length}</span>
    </header>
    <div class="bp-guide no-print">
      <div class="bp-guide-icon">💡</div>
      <div><div class="bp-guide-title">O que escrever aqui</div><div class="bp-guide-text">${s.guide}</div></div>
    </div>
    <span class="bp-field-label">Sua resposta</span>
    <textarea class="bp-field" data-key="sec${s.n}_texto" placeholder="${s.placeholder.replace(/"/g,'&quot;')}"></textarea>
    <div class="bp-checklist">
      <div class="bp-checklist-title">✓ Critérios de aceite — marque o que já está pronto</div>
      ${s.checks.map((c,i)=>`<label class="bp-check"><input type="checkbox" data-key="sec${s.n}_chk${i}" data-sec="${s.n}" /><span>${c}</span></label>`).join("")}
    </div>`;
  sectionsEl.appendChild(sec);
});

/* ===== estado / persistência ===== */
function collectState(){
  const st={};
  document.querySelectorAll("[data-key]").forEach(el=>{
    if(el.type==="checkbox") st[el.dataset.key]=el.checked;
    else if(el.isContentEditable) st[el.dataset.key]=el.innerText;
    else st[el.dataset.key]=el.value;
  });
  st._savedAt=new Date().toISOString();
  return st;
}
function applyState(st){
  if(!st) return;
  document.querySelectorAll("[data-key]").forEach(el=>{
    const v=st[el.dataset.key]; if(v===undefined) return;
    if(el.type==="checkbox") el.checked=!!v;
    else if(el.isContentEditable) el.innerText=v;
    else el.value=v;
  });
  autoGrowAll(); updateProgress();
  if(st._savedAt) showLastEdit(st._savedAt);
}
function save(){
  const st=collectState();
  try{ localStorage.setItem(STORAGE_KEY,JSON.stringify(st)); flashSaved(); }
  catch(e){ document.getElementById("saveState").textContent="⚠️ erro ao salvar"; }
  showLastEdit(st._savedAt); updateProgress();
}
let saveTimer;
function debouncedSave(){ clearTimeout(saveTimer); document.getElementById("saveState").textContent="salvando…"; saveTimer=setTimeout(save,600); }
function flashSaved(){ const el=document.getElementById("saveState"); el.textContent="✓ salvo"; el.style.color="var(--shell-primary-200)"; setTimeout(()=>{el.style.color="";},1500); }
function showLastEdit(iso){ if(!iso) return; const d=new Date(iso); document.getElementById("lastEdit").textContent=d.toLocaleDateString("pt-BR")+" "+d.toLocaleTimeString("pt-BR",{hour:"2-digit",minute:"2-digit"}); }

/* ===== progresso ===== */
function updateProgress(){
  const boxes=document.querySelectorAll('input[type="checkbox"][data-key]');
  let done=0; boxes.forEach(b=>{ if(b.checked) done++; });
  const pct=boxes.length?Math.round(done/boxes.length*100):0;
  document.getElementById("barFill").style.width=pct+"%";
  document.getElementById("barPct").textContent=pct+"%";
  SECTIONS.forEach(s=>{
    const sb=document.querySelectorAll(`input[data-sec="${s.n}"]`); let d=0; sb.forEach(b=>{ if(b.checked) d++; });
    document.getElementById("tag"+s.n).textContent=`${d}/${sb.length}`;
    document.getElementById("sec"+s.n).classList.toggle("done", d===sb.length && sb.length>0);
  });
}

/* ===== auto-crescer textareas ===== */
function autoGrow(el){ if(el.tagName!=="TEXTAREA") return; el.style.height="auto"; el.style.height=(el.scrollHeight+2)+"px"; }
function autoGrowAll(){ document.querySelectorAll("textarea").forEach(autoGrow); }

/* ===== export / import ===== */
function slug(s){ return (s||"blueprint").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g,"").replace(/[^a-z0-9]+/g,"-").replace(/^-+|-+$/g,"").slice(0,40)||"blueprint"; }
function exportJSON(){
  const st=collectState();
  const blob=new Blob([JSON.stringify(st,null,2)],{type:"application/json"});
  const a=document.createElement("a");
  a.href=URL.createObjectURL(blob);
  a.download=`blueprint-${slug(st.capa_aluno)}-${slug(st.capa_titulo)}.json`;
  a.click(); URL.revokeObjectURL(a.href);
}
function importJSON(ev){
  const file=ev.target.files[0]; if(!file) return;
  const r=new FileReader();
  r.onload=e=>{ try{ applyState(JSON.parse(e.target.result)); save(); alert("Progresso carregado."); }
    catch(err){ alert("Arquivo inválido. Use um .json salvo por este template."); }
    ev.target.value=""; };
  r.readAsText(file);
}

/* ===== listeners ===== */
document.addEventListener("input", e=>{ if(e.target.matches("[data-key]")){ if(e.target.tagName==="TEXTAREA") autoGrow(e.target); debouncedSave(); } });
document.addEventListener("change", e=>{ if(e.target.matches('input[type="checkbox"][data-key]')){ updateProgress(); debouncedSave(); } });
document.querySelectorAll('[contenteditable][data-key]').forEach(el=>el.addEventListener("input",debouncedSave));

/* ===== boot ===== */
(function init(){
  let saved=null; try{ saved=JSON.parse(localStorage.getItem(STORAGE_KEY)); }catch(e){}
  if(saved) applyState(saved); else { autoGrowAll(); updateProgress(); }
})();
'''

html = (head + "</head>\n" + body
        + "  <script>\n" + EDITOR_JS + "\n  </script>\n"
        + "  <script>" + theme_js + "</script>\n</body>\n</html>\n")

io.open(OUT, "w", encoding="utf-8").write(html)
print("wrote", OUT, len(html), "bytes")
