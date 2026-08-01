---
conceito: Atributo multivalorado
slug: atributo-multivalorado
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [atributo de múltiplos valores]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/11 - Aula 11 - Entidade e Atributos III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Atributo multivalorado é uma propriedade que pode ter vários valores para a mesma ocorrência de entidade, como telefones de uma pessoa. A multiplicidade faz parte da regra do domínio e precisa aparecer no modelo.

## Em uma frase

Atributo multivalorado permite mais de um valor associado à mesma entidade.

## O que precisa saber

No [[modelo-relacional]], guardar uma lista em uma coluna costuma dificultar integridade e consulta; o [[mapeamento-conceitual-logico]] pode criar uma relação própria. A escolha depende do modelo e do tipo de acesso, não de uma proibição abstrata.

## Erros comuns

- Separar valores por vírgulas em uma coluna sem definir validação.
- Criar uma tabela de valores sem chave ou relação clara.
- Confundir vários valores do mesmo atributo com vários atributos diferentes.

## Onde aparece

- Aula 11 — Entidade e Atributos III.
- Conecta [[atributo]], [[modelo-relacional]], [[mapeamento-conceitual-logico]] e [[tabela-associativa]].

## Fontes

- Aula 11, slides: atributos multivalorados e sua representação.
