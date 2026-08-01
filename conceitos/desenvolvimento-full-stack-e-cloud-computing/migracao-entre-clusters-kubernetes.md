---
conceito: Migração entre clusters Kubernetes
slug: migracao-entre-clusters-kubernetes
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Kubernetes cluster migration]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/10 - Aula 10 - Kubernetes III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Migração entre clusters Kubernetes é o processo de mover workloads, configurações, dependências e dados entre clusters ou provedores. Ela exige compatibilidade, plano de transição e validação da operação.

## Em uma frase

Migrar cluster move workloads sem perder configuração, dados e operação.

## O que precisa saber

Manifestos, imagens, identidade, rede, volumes, DNS, segredos e observabilidade precisam ser inventariados. [[multicloud]] pode ser contexto, mas não elimina diferenças entre provedores.

## Erros comuns

- Migrar Pods e esquecer dados persistentes.
- Copiar configurações sem revisar permissões e endpoints.
- Trocar tráfego sem testar rollback e consistência.

## Onde aparece

- Desenvolvimento Web, Aula 10, página 6.
- Relaciona-se a [[kubernetes]], [[multicloud]], [[portabilidade-de-containers]] e [[recuperacao-de-desastres]].

## Fontes

- Aula 10, página 6 dos slides: migração entre clusters.
