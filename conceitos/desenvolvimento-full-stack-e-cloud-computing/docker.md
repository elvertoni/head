---
conceito: Docker
slug: docker
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: entidade
aka: [Docker Engine]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Estratégias de Cloud Computing/26 - Aula 26 - Docker e Kubernetes - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/01 - Aula 1 - Docker - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Docker é uma plataforma e um conjunto de ferramentas para construir, distribuir e executar aplicações em containers. Ele trabalha com imagens, registries, redes, volumes e processos isolados por recursos do sistema.

## Em uma frase

Docker operacionaliza a construção e a execução de containers.

## O que precisa saber

Docker implementa práticas de [[conteinerizacao]] e pode compor uma [[arquitetura-de-nuvem]]. Imagens precisam ser versionadas, pequenas, rastreáveis e verificadas; dados e segredos não devem ser tratados como camada descartável.

## Erros comuns

- Confundir imagem com container em execução.
- Embutir segredo na imagem.
- Usar tag mutável sem registrar versão ou origem.

## Onde aparece

- Aulas 26–28 — Docker e Kubernetes.
- Conecta [[conteinerizacao]], [[kubernetes]] e [[virtualizacao]].

## Fontes

- Aula 26, páginas 2–5 dos slides: Docker, imagens e containers.
