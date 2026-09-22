---
conceito: Loop Engineering
slug: loop-engineering
disciplina: inteligencia-artificial
tipo: conceito
aka: [loop engineering, geração-verificação-correção, ciclo fechado de validação]
status: rascunho
fontes:
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/encontro-elite-05-transcricao.md
  - lake/inteligencia-artificial/elite-wiki/agentes/encontros-elite/encontro-elite-05-integracoes-e-automacoes-de-ia-com-hermes-agent-parte-1.md
  - "lake/inteligencia-artificial/elite-wiki/_transcricoes/Imersão IA para Devs PycodeBR [Aula 02] - 2026_04_23 19_12 GMT-03_00 - Anotações do Gemini.docx"
aulas: []
atualizado_em: 2026-09-21
---

Loop Engineering é estruturar uma tarefa para que a IA gere um resultado, use um verificador para medir se ele atende ao critério e corrija a saída em novas tentativas. O padrão transforma uma geração única em um ciclo controlado de geração, validação e ajuste.

## Em uma frase

Gerar, verificar e corrigir em ciclos limitados até cumprir um critério explícito.

## O que precisa saber

O verificador pode ser uma regra, um teste, uma ferramenta de visão, um [[evals|eval]] ou uma revisão humana. O critério precisa existir antes da geração; caso contrário, o agente apenas repete a própria preferência. O [[harness]] registra entradas, saídas, falhas e número de tentativas.

## Erros comuns

- Repetir o ciclo sem limite de tentativas, custo ou tempo.
- Usar o mesmo modelo como gerador e verificador sem critério independente.
- Chamar uma saída de aprovada sem guardar evidência do teste.
- Corrigir forma e ignorar factualidade, segurança ou adequação ao objetivo.

## Onde aparece

- Encontro Elite #05; material candidato a complementar [[alucinacoes]] e [[evals]].
- Conceitos vizinhos: [[harness]], [[guardrails]], [[seguranca-de-agentes]], [[observabilidade-de-agentes]]

## Fontes

- `_transcricoes/encontro-elite-05` — geração de imagem seguida de verificação por visão e nova tentativa.
- `agentes/encontros-elite/encontro-elite-05` — pipeline de conteúdo e validação antes da publicação.
