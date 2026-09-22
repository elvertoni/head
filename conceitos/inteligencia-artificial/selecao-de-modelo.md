---
conceito: Seleção de modelo
slug: selecao-de-modelo
disciplina: inteligencia-artificial
tipo: conceito
aka: [seleção de modelo, escolha de modelo, model selection]
status: rascunho
fontes:
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/Encontro_Elite_09_resumo_e_transcricao.pdf
aulas: []
atualizado_em: 2026-09-21
---

Seleção de modelo é escolher o modelo e a configuração que atendem à tarefa com qualidade, custo, latência e confiabilidade aceitáveis. A decisão deve usar tarefas representativas e medir o resultado no ambiente real, porque rankings, preços e limites mudam e não substituem o contexto de uso.

## Em uma frase

Escolher o modelo pelo trabalho que precisa ser feito, medindo qualidade, custo e tempo.

## O que precisa saber

Separe a tarefa pela complexidade: operações repetitivas podem usar modelos menores; planejamento, arquitetura e casos críticos exigem mais capacidade. Compare qualidade, custo por execução, tokens, quantidade de passos, velocidade, janela de contexto, ferramentas disponíveis e política de dados do provedor. [[evals]] tornam a comparação verificável; [[provedor-de-modelo]] e [[harness]] fazem parte da decisão.

## Erros comuns

- Escolher pelo nome, pelo hype ou por um ranking sem testar a tarefa real.
- Comparar apenas preço por milhão de tokens e ignorar quantidade de passos e retrabalho.
- Usar o modelo mais caro para toda tarefa, sem medir ganho marginal.
- Tratar uma configuração de setembro como regra permanente.

## Onde aparece

- Encontro Elite #09; material de estudo sobre setup, benchmarks e custo-benefício.
- Conceitos vizinhos: [[llm]], [[provedor-de-modelo]], [[harness]], [[evals]], [[tokens]]

## Fontes

- `Encontro_Elite_09_resumo_e_transcricao.pdf` — critérios de inteligência, custo, passos, velocidade e consumo de tokens.
