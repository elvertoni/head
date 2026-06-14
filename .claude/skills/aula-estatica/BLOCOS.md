# BLOCOS — Snippets prontos por componente

Versão: **2.0** — Adicionado BLOCO 21 (Questão de fixação) e BLOCO 22 (Mini-exemplo de calibração). Marks revisados.

Copie o bloco correspondente e substitua apenas o conteúdo interno.
Nunca altere nomes de classes. Nunca adicione `style=""` inline exceto onde explicitamente indicado.

---

## BLOCO 1 — Hero completo

```html
<section class="hero">
  <div class="hero-gradient" aria-hidden="true"></div>
  <div class="hero-inner">
    <div class="eyebrow">
      <span class="eyebrow-line"></span>
      Aula 00 · Tema curto da aula
    </div>
    <h1 class="hero-title">
      Título com <span class="accent">palavra-chave</span> em destaque
    </h1>
    <p class="hero-lead">
      Parágrafo de abertura em 1–3 frases que situa o aluno no contexto da aula.
    </p>
    <dl class="meta-grid">
      <div class="meta-card"><dt>Disciplina</dt><dd>Programação Web</dd></div>
      <div class="meta-card"><dt>Nível</dt><dd>Ensino Técnico</dd></div>
      <div class="meta-card"><dt>Duração</dt><dd>50 minutos</dd></div>
      <div class="meta-card"><dt>Entrega</dt><dd>1 atividade prática</dd></div>
    </dl>
  </div>
</section>
```

---

## BLOCO 2 — Sumário (7 itens)

```html
<nav class="sumario" id="sumario" aria-label="Sumário da aula">
  <p class="sumario-title">Nesta aula</p>
  <ol class="sumario-list">
    <li><a href="#sec-1"><span class="sumario-num">01</span><span>Título da seção 1</span></a></li>
    <li><a href="#sec-2"><span class="sumario-num">02</span><span>Título da seção 2</span></a></li>
    <li><a href="#sec-3"><span class="sumario-num">03</span><span>Título da seção 3</span></a></li>
    <li><a href="#sec-4"><span class="sumario-num">04</span><span>Título da seção 4</span></a></li>
    <li><a href="#sec-5"><span class="sumario-num">05</span><span>Título da seção 5</span></a></li>
    <li><a href="#sec-6"><span class="sumario-num">06</span><span>Título da seção 6</span></a></li>
    <li><a href="#sec-7"><span class="sumario-num">07</span><span>Fechamento</span></a></li>
  </ol>
</nav>
```

---

## BLOCO 3 — Section padrão

```html
<section class="section" id="sec-N">
  <header class="section-head">
    <span class="section-index">Seção 0N</span>
    <h2>Título da seção</h2>
  </header>

  <p>Parágrafo de abertura com <strong>termos importantes</strong> e <code>termos técnicos</code>.</p>

  <h3>Subseção opcional</h3>
  <p>Conteúdo da subseção.</p>

</section>
```

---

## BLOCO 4 — Section fechamento (sempre a última)

```html
<section class="section section-close" id="sec-N">
  <header class="section-head">
    <span class="section-index">Fechamento</span>
    <h2>O que levamos desta aula</h2>
  </header>

  <ul class="checklist">
    <li>Ponto principal 1.</li>
    <li>Ponto principal 2.</li>
    <li>Ponto principal 3.</li>
    <li>Na próxima aula vamos <strong>tópico da próxima aula</strong>.</li>
  </ul>

  <p class="footer-note">
    Material produzido pelo Prof. Toni Coimbra · <span class="mono">aulas.tonicoimbra.com</span>
  </p>
</section>
```

---

## BLOCO 5 — Callout verde (objetivo / entrega / definição positiva)

Mapeia: `:::objetivo`, `:::entrega`, `:::resultado`

```html
<aside class="callout c-primary">
  <div class="callout-mark" aria-hidden="true">✓</div>
  <div class="callout-body">
    <p class="callout-title">Entrega da aula</p>
    <p class="callout-text">Descrição clara do que o aluno vai produzir ou aprender.</p>
  </div>
</aside>
```

Outros marks válidos: `★` `▲` `↑`

---

## BLOCO 6 — Callout roxo (desafio / importante / extra)

Mapeia: `:::desafio`, `:::importante`, `:::extra`

```html
<aside class="callout c-secondary">
  <div class="callout-mark" aria-hidden="true">+</div>
  <div class="callout-body">
    <p class="callout-title">Desafio da aula</p>
    <p class="callout-text">Descrição do desafio. Indique o tempo estimado ao final.</p>
  </div>
</aside>
```

Outros marks válidos: `★` `◆`

---

## BLOCO 7 — Callout ciano (conceito / dica / informação / curiosidade / exemplo)

Mapeia: `:::conceito`, `:::definicao`, `:::dica`, `:::curiosidade`, `:::exemplo`

```html
<aside class="callout c-tertiary">
  <div class="callout-mark" aria-hidden="true">i</div>
  <div class="callout-body">
    <p class="callout-title">Nome do conceito</p>
    <p class="callout-text">Definição ou dica clara e direta.</p>
  </div>
</aside>
```

Outros marks válidos: `?` `✦`

---

## BLOCO 8 — Callout amarelo (erro comum / atenção)

Mapeia: `:::atencao`, `:::aviso`, `:::erro` (não crítico)

```html
<aside class="callout c-warning">
  <div class="callout-mark" aria-hidden="true">!</div>
  <div class="callout-body">
    <p class="callout-title">Título do erro ou alerta</p>
    <p class="callout-text"><strong>Sintoma:</strong> o que o aluno vê quando erra.<br><strong>Solução:</strong> o que fazer para corrigir.</p>
  </div>
</aside>
```

---

## BLOCO 9 — Callout vermelho (erro crítico — use com parcimônia)

Mapeia: `:::erro-critico`

```html
<aside class="callout c-error">
  <div class="callout-mark" aria-hidden="true">✗</div>
  <div class="callout-body">
    <p class="callout-title">Título do erro crítico</p>
    <p class="callout-text">Descrição do problema grave e como resolver.</p>
  </div>
</aside>
```

---

## BLOCO 10 — Code-shell HTML (com highlight manual)

```html
<div class="code-shell">
  <header class="code-top">
    <span class="dot dot-red"></span>
    <span class="dot dot-yellow"></span>
    <span class="dot dot-green"></span>
    <span class="code-lang">html</span>
  </header>
<pre><code><span class="tag">&lt;form</span> <span class="attr">id</span>=<span class="str">"meu-form"</span><span class="tag">&gt;</span>
  <span class="tag">&lt;label</span> <span class="attr">for</span>=<span class="str">"nome"</span><span class="tag">&gt;</span>Nome:<span class="tag">&lt;/label&gt;</span>
  <span class="tag">&lt;input</span> <span class="attr">type</span>=<span class="str">"text"</span> <span class="attr">id</span>=<span class="str">"nome"</span> <span class="attr">required</span><span class="tag">&gt;</span>
  <span class="tag">&lt;button</span> <span class="attr">type</span>=<span class="str">"submit"</span><span class="tag">&gt;</span>Enviar<span class="tag">&lt;/button&gt;</span>
<span class="tag">&lt;/form&gt;</span></code></pre>
</div>
```

---

## BLOCO 10-FB — Code-shell HTML (fallback sem highlight)

Use este formato sempre que houver dúvida sobre a aplicação dos `<span>` de highlight. **Mantém o escape de `<`/`>`**, apenas omite os spans coloridos.

```html
<div class="code-shell">
  <header class="code-top">
    <span class="dot dot-red"></span>
    <span class="dot dot-yellow"></span>
    <span class="dot dot-green"></span>
    <span class="code-lang">html</span>
  </header>
<pre><code>&lt;form id="meu-form"&gt;
  &lt;label for="nome"&gt;Nome:&lt;/label&gt;
  &lt;input type="text" id="nome" required&gt;
  &lt;button type="submit"&gt;Enviar&lt;/button&gt;
&lt;/form&gt;</code></pre>
</div>
```

---

## BLOCO 11 — Code-shell CSS

```html
<div class="code-shell">
  <header class="code-top">
    <span class="dot dot-red"></span>
    <span class="dot dot-yellow"></span>
    <span class="dot dot-green"></span>
    <span class="code-lang">css</span>
  </header>
<pre><code><span class="tag">body</span> {
  <span class="prop">background</span>: <span class="str">#f1f5f9</span>;
  <span class="prop">font-family</span>: Arial, sans-serif;
  <span class="prop">font-size</span>: <span class="num">16px</span>;
}</code></pre>
</div>
```

---

## BLOCO 12 — Code-shell JavaScript

```html
<div class="code-shell">
  <header class="code-top">
    <span class="dot dot-red"></span>
    <span class="dot dot-yellow"></span>
    <span class="dot dot-green"></span>
    <span class="code-lang">javascript</span>
  </header>
<pre><code><span class="tag">const</span> btn = document.querySelector(<span class="str">'#meu-form'</span>);
btn.addEventListener(<span class="str">'submit'</span>, <span class="tag">function</span>(e) {
  e.preventDefault();
  <span class="com">// lógica aqui</span>
});</code></pre>
</div>
```

---

## BLOCO 13 — Code-shell Bash / Terminal

```html
<div class="code-shell">
  <header class="code-top">
    <span class="dot dot-red"></span>
    <span class="dot dot-yellow"></span>
    <span class="dot dot-green"></span>
    <span class="code-lang">bash</span>
  </header>
<pre><code>npm init -y
npm install express cors sqlite3
node server.js</code></pre>
</div>
```

---

## BLOCO 14 — Code-shell Árvore de pastas

```html
<div class="code-shell">
  <header class="code-top">
    <span class="dot dot-red"></span>
    <span class="dot dot-yellow"></span>
    <span class="dot dot-green"></span>
    <span class="code-lang">árvore</span>
  </header>
<pre><code>projeto/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
└── backend/
    └── server.js</code></pre>
</div>
```

---

## BLOCO 15 — Demo-wrap com formulário

```html
<div class="demo-wrap">
  <div class="demo-label">Renderizado no navegador</div>
  <div class="demo-body">
    <div style="background:#fff;padding:20px;border-radius:8px;font-family:Arial,sans-serif;color:#0f172a">
      <form onsubmit="event.preventDefault()" style="display:flex;flex-direction:column;gap:10px">
        <label style="font-size:.9rem;color:#334155">
          Nome:
          <input type="text" style="display:block;margin-top:4px;padding:8px;border:1px solid #cbd5e1;border-radius:6px;width:100%">
        </label>
        <button type="submit" style="padding:10px;background:#2563eb;color:white;border:none;border-radius:6px;cursor:pointer">
          Enviar
        </button>
      </form>
    </div>
  </div>
</div>
```

---

## BLOCO 16 — Demo-wrap com tabela

```html
<div class="demo-wrap">
  <div class="demo-label">Renderizado no navegador</div>
  <div class="demo-body">
    <table class="demo">
      <thead>
        <tr><th>Coluna A</th><th>Coluna B</th><th>Coluna C</th></tr>
      </thead>
      <tbody>
        <tr><td>Dado 1</td><td>Dado 2</td><td>Dado 3</td></tr>
        <tr><td>Dado 4</td><td>Dado 5</td><td>Dado 6</td></tr>
      </tbody>
      <tfoot>
        <tr><td colspan="3">Rodapé da tabela</td></tr>
      </tfoot>
    </table>
  </div>
</div>
```

---

## BLOCO 17 — Roteiro do professor

Mapeia: `:::roteiro`

```html
<aside class="roteiro">
  <header class="roteiro-head">
    <span class="roteiro-chip">Roteiro do professor</span>
  </header>
  <p>Texto em primeira pessoa para o professor. Imperativo direto: "Mostre no projetor...", "Peça que os alunos...", "Reserve X minutos para...".</p>
  <p>Segundo parágrafo se necessário — dicas de ritmo, turmas heterogêneas, sugestões de extensão.</p>
</aside>
```

Regra: sempre **último bloco antes do fechamento** de uma section, nunca no meio do conteúdo principal.

---

## BLOCO 18 — Checklist

Mapeia: `:::resumo` (dentro de `.section-close`)

```html
<ul class="checklist">
  <li>Primeiro item verificável.</li>
  <li>Segundo item com <strong>negrito</strong> e <code>código</code>.</li>
  <li>Terceiro item.</li>
</ul>
```

---

## BLOCO 19 — Tags (pílulas de vocabulário)

Mapeia: `:::vocabulario`

```html
<ul class="tags">
  <li>&lt;table&gt;</li>
  <li>&lt;thead&gt;</li>
  <li>colspan</li>
  <li>fetch()</li>
  <li>async/await</li>
</ul>
```

Escape `<` e `>` em tags HTML: `&lt;table&gt;`

---

## BLOCO 20 — Atividade avaliativa (lista ordenada + entrega)

```html
<ol>
  <li>Instrução 1 da atividade.</li>
  <li>Instrução 2 com <strong>destaque</strong> e <code>código</code>.</li>
  <li>Instrução 3.</li>
</ol>

<aside class="callout c-primary">
  <div class="callout-mark" aria-hidden="true">↑</div>
  <div class="callout-body">
    <p class="callout-title">Entrega</p>
    <p class="callout-text">Enviar o arquivo <strong>index.html</strong> pelo Classroom até a data definida pelo professor.</p>
  </div>
</aside>
```

---

## BLOCO 21 — Questão de fixação (NOVO)

Mapeia: `:::questao` do ProfessorDash. Estrutura completa: enunciado + (opcional) trecho de código + alternativas marcadas + callout de resposta comentada.

### Versão sem código

```html
<h3>Questão de fixação</h3>
<p><strong>Pergunta principal aqui em uma única frase clara?</strong></p>

<ol type="a">
  <li>Texto da alternativa A.</li>
  <li>Texto da alternativa B. <strong>(correta)</strong></li>
  <li>Texto da alternativa C.</li>
  <li>Texto da alternativa D.</li>
</ol>

<aside class="callout c-tertiary">
  <div class="callout-mark" aria-hidden="true">i</div>
  <div class="callout-body">
    <p class="callout-title">Resposta comentada</p>
    <p class="callout-text">Explicação do porquê B é a resposta correta, com referência ao conceito da aula. Em seguida, breve justificativa de por que A, C e D estão erradas.</p>
  </div>
</aside>
```

### Versão com código

```html
<h3>Questão de fixação</h3>
<p>Antes de responder, considere o código abaixo (atenção à <strong>ORDEM</strong> das linhas):</p>

<div class="code-shell">
  <header class="code-top">
    <span class="dot dot-red"></span>
    <span class="dot dot-yellow"></span>
    <span class="dot dot-green"></span>
    <span class="code-lang">javascript</span>
  </header>
<pre><code><!-- código aqui, escapado --></code></pre>
</div>

<p>O usuário preenche e clica em Salvar. <strong>O que acontece, na ordem real?</strong></p>

<ol type="a">
  <li>Alternativa A.</li>
  <li>Alternativa B. <strong>(correta)</strong></li>
  <li>Alternativa C.</li>
  <li>Alternativa D.</li>
</ol>

<aside class="callout c-tertiary">
  <div class="callout-mark" aria-hidden="true">i</div>
  <div class="callout-body">
    <p class="callout-title">Resposta comentada</p>
    <p class="callout-text">Explicação completa do raciocínio.</p>
  </div>
</aside>
```

Convenções obrigatórias:
- `<ol type="a">` gera "a)", "b)", "c)", "d)" automaticamente
- Marque a correta com `<strong>(correta)</strong>` no final do `<li>` (a fonte ProfessorDash usa `*`)
- A explicação vai em `callout c-tertiary` com mark `i` e título "Resposta comentada"
- Não use mark "?" para questão — é callout informativo, não pergunta sem resposta

---

## BLOCO 22 — Mini-exemplo de calibração

Quando precisar mostrar um pareamento "código antes → resultado depois" curto em uma section. Útil em aulas que comparam abordagens.

```html
<h3>Antes</h3>
<div class="code-shell">
  <header class="code-top">
    <span class="dot dot-red"></span>
    <span class="dot dot-yellow"></span>
    <span class="dot dot-green"></span>
    <span class="code-lang">javascript</span>
  </header>
<pre><code>form.addEventListener(<span class="str">'submit'</span>, <span class="tag">function</span>(e) {
  <span class="com">// sem preventDefault</span>
  console.log(<span class="str">'enviou'</span>);
});</code></pre>
</div>

<p><strong>Comportamento:</strong> a página recarrega antes do log aparecer.</p>

<h3>Depois</h3>
<div class="code-shell">
  <header class="code-top">
    <span class="dot dot-red"></span>
    <span class="dot dot-yellow"></span>
    <span class="dot dot-green"></span>
    <span class="code-lang">javascript</span>
  </header>
<pre><code>form.addEventListener(<span class="str">'submit'</span>, <span class="tag">function</span>(e) {
  e.preventDefault();
  console.log(<span class="str">'enviou'</span>);
});</code></pre>
</div>

<p><strong>Comportamento:</strong> o log aparece, a página fica intacta.</p>
```
