---
conceito: Domínio de atributo
slug: dominio-de-atributo
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [domínio de valores]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/11 - Aula 11 - Entidade e Atributos III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Domínio de atributo é o conjunto de valores válidos que uma propriedade pode assumir. Ele inclui tipo, formato, faixa, unidade e outras restrições necessárias para que dados representem o domínio corretamente.

## Em uma frase

Domínio define quais valores fazem sentido para um atributo.

## O que precisa saber

O domínio liga [[atributo]] a regras de qualidade de [[dado]]. No [[modelo-relacional]], restrições de tipo e valor ajudam o [[sgbd]] a rejeitar estados inválidos. Domínio não é apenas o tipo técnico: uma string pode ter formato, tamanho e conjunto de valores específicos.

## Erros comuns

- Usar texto para tudo e deixar regras importantes implícitas.
- Confundir domínio com um único tipo primitivo.
- Aceitar valores vazios, negativos ou fora de faixa sem decisão de negócio.

## Onde aparece

- Aula 11 — Entidade e Atributos III.
- Conecta [[atributo]], [[dado]], [[modelo-relacional]] e restrições do modelo.

## Fontes

- Aula 11, slides: domínio e restrições de valores de atributos.
