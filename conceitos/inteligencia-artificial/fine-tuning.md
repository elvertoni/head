---
conceito: Fine-tuning
slug: fine-tuning
disciplina: inteligencia-artificial
tipo: conceito
aka: [ajuste fino, fine tuning]
status: vivo
fontes:
  - aulas/inteligencia-artificial/fundamentos-de-ia/12-treino-fine-tuning-e-cutoff/canonica.md
aulas: [12]
atualizado_em: 2026-06-15
---

Fine-tuning ("ajuste fino") é um treino **menor e direcionado**, feito depois do pré-treino, que molda um [[llm]] para uma tarefa ou estilo específico — virar um bom assistente, seguir instruções, evitar respostas ofensivas. O pré-treino dá o conhecimento amplo; o fine-tuning dá o "jeito".

## Em uma frase

Ajuste direcionado, após o pré-treino, que especializa o modelo num comportamento ou tarefa.

## O que precisa saber

É uma das duas fases de construção de um modelo (pré-treino + fine-tuning). Não confundir com [[rag]]: fine-tuning **muda o modelo** (treino), enquanto RAG apenas **fornece informação no contexto** sem alterar pesos. Para a maioria dos casos de "dar conhecimento novo", RAG é mais barato; fine-tuning vale para moldar comportamento/estilo.

## Erros comuns

- Achar que fine-tuning é a forma de "ensinar fatos novos" — geralmente isso se resolve com [[rag]], não com retreino.

## Onde aparece

- Aula 12 — *Treino, Fine-tuning e Cutoff*
- Conceitos vizinhos: [[llm]], [[cutoff]], [[rag]]

## Fontes

- Canônica da Aula 12 (modo Tema).
