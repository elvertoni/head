---
conceito: Manipulação do DOM
slug: manipulacao-do-dom
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [DOM scripting, manipulação da árvore do documento]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Padrões Web - HTML e CSS/05 - Aula 5 - Criando Soluções WEB - Resumo (Aula em PDF).pdf"
aulas: [16]
atualizado_em: 2026-09-24
---

Manipulação do DOM é o uso de JavaScript para localizar, ler, criar ou alterar nós da árvore que representa um documento HTML. Ela conecta dados e comportamento do programa aos elementos que a pessoa vê e utiliza.

## Em uma frase

Manipular o DOM é programar a árvore HTML que o navegador mantém em memória.

## O que precisa saber

O DOM nasce da [[estrutura-de-documento-html]]. Métodos como getElementById ou `querySelector` localizam elementos; depois, propriedades e eventos alteram conteúdo ou comportamento. `querySelector` usa a mesma linguagem de seletor do CSS (`#id`, `.classe`), e `addEventListener` não executa nada na hora — só registra a função para rodar quando o evento acontecer. Um erro clássico é o script rodar antes de o elemento existir no documento: `querySelector` devolve `null`, e qualquer chamada em cima estoura `Cannot read properties of null`; a correção é colocar o `<script>` como última coisa antes de `</body>`. [[caixas-de-dialogo-javascript]] oferece interação simples, enquanto [[integracao-javascript-html]] combina DOM, eventos e funções em uma interface.

## Erros comuns

- Tentar acessar um elemento antes de ele existir no documento.
- Alterar HTML com texto não confiável e criar risco de injeção.
- Acoplar toda a lógica a ids e estruturas que mudam frequentemente.

## Onde aparece

- Aula 5 — Criando Soluções WEB.
- Aula 16 — *JavaScript na conta certa: três comportamentos, vinte linhas* `aulas/programacao-front-end/landing-page-mvp/16-os-tres-javascripts/canonica.md` — `querySelector`, `addEventListener` e o erro de script executado antes de o elemento existir.
- Conecta [[javascript]], [[estrutura-de-documento-html]], [[caixas-de-dialogo-javascript]], [[integracao-javascript-html]] e [[classlist]].

## Fontes

- Resumo da Aula 5, páginas 2–3 e 8: acesso a elementos, alteração de conteúdo e conversão de tipos.
