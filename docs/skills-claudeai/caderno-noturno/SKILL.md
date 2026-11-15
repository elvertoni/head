---
name: "caderno-noturno"
description: "Aplica o design system Caderno Noturno (DS v4 de aulas.tonicoimbra.com) a apostilas, aulas e páginas HTML. Use quando o Toni pedir \"Caderno Noturno\", \"meu design system\" ou \"padrão do portal\"."
---

# Caderno Noturno (DS v4)

É o design system do portal do Toni (aulas.tonicoimbra.com, D.19), usado como **superfície de leitura** ("Caderno de Trilha"). No topo fica uma faixa azul-noite curta, com numeral amarelo e um leque de cartões (anterior / atual / próxima). Abaixo vêm três colunas: a trilha à esquerda, a folha branca no centro e "Nesta aula" / "Neste capítulo" à direita. O aluno lê no tema claro e o professor/admin no escuro, e os dois temas são obrigatórios.

Os tokens são os mesmos do `caderno.css` do ProfessorDash e da skill `aula-estatica` do vault, que é a fonte (esta skill é a derivada para artifacts). Se algo divergir, vale o portal.

Quando o Toni pedir este DS, siga as regras e use o CSS de referência abaixo **sem reinventar o visual**. O CSS é o contrato: copie-o e só acrescente o que faltar, sempre com os mesmos tokens. A apostila de JavaScript (artifact "Apostila de JavaScript", nov/2026) é o exemplo completo aplicado.

## Regras do DS (não negociáveis)

- **O conteúdo começa na primeira dobra.** A identidade fica na faixa noturna curta. Nada de capa de tela cheia nem hero de `100vh`.
- **A largura é ocupada por navegação útil**: a trilha (lista de aulas/capítulos com progresso) e o sumário com o botão Concluir. A linha de texto não alarga: `--cn-measure: 42rem`, sempre em `rem`, nunca em `ch`.
- **Uma linguagem só na página.** O cabeçalho é sempre noturno, com o monograma **TC desenhado pelo Toni** (o corte do T acompanha a curva do C): SVG inline, T em `currentColor`, C **sempre** `#ffd43b`. Copie o SVG da seção "Monograma" exatamente; não redesenhe, não recolore, não troque por texto em fonte.
- **Folha branca sobre papel.** As caixas internas (destaques, objetivos, quiz, diagrama, exercícios) usam `--cn-box`, **sem borda nem faixa lateral colorida**.
- **Código é sempre noturno**, com rótulo da linguagem e botão Copiar, também no tema claro.
- **Botões em pílula** com a cor de ação chapada: azul no claro, amarelo no escuro. O vermelho (`--cn-err`) aparece **só** para erro.
- **Links não são amarelos.** Link é `--cn-link`: azul `#1747c7` no claro, azul-claro `#8dbcf5` no escuro. Amarelo é ação (botão) e destaque (numeral, carta atual, marca).
- **Kickers em cor neutra.** Rótulos curtos (kicker de parte, "Pratique", rótulo do gabarito) são mono 12px em caixa alta na cor `--cn-muted`, nunca na cor de ação.
- **Foco visível de 3px:** azul (`--cn-focus`) na folha e no papel; amarelo (`--cn-hi`) só nas áreas noturnas (faixa, código, cabeçalho de capítulo, Exemplo), onde o azul some.
- **Destaques com ícone em círculo tingido:** o ícone (Lucide, por máscara) e o rótulo `b` vêm na cor do tom; o círculo é o tom a 14% sobre a folha. Nada de círculo chapado com glifo branco.
- **Tipografia:** Archivo 800 nos títulos e numerais, Geist no corpo (≈17,5–18px, line-height 1.75) e JetBrains Mono só em código e rótulos curtos (eyebrows, metadados, kickers em caixa alta com letter-spacing).
- **Sem marcação nova no acervo.** A grade age sobre o HTML que o parser emite. Regras internas da folha usam *container queries* (`container-type: inline-size` na folha).

## Tokens

| Token | Claro (aluno) | Escuro (professor) | Uso |
| --- | --- | --- | --- |
| `--cn-bg` | #f1f0ec | #080c17 | Papel da página |
| `--cn-surface` | #ffffff | #0f1729 | Folha |
| `--cn-box` | #f5f4f0 | #17213a | Destaques, objetivos, quiz, exercícios |
| `--cn-text` | #16181d | #eef2f8 | Texto |
| `--cn-muted` | #555a64 | #a3b1c9 | Metadados, notas |
| `--cn-line` | #e2dfd8 | #1d2a4a | Divisórias de tabela |
| `--cn-action` | #1747c7 | #ffd43b | Botões (Concluir), marcador do sumário |
| `--cn-on-action` | #ffffff | #1b1500 | Texto sobre a cor de ação |
| `--cn-link` | #1747c7 | #8dbcf5 | Links, número do gabarito, ano da linha do tempo |
| `--cn-focus` | #1747c7 | #8dbcf5 | Contorno de foco na folha (nas áreas noturnas, `--cn-hi`) |
| `--cn-ok` | #1c7447 | #5fd08d | Progresso, concluída, Dica |
| `--cn-warn` | #8f5400 | #f2bd4b | Atenção, Importante |
| `--cn-err` | #b93028 | #ff8a80 | Só erro |
| `--cn-hi` | #ffd43b (fixo) | — | Numeral, carta atual, monograma |
| `--cn-night` | #0a0e1a (fixo) | — | Faixa, código, Exemplo, cabeçalho de capítulo |
| `--cn-night-2` / `-3` | #121d36 / #1a2a4d (fixos) | — | Superfícies dentro da noite: chips, cartas, botão de tema, Copiar, ícone do Exemplo |
| `--cn-night-line` | #2a3d66 (fixo) | — | Filetes dentro da noite (topbar, legenda do código) |
| `--cn-night-text` / `-muted` | #f8fafc / #a9b8d0 (fixos) | — | Texto e texto secundário na noite |

Fontes via Google Fonts: `Archivo:wght@800`, `Geist:wght@400;500;600;700`, `JetBrains+Mono:wght@400;500`. No runtime do portal elas são self-hosted em `static/fonts/`.

## Grade

| Largura | Comportamento |
| --- | --- |
| < 760px | Coluna única. Faixa só com texto (numeral acima do título abaixo de 600px), trilha em faixa rolável de números, folha de ponta a ponta |
| 760–1023px | A folha vira cartão com sombra e raio 20px; o leque aparece a partir de 900px |
| 1024–1279px | Folha + coluna "Nesta aula" fixa à direita (240px); a trilha continua em faixa acima |
| ≥ 1280px | Três colunas: trilha 270px fixa · folha · "Nesta aula" 240px |

**Atenção à ordem no DOM:** trilha, aside e main. Por isso cada coluna precisa de `grid-column` e `grid-row` explícitos em cada breakpoint (já estão no CSS). Sem isso, a folha cai na coluna estreita.

## Componentes (marcação)

- **Faixa:** `header.cn-cover > .cn-wrap > .cn-topbar` (`.cn-brand` com `span.cn-mono` contendo o SVG do monograma + o nome "Prof. Toni Coimbra" + `.cn-theme`), `.cn-crumb`, `.cn-hero` (`p.cn-num` com `span.cn-num-hollow` no 1º dígito, bloco com `.cn-eyebrow` + `h1` + `.cn-lead` + `ul.cn-meta`, e `nav.cn-fan` com `.cn-card--prev/--current/--next`, cada um com `.cn-card-top` + `.cn-card-glyph`).
- **Grade:** `.cn-wrap.cn-layout` > `nav.cn-trail` (`.cn-trail-head` com `.cn-kicker`, `.cn-trail-name`, `.cn-trail-status`, `.cn-meter > i`; `ol.cn-steps` com `li.cn-trail-part` e `a` > `.cn-step-num` + `.cn-step-label`, estados `.is-current` / `.is-done`) · `aside.cn-aside` (`.cn-toc` + `.cn-aside-action` com `.cn-btn.cn-btn--action`) · `main.cn-main > article.cn-sheet`.
- **Folha:** `header.cn-part` (`.cn-part-kicker` + `h2`) · `section.cn-chapter` > `header.cn-chead` (bloco noturno: `.cn-cnum` amarelo + `.cn-eyebrow` + `h2` + `.cn-lead`) · `.cn-prose` (h3 Archivo 23px, ids para o sumário) · `footer.cn-cfoot` com o botão Concluir/Marcar como lido.
- **Objetivos:** `section.cn-goals` (kicker "Objetivos" + "Ao final… você será capaz de:" + `ul`; em duas colunas quando a folha ≥ 600px).
- **Destaques:** `section.callout.{conceito|dica|atencao|importante|curiosidade|exemplo|erro}` > `div.ic` (vazio, `aria-hidden="true"`; o ícone vem da máscara do tipo) + `div.ct` (`b` "Dica · título" + conteúdo). Tons: conceito e curiosidade azul (`--cn-link`), dica verde, atenção e importante `--cn-warn` com fundo levemente tingido, erro vermelho (só erro), `exemplo` noturno com ícone azul-claro sobre `--cn-night-3`.
- **Código:** `figure.cn-code > figcaption (span rótulo + button.cn-copy) + pre > code`. A saída do console usa `.cn-code.is-out` (caixa clara, sem Copiar). Realce de sintaxe por classes Pygments (`.k` amarelo, `.s` verde, `.mi`/`.kc` laranja, `.nf`/`.nb` azul-claro, `.c1` cinza-azulado itálico).
- **Exercícios:** `section.cn-ex` (kicker "Pratique" + `h3` + níveis em `h4` pílula: Fixação / Prática / Desafio + `ol` com numeração contínua).
- **Linha do tempo:** `ol.timeline > li(.big) > span.y + span.d + span.t(b + texto)`.
- **Gabarito:** `details > summary(span "Capítulo 01" + título + em contagem)` com `.cn-gab` (`.cn-gab-n` número + `.cn-gab-a` resposta).
- **Tabelas** sempre dentro de `div.cn-table` (overflow-x), com cabeçalho em mono maiúsculo sobre `--cn-box`.

## Comportamento (JS)

1. **Tema:** o botão alterna `data-theme` no `<html>`, partindo do `prefers-color-scheme`. Guarde a escolha em `localStorage`, dentro de try/catch.
2. **Copiar:** `navigator.clipboard.writeText` dentro do clique. Se falhar, selecione o texto. O botão mostra "Copiado" por 1,6 s.
3. **Trilha e sumário:** o scrollspy marca o capítulo atual (`.is-current` + `aria-current`) e reconstrói o "Neste capítulo" com os `h3[id]`, destacando a seção atual.
4. **Progresso:** "Marcar como lido" por capítulo, salvo em `localStorage` (só neste navegador; avise na `.cn-aside-note`). Atualiza o medidor, a contagem e o ✓ na trilha.
5. Em artifacts não existe `window.print()`. Não ofereça botão de imprimir/PDF.

## Checklist antes de entregar

- [ ] Os dois temas funcionam: sem `data-theme` (sistema), com `light` e com `dark`.
- [ ] Sem rolagem horizontal em 400px, 1100px e 1440px. Tabelas e código rolam dentro do próprio contêiner.
- [ ] A folha fica na coluna central em ≥ 1280px.
- [ ] Nenhuma caixa interna com borda ou faixa lateral colorida; vermelho só em erro.
- [ ] O monograma é o SVG da seção "Monograma" (C amarelo), não "TC" em texto.
- [ ] Kickers em `--cn-muted`; links em `--cn-link` (nunca amarelos).
- [ ] Tab mostra foco azul na folha e amarelo na faixa e no código.
- [ ] Todo bloco de código é noturno e tem rótulo e Copiar.
- [ ] Sem `:::` nem marcadores de build sobrando no HTML.

## Monograma (copiar exatamente)

```html
<span class="cn-mono"><svg viewBox="0 0 403.93 226.77" xmlns="http://www.w3.org/2000/svg" focusable="false" aria-hidden="true"><path fill="currentColor" d="M70.87 0.00L127.56 0.00L226.77 0.00L226.77 0.08C201.18 16.55 181.53 41.46 171.75 70.87L127.56 70.87L127.56 226.77L70.87 226.77L70.87 70.87L0.00 70.87L0.00 0.00L70.87 0.00Z"/><path fill="#ffd43b" d="M299.54 170.08L403.93 170.08L403.93 226.77L299.54 226.77C268.23 226.77 239.88 214.08 219.36 193.56C198.84 173.04 186.15 144.69 186.15 113.39C186.15 82.08 198.84 53.73 219.36 33.21C239.88 12.69 268.23 0.00 299.54 0.00L403.93 0.00L403.93 56.69L299.54 56.69C283.88 56.69 269.71 63.04 259.45 73.30C249.19 83.55 242.84 97.73 242.84 113.39C242.84 129.04 249.19 143.22 259.45 153.48C269.71 163.73 283.88 170.08 299.54 170.08Z"/></svg></span>
```

## CSS de referência (copiar inteiro)

```css
:root {
  --cn-bg: #f1f0ec; --cn-surface: #ffffff; --cn-box: #f5f4f0; --cn-text: #16181d;
  --cn-muted: #555a64; --cn-line: #e2dfd8; --cn-action: #1747c7; --cn-on-action: #ffffff;
  --cn-link: #1747c7; --cn-focus: #1747c7;
  --cn-ok: #1c7447; --cn-warn: #8f5400; --cn-err: #b93028;
  --cn-hi: #ffd43b; --cn-night: #0a0e1a; --cn-night-2: #121d36; --cn-night-3: #1a2a4d; --cn-night-line: #2a3d66;
  --cn-night-text: #f8fafc; --cn-night-muted: #a9b8d0; --cn-night-blue: #8dbcf5;
  --cn-shadow: 0 1px 2px rgba(22,24,29,.06), 0 12px 32px rgba(22,24,29,.07);
  --cn-measure: 42rem;
  --f-display: 'Archivo', 'Arial Narrow', system-ui, sans-serif;
  --f-body: 'Geist', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --f-mono: 'JetBrains Mono', ui-monospace, 'SFMono-Regular', Consolas, monospace;
  /* ícones dos destaques (Lucide), aplicados por máscara */
  --i-conceito: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5'/%3E%3Cpath d='M9 18h6'/%3E%3Cpath d='M10 22h4'/%3E%3C/svg%3E");
  --i-atencao: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3'/%3E%3Cpath d='M12 9v4'/%3E%3Cpath d='M12 17h.01'/%3E%3C/svg%3E");
  --i-dica: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z'/%3E%3C/svg%3E");
  --i-exemplo: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 5v16'/%3E%3Cpath d='M20.001 19A2 2 0 0022 17V5a2 2 0 00-1.999-2L16 3.002A5 5 0 0012 5a5 5 0 00-4-2H4a2 2 0 00-2 2v12a2 2 0 001.999 2H8a5 5 0 014 2 5 5 0 014-2z'/%3E%3C/svg%3E");
  --i-importante: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z'/%3E%3C/svg%3E");
  --i-curiosidade: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m16.24 7.76-1.804 5.411a2 2 0 0 1-1.265 1.265L7.76 16.24l1.804-5.411a2 2 0 0 1 1.265-1.265z'/%3E%3Ccircle cx='12' cy='12' r='10'/%3E%3C/svg%3E");
  --i-objetivo: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'/%3E%3Ccircle cx='12' cy='12' r='6'/%3E%3Ccircle cx='12' cy='12' r='2'/%3E%3C/svg%3E");
  --i-erro: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'/%3E%3Cpath d='m15 9-6 6'/%3E%3Cpath d='m9 9 6 6'/%3E%3C/svg%3E");
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --cn-bg: #080c17; --cn-surface: #0f1729; --cn-box: #17213a; --cn-text: #eef2f8;
    --cn-muted: #a3b1c9; --cn-line: #1d2a4a; --cn-action: #ffd43b; --cn-on-action: #1b1500;
    --cn-link: #8dbcf5; --cn-focus: #8dbcf5;
    --cn-ok: #5fd08d; --cn-warn: #f2bd4b; --cn-err: #ff8a80; --cn-shadow: 0 0 0 1px #1d2a4a; color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --cn-bg: #080c17; --cn-surface: #0f1729; --cn-box: #17213a; --cn-text: #eef2f8;
  --cn-muted: #a3b1c9; --cn-line: #1d2a4a; --cn-action: #ffd43b; --cn-on-action: #1b1500;
  --cn-link: #8dbcf5; --cn-focus: #8dbcf5;
  --cn-ok: #5fd08d; --cn-warn: #f2bd4b; --cn-err: #ff8a80; --cn-shadow: 0 0 0 1px #1d2a4a; color-scheme: dark;
}
*, *::before, *::after { box-sizing: border-box; }
html { scroll-behavior: smooth; scroll-padding-top: 16px; }
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
body { background: var(--cn-bg); color: var(--cn-text); font: 400 17px/1.7 var(--f-body); -webkit-font-smoothing: antialiased; }
body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10; background: var(--cn-night); }
a { color: var(--cn-link); text-underline-offset: 3px; }
:focus-visible { outline: 3px solid var(--cn-focus); outline-offset: 2px; border-radius: 4px; }
/* nas áreas noturnas o azul some: foco amarelo, link azul-claro */
:is(.cn-cover, .cn-code, .cn-chead, .callout.exemplo) :focus-visible { outline-color: var(--cn-hi); }
:is(.cn-cover, .cn-chead, .callout.exemplo) a:not(.cn-card):not(.cn-brand) { color: var(--cn-night-blue); }
.cn-wrap { max-width: 1440px; margin: 0 auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }

/* faixa noturna */
.cn-cover { background: var(--cn-night); color: var(--cn-night-text); }
.cn-topbar { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding-block: 14px; border-bottom: 1px solid var(--cn-night-line); }
.cn-brand { display: flex; align-items: center; gap: 12px; min-height: 44px; font: 800 15px var(--f-display); letter-spacing: -.01em; color: var(--cn-night-text); text-decoration: none; }
.cn-mono { display: grid; place-items: center; flex: none; color: var(--cn-night-text); }
.cn-mono svg { display: block; width: 50px; height: 28px; }
.cn-theme { border: 0; border-radius: 999px; padding: 8px 14px; background: var(--cn-night-2); color: var(--cn-night-text); font: 600 13px var(--f-body); cursor: pointer; }
.cn-theme:hover { background: var(--cn-night-3); }
.cn-crumb { display: flex; flex-wrap: wrap; gap: 8px; margin: 0; padding-top: 22px; font: 500 12px var(--f-mono); color: var(--cn-night-muted); letter-spacing: .02em; }
.cn-hero { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: clamp(16px, 4vw, 40px); align-items: center; padding-block: 18px 30px; }
.cn-num { margin: 0; font: 800 clamp(84px, 13vw, 168px)/.82 var(--f-display); letter-spacing: -.06em; color: var(--cn-hi); }
.cn-num-hollow { color: transparent; -webkit-text-stroke: 2px var(--cn-hi); }
.cn-eyebrow { margin: 0 0 6px; font: 500 12px var(--f-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--cn-night-muted); }
.cn-hero h1 { margin: 0; font: 800 clamp(30px, 4.6vw, 52px)/1.02 var(--f-display); letter-spacing: -.03em; text-wrap: balance; max-width: 18ch; }
.cn-hero .cn-lead { margin: 12px 0 0; color: var(--cn-night-muted); max-width: 52ch; font-size: 17px; }
.cn-meta { display: flex; flex-wrap: wrap; gap: 8px; list-style: none; margin: 16px 0 0; padding: 0; }
.cn-meta li { padding: 4px 10px; border-radius: 999px; background: var(--cn-night-2); font: 500 12px var(--f-mono); color: var(--cn-night-text); }
.cn-fan { display: none; position: relative; width: 290px; height: 150px; }
.cn-card { position: absolute; top: 10px; width: 104px; height: 132px; border-radius: 14px; padding: 12px; display: flex; flex-direction: column; justify-content: space-between; background: var(--cn-night-2); color: var(--cn-night-text); text-decoration: none; box-shadow: 0 10px 30px rgba(0,0,0,.4); transition: transform .2s; }
.cn-card-top { font: 500 11px var(--f-mono); letter-spacing: .06em; text-transform: uppercase; color: var(--cn-night-muted); }
.cn-card-glyph { font: 800 40px/1 var(--f-display); letter-spacing: -.04em; }
.cn-card--prev { left: 0; transform: rotate(-9deg); }
.cn-card--next { right: 0; transform: rotate(9deg); }
.cn-card--current { left: 93px; top: 0; z-index: 2; background: var(--cn-hi); color: var(--cn-night); }
.cn-card--current .cn-card-top { color: #3a3200; }
a.cn-card:hover { transform: rotate(0) translateY(-4px); }
@media (max-width: 599px) { .cn-hero { grid-template-columns: minmax(0, 1fr); gap: 4px; } .cn-num { font-size: 72px; margin-bottom: 10px; } }
@media (min-width: 900px) { .cn-hero { grid-template-columns: auto minmax(0, 1fr) auto; } .cn-fan { display: block; } }
@media (prefers-reduced-motion: reduce) { .cn-card { transition: none; } }

/* grade */
.cn-layout { display: grid; grid-template-columns: minmax(0, 1fr); gap: 24px; padding-block: 24px 64px; }
.cn-trail { min-width: 0; }
.cn-trail-head { display: none; }
.cn-steps { display: flex; gap: 6px; overflow-x: auto; list-style: none; margin: 0; padding: 0 0 6px; scrollbar-width: thin; }
.cn-steps a { display: flex; align-items: center; gap: 10px; text-decoration: none; color: var(--cn-text); border-radius: 10px; }
.cn-step-num { display: grid; place-items: center; min-width: 36px; height: 36px; padding-inline: 6px; border-radius: 10px; background: var(--cn-surface); box-shadow: inset 0 0 0 1px var(--cn-line); font: 500 13px var(--f-mono); font-variant-numeric: tabular-nums; }
.cn-step-label, .cn-trail-part, .cn-aside { display: none; }
.cn-steps a.is-current .cn-step-num { background: var(--cn-night); color: var(--cn-hi); box-shadow: none; }
.cn-steps a.is-done .cn-step-num { color: var(--cn-ok); box-shadow: inset 0 0 0 1.5px var(--cn-ok); }
.cn-main { min-width: 0; }
.cn-sheet { background: var(--cn-surface); padding: 28px max(16px, env(safe-area-inset-left, 0px)) 40px; margin-inline: calc(-1 * max(16px, env(safe-area-inset-left, 0px))); container-type: inline-size; }
@media (min-width: 760px) { .cn-sheet { margin-inline: 0; border-radius: 20px; box-shadow: var(--cn-shadow); padding: 48px clamp(28px, 6vw, 72px) 56px; } }
@media (min-width: 1024px) {
  .cn-layout { grid-template-columns: minmax(0, 1fr) 240px; }
  .cn-trail { grid-column: 1 / -1; grid-row: 1; }
  .cn-main { grid-column: 1; grid-row: 2; }
  .cn-aside { grid-column: 2; grid-row: 2; display: block; position: sticky; top: calc(16px + env(safe-area-inset-top, 0px)); align-self: start; max-height: calc(100vh - 32px); overflow: auto; }
}
@media (min-width: 1280px) {
  .cn-layout { grid-template-columns: 270px minmax(0, 1fr) 240px; gap: 32px; }
  .cn-main { grid-column: 2; grid-row: 1; }
  .cn-aside { grid-column: 3; grid-row: 1; }
  .cn-trail { grid-column: 1; grid-row: 1; position: sticky; top: calc(16px + env(safe-area-inset-top, 0px)); align-self: start; max-height: calc(100vh - 32px); overflow: auto; padding-right: 4px; }
  .cn-trail-head { display: block; margin-bottom: 14px; }
  .cn-steps { flex-direction: column; overflow: visible; gap: 2px; }
  .cn-steps a { padding: 5px 8px 5px 5px; }
  .cn-steps a:hover { background: var(--cn-box); }
  .cn-step-num { min-width: 30px; height: 30px; font-size: 12px; border-radius: 8px; }
  .cn-step-label { display: block; font-size: 14px; line-height: 1.3; }
  .cn-steps a.is-current { background: var(--cn-surface); box-shadow: var(--cn-shadow); }
  .cn-steps a.is-current .cn-step-label { font-weight: 600; }
  .cn-trail-part { display: block; margin: 14px 0 4px; font: 500 11px var(--f-mono); letter-spacing: .06em; text-transform: uppercase; color: var(--cn-muted); }
}
.cn-kicker { margin: 0; font: 500 11px var(--f-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--cn-muted); }
.cn-trail-name { margin: 4px 0 10px; font: 800 18px/1.15 var(--f-display); letter-spacing: -.01em; }
.cn-trail-status { display: flex; justify-content: space-between; font: 500 12px var(--f-mono); color: var(--cn-muted); font-variant-numeric: tabular-nums; }
.cn-meter { height: 6px; border-radius: 99px; background: var(--cn-line); margin-top: 6px; overflow: hidden; }
.cn-meter i { display: block; height: 100%; width: 0; background: var(--cn-ok); border-radius: inherit; transition: width .3s; }
.cn-toc { background: var(--cn-surface); border-radius: 16px; padding: 18px; box-shadow: var(--cn-shadow); }
.cn-toc-cap { margin: 4px 0 12px; font: 800 17px/1.15 var(--f-display); }
.cn-toc ol { list-style: none; margin: 0; padding: 0 0 0 12px; border-left: 2px solid var(--cn-line); display: grid; gap: 2px; }
.cn-toc a { display: block; padding: 4px 0 4px 10px; margin-left: -14px; border-left: 2px solid transparent; color: var(--cn-muted); text-decoration: none; font-size: 14px; line-height: 1.35; }
.cn-toc a:hover { color: var(--cn-text); }
.cn-toc a[aria-current="location"] { color: var(--cn-text); font-weight: 600; border-left-color: var(--cn-action); }
.cn-aside-action { margin-top: 12px; display: grid; gap: 8px; }
.cn-btn { border: 0; border-radius: 999px; padding: 11px 18px; font: 600 14px var(--f-body); cursor: pointer; }
.cn-btn--action { background: var(--cn-action); color: var(--cn-on-action); }
.cn-btn--action:hover { filter: brightness(1.08); }
.cn-btn.is-done { background: transparent; color: var(--cn-ok); box-shadow: inset 0 0 0 1.5px var(--cn-ok); }
.cn-aside-note { margin: 0; font-size: 12px; color: var(--cn-muted); line-height: 1.45; }

/* folha */
.cn-part { padding-block: 56px 8px; border-top: 1px solid var(--cn-line); margin-top: 56px; }
.cn-part:first-child { border-top: 0; margin-top: 0; padding-top: 0; }
.cn-part-kicker { margin: 0; font: 500 12px var(--f-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--cn-muted); }
.cn-part h2 { margin: 6px 0 8px; font: 800 clamp(30px, 5vw, 44px)/1.02 var(--f-display); letter-spacing: -.03em; text-wrap: balance; }
.cn-chapter { margin-top: 40px; scroll-margin-top: 16px; }
.cn-chead { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 18px; align-items: center; background: var(--cn-night); color: var(--cn-night-text); border-radius: 16px; padding: 20px 22px; }
.cn-cnum { margin: 0; font: 800 clamp(48px, 9vw, 72px)/.85 var(--f-display); letter-spacing: -.05em; color: var(--cn-hi); font-variant-numeric: tabular-nums; }
.cn-chead h2 { margin: 0; font: 800 clamp(24px, 3.4vw, 32px)/1.08 var(--f-display); letter-spacing: -.02em; text-wrap: balance; }
.cn-chead .cn-lead { margin: 6px 0 0; color: var(--cn-night-muted); font-size: 15px; line-height: 1.5; }
.cn-prose { max-width: var(--cn-measure); margin-inline: auto; font-size: 17.5px; line-height: 1.75; }
.cn-prose > * + * { margin-top: 1em; }
:where(.cn-prose) :is(p, ul, ol, figure, table) { margin-block: 0; }
.cn-prose > :first-child { margin-top: 28px; }
.cn-prose h3 { margin: 2.2em 0 0; font: 800 23px/1.2 var(--f-display); letter-spacing: -.015em; text-wrap: balance; scroll-margin-top: 16px; }
.cn-prose h4 { margin: 1.6em 0 0; font: 600 17px/1.3 var(--f-body); }
.cn-prose ul, .cn-prose ol { padding-left: 1.3em; }
.cn-prose li + li { margin-top: .35em; }
.cn-prose li::marker { color: var(--cn-muted); }
.cn-prose strong { font-weight: 600; }
.cn-prose code { font: 500 .86em var(--f-mono); background: var(--cn-box); padding: .12em .36em; border-radius: 5px; overflow-wrap: anywhere; }
.cn-table { overflow-x: auto; }
.cn-prose table { width: 100%; border-collapse: collapse; font-size: 15px; line-height: 1.5; }
.cn-prose th, .cn-prose td { text-align: left; vertical-align: top; padding: 9px 12px; border-bottom: 1px solid var(--cn-line); }
.cn-prose th { font: 500 12px var(--f-mono); letter-spacing: .05em; text-transform: uppercase; color: var(--cn-muted); background: var(--cn-box); }
.cn-prose td code { white-space: nowrap; }

/* código: sempre noturno */
.cn-code { margin: 1.4em 0 0; background: var(--cn-night); border-radius: 12px; overflow: hidden; }
.cn-code figcaption { display: flex; align-items: center; justify-content: space-between; gap: 8px; padding: 7px 8px 7px 14px; border-bottom: 1px solid var(--cn-night-line); font: 500 11px var(--f-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--cn-night-muted); }
.cn-copy { border: 0; border-radius: 999px; padding: 4px 11px; background: var(--cn-night-2); color: var(--cn-night-text); font: 600 12px var(--f-body); cursor: pointer; }
.cn-copy:hover { background: var(--cn-night-3); }
.cn-code pre { margin: 0; padding: 14px 16px 16px; overflow-x: auto; }
.cn-code pre code { font: 400 14px/1.65 var(--f-mono); color: #e6ebf5; background: none; padding: 0; white-space: pre; overflow-wrap: normal; }
.cn-code.is-out { background: var(--cn-box); box-shadow: inset 0 0 0 1px var(--cn-line); }
.cn-code.is-out figcaption { color: var(--cn-muted); border-bottom-color: var(--cn-line); }
.cn-code.is-out pre code { color: var(--cn-text); }
.cn-code .c, .cn-code .c1, .cn-code .cm { color: #7d8bab; font-style: italic; }
.cn-code .k, .cn-code .kd, .cn-code .kr, .cn-code .kn, .cn-code .nt { color: #ffd43b; }
.cn-code .kc, .cn-code .mi, .cn-code .mf, .cn-code .m { color: #f2a65a; }
.cn-code .s, .cn-code .s1, .cn-code .s2, .cn-code .sb, .cn-code .sa, .cn-code .si { color: #5fd08d; }
.cn-code .nb, .cn-code .nf, .cn-code .na { color: #8fb4ff; }
.cn-code .o, .cn-code .p { color: #c9d3e6; }

/* destaques: caixa sem borda nem faixa lateral; ícone em círculo tingido na cor do tom */
.callout { --tone: var(--cn-link); --i: var(--i-conceito); display: grid; grid-template-columns: 36px minmax(0, 1fr); gap: 14px; margin-top: 1.4em; padding: 16px 18px; border-radius: 16px; background: var(--cn-box); }
.callout .ic { display: grid; place-items: center; width: 36px; height: 36px; border-radius: 50%; color: var(--tone); background: color-mix(in srgb, var(--tone) 14%, var(--cn-surface)); }
.callout .ic::before { content: ""; width: 20px; height: 20px; background: currentColor; -webkit-mask: var(--i) center / contain no-repeat; mask: var(--i) center / contain no-repeat; }
.callout .ct { min-width: 0; font-size: 16px; line-height: 1.7; }
.callout .ct > b { display: block; color: var(--tone); font: 650 15px/1.5 var(--f-body); margin-bottom: 2px; padding-top: 6px; }
.callout .ct > * + * { margin-top: .7em; }
.callout :not(pre) > code { background: var(--cn-surface); }
.callout.dica { --tone: var(--cn-ok); --i: var(--i-dica); }
.callout.atencao { --tone: var(--cn-warn); --i: var(--i-atencao); background: color-mix(in srgb, var(--cn-warn) 8%, var(--cn-surface)); }
.callout.importante { --tone: var(--cn-warn); --i: var(--i-importante); background: color-mix(in srgb, var(--cn-warn) 8%, var(--cn-surface)); }
.callout.curiosidade { --i: var(--i-curiosidade); }
.callout.erro { --tone: var(--cn-err); --i: var(--i-erro); background: color-mix(in srgb, var(--cn-err) 8%, var(--cn-surface)); }
.callout.exemplo { --tone: var(--cn-night-blue); --i: var(--i-exemplo); background: var(--cn-night); color: var(--cn-night-text); }
.callout.exemplo .ic { background: var(--cn-night-3); }
.callout.exemplo :not(pre) > code { background: var(--cn-night-3); color: var(--cn-night-text); }
@media (max-width: 479px) { .callout { grid-template-columns: minmax(0, 1fr); gap: 10px; } }

/* objetivos e exercícios */
.cn-goals { margin-top: 28px !important; padding: 18px 20px; border-radius: 14px; background: var(--cn-box); }
.cn-goals > p { margin: 0; }
.cn-goals ul { margin: 8px 0 0; font-size: 16px; }
@container (min-width: 600px) { .cn-goals ul { columns: 2; column-gap: 28px; } .cn-goals li { break-inside: avoid; } }
.cn-ex { margin-top: 2.6em; padding: 22px clamp(16px, 4vw, 28px) 26px; border-radius: 16px; background: var(--cn-box); }
.cn-ex-kicker { margin: 0; font: 500 12px var(--f-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--cn-muted); }
.cn-ex h4 { display: inline-block; margin: 1.4em 0 .2em; padding: 3px 10px; border-radius: 999px; background: var(--cn-surface); font: 600 12px var(--f-mono); letter-spacing: .06em; text-transform: uppercase; }
.cn-ex li::marker { font: 600 .9em var(--f-mono); color: var(--cn-text); }
.cn-ex > * + * { margin-top: .7em; }

/* linha do tempo */
.timeline { list-style: none; padding: 0 !important; display: grid; }
.timeline li { display: grid; grid-template-columns: 64px 18px minmax(0, 1fr); gap: 10px; margin: 0 !important; }
.timeline .y { font: 600 14px/1.9 var(--f-mono); color: var(--cn-link); text-align: right; }
.timeline .d { position: relative; }
.timeline .d::before { content: ""; position: absolute; left: 8px; top: 0; bottom: 0; width: 2px; background: var(--cn-line); }
.timeline .d::after { content: ""; position: absolute; left: 3px; top: 9px; width: 12px; height: 12px; border-radius: 50%; background: var(--cn-surface); box-shadow: inset 0 0 0 3px var(--cn-link); }
.timeline .t { padding-bottom: 14px; font-size: 16px; line-height: 1.55; }
.timeline .t b { display: block; font-weight: 600; }
.timeline li.big .d::after { background: var(--cn-hi); box-shadow: inset 0 0 0 3px var(--cn-night); }

/* gabarito */
.cn-prose details { background: var(--cn-box); border-radius: 12px; padding: 0 18px; }
.cn-prose details + details { margin-top: 8px; }
.cn-prose summary { cursor: pointer; padding: 12px 0; font-weight: 600; display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 10px; }
.cn-prose summary span { font: 500 12px var(--f-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--cn-muted); }
.cn-prose summary em { margin-left: auto; font: 400 12px var(--f-mono); font-style: normal; color: var(--cn-muted); }
.cn-prose details[open] { padding-bottom: 16px; }
.cn-gab { display: grid; grid-template-columns: 44px minmax(0, 1fr); gap: 10px; padding-top: 14px; border-top: 1px solid var(--cn-line); }
.cn-gab-n { margin: 0; font: 600 14px/1.7 var(--f-mono); color: var(--cn-link); }
.cn-gab-a { min-width: 0; font-size: 16px; }
.cn-cfoot { max-width: var(--cn-measure); margin: 32px auto 0; padding-top: 20px; border-top: 1px solid var(--cn-line); display: flex; justify-content: flex-end; }
```