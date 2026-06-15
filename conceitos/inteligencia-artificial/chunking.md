---
conceito: Chunking
slug: chunking
disciplina: inteligencia-artificial
tipo: conceito
aka: [fatiamento de documentos, divisão em pedaços]
status: vivo
fontes:
  - lake/inteligencia-artificial/elite-wiki/arquitetura/blueprint-sistema-rag-para-suporte-a-alunos.md
aulas: [17]
atualizado_em: 2026-06-15
---

Chunking é cortar um documento grande em pedaços menores antes de transformá-los em [[embeddings]]. É a primeira etapa do pipeline de ingestão de um [[rag]]: o banco vetorial não guarda "o PDF inteiro", guarda dezenas de fatias dele, cada uma vetorizada e buscável por conta própria.

## Em uma frase

Quebrar cada documento em pedaços do tamanho certo para que a busca semântica do [[rag]] devolva trechos úteis, nem grandes nem pequenos demais.

## O que precisa saber

O tamanho do chunk é uma decisão de projeto com tradeoff direto. Pedaço grande carrega mais contexto, mas dilui o significado: o [[embeddings|embedding]] vira uma média borrada de vários assuntos e a busca perde precisão. Pedaço pequeno é preciso, mas pode cortar uma ideia no meio e devolver um trecho sem o contexto que o tornava útil. Por isso é comum usar **sobreposição** (overlap): cada chunk repete um pouco do fim do anterior, para nenhuma ideia ficar partida exatamente na fronteira.

Não existe número mágico — depende do material e do tipo de pergunta. É o primeiro parâmetro a ajustar quando um [[rag]] recupera trechos ruins.

## Erros comuns

- **Chunk fixo por número de caracteres ignorando estrutura.** Cortar no meio de uma frase ou tabela degrada a recuperação. Respeitar parágrafos/seções quando der.
- **Zero overlap.** Sem sobreposição, ideias na fronteira entre dois chunks se perdem.
- **Tratar chunking como detalhe.** É frequentemente a causa real de um RAG que "não acha nada".

## Onde aparece

- Aula 17 — *Chunking, embeddings e vector stores*
- Conceitos vizinhos: [[rag]], [[embeddings]], [[vector-store]]

## Fontes

- `blueprint-sistema-rag-para-suporte-a-alunos.md` (elite-wiki) — etapa de chunking no pipeline de ingestão.
