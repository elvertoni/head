---
conceito: Socket de rede
slug: socket-de-rede
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [network socket, socket TCP]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/01 - Aula 1 - Arquitetura de Uma Aplicação Web e o Formato Json - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/21 - Aula 21 - Programação Assíncrona III - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/22 - Aula 22 - Programação Assíncrona IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Socket de rede é um ponto de comunicação identificado por endereço e porta. Ele representa a extremidade pela qual um processo estabelece e mantém a troca de dados com outro processo em uma rede.

## Em uma frase

Socket é a extremidade endereçável de uma comunicação entre processos.

## O que precisa saber

Serviços Web usam sockets por baixo de abstrações como [[http]] e [[websocket]]. A comunicação envolve conexão, leitura, escrita, encerramento e tratamento de falhas; [[programacao-assincrona]] ajuda a coordenar essas operações sem bloquear o processo.

## Erros comuns

- Confundir socket com o protocolo HTTP ou com [[websocket]]: socket é a extremidade de comunicação, não o contrato completo da aplicação.
- Ignorar timeout, encerramento, backpressure e falhas de rede porque a conexão parece contínua.

## Onde aparece

Relaciona-se a [[nodejs]], [[http]], [[event-loop]], [[streams-nodejs]], [[programacao-assincrona]] e [[websocket]]. Ainda não há aula canônica registrada em `aulas`.

## Fontes

- Aula 1 e aulas 21–22 de Arquitetura e Programação, slides indicados no frontmatter.

