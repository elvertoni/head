---
conceito: Driver
slug: driver
disciplina: introducao-a-computacao
tipo: conceito
aka: [driver de dispositivo]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 35_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/rco/2tri/37-o-que-e-um-sistema-operacional.md"
aulas: [35, 37]
atualizado_em: 2026-09-22
---

É um pequeno programa que ensina o [[sistema-operacional]] a conversar com um dispositivo específico, traduzindo os comandos gerais do SO para a linguagem exata daquele hardware. Sem o driver certo, o dispositivo não funciona direito — daí a frase comum "preciso instalar o driver".

## Em uma frase

O programa que traduz os comandos do sistema operacional para a linguagem de um dispositivo específico.

## O que precisa saber

Teclado, fone, impressora e câmera funcionam de um jeito físico diferente cada um, e o [[sistema-operacional]] não nasce sabendo conversar com todos — por isso existem drivers, posicionados perto do [[kernel]], em volta dele, junto com os demais serviços do sistema. É essa camada que permite plugar um fone e ele simplesmente tocar (porque o SO já tinha o driver certo) ou uma impressora nova não ser reconhecida (porque falta o driver dela). O driver é uma das quatro funções centrais do SO no dia a dia, ao lado da [[gerencia-de-memoria]], do [[sistema-de-arquivos]] e do escalonamento de [[processo|processos]] — a diferença é que o driver mira em [[dispositivos-de-entrada-e-saida|dispositivos]] específicos, não em recursos genéricos da máquina.

## Erros comuns

- Achar que um dispositivo "não funciona" por estar quebrado, quando o problema real é o driver ausente ou incompatível com a versão do SO.
- Achar que instalar o driver é opcional ou só cosmético: sem o driver certo, o SO não sabe traduzir seus comandos para aquele hardware específico, e o dispositivo simplesmente não responde direito.

## Onde aparece

- Aula 35 — *Sistema Operacional - Conceito e Estrutura* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/35-sistema-operacional-conceito-e-estrutura/canonica.md`
- Aula 37 — *O Que o Sistema Operacional Faz por Você* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/37-o-que-o-sistema-operacional-faz-por-voce/canonica.md`
- Conceitos vizinhos: [[sistema-operacional]], [[kernel]], [[dispositivos-de-entrada-e-saida]]

## Fontes

- Posição do driver na estrutura em camadas (junto ao kernel): base da canônica aprovada da Aula 35, derivada dos slides SEED (`lake/introducao-a-computacao/AULA 35_INTRODUÇÃO A COMPUTAÇÃO.pptx`).
- Definição funcional e exemplo da impressora: base da canônica aprovada da Aula 37, apoiada na extração RCO (`lake/introducao-a-computacao/rco/2tri/37-o-que-e-um-sistema-operacional.md`), que cita "facilitar a comunicação entre os programas e os componentes do computador" entre as funções do SO.
