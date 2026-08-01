---
conceito: Terraform
slug: terraform
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: entidade
aka: [HashiCorp Terraform]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Cultura DevOps e Integração Contínua/16 - Aula 16 - Ferramentas de Automação - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Terraform é uma ferramenta de infraestrutura como código que descreve recursos declarativamente e calcula mudanças para aproximar o ambiente de um estado definido. Ela registra estado e permite revisar planos antes de aplicar alterações.

## Em uma frase

Terraform transforma configuração declarativa em mudanças revisáveis de infraestrutura.

## O que precisa saber

Terraform apoia [[devops]], [[pipeline-ci-cd]] e [[computacao-em-nuvem]]. Estado, segredos, dependências e concorrência exigem armazenamento e governança; um plan não substitui revisão de impacto.

## Erros comuns

- Cometer estado ou segredo no repositório.
- Aplicar mudanças sem revisar o plano.
- Drift e recursos manuais sem estratégia de reconciliação.

## Onde aparece

- Aulas 16–24 — Ferramentas e Automação de Infraestrutura.
- Conecta [[infraestrutura-como-codigo]], [[pipeline-ci-cd]], [[devops]] e [[computacao-em-nuvem]].

## Fontes

- Aula 16, páginas 2–4 dos slides: ferramentas de automação e Terraform.
