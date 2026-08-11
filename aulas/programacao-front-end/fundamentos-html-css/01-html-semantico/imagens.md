# Imagens — HTML semântico: por que `<div>` não conta a história toda

Brief neutro de plataforma, no contrato v6: **um brief de `capa` + no máximo um de `infografico`**. Os prompts finais são montados pela skill `gerar-imagem-aula` sobre `tools/imagen-generator/prompt.xml` — não escreva prompt à mão aqui. Logo, curso e normalização de canvas são aplicados externamente pela action do Photoshop. O `alt` continua carregando a informação de verdade para acessibilidade.

---

## 1. Capa da aula

- **perfil:** `capa`
- **arquivo:** capa.png
- **estado:** aprovada — gerada pelo `image_gen` nativo do Codex a partir do prompt v6 montado, auditada nos 12 defeitos, 1536×1024 (3:2 exato). Escolhida entre três candidatas por ter 7 blocos, a mediana do acervo.
- **objetivo:** Dar o mapa da aula inteira: o que é uma tag semântica, quais são as cinco do catálogo (`header`, `nav`, `main`/`article`, `aside`, `footer`), o que a div-soup custa na prática (leitor de tela, SEO, manutenção) e a regra de bolso para escolher a tag certa. Serve de material de revisão depois da aula.
- **esboço de blocos:**
  1. `O PROBLEMA` — div-soup: todo elemento é `<div>`, o significado mora só no `class`.
  2. `O CATÁLOGO` — as cinco tags de marco, cada uma com ícone e cor semântica.
  3. `QUEM LÊ ALÉM DA TELA` — leitor de tela, buscador, outro dev.
  4. `A REGRA DE BOLSO` — se existe tag com esse significado, use a tag.
  5. `ERRO COMUM` — trocar `<div class="header">` por `<header class="header">` e achar que resolveu.
- **faixa de síntese:** `EM RESUMO` — a tag certa não muda o pixel; muda quem consegue entender a página.
- **alt:** Capa da aula sobre HTML semântico. Mostra, de um lado, uma página construída só com `<div>` diferenciadas por atributo `class` e, de outro, a mesma página usando as tags `<header>`, `<nav>`, `<main>`, `<aside>` e `<footer>`, cada uma com cor e ícone próprios. Blocos laterais explicam quem depende desse significado — leitores de tela, buscadores e outros desenvolvedores — e uma faixa final resume que a tag certa não altera a aparência, mas altera quem consegue entender a página.

## 2. Infográfico de miolo

- **perfil:** `infografico`
- **arquivo:** img/mesmo-visual-dois-codigos.png
- **secao:** Desenvolvimento › O problema da div-soup / O catálogo que resolve isso
- **estado:** aprovada — arte v6 substituiu a v5 em 2026-08-11. A v5 reprovava em D10 (só o lado das tags semânticas era rotulado; o lado da div vinha sem `class` visível, o que invertia o argumento da aula) e D9 (nós cinza sem cor nem rótulo). 1664×936, 16:9 exato.
- **objetivo:** Provar, num golpe de vista, que os dois códigos produzem o mesmo resultado visual e que só um deles carrega significado. É o ponto exato onde o texto sozinho não convence: o aluno precisa **ver** que a tela é idêntica.
- **alt:** Duas árvores de elementos HTML lado a lado, representando o mesmo layout visual (header no topo, article/aside/nav no meio, footer embaixo). À esquerda, todos os nós são `<div>` cinza, diferenciados apenas pelo atributo `class`. À direita, os mesmos nós usam as tags `<header>`, `<article>`, `<aside>`, `<nav>` e `<footer>`, destacadas em cores distintas. Um sinal de igual entre os dois painéis mostra que o resultado renderizado é o mesmo — o significado estrutural é explícito na tag, não no nome da classe.

---

### Proposta descartada

"Como o leitor de tela navega a página" — comparação entre leitura linear e pulo entre landmarks. Descartada porque duplica o `diagrama-progressivo` já presente na Canônica, que atravessa inteiro para os dois renderers. Regra de seleção em `.claude/skills/gerar-imagem-aula/SKILL.md`.
