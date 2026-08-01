---
conceito: Restrição semântica
slug: restricao-semantica
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [restrição de negócio]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/27 - Aula 27 - Restrições do Modelo Relacional IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Restrição semântica é uma regra de negócio que limita quais estados do banco são válidos além das restrições de domínio, chave e integridade referencial. Ela traduz significado do domínio, como limites de crédito ou compatibilidade entre estados, e pode exigir CHECK, gatilhos, código ou processos de validação.

## Em uma frase

Restrição semântica preserva regras de negócio que não cabem apenas em tipos e chaves.

## O que precisa saber

Uma restrição semântica deve ser identificável, testável e aplicada no ponto adequado, de preferência o mais próximo possível da fonte de verdade. [[integridade-referencial]] protege referências; a restrição semântica protege condições de significado. Documentar a regra evita que ela se perca entre aplicação, banco e operação.

## Erros comuns

- Confundir qualquer validação de formulário com integridade do domínio.
- Esconder regra crítica em uma única tela da aplicação.
- Criar restrições contraditórias entre banco e código.

## Onde aparece

- Modelagem de Banco de Dados, Aula 27, páginas 2–3.
- Relaciona-se a [[restricoes-do-modelo-relacional]], [[integridade-referencial]], [[modelo-relacional]] e [[banco-de-dados]].

## Fontes

- Modelagem de Banco de Dados, Aula 27, slides sobre restrições semânticas.
