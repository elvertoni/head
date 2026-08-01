---
conceito: Versionamento de arquivos estáticos
slug: versionamento-de-arquivos-estaticos
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [static asset versioning]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/29 - Aula 29 - Projeto Web 5 - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Versionamento de arquivos estáticos associa uma versão ou hash ao nome de CSS, JavaScript, imagens e outros ativos publicados. Isso permite cache longo sem servir conteúdo antigo depois de uma mudança.

## Em uma frase

Versionar ativos separa conteúdo novo de cópias antigas em cache.

## O que precisa saber

O HTML precisa referenciar o ativo correto e a política de cache deve combinar com o ciclo de deploy. O mecanismo se relaciona a [[cache-control]], [[deployment]] e [[performance-web]].

## Erros comuns

- Alterar arquivo mantendo o mesmo nome e TTL longo.
- Remover ativo ainda referenciado por uma versão anterior.
- Gerar hash sem garantir build reprodutível.

## Onde aparece

- Desenvolvimento Web, Aula 29, página 5.
- Relaciona-se a [[cache-control]], [[deployment]], [[firebase-hosting]] e [[performance-web]].

## Fontes

- Aula 29, página 5 dos slides: versionamento de arquivos estáticos.
