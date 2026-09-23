---
conceito: LLM
slug: llm
disciplina: inteligencia-artificial
tipo: conceito
aka: [large language model, modelo de linguagem de grande escala, modelo de linguagem]
status: vivo
fontes: []
aulas: [9, 10, 11, 12, 14, 15, 16, 18, 19, 21, 23]
atualizado_em: 2026-06-15
---

LLM (Large Language Model) é uma [[rede-neural]] profunda treinada com uma quantidade enorme de texto para **prever o próximo [[tokens|token]]** mais provável. Toda "conversa" com um LLM é essa previsão encadeada, repetida muito rápido. É o motor da [[ia-generativa]] de texto (ChatGPT e similares).

## Em uma frase

Rede neural treinada em texto massivo que gera respostas prevendo o próximo token, um a um.

## O que precisa saber

O LLM **não entende** no sentido humano e, por padrão, **não busca na internet** — gera o texto estatisticamente mais provável a partir do que aprendeu no treino. Por isso pode errar com confiança (ver [[alucinacoes]]). Seu conhecimento congela no [[cutoff]]; para info fresca usa-se [[rag]] ou busca. É construído com [[transformers]] e ajustado por [[fine-tuning]]. Em 2026 as famílias líderes (GPT, Claude, Gemini, Llama) trocam de versão rápido — o conceito (prever token) é o que permanece.

## Erros comuns

- Achar que o LLM entende e consulta fatos — ele prevê texto provável.
- Tratar a resposta como verdade absoluta sem conferir.

## Onde aparece
- [[segundo-cerebro]] — vault pessoal versionado como memória de longo prazo do agente

- Canônica: `aulas/inteligencia-artificial/fundamentos-de-ia/09-o-que-e-um-llm/canonica.md`
- Canônica: `aulas/inteligencia-artificial/fundamentos-de-ia/10-tokens-embeddings-e-vetores/canonica.md`
- Canônica: `aulas/inteligencia-artificial/fundamentos-de-ia/11-transformers-e-atencao/canonica.md`
- Canônica: `aulas/inteligencia-artificial/fundamentos-de-ia/12-treino-fine-tuning-e-cutoff/canonica.md`
- Canônica: `aulas/inteligencia-artificial/fundamentos-de-ia/14-prompt-engineering/canonica.md`
- Canônica: `aulas/inteligencia-artificial/fundamentos-de-ia/15-context-engineering/canonica.md`
- Canônica: `aulas/inteligencia-artificial/fundamentos-de-ia/16-rag-recuperacao-com-geracao-aumentada/canonica.md`
- Canônica: `aulas/inteligencia-artificial/fundamentos-de-ia/18-agentes-e-subagentes/canonica.md`
- Canônica: `aulas/inteligencia-artificial/fundamentos-de-ia/19-tool-use-e-function-calling/canonica.md`
- Canônica: `aulas/inteligencia-artificial/fundamentos-de-ia/21-harness-engineering/canonica.md`
- Canônica: `aulas/inteligencia-artificial/fundamentos-de-ia/23-alucinacoes-causas-tipos-e-mitigacao/canonica.md`

- Aula 9 — *O que é um LLM*
- Conceitos vizinhos: [[rede-neural]], [[tokens]], [[transformers]], [[ia-generativa]], [[cutoff]], [[fine-tuning]], [[rag]], [[alucinacoes]]

## Fontes

- Canônica da Aula 9 (modo Tema); cenário de modelos 2026 verificado na web.
