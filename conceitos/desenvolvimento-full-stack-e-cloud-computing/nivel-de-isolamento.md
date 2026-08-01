---
conceito: Nível de isolamento
slug: nivel-de-isolamento
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [isolamento de transações]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/28 - Aula 28 - Consumindo Dados de um Banco de Dados Relacional III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Nível de isolamento define quanto uma transação pode observar ou interferir nas alterações concorrentes de outras transações. Ele equilibra consistência, concorrência e desempenho.

## Em uma frase

Isolamento controla anomalias de leitura entre transações concorrentes.

## O que precisa saber

Níveis mais fracos permitem mais concorrência e podem admitir leituras sujas, não repetíveis ou fantasmas; níveis fortes reduzem anomalias com custo potencial. A implementação depende do SGBD.

## Erros comuns

- Escolher isolamento sem identificar a anomalia que precisa ser evitada.
- Confundir isolamento com atomicidade.
- Supor que o nome do nível tenha a mesma implementação em todo SGBD.

## Onde aparece

- Arquitetura e Programação, Aula 28, página 5.
- Relaciona-se a [[transacao-de-banco]], [[acid]] e [[banco-de-dados-relacional]].

## Fontes

- Aula 28, página 5 dos slides: níveis de isolamento.
