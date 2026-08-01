---
conceito: Agrupamento de dados SQL
slug: agrupamento-de-dados-sql
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [GROUP BY, HAVING]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/26 - Aula 26 - Funções de Agregação de Dados II - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/27 - Aula 27 - Funções de Agregação de Dados III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Agrupamento de dados SQL particiona linhas por valores comuns para que [[funcoes-de-agregacao-sql]] seja calculada separadamente em cada grupo. GROUP BY define os grupos e HAVING filtra seus resultados agregados.

## Em uma frase

GROUP BY resume dados por grupos e HAVING filtra grupos.

## O que precisa saber

WHERE filtra linhas antes da agregação; HAVING filtra depois. Toda coluna selecionada sem agregação precisa ser compatível com o agrupamento segundo o dialeto e a consulta.

## Erros comuns

- Usar HAVING para uma condição simples de linha.
- Esperar que GROUP BY preserve a ordem dos grupos.
- Agrupar por uma chave inadequada e misturar entidades distintas.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aulas 26–27.
- Relaciona-se a [[funcoes-de-agregacao-sql]], [[filtro-de-consulta-sql]] e [[ordenacao-de-consulta-sql]].

## Fontes

- Aulas 26–27, páginas 1–4 dos slides: GROUP BY, HAVING e agregações.
