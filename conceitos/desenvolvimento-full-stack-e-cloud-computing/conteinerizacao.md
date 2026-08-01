---
conceito: Conteinerização
slug: conteinerizacao
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [containerização, containers]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Estratégias de Cloud Computing/17 - Aula 17 - Conceitos de Virtualização e Conteinerização - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Estratégias de Cloud Computing/18 - Aula 18 - Conceitos de Virtualização e Conteinerização II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Conteinerização empacota aplicação, dependências e configurações em unidades executáveis que compartilham o kernel do sistema hospedeiro. Ela favorece consistência entre ambientes, mas exige gestão de imagens, redes, volumes e segurança.

## Em uma frase

Conteinerização empacota aplicações em ambientes reproduzíveis e leves.

## O que precisa saber

[[docker]] oferece ferramentas para construir e executar containers; [[kubernetes]] orquestra conjuntos deles. Containers não são máquinas virtuais completas e não substituem isolamento, atualização, observabilidade ou controle de segredos.

## Erros comuns

- Guardar dados persistentes apenas dentro da camada efêmera do container.
- Executar como root sem necessidade.
- Confundir imagem imutável com aplicação sempre segura.

## Onde aparece

- Aulas 17–22 e 26–28 — Virtualização, Docker e Kubernetes.
- Conecta [[virtualizacao]], [[docker]], [[kubernetes]] e [[arquitetura-de-nuvem]].

## Fontes

- Aula 17, páginas 2–5 dos slides: virtualização e conteinerização.
