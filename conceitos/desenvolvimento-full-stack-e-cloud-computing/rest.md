---
conceito: REST
slug: rest
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Representational State Transfer]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/03 - Aula 3 - Arquitetura de Uma Aplicação Web e o Formato Json III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

REST é um estilo arquitetural para sistemas distribuídos que organiza recursos, representações, restrições de interação e ausência de estado entre requisições. Ele orienta o desenho de APIs, mas não é um protocolo nem uma biblioteca.

## Em uma frase

REST é um estilo para projetar interações distribuídas orientadas a recursos.

## O que precisa saber

Uma [[api-rest]] pode usar [[http]], métodos, status e [[json]] para implementar parte do estilo. Stateless não significa ausência de autenticação ou de dados persistidos; significa que cada requisição carrega o contexto necessário para ser processada.

## Erros comuns

- Chamar qualquer API HTTP de REST sem avaliar restrições.
- Usar verbos na URL para esconder modelagem de recursos.
- Confundir estado do servidor com estado da sessão do cliente.

## Onde aparece

- Aula 3 e Aulas 30–36 — Web Services, ciclo de vida e API REST.
- Conecta [[api]], [[api-rest]], [[http]] e [[json]].

## Fontes

- Aula 3, páginas 2–5 dos slides: SOAP, REST e Web Services.
