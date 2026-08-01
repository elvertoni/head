---
conceito: WebSocket
slug: websocket
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [WebSockets]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/38 - Aula 38 - Novas Abordagens Arquiteturiais de APIs III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

WebSocket estabelece um canal persistente e bidirecional entre cliente e servidor para troca de mensagens após um handshake inicial. Ele é útil quando o servidor precisa enviar atualizações sem polling repetido.

## Em uma frase

WebSocket mantém comunicação bidirecional de baixa latência entre as pontas.

## O que precisa saber

Sessão, autenticação, reconexão, ordenação, backpressure e escalabilidade precisam ser projetadas. WebSocket complementa [[http]] e [[api]], mas não é substituto de todo endpoint HTTP.

## Erros comuns

- Esquecer autorização durante a vida da conexão.
- Presumir que conexão aberta significa mensagem entregue.
- Não tratar reconexão, duplicação e limite de clientes.

## Onde aparece

- Frameworks e Aplicações, Aula 38, páginas 1–3.
- Relaciona-se a [[http]], [[api]], [[event-emitter]] e [[arquitetura-orientada-a-eventos]].

## Fontes

- Aula 38, páginas 1–3 dos slides: WebSocket e APIs em tempo real.
