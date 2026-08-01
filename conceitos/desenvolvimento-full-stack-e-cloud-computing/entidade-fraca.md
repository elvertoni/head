---
conceito: Entidade fraca
slug: entidade-fraca
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [weak entity]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/10 - Aula 10 - Entidade e Atributos II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Entidade fraca é uma entidade cuja identificação depende de outra entidade e de um relacionamento de identificação. Seus atributos próprios não bastam para distinguir uma ocorrência globalmente.

## Em uma frase

Entidade fraca precisa de uma entidade proprietária para completar sua identidade.

## O que precisa saber

Ela se diferencia da [[entidade-forte]] pela dependência de identidade, não por ser menos importante. A transformação para o [[modelo-logico]] deve preservar proprietário, chave parcial e participação; o [[modelo-entidade-relacionamento]] torna essa dependência explícita.

## Erros comuns

- Chamar toda entidade relacionada de fraca.
- Omitir a chave da entidade proprietária.
- Usar entidade fraca quando uma chave própria resolveria o domínio.

## Onde aparece

- Aula 10 — Entidade e Atributos II.
- Conecta [[entidade]], [[entidade-forte]], [[modelo-entidade-relacionamento]] e [[modelo-logico]].

## Fontes

- Aula 10, slides: entidade fraca, dependência e identificação.
