---
conceito: Função de banco de dados
slug: funcao-de-banco-de-dados
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [database function]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/35 - Aula 35 - Modelo Físico de Dados IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Função de banco de dados é uma rotina armazenada que recebe valores e retorna um resultado, podendo ser usada em consultas ou operações conforme o SGBD. Ela encapsula cálculos ou regras próximas dos dados.

## Em uma frase

Função de banco encapsula uma transformação reutilizável executada pelo SGBD.

## O que precisa saber

Funções podem ser escalares ou retornar conjuntos, conforme o dialeto. Devem ter comportamento testável e custo conhecido; usar uma [[stored-procedure]] ou uma função na aplicação é uma decisão de arquitetura, não apenas de sintaxe.

## Erros comuns

- Executar função cara em cada linha sem medir impacto.
- Confundir função determinística com resultado sempre atual.
- Esconder regras de negócio sem documentação.

## Onde aparece

- Aula 35 — Modelo Físico de Dados IV.
- Conecta [[stored-procedure]], [[sql]], [[dql]] e [[modelo-fisico]].

## Fontes

- Aula 35, slides: funções e objetos programáveis do banco.
