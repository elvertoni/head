---
conceito: Banco de dados relacional
slug: banco-de-dados-relacional
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [banco relacional, relational database]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/02 - Aula 2 - Fundamentos de Banco de Dados II - Apostila (Slides).pdf"
aulas: [1, 4, 5]
atualizado_em: 2026-09-24
---

Banco de dados relacional organiza dados em relações, usualmente representadas como tabelas com linhas e colunas, e usa chaves e restrições para expressar vínculos e consistência. Consultas relacionam relações por operações formais ou por [[sql]].

## Em uma frase

O modelo relacional representa dados em relações conectadas por chaves e regras.

## O que precisa saber

O desenho começa no [[modelo-entidade-relacionamento]] e pode ser transformado em [[modelo-relacional]]. [[chave-primaria]], [[chave-estrangeira]] e [[integridade-referencial]] ajudam a preservar identidade e vínculos. Ele difere de bancos [[banco-de-dados-nao-relacional]] e orientados a objetos por seu modelo central.

## Erros comuns

- Confundir tabela com qualquer planilha sem considerar restrições.
- Usar texto duplicado em vez de modelar relações.
- Escolher modelo relacional sem avaliar o acesso e o domínio.

## Onde aparece

- Aulas 2–4 e 18–20 — Fundamentos e Modelo Relacional.
- Aula 1 — *Blueprint · A.N.N Beauty* `aulas/tcc/blueprint-tcc/01-blueprint-a-n-n-beauty/canonica.md` — SQLite, escolhido pela leveza e por dispensar servidor separado em projeto acadêmico.
- Aula 4 — *Blueprint · Espaço Delas* `aulas/tcc/blueprint-tcc/04-blueprint-espaco-delas/canonica.md` — PostgreSQL, escolhido por consultas concorrentes e transações atômicas robustas.
- Aula 5 — *Blueprint · Gold Fit* `aulas/tcc/blueprint-tcc/05-blueprint-gold-fit/canonica.md` — PostgreSQL, escolhido por suportar consultas complexas de histórico e séries.
- Conecta [[modelo-relacional]], [[sql]], [[chave-primaria]], [[chave-estrangeira]] e [[integridade-referencial]].

## Fontes

- Aula 2, slides: características e organização de bancos relacionais.
