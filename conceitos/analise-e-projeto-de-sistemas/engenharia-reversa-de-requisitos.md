---
conceito: Engenharia reversa de requisitos
slug: engenharia-reversa-de-requisitos
disciplina: analise-e-projeto-de-sistemas
tipo: conceito
aka: [reverse engineering de requisitos]
status: rascunho
fontes: []
aulas: [31]
atualizado_em: 2026-09-24
---

Engenharia reversa de requisitos é o exercício de recuperar, a partir de um produto pronto, as decisões que alguém tomou e que não aparecem em nenhuma tela — quem usa o sistema, o que ele faz, com que qualidade faz e quais regras cumpre nos casos em que algo dá errado.

## Em uma frase

Todo app pronto é uma pilha de decisões; engenharia reversa é recuperá-las.

## O que precisa saber

O exercício levanta três camadas a partir do produto: os [[ator|atores]] que interagem com o sistema, os [[requisito-funcional|requisitos funcionais]] e [[requisito-nao-funcional|não-funcionais]] que ele cumpre, e as [[regra-de-negocio|regras de negócio]] escondidas no caminho do erro. Depois de levantada, a lista de requisitos ainda precisa de prioridade — é aí que entra a [[matriz-gut|Matriz GUT]], que troca achismo por argumento.

## Erros comuns

- Analisar só o caminho feliz de um app pronto e ignorar o que acontece quando algo dá errado — é justamente ali que moram as regras de negócio mais reveladoras.

## Onde aparece

- Aula 31 — *Engenharia reversa — desmonte o app que você usa todo dia* `aulas/analise-e-projeto-de-sistemas/analise-de-requisitos/31-engenharia-reversa-de-app/canonica.md`
- Conceitos vizinhos: [[ator]], [[regra-de-negocio]], [[requisito-funcional]], [[requisito-nao-funcional]], [[matriz-gut]]

## Fontes

- Conteúdo autoral da Aula 31 (modo_origem: tema), sem fonte externa direta — engenharia reversa como exercício de recuperar decisões a partir do produto pronto.
