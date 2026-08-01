---
conceito: Cache-Control
slug: cache-control
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [cabeçalho Cache-Control]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/08 - Aula 8 - Gerenciamento de Sessão e Controle de Cache IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Cache-Control é o cabeçalho HTTP que comunica diretivas sobre armazenamento, revalidação e compartilhamento de respostas. Ele permite ao servidor declarar políticas para navegadores, proxies e CDNs.

## Em uma frase

Cache-Control define como uma resposta HTTP pode ser armazenada e reutilizada.

## O que precisa saber

Diretivas como max-age, no-cache, no-store e private têm efeitos diferentes. A política precisa respeitar sensibilidade, personalização e necessidade de atualização do recurso.

## Erros comuns

- Confundir no-cache com no-store.
- Permitir cache público de resposta personalizada.
- Definir TTL longo sem mecanismo de invalidação ou revalidação.

## Onde aparece

- Arquitetura e Programação, Aula 8, páginas 1–6.
- Relaciona-se a [[cache-http]], [[etag]], [[http]] e [[redis]].

## Fontes

- Aula 8, páginas 1–6 dos slides: controle de cache HTTP.
