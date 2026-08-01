---
conceito: ARIA
slug: aria
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [WAI-ARIA, Accessible Rich Internet Applications]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/05 - Aula 5 - Imersão JavaScript - Coleções e Funções - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

ARIA é um conjunto de papéis, estados e propriedades que comunica semântica de interfaces dinâmicas às tecnologias assistivas. Ele complementa o HTML quando a semântica nativa não expressa o widget necessário.

## Em uma frase

ARIA descreve papéis e estados de componentes para tecnologias assistivas.

## O que precisa saber

ARIA não cria comportamento, foco ou teclado; o código precisa implementá-los. A regra prática é preferir HTML nativo e usar ARIA apenas quando a semântica está correta.

## Erros comuns

- Adicionar role sem implementar teclado e estados.
- Substituir botão nativo por div com role button.
- Declarar estado ARIA que não acompanha a interface.

## Onde aparece

- JavaScript e Aplicações Práticas, Aula 5, páginas 2–5.
- Relaciona-se a [[acessibilidade]], [[nome-acessivel]], [[foco-de-teclado]] e [[arvore-de-acessibilidade]].

## Fontes

- Aula 5, páginas 2–5 dos slides: ARIA e acessibilidade.
