---
conceito: Mensageria
slug: mensageria
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [messaging, comunicação por mensagens]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desafio_ Docker e Desenvolvimento de Aplicações/03 - Aula 3 - Desenvolvimento II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Mensageria integra produtores e consumidores por mensagens mediadas por um broker, permitindo comunicação assíncrona, desacoplamento temporal e processamento independente entre serviços. O sistema precisa definir entrega, ordenação, retenção, confirmação, repetição e tratamento de falhas; enviar uma mensagem não garante que o trabalho foi concluído.

## Em uma frase

Mensageria desacopla produtores e consumidores por meio de mensagens e um canal intermediário.

## O que precisa saber

Filas distribuem trabalho; tópicos permitem que múltiplos consumidores recebam eventos. [[broker]] intermedeia o fluxo, enquanto [[arquitetura-orientada-a-eventos]] organiza reações e [[programacao-assincrona]] separa envio de processamento. Mensageria pode ser gerenciada, como [[cloud-messaging]], ou operada pela própria arquitetura.

## Erros comuns

- Assumir entrega exatamente uma vez sem verificar o sistema real.
- Não tornar consumidores idempotentes diante de repetição.
- Ignorar mensagens presas, ordem, poison messages e observabilidade.

## Onde aparece

- Desafio Docker e Desenvolvimento de Aplicações, Aulas 1, 3 e 5, páginas 2–4.
- Relaciona-se a [[broker]], [[arquitetura-orientada-a-eventos]], [[programacao-assincrona]], [[cloud-messaging]] e [[arquitetura-de-microservicos]].

## Fontes

- Desafio Docker e Desenvolvimento de Aplicações, slides sobre integração entre serviços por mensagens.
