---
conceito: Stored procedure
slug: stored-procedure
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [procedimento armazenado]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/35 - Aula 35 - Modelo Físico de Dados IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Stored procedure é um procedimento programado e armazenado no SGBD, chamado para executar operações definidas com parâmetros e regras do banco. Ele pode centralizar lógica próxima dos dados, mas aumenta dependência do dialeto e exige governança.

## Em uma frase

Stored procedure encapsula operações executáveis dentro do banco.

## O que precisa saber

Procedures podem usar [[dml]], transações e restrições; sua escolha deve considerar segurança, testes, versionamento e distribuição da lógica entre aplicação e [[sgbd]]. Elas não corrigem um modelo mal definido.

## Erros comuns

- Esconder regras críticas sem documentação e testes.
- Criar procedure impossível de versionar junto à aplicação.
- Confiar em permissões amplas para executá-la.

## Onde aparece

- Aula 35 — Modelo Físico de Dados IV.
- Conecta [[sql]], [[sgbd]], [[dml]], [[dtl]] e [[modelo-fisico]].

## Fontes

- Aula 35, slides: procedimentos armazenados e objetos do banco.
