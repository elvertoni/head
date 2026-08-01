---
conceito: Cache HTTP
slug: cache-http
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [HTTP caching]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/07 - Aula 7 - Gerenciamento de Sessão e Controle de Cache III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Cache HTTP armazena respostas para reutilizá-las em requisições posteriores, reduzindo latência, tráfego e carga. Cabeçalhos e validadores determinam quando uma resposta é fresca, obsoleta ou precisa ser revalidada.

## Em uma frase

Cache HTTP troca armazenamento temporário por respostas mais rápidas e menos carga.

## O que precisa saber

Cache-Control, ETag e Last-Modified participam da política; dados privados e personalizados exigem cuidado. Cache não é sessão: [[gerenciamento-de-sessao]] preserva contexto, enquanto cache reutiliza respostas. Invalidação e consistência são decisões do contrato.

## Erros comuns

- Cachear resposta privada ou sensível como pública.
- Ignorar invalidação após mudança de dados.
- Medir apenas hit rate e não correção ou frescor.

## Onde aparece

- Aulas 7–8 — Controle de Cache.
- Conecta [[http]], [[gerenciamento-de-sessao]] e computação em nuvem.

## Fontes

- Aula 7, páginas 1–4 dos slides: cache HTTP e Redis.
