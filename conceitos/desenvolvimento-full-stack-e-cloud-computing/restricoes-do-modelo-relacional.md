---
conceito: Restrições do modelo relacional
slug: restricoes-do-modelo-relacional
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [restrições relacionais]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/24 - Aula 24 - Restrições do Modelo Relacional - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Restrições do modelo relacional são regras que limitam estados inválidos em relações, chaves, domínios e vínculos. Elas fazem parte do modelo e devem ser aplicadas pelo banco ou pela aplicação de forma explícita e verificável.

## Em uma frase

Restrições impedem que o banco aceite estados incompatíveis com seu modelo.

## O que precisa saber

O conjunto inclui restrições de domínio, chave, entidade, referências e semântica. [[chave-primaria]] preserva identidade; [[chave-estrangeira]] apoia [[integridade-referencial]]; [[dominio-de-atributo]] limita valores. As regras devem ser definidas na [[modelagem-de-dados]].

## Erros comuns

- Deixar toda regra apenas no código da aplicação.
- Confundir validação de formato com integridade referencial.
- Criar restrições que contradizem fluxos legítimos do domínio.

## Onde aparece

- Aulas 24–27 — Restrições do Modelo Relacional.
- Conecta [[modelo-relacional]], [[chave-primaria]], [[chave-estrangeira]], [[dominio-de-atributo]] e [[integridade-referencial]].

## Fontes

- Aula 24, slides: restrições de chave, domínio, entidade e referências.
