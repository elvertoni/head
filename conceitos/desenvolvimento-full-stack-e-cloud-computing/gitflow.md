---
conceito: Gitflow
slug: gitflow
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [fluxo Gitflow]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Cultura DevOps e Integração Contínua/09 - Aula 9 - Controle de Versão III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Gitflow é um fluxo de trabalho sobre [[git]] que separa branches de desenvolvimento, funcionalidades, releases, correções e produção. Ele oferece pontos explícitos para preparar versões, mas pode introduzir coordenação e branches longas em equipes que precisam integrar continuamente.

## Em uma frase

Gitflow organiza branches por fases de desenvolvimento, release e correção.

## O que precisa saber

O fluxo clássico distingue uma linha principal de desenvolvimento e branches temporárias ou de suporte. A convenção deve servir ao ritmo e ao risco do produto; [[github-flow]] é uma alternativa mais leve baseada em branches curtas e integração frequente. Ambos dependem de revisão e automação, não apenas de nomes.

## Erros comuns

- Adotar Gitflow sem necessidade e acumular branches divergentes.
- Manter release branch viva por tempo indefinido.
- Confundir branch com ambiente isolado e reproduzível.

## Onde aparece

- Cultura DevOps e Integração Contínua, Aula 9, página 4.
- Relaciona-se a [[git]], [[controle-de-versao]], [[github-flow]] e [[pipeline-ci-cd]].

## Fontes

- Cultura DevOps e Integração Contínua, Aula 9, slide sobre fluxos de branches.
