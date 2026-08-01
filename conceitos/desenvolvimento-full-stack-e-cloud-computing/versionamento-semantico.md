---
conceito: Versionamento semântico
slug: versionamento-semantico
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Semantic Versioning, SemVer]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Cultura DevOps e Integração Contínua/09 - Aula 9 - Controle de Versão III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Versionamento semântico usa a forma Major.Minor.Patch para comunicar compatibilidade de uma versão de software ou biblioteca: mudanças incompatíveis aumentam Major, recursos compatíveis aumentam Minor e correções compatíveis aumentam Patch. A convenção depende de um contrato público bem definido.

## Em uma frase

SemVer comunica o impacto esperado de mudanças por números de versão.

## O que precisa saber

Consumidores usam a versão para decidir atualização e compatibilidade. A convenção não impede bugs nem garante que um projeto a aplique corretamente; exige definir o que é API pública e manter changelog. Ela se articula a [[controle-de-versao]], [[git]] e [[versionamento-de-api]].

## Erros comuns

- Aumentar Patch para uma quebra de contrato.
- Usar versão como substituto de testes e notas de mudança.
- Declarar compatibilidade sem verificar consumidores reais.

## Onde aparece

- Cultura DevOps e Integração Contínua, Aula 9, páginas 2–3.
- Relaciona-se a [[controle-de-versao]], [[git]], [[versionamento-de-api]] e [[entrega-continua]].

## Fontes

- Cultura DevOps e Integração Contínua, Aula 9, slides sobre versões e compatibilidade.
