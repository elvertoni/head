---
conceito: Independência de dados
slug: independencia-de-dados
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [data independence]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/19 - Aula 19 - Modelo Relacional II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Independência de dados é a capacidade de alterar um nível da arquitetura ou da implementação sem exigir mudanças indevidas nos níveis superiores. Ela reduz o acoplamento entre aplicações, modelo lógico e armazenamento físico.

## Em uma frase

Independência de dados separa mudanças de representação de mudanças no uso do banco.

## O que precisa saber

A ideia relaciona-se à [[arquitetura-de-tres-esquemas]] e aos níveis [[modelo-conceitual]], [[modelo-logico]] e [[modelo-fisico]]. Independência não significa que qualquer mudança seja invisível: alterações de significado ou contrato ainda exigem migração.

## Erros comuns

- Prometer que uma mudança de coluna nunca afeta aplicações.
- Confundir abstração com ausência de dependências.
- Ignorar compatibilidade, migração e versionamento de esquemas.

## Onde aparece

- Aula 19 — Modelo Relacional II.
- Conecta [[modelo-relacional]], [[modelo-fisico]] e arquitetura de três esquemas.

## Fontes

- Aula 19, slides: independência lógica e física de dados.
