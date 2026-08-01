---
conceito: Programação assíncrona
slug: programacao-assincrona
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [programação não bloqueante]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/19 - Aula 19 - Programação Assíncrona - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/21 - Aula 21 - Programação Assíncrona III - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/22 - Aula 22 - Programação Assíncrona IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Programação assíncrona permite iniciar uma operação e continuar o fluxo enquanto o resultado fica pendente, recebendo depois sucesso ou falha por callback, promise ou async/await. Ela é útil para I/O, mas não elimina a necessidade de coordenar estado e erros.

## Em uma frase

Assíncrono separa início e conclusão de uma operação sem bloquear todo o fluxo.

## O que precisa saber

[[event-loop]] e [[call-stack]] explicam parte do modelo no [[nodejs]]. Promises e async/await melhoram composição, mas exceções, cancelamento, timeout e concorrência precisam ser tratados. Assíncrono não significa paralelo.

## Erros comuns

- Esquecer await ou tratar rejeição como sucesso.
- Disparar operações dependentes em paralelo sem intenção.
- Criar chamadas não observadas que falham silenciosamente.

## Onde aparece

- Aulas 19–22 — Programação Assíncrona.
- Conecta [[nodejs]], [[event-loop]], [[call-stack]] e Promises.

## Fontes

- Aula 19, páginas 1–4 dos slides: async, await e I/O assíncrono.
