---
name: aula-estatica
description: Transforma conteúdo de aula (markdown com sintaxe :::tipo do ProfessorDash, texto colado, descrição oral ou outra apostila) em um arquivo HTML standalone único seguindo o design system visual de aulas.tonicoimbra.com. Use SEMPRE que o usuário pedir "aplica skill aula-estatica", "transforma essa aula em apostila HTML", "apostila HTML para distribuir", "gera versão estática da Aula NN", "aula em arquivo único", "converte para o padrão tonicoimbra" ou "salvar PDF da aula". Use também sempre que o usuário enviar um arquivo .md de aula sem outra instrução clara — assuma que ele quer a versão estática. Distinta de skills que enviam conteúdo para ProfessorDash: esta produz UM .html para download e distribuição offline. O resultado tem CSS, JS e SVG embutidos, abre com duplo clique no navegador, alterna entre dark/light e exporta PDF via window.print() com layout A4.
---

# Skill: Apostila HTML Estática — Prof Toni Coimbra

## O que esta skill faz

Transforma qualquer conteúdo de aula em uma **apostila HTML standalone** seguindo o design system visual de `aulas.tonicoimbra.com`. O resultado é um único arquivo `.html` que:

- Abre com duplo clique no navegador, sem servidor, sem instalação
- Funciona offline após o primeiro carregamento das fontes Google
- Tem botão de alternar entre modo escuro e claro (com memória em `localStorage`)
- Tem botão "Salvar PDF" que usa `window.print()` com layout A4 e o roteiro do professor oculto
- É visualmente idêntico independente de qual IA o gerou

Esta skill foi projetada para ser usada com **qualquer LLM**: Claude, ChatGPT, Gemini, Hermes, Mistral. Todos os valores são explícitos no design system — a IA não precisa adivinhar nada.

---

## Arquivos desta skill

| Arquivo | Propósito |
|---|---|
| `SKILL.md` (este arquivo) | Frontmatter, gatilhos, fluxo, regras invioláveis |
| `DESIGN_SYSTEM.md` | Tokens, cores, escalas, componentes, mapeamentos, exemplo antes/depois |
| `BLOCOS.md` | Catálogo de snippets HTML prontos copiáveis por componente |
| `template.html` | Template standalone aprovado — ponto de partida obrigatório |

---

## Gatilhos — quando usar esta skill

Use quando o usuário pedir:

- "aplica skill aula-estatica em [conteúdo]"
- "transforma essa aula em apostila HTML"
- "gera versão estática da Aula X"
- "apostila HTML para distribuir para os alunos"
- "aula em arquivo único / standalone"
- "converte esse conteúdo para o padrão tonicoimbra"
- "salvar PDF da aula"
- Quando o usuário envia um arquivo `.md` de aula sem outra instrução clara

**Não use** para conteúdo que vai para o ProfessorDash (que tem renderizador próprio de Markdown com sintaxe `:::tipo`).

---

## Fluxo obrigatório

### Passo 1 — Receber o conteúdo

O conteúdo pode vir de qualquer fonte:
- Texto colado diretamente na conversa
- Arquivo Markdown com sintaxe `:::tipo` do ProfessorDash
- Markdown comum sem callouts
- Descrição oral do que a aula deve conter
- Outra apostila para ser reformatada

### Passo 2 — Abrir o `template.html`

O `template.html` já contém:
- CSS completo embutido em `<style>`
- JavaScript embutido em `<script>` (toggle de tema + ano dinâmico)
- SVG do logo oficial inline (duas cores: ciano `#00B4D8` e azul `#023E8A`)

**Não reescreva o CSS, JS ou SVG.** Use o template como está e preencha apenas o conteúdo marcado com `<!-- [EDIT-*] -->` ou `<!-- [EDIT] -->`. Remova esses comentários após preencher.

### Passo 3 — Mapear o conteúdo nos componentes

Use a **Tabela A — ProfessorDash → Componente** abaixo (cobre todos os `:::tipo`) e os snippets do `BLOCOS.md`. Quando o conteúdo vier sem callouts (markdown puro), use a **Tabela B — Tipo de conteúdo → Componente** em `DESIGN_SYSTEM.md` seção 9.

#### Tabela A — Mapeamento ProfessorDash → Componente HTML

| Sintaxe no markdown | Componente HTML | Mark | Cor |
|---|---|---|---|
| `:::objetivo` | `callout c-primary` | `✓` | verde |
| `:::entrega` | `callout c-primary` | `↑` | verde |
| `:::resultado` | `callout c-primary` | `★` | verde |
| `:::conceito` | `callout c-tertiary` | `i` | ciano |
| `:::definicao` | `callout c-tertiary` | `i` | ciano |
| `:::dica` | `callout c-tertiary` | `i` | ciano |
| `:::curiosidade` | `callout c-tertiary` | `✦` | ciano |
| `:::exemplo` | `callout c-tertiary` | `i` | ciano |
| `:::atencao` | `callout c-warning` | `!` | amarelo |
| `:::aviso` | `callout c-warning` | `!` | amarelo |
| `:::erro` (não crítico) | `callout c-warning` | `!` | amarelo |
| `:::erro-critico` | `callout c-error` | `✗` | vermelho |
| `:::importante` | `callout c-secondary` | `+` | roxo |
| `:::desafio` | `callout c-secondary` | `★` | roxo |
| `:::extra` | `callout c-secondary` | `+` | roxo |
| `:::roteiro` | `.roteiro` (oculto na impressão) | — | ciano dashed |
| `:::resumo` | `.checklist` dentro de `.section.section-close` | — | — |
| `:::vocabulario` | `.tags` (pílulas) | — | — |
| `:::questao` | Componente "Questão de fixação" (BLOCOS.md §21) | — | — |
| `:::codigo` ou ` ``` ` | `.code-shell` com syntax highlight manual | — | — |
| `:::demo` ou bloco HTML real | `.demo-wrap` | — | — |

Texto comum entre callouts vira `<p>` direto na section. Sub-tópicos viram `<h3>`.

### Passo 4 — Definir o accent do título

Escolha **uma palavra** do título para receber o gradient ciano→roxo (`<span class="accent">`). Deve ser o conceito central da aula, não palavras genéricas.

Exemplos corretos: `HTML`, `CSS`, `JavaScript`, `CRUD`, `Node.js`, `semântico`, `formulários`, `tabelas`
Exemplos errados: `Aula`, `Parte`, `Introdução`, `Conteúdo`

### Passo 5 — Syntax highlighting em code-shells

O highlighting manual com `<span>` (documentado no DESIGN_SYSTEM §5.6) é o ideal, mas é frágil. **Fallback aceitável: se houver qualquer dúvida sobre escape ou classes, omita os spans de highlight.** Um code-shell sem spans renderiza com cor neutra mas íntegro — melhor que um code-shell quebrado.

A regra de escape é inegociável: dentro de `<pre><code>`, todo `<` vira `&lt;` e todo `>` vira `&gt;`, **com ou sem highlight**.

```html
<!-- Forma ideal (com highlight) -->
<pre><code><span class="tag">&lt;input</span> <span class="attr">type</span>=<span class="str">"text"</span><span class="tag">&gt;</span></code></pre>

<!-- Forma de fallback (sem highlight, mas escapada) -->
<pre><code>&lt;input type="text"&gt;</code></pre>
```

Nunca deixe `<` ou `>` literais dentro de `<pre><code>`.

### Passo 6 — Voz e tom

Esta skill controla o visual, **não** o tom. Preserve a voz do autor:

- Mantenha a segunda pessoa ("você", "preencha", "olhe")
- Mantenha analogias, gírias técnicas e exemplos concretos
- Não "polir" para um tom corporativo neutro
- Não cortar humor, ironia ou referências culturais
- Não adicionar disclaimers tipo "consulte um especialista" — não é a voz do material
- Resista a "melhorar" parágrafos: faça apenas pequenos ajustes para encaixar no componente (ex: remover marcadores `**bold**` redundantes quando já há `<strong>`)

Se o conteúdo de origem for muito longo para uma seção, divida em duas sections — não corte texto.

### Passo 7 — Validar antes de entregar

Checklist obrigatório:

- [ ] Um único `<h1>` na página (dentro de `.hero-title`)
- [ ] Um único `<span class="accent">` na página
- [ ] CSS embutido em `<style>` (sem `<link rel="stylesheet">` para arquivo local)
- [ ] JS embutido em `<script>` (sem `<script src="">` para arquivo local)
- [ ] SVG do logo inline (sem `<img src="favicon.svg">`)
- [ ] Fontes via Google Fonts CDN (único link externo permitido)
- [ ] Todos os `<` e `>` dentro de `<pre><code>` escapados como `&lt;` e `&gt;`
- [ ] Cada `id="sec-N"` nas sections bate com um `href="#sec-N"` no sumário
- [ ] Última section tem a classe `section-close`
- [ ] Apenas um `</main>` (o template histórico tinha um duplicado — confira)
- [ ] `<title>` no formato: `Aula NN · Tema curto · Prof Toni Coimbra`
- [ ] Topbar disciplina preenchida (substitui `[EDIT-DISCIPLINA]`)
- [ ] Nenhum comentário `<!-- [EDIT...] -->` restante no body
- [ ] Arquivo nomeado em kebab-case sem acento: `aula-NN-tema-curto.html`

### Passo 8 — Entregar

Salve o arquivo e apresente ao usuário. Informe as três formas de uso:
1. **Abrir direto** — duplo clique no arquivo
2. **PDF** — botão "Salvar PDF" na topbar
3. **Hospedar** — GitHub Pages, Netlify Drop, Cloudflare Pages ou qualquer servidor estático

---

## Regras invioláveis

1. **Nunca reescreva o CSS do design system.** Se precisar de um ajuste pequeno, adicione uma regra ao final do `<style>`, nunca edite as regras existentes.

2. **Nunca use `<h1>` fora do `.hero-title`.** Seções usam `<h2>`. Subseções usam `<h3>`.

3. **Nunca coloque mais de um `<span class="accent">` por página.**

4. **Nunca invente componentes novos.** Use apenas os documentados em `BLOCOS.md`. Conteúdo sem componente correspondente vira `<p>` simples.

5. **Código dentro de `<pre><code>` é sempre escapado** (`<` → `&lt;`, `>` → `&gt;`), com ou sem highlight.

6. **O `.roteiro` é sempre o último bloco antes do fechamento** de uma seção — nunca no meio do conteúdo principal.

7. **A última section sempre tem `class="section section-close"`** com checklist de fechamento e `.footer-note`.

8. **Preserve a voz do autor.** Não polir, não normalizar tom, não cortar humor ou exemplos concretos.

9. **Não toque no SVG do logo.** As duas cores `#00B4D8` e `#023E8A` são fixas no SVG por decisão de marca; o CSS não deve sobrescrever via `fill: currentColor`.

10. **Comentários HTML nunca contêm `-->` literais.** O parser HTML fecha o comentário no PRIMEIRO `-->` que encontra — não há aninhamento. Se precisar mencionar um comentário-marcador dentro de outro comentário (ex: "substitua os marcadores `[EDIT]`"), reescreva sem usar `<!-- -->` literais. Erro típico: escrever `<!-- Substitua <!-- [EDIT] --> pelo conteúdo -->` faz o comentário fechar cedo e o texto restante vira HTML visível no topo da página.

---

## Estrutura canônica de uma aula

```
topbar
└── hero (h1, eyebrow, lead, meta-grid)
└── sumário (nav com 4–8 itens)
└── section id="sec-1" (objetivo/definição)
└── section id="sec-2" (conceito ou pré-requisitos)
└── section id="sec-3" (passo a passo / prática)
└── section id="sec-4" (checkpoint)
└── section id="sec-5" (erros comuns)
└── section id="sec-6" (desafio + roteiro)
└── section.section-close id="sec-7" (fechamento com checklist)
footer
```

Número de seções: mínimo 4, máximo 8. Ajuste conforme o volume.

---

## Nota para uso em ChatGPT, Gemini, Hermes ou outros LLMs

Ao usar esta skill em um LLM que não é o Claude:

1. Forneça `DESIGN_SYSTEM.md` e `BLOCOS.md` como arquivos de contexto ou cole o conteúdo no prompt de sistema.
2. Forneça o `template.html` e instrua a IA a **preencher o template**, não gerar HTML do zero.
3. Instrua: *"Não reescreva o CSS ou JavaScript do template. Preencha apenas as seções marcadas com `<!-- [EDIT...] -->` e remova esses comentários após o preenchimento."*
4. Se o LLM não conseguir produzir syntax highlighting manual confiável nos code-shells, instrua-o a usar o fallback (sem `<span>`, só escape de `<`/`>`).
5. O resultado deve ser um único arquivo HTML que, aberto no navegador, seja visualmente coerente com o exemplo de referência.
