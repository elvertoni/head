---
conceito: ETag
slug: etag
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Entity Tag, etiqueta de entidade]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/08 - Aula 8 - Gerenciamento de Sessão e Controle de Cache IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

ETag é um identificador de versão associado à representação de um recurso HTTP. O cliente pode enviá-lo em uma requisição condicional para que o servidor responda sem retransmitir conteúdo inalterado.

## Em uma frase

ETag permite revalidar se uma representação HTTP mudou.

## O que precisa saber

If-None-Match compara a etiqueta e pode resultar em 304 Not Modified; If-Match ajuda em atualizações condicionais. A etiqueta deve refletir a representação e não vazar informação sensível.

## Erros comuns

- Gerar ETag instável e perder revalidação.
- Usar validação de cache como controle de autorização.
- Ignorar concorrência perdida em atualizações sem If-Match.

## Onde aparece

- Arquitetura e Programação, Aula 8, páginas 1–6.
- Relaciona-se a [[cache-control]], [[cache-http]], [[http]] e [[ciclo-de-vida-de-api]].

## Fontes

- Aula 8, páginas 1–6 dos slides: ETag e controle de cache.
