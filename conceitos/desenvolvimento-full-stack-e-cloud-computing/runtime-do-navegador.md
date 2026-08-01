---
conceito: Runtime do navegador
slug: runtime-do-navegador
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [ambiente de execução do browser]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Desafio_ Desenvolvimento Front - End/01 - Aula 1 - Hands on_ Desenvolvimento Front - End - Contextualização - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Runtime do navegador é o ambiente em que JavaScript é executado no browser, com pilha, filas, event loop e acesso controlado a APIs Web. Ele combina linguagem, engine e capacidades do documento.

## Em uma frase

Runtime do navegador executa JavaScript e coordena suas interações com a Web.

## O que precisa saber

O runtime se relaciona a [[event-loop]], [[promises]] e [[web-apis-do-navegador]]. Bloqueios na thread principal prejudicam resposta e [[performance-web]].

## Erros comuns

- Supor que JavaScript rode em uma thread isolada de toda tarefa.
- Executar trabalho pesado na thread principal.
- Confundir API do browser com recurso garantido pela linguagem.

## Onde aparece

- Desafio Desenvolvimento Front-End, Aula 1, páginas 2–5.
- Relaciona-se a [[navegador-web]], [[event-loop]] e [[web-apis-do-navegador]].

## Fontes

- Aula 1, páginas 2–5 dos slides: runtime e execução no navegador.
