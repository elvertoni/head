---
conceito: Visão materializada
slug: visao-materializada
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [materialized view]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/34 - Aula 34 - Modelo Físico de Dados III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Visão materializada é o resultado persistido de uma consulta, mantido para reduzir o custo de leituras repetidas. Ela acelera certos acessos, mas precisa ser atualizada ou reconstruída quando os dados de origem mudam.

## Em uma frase

Visão materializada troca armazenamento e atualização por consultas mais rápidas.

## O que precisa saber

Ela contrasta com [[visao-de-banco-de-dados]], que normalmente calcula o resultado sob demanda. A escolha pertence ao [[modelo-fisico]] e depende de frescor, volume, frequência de consulta e custo de atualização.

## Erros comuns

- Tratar o resultado materializado como fonte primária sem governança.
- Ignorar defasagem entre origem e resultado.
- Materializar uma consulta pouco usada e aumentar custo operacional.

## Onde aparece

- Aula 34 — Modelo Físico de Dados III.
- Conecta [[visao-de-banco-de-dados]], [[modelo-fisico]], [[indice-de-banco-de-dados]] e [[sgbd]].

## Fontes

- Aula 34, slides: visões, materialização e objetos físicos.
