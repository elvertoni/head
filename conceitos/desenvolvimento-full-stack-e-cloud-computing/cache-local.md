---
conceito: Cache local
slug: cache-local
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [local cache]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Aplicações em Cloud Computing/07 - Aula 7 - Soluções de Cloud Computing IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Cache local mantém temporariamente dados no dispositivo ou processo consumidor para reduzir latência e continuar oferecendo informação quando a rede falha. A cópia precisa de validade e indicação de atualidade.

## Em uma frase

Cache local reduz dependência da rede ao reutilizar dados próximos.

## O que precisa saber

TTL, invalidação, tamanho, privacidade e comportamento offline devem ser projetados. Ele complementa [[cache-http]], [[cache-de-entidades]] e [[redis]].

## Erros comuns

- Servir dado sensível a outro usuário do dispositivo.
- Não informar que o dado está desatualizado.
- Armazenar sem limite e degradar o dispositivo.

## Onde aparece

- Aplicações em Cloud Computing, Aula 7, página 3.
- Relaciona-se a [[cache-http]], [[cache-de-entidades]] e [[pwa]].

## Fontes

- Aula 7, página 3 dos slides: cache local e resiliência.
