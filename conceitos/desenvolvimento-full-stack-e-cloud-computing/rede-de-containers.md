---
conceito: Rede de containers
slug: rede-de-containers
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [container networking]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/04 - Aula 4 - Docker e Desenvolvimento de Aplicações - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Rede de containers define como processos empacotados se comunicam entre si, com o host e com serviços externos.

## Em uma frase

Rede conecta containers sem transformar suas interfaces em segurança automática.

## O que precisa saber

Bridge, DNS, portas publicadas e redes privadas têm usos distintos. Exposição deve seguir menor privilégio e ser monitorada.

## Erros comuns

- Publicar toda porta no host.
- Confundir isolamento de rede com autenticação.

## Onde aparece

- Aulas 1–7 — Docker.

## Fontes

- Aula 4, páginas 2–10 dos slides: networking e port mapping.
