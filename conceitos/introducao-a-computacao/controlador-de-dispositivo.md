---
conceito: Controlador de dispositivo
slug: controlador-de-dispositivo
disciplina: introducao-a-computacao
tipo: conceito
aka: [controlador, controller]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 24_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [24]
atualizado_em: 2026-09-22
---

Controlador de dispositivo é um chip, ou conjunto de chips, que controla fisicamente um dispositivo periférico. Ele recebe comandos gerais do sistema operacional ou da [[cpu]], executa a operação exigindo conhecimento dos detalhes elétricos e mecânicos daquele dispositivo específico, e devolve o resultado. Em vez de a CPU conhecer os detalhes de cada teclado, SSD ou placa de rede, o controlador faz essa ponte.

## Em uma frase

Controlador de dispositivo é o chip que traduz comandos gerais do sistema em ações específicas sobre um hardware periférico.

## O que precisa saber

Sem controlador, cada [[dispositivos-de-entrada-e-saida|dispositivo de entrada/saída]] exigiria que a CPU soubesse todos os detalhes físicos e elétricos de cada peça conectada — o que sobrecarregaria o processador com tarefas que não são sua função central. O controlador recebe o pedido do sistema, comunica-se com o dispositivo através do [[barramento]], e devolve o resultado processado. Esse é também o papel do [[driver]] em software: o driver ensina o sistema operacional a "conversar" com o controlador de um dispositivo específico, complementando em software a tradução que o controlador faz em hardware.

## Erros comuns

- Achar que a CPU controla diretamente cada tecla, pixel ou setor de disco: muitos desses detalhes ficam a cargo do controlador especializado.
- Confundir controlador (hardware) com driver (software) — são camadas diferentes que colaboram na mesma tradução entre sistema e dispositivo.
- Ignorar que sem controlador nenhum dispositivo periférico funciona, mesmo que o restante do computador esteja saudável.

## Onde aparece

- Aula 24 — *Introdução à Arquitetura de Computadores - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/24-introducao-a-arquitetura-de-computadores-parte-2/canonica.md`
- Conceitos vizinhos: [[dispositivos-de-entrada-e-saida]], [[barramento]], [[cpu]], [[driver]]

## Fontes

- Definição de controlador de dispositivo e sua função de ponte entre CPU e periféricos: slides SEED da Aula 24.
