---
conceito: Dados, Treino e Inferência
slug: dados-treino-inferencia
disciplina: inteligencia-artificial
tipo: conceito
aka: [treino e inferência, training and inference, ciclo de aprendizado]
status: vivo
fontes:
  - aulas/inteligencia-artificial/fundamentos-de-ia/04-como-a-maquina-aprende/canonica.md
aulas: [4]
atualizado_em: 2026-06-15
---

São as três peças de como uma máquina aprende. **Dados** são os exemplos que ela estuda (fotos marcadas "cachorro"/"não cachorro"). **Treino** é a fase em que o modelo estuda esses exemplos e se ajusta até captar os padrões. **Inferência** é o uso depois do treino: mostra-se um dado **novo** e o modelo responde. Treinar é estudar; inferir é fazer a prova.

## Em uma frase

Dados são os exemplos; treino é estudá-los; inferência é responder sobre dados novos.

## O que precisa saber

O objetivo do treino é **generalizar** — acertar o que nunca se viu — e não decorar os exemplos (decorar = *overfitting*, considerado ruim). O modelo decide olhando **características (features)** dos dados; no [[deep-learning]], ele descobre sozinho quais importam. Regra prática da profissão: "lixo entra, lixo sai" — dados ruins produzem modelos ruins, por isso coletar e limpar dados é metade do trabalho de [[aprendizado-de-maquina]].

## Erros comuns

- Achar que a máquina decora o treino; o certo é generalizar.
- Subestimar a importância dos dados frente ao algoritmo — dados ruins quebram qualquer modelo.

## Onde aparece

- Aula 4 — *Como a Máquina Aprende*
- Conceitos vizinhos: [[aprendizado-de-maquina]], [[deep-learning]]

## Fontes

- Canônica da Aula 4 (modo Tema).
