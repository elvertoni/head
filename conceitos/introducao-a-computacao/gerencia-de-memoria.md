---
conceito: Gerência de memória
slug: gerencia-de-memoria
disciplina: introducao-a-computacao
tipo: conceito
aka: [gerenciamento de memória, gestão de memória]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/rco/2tri/37-o-que-e-um-sistema-operacional.md"
aulas: [37]
atualizado_em: 2026-09-22
---

É uma das funções centrais do [[sistema-operacional]]: dividir a memória RAM entre os programas em execução, dando a cada um o espaço de que precisa, evitando que um invada o espaço do outro e liberando a memória quando um programa é fechado.

## Em uma frase

A função do sistema operacional que reparte a RAM entre os programas e evita que um invada o espaço do outro.

## O que precisa saber

Essa gerência acontece o tempo todo, de forma invisível: é por isso que abrir programas demais deixa o computador lento — o [[sistema-operacional]] está fazendo malabarismo para encaixar todos na [[memoria-ram]] disponível — e é o SO que devolve a memória automaticamente quando um app é fechado, liberando espaço para os outros. É uma das quatro funções que, junto com o escalonamento de [[processo|processos]], o [[sistema-de-arquivos]] e os [[driver|drivers]], transformam um monte de [[hardware]] num computador utilizável. Diagnosticar lentidão por excesso de programas abertos como um problema de gerência de memória (e não de processador) é o tipo de raciocínio técnico que essa função ensina a fazer.

## Erros comuns

- Atribuir lentidão com "muita coisa aberta" só à CPU: o sintoma mais comum desse cenário é a memória RAM sob pressão, não o processador sobrecarregado.
- Achar que a memória liberada por um programa fechado continua "ocupada" até reiniciar o computador: o SO devolve esse espaço automaticamente, na hora, para os demais programas usarem.

## Onde aparece

- Aula 37 — *O Que o Sistema Operacional Faz por Você* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/37-o-que-o-sistema-operacional-faz-por-voce/canonica.md`
- Conceitos vizinhos: [[sistema-operacional]], [[memoria-ram]], [[processo]], [[sistema-de-arquivos]]

## Fontes

- Definição da função e exemplo de lentidão por memória: base da canônica aprovada da Aula 37, apoiada na extração RCO (`lake/introducao-a-computacao/rco/2tri/37-o-que-e-um-sistema-operacional.md`), que lista "controlar o uso da memória" entre as funções do SO no estudo de caso da prática.
