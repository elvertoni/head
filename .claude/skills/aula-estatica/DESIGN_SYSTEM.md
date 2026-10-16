# Design System da apostila — v3 · Volta Atelier

Versão **3.0**. Fonte de verdade de origem: repositório do ProfessorDash
(`DESIGN.md`, `design-system/volta-atelier.html`, `static/css/app.css`, `static/logo.svg`).
Este documento traduz o Volta Atelier para o formato apostila (arquivo único, offline, A4).
O CSS já está pronto no `template.html` — aqui fica o **porquê** de cada escolha, para que
qualquer IA mantenha a coerência quando o conteúdo pedir algo que o template não prevê.

Sumário: 1 identidade · 2 cor · 3 tipografia · 4 espaço e forma · 5 componentes ·
6 comportamento · 7 impressão · 8 acessibilidade · 9 o que mudou do v2 · 10 proibido

---

## 1. Identidade

**Brutalismo editorial refinado.** Alto contraste, tipografia de estúdio, linhas de registro
organizando a página em vez de caixas empilhadas. A apostila é uma bancada de leitura, não um
slide decorado: o aluno está ali para entender e terminar a tarefa.

- **Marca:** ligadura **TC** (`assets/logo.svg`). O C é sempre `--signal` `#fb3732`; o T acompanha
  o tema (osso no escuro, tinta no claro), com o vão recortado por máscara. Vai inline no cabeçalho
  exatamente como está no template — não redesenhe, não recolora, não troque pelo logo antigo.
- **Favicon:** o corte próprio de 16 px (`assets/favicon.svg`), embutido como data URI.
- **Assinatura:** "Prof. Toni Coimbra" em Archivo 800; rodapé `Material produzido pelo Prof. Toni
  Coimbra · aulas.tonicoimbra.com`.
- **Tema padrão: claro.** No portal, aluno = claro e professor = escuro. A apostila é material de
  aluno, então abre clara; o botão alterna e a escolha fica salva (`localStorage: apostila-theme`).

## 2. Cor

Tokens canônicos (iguais ao `app.css`). Cada cor tem **função**; não use cor como enfeite.

| Token | Escuro (`:root`) | Claro (`[data-theme='light']`) | Função |
|---|---|---|---|
| `--ink` | `#141414` | `#f6f5f2` | fundo da página |
| `--ink-deep` | `#0d0d0d` | `#eceae5` | rodapé, poços |
| `--panel` | `#1c1c1e` | `#ffffff` | superfície de callout, quiz, passos |
| `--panel-2` | `#232326` | `#faf9f7` | superfície elevada |
| `--line` / `--line-2` | branco 11% / 20% | tinta 10% / 18% | divisores / bordas ativas |
| `--bone` | `#f4f3f0` | `#141414` | texto principal |
| `--muted` | `#8e8e95` | `#5c5c63` | texto secundário |
| `--dim` | `#8d8d96` | `#6b6b72` | metadados |
| `--signal` | `#fb3732` | `#fb3732` | **acento**: palavra-chave do título, eyebrow, hover, número de passo, erro |
| `--signal-text` | `#ff5c57` | `#c81e1a` | signal quando é **texto** (contraste AA) |
| `--amber` | `#ffa31a` | `#d97706` | atenção, importante |
| `--emerald` | `#10b981` | `#059669` | conclusão: checklist, dica, objetivo, acerto no quiz |
| `--volt` | `#3b49e4` | `#2563eb` | apoio: roteiro do professor |
| info | `#38bdf8` | `#0284c7` | conceito, exemplo |

Regras:

- **Signal com parcimônia.** Ele marca o que é central; se tudo é vermelho, nada é.
- Texto em cor de acento usa a variante `-text`/`-deep` (contraste ≥ 4,5:1 no claro).
- **Sem degradê como tema.** O único gradiente permitido é o filete fino da capa (signal → linha →
  transparente), herdado do portal.
- Blocos de código são **sempre escuros** (`--code-bg`), nos dois temas — como num editor.

## 3. Tipografia

| Papel | Família | Uso |
|---|---|---|
| Display | **Archivo** 800 | título da capa, `h2` de seção, título de parte, marca, valores da capa |
| Corpo / mono | **JetBrains Mono** 400–700 | texto corrido, `h3`/`h4`, rótulos, código, chips, botões |

- Corpo de leitura em mono, como no leitor do portal (D.15): `--reader-size` 16–18 px, `line-height` 1.8,
  `word-spacing` .02em, medida `--measure: 62ch`. Leitura longa precisa respirar.
- Escala: capa `clamp(36px, 5.4vw, 64px)` · seção `clamp(28px, 3.6vw, 44px)` · parte `clamp(22px, 2.4vw, 30px)`
  · `h3` 1.16em · `h4` 1.04em · rótulos 11–12 px em caixa-alta com `letter-spacing` .1–.16em.
- Títulos Archivo com `letter-spacing: -.03em` e `line-height` ~1; mono nunca tem tracking negativo.
- **Fontes:** o template carrega pelo Google Fonts; o `scripts/build.py` troca por cópias embutidas
  (`assets/fonts/*.woff2`, as mesmas que o portal hospeda), e o arquivo passa a abrir 100% offline.

## 4. Espaço e forma

- Grade de 4 px: `--space-1..10` = 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64.
- Raios: 4 (código inline) · 12 (callout, código, tabela) · 18 (quiz) · 999 (botões e chips: **pílula**).
- **Profundidade por borda**, não por sombra: superfícies se separam por `--line` e por
  `--panel` sobre `--ink`. A única sombra é o brilho do botão primário.
- Página: coluna de até 1120 px; texto preso na medida; tabelas, código e demos usam a largura toda.
- **Leitura ampla (opcional):** `<body data-layout="amplo">` alinha texto, títulos, callouts,
  exercícios e tabelas na largura disponível, com casca de até 1200 px. Use quando o Toni pedir
  melhor aproveitamento horizontal. Mantém Archivo + JetBrains Mono, margens fluidas e tabelas
  roláveis no celular; no A4, usa toda a largura útil e permite que questões longas continuem na
  página seguinte sem separar as alternativas. Pode combinar com `data-print="capitulos"`.
- Seções separadas por **linhas de registro** (borda de 1 px), não por cartões.

## 5. Componentes

Snippets em `BLOCOS.md`. Resumo de intenção:

| Componente | Origem no portal | Ideia |
|---|---|---|
| Cabeçalho fixo | `.site-header` + `.brand` + `.btn` | marca TC, Sumário, tema, PDF sem respostas, Salvar PDF |
| Capa | `.lesson-header`, `.chip`, `h1 em` | eyebrow, chips, título com palavra-chave em signal, dek, meta |
| Sumário | registro de linhas | lista numerada em mono, 2–3 colunas |
| Seção | `.section-heading` + `.prose` | eyebrow + h2 Archivo; texto na medida |
| Divisor de parte | (extensão) | filete grosso + eyebrow + h3 Archivo, para material longo |
| Callout | `.callout .ic .ct` | ícone Lucide em quadrado tingido + rótulo "Tipo · Título" |
| Código | `.prose pre` | painel escuro, rótulo da linguagem, botão Copiar |
| Tabela | `.prose table` | cabeçalho mono caixa-alta, rolagem horizontal |
| Passos | `.lesson-steps` | índice quadrado em signal |
| Exercícios | `.lesson-quiz`, `.quiz-option` | alternativas clicáveis, feedback, gabarito comentado |
| Checklist | (verde = conclusão) | check esmeralda |
| Roteiro | (extensão) | tracejado volt, some no PDF |
| Capa ilustrada | `.lesson-hero` | imagem 3:2 da `gerar-imagem-aula`, borda fina, raio 18 |
| Gráfico SVG | (extensão) | moldura de painel; cores por classe de token, texto real, troca de tema sozinho |

**Imagem gerada × SVG.** Ilustração conceitual vem da skill `gerar-imagem-aula` (prompt v7, mesmo
Volta Atelier: grafite, cor chapada, signal como âncora). Dado, número e palavra exata são SVG.
As imagens geradas são sempre escuras (grafite) — no tema claro elas aparecem como placas
escuras emolduradas, do mesmo jeito que os blocos de código.

## 6. Comportamento (JS do template — não reescreva)

1. **Tema:** alterna `data-theme` claro/escuro e salva a escolha.
2. **Régua de leitura:** barra de 2 px em signal no topo, via `requestAnimationFrame`.
3. **Copiar:** botão em cada `<pre><code>`.
4. **Quiz:** clique → `is-correct` / `is-wrong` / `is-revealed` / `is-dimmed` (mesmas classes do
   portal), feedback com `aria-live`, gabarito abre; placar com próximo passo quando todas forem
   respondidas; botão **Refazer** zera o bloco (recuperar a resposta é a prática que fixa).
4b. **Orientação:** o cabeçalho mostra a seção em que o aluno está; tabelas e gráficos largos
   ganham sombra nas bordas quando há mais conteúdo para rolar.
4c. **Checklist de estudo** (`.checklist.todo`) marca e lembra no navegador.
5. **Impressão:** antes de imprimir, abre todos os `<details>` (o gabarito sai no PDF). O botão
   **PDF sem respostas** imprime a versão de treino (`body[data-print-mode="treino"]`): some o
   gabarito comentado, a solução das atividades e as marcações de quem já respondeu; o gabarito
   rápido do fechamento continua.

Movimento é curto e funcional (hover de pílula com wipe, deslize de 2 px na alternativa), e
`prefers-reduced-motion` desliga tudo.

## 7. Impressão (A4)

`@page A4, 14 mm`. No PDF a paleta é forçada para o claro de alto contraste; somem cabeçalho,
régua, sumário, roteiro e botões Copiar; código vira fundo claro com quebra de linha; callouts,
questões, tabelas e passos não quebram no meio. Para material longo, `<body data-print="capitulos">`
faz cada seção começar em página nova.

## 8. Acessibilidade (piso, não enfeite)

- Contraste AA em todos os pares texto/superfície (por isso existem as variantes `-text`/`-deep`).
- Foco visível em signal em tudo que é clicável; link "Pular para o conteúdo" que aparece no foco.
- Código inline em cor de texto (não signal): o vermelho fica reservado para o destaque e o erro.
- Ícones decorativos com `aria-hidden`; informação nunca só por cor (o quiz usa ✓/✗ e texto).
- `lang="pt-BR"`, HTML semântico (`header`, `nav`, `main`, `section`, `aside`, `figure`).

## 9. O que mudou do v2 para o v3

| v2 (aulas.tonicoimbra.com antigo) | v3 (Volta Atelier) |
|---|---|
| Logo C ciano `#00B4D8` + seta azul | Ligadura **TC** com C em `#fb3732` |
| Geist / Geist Mono | **Archivo** (display) + **JetBrains Mono** (corpo) |
| Abre escuro | Abre **claro** (material de aluno) |
| Degradê verde→roxo→ciano, `.accent` com gradiente | Cor chapada; palavra-chave em `<em>` signal |
| `callout c-primary/c-secondary/c-tertiary/c-warning/c-error` com marca de texto | `callout conceito/atencao/dica/exemplo/importante/curiosidade/objetivo/erro` com ícone Lucide |
| `.code-shell` com bolinhas de janela | `<pre data-lang>` + botão Copiar |
| `.demo-wrap` + `table.demo` | `<table>` com `<caption>`; `.demo` só para HTML renderizado |
| Questão com "(correta)" marcada + callout de resposta | `.lesson-quiz` interativo + gabarito em `<details>` |
| `.tags` | `.chips` / `.chip` |
| `.section-close` | `.section--close` |
| Google Fonts obrigatório | fontes embutidas pelo `build.py` (offline de verdade) |

Apostilas antigas: `scripts/migrar_v2.py antiga.html nova.html` faz a tradução automática.

## 10. Proibido

- Degradê multicolorido, glassmorphism, sombra colorida, neon aleatório.
- Barra lateral colorida de 4 px em citação ou callout (o portal baniu).
- Mais de uma palavra-chave `<em>` no título; signal espalhado em parágrafos.
- Componente inventado fora do `BLOCOS.md` (conteúdo sem componente vira `<p>`).
- Reescrever o CSS do template (ajuste pontual vai **no fim** do `<style>`).
- `<` ou `>` sem escapar dentro de `<pre><code>`.
- Comentário HTML dentro de comentário HTML.
