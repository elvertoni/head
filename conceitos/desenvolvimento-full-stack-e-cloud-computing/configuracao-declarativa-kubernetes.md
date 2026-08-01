---
conceito: Configuração declarativa do Kubernetes
slug: configuracao-declarativa-kubernetes
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Kubernetes declarative configuration]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/10 - Aula 10 - Kubernetes III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Configuração declarativa do Kubernetes descreve recursos e estado desejado em manifestos, frequentemente YAML, para que controladores reconciliem o cluster. O operador declara o resultado, não cada passo imperativo.

## Em uma frase

Configuração declarativa descreve o estado que o cluster deve manter.

## O que precisa saber

Manifestos precisam de versionamento, validação, revisão e separação de ambientes. [[yaml]], [[estado-desejado-kubernetes]] e [[infraestrutura-como-codigo]] tornam o processo rastreável.

## Erros comuns

- Aplicar YAML sem revisar namespace, permissões ou imagens.
- Misturar segredo em manifesto público.
- Confundir declaração aplicada com serviço saudável.

## Onde aparece

- Desenvolvimento Web, Aula 10, página 8; Aula 14, página 2.
- Relaciona-se a [[yaml]], [[estado-desejado-kubernetes]], [[kubectl]] e [[kubernetes]].

## Fontes

- Aula 10, página 8, e Aula 14, página 2 dos slides: configuração declarativa.
