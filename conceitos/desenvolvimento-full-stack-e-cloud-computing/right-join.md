---
conceito: RIGHT JOIN
slug: right-join
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [RIGHT OUTER JOIN, junção externa à direita]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/24 - Aula 24 - Junções IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

RIGHT JOIN preserva todas as linhas da relação à direita e acrescenta dados correspondentes da relação à esquerda. A ausência de correspondência produz NULL nas colunas da esquerda.

## Em uma frase

RIGHT JOIN mantém a relação direita mesmo sem correspondência.

## O que precisa saber

Sua semântica é equivalente a inverter tabelas e usar LEFT JOIN, mas a forma explícita pode acompanhar a leitura do domínio. A posição de filtros continua alterando o resultado.

## Erros comuns

- Ler a direção da junção pelo nome da tabela errada.
- Filtrar a tabela preservada no WHERE e remover seus NULLs.
- Usar RIGHT JOIN apenas para evitar reorganizar uma consulta confusa.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aula 24, páginas 1–4.
- Relaciona-se a [[juncao-relacional]], [[inner-join]] e [[left-join]].

## Fontes

- Aula 24, páginas 1–4 dos slides: junção externa à direita.
