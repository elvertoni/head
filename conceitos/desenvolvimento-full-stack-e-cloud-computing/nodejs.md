---
conceito: Node.js
slug: nodejs
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: entidade
aka: [NodeJS, plataforma Node]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/09 - Aula 9 - Fundamentos da Plataforma NodeJS I - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/10 - Aula 10 - Fundamentos da Plataforma NodeJS II - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/11 - Aula 11 - Fundamentos da Plataforma NodeJS III - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/12 - Aula 12 - Sistema de Módulos do NodeJS I - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/13 - Aula 13 - Sistema de Módulos do NodeJS II - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/14 - Aula 14 - Sistema de Módulos do NodeJS III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Node.js é um ambiente de execução de JavaScript baseado no motor V8, voltado a aplicações fora do navegador e especialmente a serviços orientados a eventos e operações de entrada e saída. Seu modelo não torna toda tarefa automaticamente não bloqueante.

## Em uma frase

Node.js executa JavaScript no servidor com um modelo orientado a eventos e I/O.

## O que precisa saber

O runtime se articula a [[javascript]], módulos, callbacks, [[event-loop]] e [[programacao-assincrona]]. Operações de CPU intensiva podem bloquear o processo; a arquitetura precisa considerar concorrência, filas, memória e observabilidade.

## Erros comuns

- Confundir concorrência de I/O com paralelismo de CPU.
- Bloquear o event loop com processamento pesado.
- Expor dependências sem controlar versões e vulnerabilidades.

## Onde aparece

- Aulas 9–14 — Fundamentos e Sistema de Módulos do NodeJS.
- Conecta [[event-loop]], [[programacao-assincrona]], [[expressjs]] e JavaScript.

## Fontes

- Aula 9, páginas 1–5 dos slides: plataforma NodeJS e runtime.
