---
conceito: Transformers
slug: transformers
disciplina: inteligencia-artificial
tipo: conceito
aka: [transformer, arquitetura transformer]
status: vivo
fontes:
  - aulas/inteligencia-artificial/fundamentos-de-ia/11-transformers-e-atencao/canonica.md
aulas: [11]
atualizado_em: 2026-06-15
---

Transformer é a **arquitetura** de rede neural apresentada em 2017 ("Attention is All You Need") que virou a base de praticamente todos os [[llm]] modernos. Sua sacada: em vez de ler o texto em fila (esquecendo o começo), olha para **todas as palavras ao mesmo tempo** e usa [[atencao]] para decidir quais importam. O "T" de GPT vem dele.

## Em uma frase

A arquitetura (2017) que processa o texto em paralelo com atenção, base dos LLMs atuais.

## O que precisa saber

Resolveu o problema dos modelos antigos, que liam palavra a palavra e perdiam o contexto inicial em frases longas. O processamento **em paralelo** (todas as palavras juntas) também viabilizou treinar modelos gigantes — parte do porquê da explosão da IA (ver [[inverno-da-ia]]). Seu mecanismo central é a [[atencao]].

## Erros comuns

- Imaginar que lê "em ordem como um humano" — processa em paralelo, não em fila.

## Onde aparece

- Aula 11 — *Transformers e Atenção*
- Conceitos vizinhos: [[atencao]], [[llm]], [[rede-neural]]

## Fontes

- Canônica da Aula 11 (modo Tema); marco histórico (artigo de 2017).
