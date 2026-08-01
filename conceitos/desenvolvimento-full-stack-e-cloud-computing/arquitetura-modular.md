---
conceito: Arquitetura modular
slug: arquitetura-modular
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [modularidade de software]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/14 - Aula 14 - Criando a Sua Primeira Aplicação Modular I - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/16 - Aula 16 - Criando a Sua Primeira Aplicação Modular III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Arquitetura modular organiza uma aplicação em módulos com responsabilidades, interfaces e dependências delimitadas. Cada módulo concentra uma parte coerente do problema e pode ser composto com outros, reduzindo acoplamento sem prometer isolamento absoluto.

## Em uma frase

Arquitetura modular divide o sistema em partes coerentes conectadas por limites explícitos.

## O que precisa saber

Um módulo pode agrupar componentes, funções, estilos, dados ou regras de uma capacidade. A modularidade se apoia no [[principio-da-responsabilidade-unica]] e pode aparecer em diferentes arquiteturas, inclusive em camadas. Bons limites escondem detalhes, reduzem mudanças espalhadas e deixam dependências visíveis.

## Erros comuns

- Criar módulos pequenos demais sem coesão ou motivo claro.
- Esconder dependências globais atrás de nomes de módulo.
- Confundir organização de arquivos com arquitetura modular real.

## Onde aparece

- Projeto Front-End e Desenvolvimento Web, Aulas 14 e 16, páginas 1–4.
- Relaciona-se a [[principio-da-responsabilidade-unica]], [[arquitetura-em-camadas]] e [[componente-react]].

## Fontes

- Projeto Front-End e Desenvolvimento Web, Aulas 14 e 16, slides sobre aplicação modular.
