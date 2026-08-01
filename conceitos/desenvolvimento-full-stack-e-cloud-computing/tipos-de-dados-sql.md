---
conceito: Tipos de dados SQL
slug: tipos-de-dados-sql
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [tipos de dados relacionais]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/32 - Aula 32 - Modelo Físico de Dados - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Tipos de dados SQL definem como um SGBD representa valores em colunas, incluindo números, textos, datas, horários e valores lógicos conforme o dialeto. A escolha registra expectativas sobre domínio, precisão, tamanho e operações.

## Em uma frase

Tipo SQL limita e descreve a representação dos valores armazenados.

## O que precisa saber

Tipos fazem parte do [[modelo-fisico]] e devem refletir o [[dominio-de-atributo]]. Precisão, escala, fuso e nulos importam; tipos semelhantes podem ter custos e semânticas diferentes entre SGBDs. [[sql]] padroniza conceitos, mas dialetos variam.

## Erros comuns

- Usar texto para datas e números sem necessidade.
- Perder precisão escolhendo tipo numérico inadequado.
- Presumir que o mesmo tipo tem comportamento idêntico em todo SGBD.

## Onde aparece

- Aulas 32–35 — Modelo Físico de Dados.
- Conecta [[modelo-fisico]], [[dominio-de-atributo]], [[sql]] e [[sgbd]].

## Fontes

- Aula 32, slides: tipos e objetos do modelo físico.
