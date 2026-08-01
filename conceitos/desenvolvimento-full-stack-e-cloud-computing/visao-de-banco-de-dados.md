---
conceito: Visão de banco de dados
slug: visao-de-banco-de-dados
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [view, visão SQL]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/34 - Aula 34 - Modelo Físico de Dados III - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/31 - Aula 31 - Visões - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/32 - Aula 32 - Visões II - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/33 - Aula 33 - Visões III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Visão de banco de dados é uma relação virtual definida por uma consulta sobre outras relações. Ela oferece uma interface de leitura ou controle de acesso sem necessariamente duplicar os dados subjacentes.

## Em uma frase

Visão apresenta uma consulta como uma relação reutilizável e controlável.

## O que precisa saber

Visões podem simplificar consultas, esconder colunas e apoiar a [[arquitetura-de-tres-esquemas]]. Elas dependem das relações de origem e podem ter restrições de atualização. Uma [[visao-materializada]] armazena resultados para reduzir custo, mas exige atualização.

## Erros comuns

- Confundir visão com cópia independente dos dados.
- Expor colunas sensíveis por meio de uma view ampla.
- Ignorar custo e comportamento de atualização.

## Onde aparece

- Aula 34 — Modelo Físico de Dados III.
- Conecta [[sql]], [[modelo-fisico]], [[visao-materializada]] e [[dcl]].

## Fontes

- Aula 34, slides: visões e objetos do banco.
