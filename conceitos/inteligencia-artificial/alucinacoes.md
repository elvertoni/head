---
conceito: Alucinações
slug: alucinacoes
disciplina: inteligencia-artificial
tipo: conceito
aka: [alucinação, hallucination, alucinação de IA]
status: vivo
fontes:
  - aulas/inteligencia-artificial/fundamentos-de-ia/23-alucinacoes-causas-tipos-e-mitigacao/canonica.md
aulas: [23]
atualizado_em: 2026-06-15
---

Alucinação é quando um [[llm]] gera informação **falsa ou inventada** apresentando-a como verdadeira, com total confiança. Não é mentira (sem intenção) nem defeito: é consequência direta de o modelo **prever o texto mais provável** ([[llm]]) em vez de consultar fatos. Quando não "sabe", ele completa com o que soa plausível.

## Em uma frase

O LLM afirmar com confiança algo falso, porque gera o provável e não o verdadeiro.

## O que precisa saber

Tipos comuns: fatos inventados, **fontes falsas** (livros/leis/links que não existem), citações erradas — sempre com tom seguro. Causas se ligam ao [[cutoff]] e à falta de contexto. Mitigação reúne as ferramentas da trilha: dar contexto/[[rag]], pedir a fonte, usar [[tool-use|ferramentas]] (busca, calculadora) e **verificar sempre**. Regra de ouro: texto bem escrito não é prova de verdade — confiar, mas verificar.

## Erros comuns

- Confiar porque "a resposta está bem escrita" — o LLM é ótimo em soar convincente.

## Onde aparece

- Aula 23 — *Alucinações — Causas, Tipos e Mitigação*
- Conceitos vizinhos: [[llm]], [[cutoff]], [[rag]], [[tool-use]]

## Fontes

- Canônica da Aula 23 (modo Tema).
