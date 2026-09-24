---
conceito: Regra de negócio
slug: regra-de-negocio
disciplina: analise-e-projeto-de-sistemas
tipo: conceito
aka: [business rule]
status: rascunho
fontes: []
aulas: [31]
atualizado_em: 2026-09-24
---

Regra de negócio é uma decisão da área de negócio que o sistema é obrigado a respeitar — não é escolha do programador. "Cupom de primeira compra só vale para quem nunca fez pedido" é regra de negócio; "o botão fica verde" não é. A regra sobrevive à troca de linguagem, de banco e de time; o botão, não.

## Em uma frase

A regra sobrevive à troca de tecnologia; a decisão de interface, não.

## O que precisa saber

Regra de negócio quase sempre mora no caminho do erro, não no caminho feliz — aparece quando algo dá errado (cancelamento, estoque acabando, cupom já usado), não na tela do fluxo normal. A ferramenta do analista para achá-la é uma pergunta repetida: "e se…?" — cada "e se" que faz o cliente parar e pensar revela uma regra que ele nunca contaria sozinho. Recuperar essas regras a partir de um produto pronto é parte central da [[engenharia-reversa-de-requisitos|engenharia reversa de requisitos]].

## Erros comuns

- Achar que o cliente vai contar todas as regras de negócio de bandeja — ele descreve o caminho feliz e acha que acabou; a regra só aparece quando alguém pergunta "e se...?".

## Onde aparece

- Aula 31 — *Engenharia reversa — desmonte o app que você usa todo dia* `aulas/analise-e-projeto-de-sistemas/analise-de-requisitos/31-engenharia-reversa-de-app/canonica.md`
- Conceitos vizinhos: [[engenharia-reversa-de-requisitos]], [[ator]], [[requisito-funcional]]

## Fontes

- Conteúdo autoral da Aula 31 (modo_origem: tema), sem fonte externa direta — regra de negócio, o caminho do erro e a pergunta "e se…?".
