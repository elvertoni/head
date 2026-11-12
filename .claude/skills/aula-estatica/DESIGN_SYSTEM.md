# Design System da apostila — v4 · Caderno Noturno

Versão **4.0** (decisão #042, 2026-11-12). Fonte de verdade de origem: repositório do ProfessorDash
(`DESIGN.md` — o topo vale sobre o "Histórico Volta Atelier" —, `design-system/caderno-noturno.html`,
`static/css/caderno.css`, `static/css/lesson.css`, `templates/partials/_brand.html`).
Este documento traduz o Caderno Noturno para o formato apostila (arquivo único, offline, A4).
O CSS já está pronto no `template.html`; aqui fica o **porquê** de cada escolha, para que
qualquer IA mantenha a coerência quando o conteúdo pedir algo que o template não prevê.

Sumário: 1 identidade · 2 cor · 3 tipografia · 4 espaço e forma · 5 componentes ·
6 comportamento · 7 impressão · 8 acessibilidade · 9 versões · 10 proibido

---

## 1. Identidade

**Sóbrio e editorial: azul-noite + amarelo na identidade, papel claro e folha branca na leitura.**
O conteúdo começa logo depois da faixa da aula; a apostila é uma folha de estudo, não um slide.

- **Marca:** monograma **TC** desenhado pelo Toni (o corte do T acompanha a curva do C). Inline no
  cabeçalho exatamente como está no template (paths de `_brand.html`): T em `currentColor`, C
  **sempre** amarelo `#ffd43b`. Não redesenhe, não recolora. Arquivos: `assets/logo.svg` (fundo
  escuro) e `assets/favicon.svg` (fundo `#0a0e1a`).
- **Cabeçalho sempre noturno**, nos dois temas, com a marca, Sumário, tema, PDF sem respostas e
  Salvar PDF (pílula amarela).
- **Faixa noturna da aula** (`.lesson-header`): numeral amarelo grande, rótulo em mono, título
  Archivo 800, lead, chips, metadados e a capa ilustrada ao lado.
- **Assinatura:** "Prof. Toni Coimbra" em Archivo 800; rodapé `Material produzido pelo Prof. Toni
  Coimbra · aulas.tonicoimbra.com`.
- **Tema:** abre **claro** (no portal, aluno = claro); o aluno troca no botão e a escolha fica salva
  (`localStorage: apostila-theme`). O escuro é o azul-noite com ação amarela.

## 2. Cor

Tokens iguais ao `caderno.css`. Cada cor tem **função**; não use cor como enfeite.

| Token | Escuro (`:root`) | Claro (`[data-theme='light']`) | Função |
|---|---|---|---|
| `--ink` | `#080c17` | `#f1f0ec` (papel) | fundo da página |
| `--panel` | `#0f1729` | `#ffffff` (folha) | folha de leitura, fundo das alternativas |
| `--panel-2` | `#17213a` | `#f5f4f0` | caixa: callout, quiz, diagrama, tabela |
| `--line` / `--line-2` / `--line-ui` | `#1d2a4a` / `#2f4170` / `#47598a` | `#e2dfd8` / `#cfcbc2` / `#a9a59c` | divisor / borda / borda de controle |
| `--bone` | `#eef2f8` | `#16181d` | texto principal |
| `--muted` | `#a3b1c9` | `#555a64` | texto secundário, rótulos |
| `--accent` (+ `--accent-ink`) | `#ffd43b` (tinta `#1b1500`) | `#1747c7` (tinta branca) | **ação**: botão primário, preenchimento de destaque em gráfico |
| `--link` | `#8dbcf5` | `#1747c7` | link, número de passo, tom padrão de callout |
| `--ok` | `#5fd08d` | `#1c7447` | conclusão: checklist, dica, objetivo, acerto |
| `--warn` / `--warn-text` | `#f2bd4b` | `#b86e00` / `#8f5400` | atenção, importante |
| `--danger` | `#ff8a80` | `#b93028` | **só erro**: alternativa errada, callout `erro` |
| `--night*` | `#0a0e1a`, `#121d36`, `#1a2a4d`… | iguais | cabeçalho, faixa da aula, código, callout Exemplo |
| `--hi` | `#ffd43b` | `#ffd43b` | marca, numeral da aula, régua de leitura, seleção |

Regras:

- **Vermelho é só erro.** Nada de vermelho como acento, título ou enfeite.
- **Ação, erro e "texto sobre a ação" são tokens separados.** Texto sobre um preenchimento sólido usa
  `--accent-ink` (escuro no tema escuro, branco no claro), nunca branco fixo.
- Os nomes do v3 (`--signal`, `--emerald`, `--amber`, `--volt`, `--signal-text`…) continuam como
  **aliases** dos tokens novos, para apostilas e gráficos já escritos.
- **Sem degradê.** Cor chapada; superfícies se separam por cor de caixa, não por sombra.
- Código é **sempre** janela noturna (`--night`), nos dois temas.

## 3. Tipografia

| Papel | Família | Uso |
|---|---|---|
| Display | **Archivo** 800 | título da faixa, `h2`, `h3`, título de parte, marca, numeral |
| Texto e interface | **Geist** 400–650 | texto corrido, botões, rótulo de callout, alternativas |
| Mono | **JetBrains Mono** 400–600 | só código, medidas e rótulos curtos (kickers, `caption`, número do passo) |

- Leitura: Geist 17 px, `line-height` 1.75, medida `--measure: 42rem` (em rem, para valer igual com
  fontes diferentes). No PDF, 10,5 pt.
- Escala: faixa `clamp(30px, 3.6vw, 48px)` · seção `clamp(26px, 2.6vw, 36px)` · `h3` 20–24 px ·
  kickers mono 12 px em caixa-alta, cor neutra.
- `data-texto="proporcional"` (decisão #017) virou o padrão: o atributo ainda é aceito e não muda nada.
- **Fontes:** o template carrega pelo Google Fonts; o `scripts/build.py` troca por cópias embutidas
  (`assets/fonts/*.woff2`, os mesmos arquivos que o portal hospeda), e o arquivo passa a abrir 100%
  offline. As três são SIL OFL 1.1 (`assets/fonts/OFL.txt`).

## 4. Espaço e forma

- Grade de 4 px: `--space-1..10` = 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64.
- Raios: 4 (código inline) · 6 (chip de vocabulário) · 10 (código, tabela, alternativa) · 16 (callout,
  quiz, diagrama, folha) · 999 (botões e chips: **pílula**).
- **Papel e folha:** a página é papel (`--ink`); o conteúdo fica numa folha (`--panel`) de até
  1040 px, com cantos de 16 px a partir de 640 px. No celular a folha vai de ponta a ponta.
- Texto preso na medida; tabelas, código, diagramas e gráficos usam a largura da folha.
- Alvos de toque de **44 px** no mínimo (botões, sumário, gabarito, rodapé), como no portal (D.20).
- **Leitura ampla (opcional):** `<body data-layout="amplo">` solta a medida e alarga a folha para
  1200 px. Pode combinar com `data-print="capitulos"`.

## 5. Componentes

Snippets em `BLOCOS.md`. Resumo de intenção:

| Componente | Origem no portal | Ideia |
|---|---|---|
| Cabeçalho | `.site-header` (noturno) | marca TC, Sumário, tema, PDF sem respostas, Salvar PDF |
| Faixa da aula | `.cn-cover` / `.cn-hero` | numeral amarelo, kicker, título, lead, chips, metadados, capa |
| Sumário | registro de linhas | lista numerada, 2–3 colunas |
| Seção | `.cn-prose h2` | kicker + `h2` Archivo; texto na medida |
| Divisor de parte | (extensão) | filete grosso + kicker + `h3` Archivo, para material longo |
| Callout | `.cn-prose .callout` | caixa sem borda, ícone Lucide em círculo tingido, rótulo Geist na cor do tom |
| Exemplo | `.callout.exemplo` | caixa noturna nos dois temas |
| Código | `.cn-code` | janela noturna, barra com a linguagem, botão Copiar |
| Tabela | `.cn-prose table` | linhas finas, cabeçalho em caixa, rolagem horizontal |
| Diagrama | `.lesson-diagram` | caixa com `figcaption` e etapas numeradas em círculo |
| Exercícios | `.lesson-quiz`, `.quiz-option` | alternativas clicáveis, feedback, gabarito comentado |
| Checklist | (verde = conclusão) | check verde |
| Resumo do tema | (extensão) | ficha por habilidade |
| Roteiro | (extensão) | tracejado azul; só na versão do professor |
| Capa ilustrada | card da capa na faixa | imagem 3:2 da `gerar-imagem-aula`, ao lado do título |
| Gráfico SVG | (extensão) | caixa; cores por classe de token, texto real, troca de tema sozinho |

**Imagem gerada × SVG.** Ilustração conceitual vem da skill `gerar-imagem-aula`; dado, número e
palavra exata são SVG. Desde o prompt v9 (decisão #043) as peças geradas saem no mesmo azul-noite
da faixa e do código, nos dois temas; arte antiga do v8 (grafite) aparece como placa escura
emoldurada até ser regerada.

## 6. Comportamento (JS do template — não reescreva)

1. **Tema:** alterna `data-theme` claro/escuro e salva a escolha.
2. **Régua de leitura:** barra de 2 px amarela no topo, via `requestAnimationFrame`.
3. **Copiar:** botão em cada `<pre><code>`.
4. **Quiz:** clique → `is-correct` / `is-wrong` / `is-revealed` / `is-dimmed` (mesmas classes do
   portal), feedback com `aria-live`, gabarito abre; placar quando todas forem respondidas; botão
   **Refazer** zera o bloco.
5. **Orientação:** o cabeçalho mostra a seção em que o aluno está; seção longa ganha a lista
   "Tópicos desta seção"; tabelas e gráficos largos ganham sombra nas bordas e aviso de arraste.
6. **Checklist de estudo** (`.checklist.todo`) marca e lembra no navegador.
7. **Impressão:** antes de imprimir, abre todos os `<details>` (o gabarito sai no PDF). O botão
   **PDF sem respostas** imprime a versão de treino (`body[data-print-mode="treino"]`).

Movimento é curto e funcional; `prefers-reduced-motion` desliga tudo.

## 7. Impressão (A4)

`@page A4, 14 mm`. No PDF a paleta vira papel branco e tinta escura; a "noite" vira cinza-papel
(código, faixa e callout Exemplo não gastam toner). Somem cabeçalho, régua, sumário, roteiro e
botões Copiar; a capa ilustrada desce para baixo do título; código quebra linha; caixas ganham
borda fina; callouts, questões, tabelas e passos não quebram no meio. Para material longo,
`<body data-print="capitulos">` faz cada seção começar em página nova.

## 8. Acessibilidade (piso, não enfeite)

- Contraste AA em todos os pares texto/superfície (por isso `--warn-text`, `--ok-text` e `--accent-ink`).
- Foco visível de 3 px (azul na folha, amarelo nas áreas noturnas); "Pular para o conteúdo" no foco.
- Alvos de toque de 44 px no celular.
- Ícones decorativos com `aria-hidden`; informação nunca só por cor (o quiz usa ✓/✗ e texto).
- `lang="pt-BR"`, HTML semântico (`header`, `nav`, `main`, `section`, `aside`, `figure`).

## 9. Versões

| | v2 (aulas.tonicoimbra.com antigo) | v3 (Volta Atelier) | v4 (Caderno Noturno) |
|---|---|---|---|
| Marca | logo C ciano `#00B4D8` | ligadura TC, C vermelho `#fb3732` | monograma TC do Toni, C amarelo `#ffd43b` |
| Fontes | Geist / Geist Mono | Archivo + JetBrains Mono no corpo | Archivo + **Geist** no corpo + JetBrains Mono no código |
| Cor | degradê verde→roxo→ciano | grafite + vermelho signal | azul-noite + amarelo; azul de ação no claro; vermelho só erro |
| Título | `.accent` com gradiente | palavra-chave em `<em>` vermelho | sem palavra destacada |
| Capa | — | cabeçalho claro + filete vermelho | faixa noturna com numeral e capa ao lado |
| Callouts | `c-primary`… com marca de texto | ícone em quadrado, borda | ícone em círculo tingido, caixa sem borda, Exemplo noturno |
| Botões | — | pílula com wipe vermelho | pílula chapada, sem wipe |
| Questões | "(correta)" marcada | `.lesson-quiz` interativo | igual, no visual do portal |

Apostilas v2: `scripts/migrar_v2.py antiga.html nova.html` traduz direto para o v4. Apostilas v3
continuam abrindo como estão; para atualizar, regere a partir da canônica (nunca edite a saída).

## 10. Proibido

- Vermelho fora de erro; degradê, glassmorphism, sombra colorida, neon.
- Barra lateral colorida em citação ou callout.
- Palavra destacada (`<em>`) no título (o `build.py` acusa).
- Componente inventado fora do `BLOCOS.md` (conteúdo sem componente vira `<p>`).
- Reescrever o CSS do template (ajuste pontual vai **no fim** do `<style>`).
- `<` ou `>` sem escapar dentro de `<pre><code>`.
- Comentário HTML dentro de comentário HTML.
