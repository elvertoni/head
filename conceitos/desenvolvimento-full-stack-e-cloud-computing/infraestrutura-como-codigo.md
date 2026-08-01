---
conceito: Infraestrutura como código
slug: infraestrutura-como-codigo
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Infrastructure as Code, IaC]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Cultura DevOps e Integração Contínua/19 - Aula 19 - Implementando Ambiente com IAC - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Infraestrutura como código descreve recursos e configurações de infraestrutura em arquivos versionáveis e automatizáveis. Ela permite revisar, reproduzir e auditar ambientes, tratando mudanças de infraestrutura como mudanças de software.

## Em uma frase

IaC torna infraestrutura declarativa, versionável e reproduzível.

## O que precisa saber

[[terraform]] é uma ferramenta de IaC; revisão, estado, secrets, drift e políticas são partes do processo. IaC pode alimentar [[pipeline-ci-cd]] e apoiar [[computacao-em-nuvem]], mas não remove necessidade de segurança e operação.

## Erros comuns

- Cometer credenciais ou estado sensível no repositório.
- Aplicar sem revisar plano e dependências.
- Ignorar recursos criados manualmente e divergência do estado.

## Onde aparece

- Aulas 16–24 — Automação e Infraestrutura como Código.
- Conecta [[terraform]], [[devops]], [[pipeline-ci-cd]] e [[monitoramento]].

## Fontes

- Aula 19, páginas 2–3 dos slides: implementação e validação de IaC.
