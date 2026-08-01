---
conceito: Entidade forte
slug: entidade-forte
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [entidade regular, strong entity]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/10 - Aula 10 - Entidade e Atributos II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Entidade forte é uma entidade cuja ocorrência pode ser identificada por seus próprios atributos-chave, sem depender da identidade de outra entidade. Ela pode ainda participar de relacionamentos e possuir dependências de negócio.

## Em uma frase

Entidade forte possui identidade própria no modelo.

## O que precisa saber

O contraste com [[entidade-fraca]] trata da identificação. A chave da entidade forte costuma originar uma [[chave-primaria]] no [[modelo-relacional]]. Ser forte não significa ser independente de todas as regras ou relacionamentos do domínio.

## Erros comuns

- Confundir independência de identidade com ausência de relacionamentos.
- Escolher uma chave sem estabilidade no domínio.
- Criar chave artificial e abandonar atributos naturais sem avaliar o caso.

## Onde aparece

- Aula 10 — Entidade e Atributos II.
- Conecta [[entidade]], [[entidade-fraca]], [[chave-primaria]] e [[modelo-relacional]].

## Fontes

- Aula 10, slides: entidade forte e identificação própria.
