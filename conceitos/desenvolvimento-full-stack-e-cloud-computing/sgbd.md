---
conceito: Sistema gerenciador de banco de dados
slug: sgbd
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [SGBD, DBMS, sistema de gerenciamento de banco de dados]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/04 - Aula 4 - Fundamentos de Banco de Dados IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Sistema gerenciador de banco de dados é o software que define, armazena, consulta, protege e administra dados persistentes. Ele intermedeia aplicações e arquivos, oferecendo mecanismos para concorrência, transações, autorização, recuperação e integridade.

## Em uma frase

SGBD é o software que administra dados e as regras de acesso a eles.

## O que precisa saber

O SGBD implementa um modelo, como o [[banco-de-dados-relacional]], e recebe operações por linguagens como [[sql]]. O desenho conceitual e lógico continua sendo responsabilidade da [[modelagem-de-dados]]; o SGBD não corrige um modelo inadequado sozinho.

## Erros comuns

- Confundir SGBD com o banco de dados armazenado.
- Delegar ao SGBD decisões de domínio que deveriam estar no modelo.
- Ignorar backup, permissões e concorrência porque a consulta funciona.

## Onde aparece

- Aula 4 — Fundamentos de Banco de Dados IV.
- Implementa serviços de [[banco-de-dados]], [[modelo-relacional]] e [[sql]].

## Fontes

- Aula 4, slides: funções, componentes e responsabilidades de um SGBD.
