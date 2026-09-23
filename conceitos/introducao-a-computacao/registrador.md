---
conceito: Registrador
slug: registrador
disciplina: introducao-a-computacao
tipo: conceito
aka: [registradores, register]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 24_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [24]
atualizado_em: 2026-09-22
---

Registrador é uma pequena área de memória dentro da [[cpu]], usada para guardar valores intermediários, endereços e informações de controle enquanto uma instrução está sendo executada. Por ficar dentro do próprio processador, o registrador é a memória mais rápida do computador — mais rápida até que a [[memoria-cache]] — mas também a menor: guarda apenas o que a CPU precisa naquele instante específico, não o programa inteiro.

## Em uma frase

Registrador é a memória mais rápida do computador, dentro da CPU, que guarda os valores que uma instrução está usando agora.

## O que precisa saber

Se a [[memoria-ram]] é a mesa de trabalho onde ficam os arquivos abertos, os registradores são os poucos objetos que estão literalmente na mão de quem trabalha — o valor que acabou de ser calculado, o endereço da próxima instrução. Um deles tem função especial: o [[contador-de-programa]], que guarda a posição da próxima instrução a ser buscada e garante que o [[ciclo-de-instrucao]] avance na ordem certa. Registradores fazem parte da estrutura interna da CPU descrita na [[arquitetura-de-computadores]], junto com as unidades de cálculo e controle.

## Erros comuns

- Confundir registrador com RAM: registrador é interno à CPU, muito menor e mais rápido; a RAM guarda o programa inteiro em execução.
- Achar que o registrador guarda dados de forma persistente — ele guarda apenas o que está sendo processado naquele instante, sem função de armazenamento de longo prazo.
- Ignorar que o contador de programa é, ele próprio, um registrador com um papel específico dentro do ciclo de instrução.

## Onde aparece

- Aula 24 — *Introdução à Arquitetura de Computadores - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/24-introducao-a-arquitetura-de-computadores-parte-2/canonica.md`
- Conceitos vizinhos: [[cpu]], [[contador-de-programa]], [[ciclo-de-instrucao]], [[memoria-cache]]

## Fontes

- Definição de registrador como memória de altíssima velocidade dentro da CPU: slides SEED da Aula 24.
