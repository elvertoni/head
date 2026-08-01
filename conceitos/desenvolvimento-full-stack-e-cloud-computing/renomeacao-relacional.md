---
conceito: Renomeação relacional
slug: renomeacao-relacional
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [operador renomeação, rho relacional]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/03 - Aula 3 - Álgebra Relacional III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Renomeação relacional é a operação ρ que atribui outro nome a uma relação ou aos seus atributos durante uma expressão. Ela permite distinguir papéis diferentes da mesma relação.

## Em uma frase

Renomeação dá nomes temporários a relações ou atributos de uma consulta.

## O que precisa saber

Ela é útil em autojunções e em expressões longas da [[algebra-relacional]]. O alias de [[sql]] cumpre papel semelhante na escrita, mas a operação formal também explicita a mudança de nomes na expressão.

## Erros comuns

- Confundir alias local com alteração permanente do esquema.
- Usar nomes ambíguos em uma autojunção.
- Renomear sem atualizar referências aos atributos.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aula 3, página 5.
- Relaciona-se a [[algebra-relacional]] e [[juncao-relacional]].

## Fontes

- Aula 3, página 5 dos slides: operador ρ e renomeação.
