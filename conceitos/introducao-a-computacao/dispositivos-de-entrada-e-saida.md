---
conceito: Dispositivos de entrada e saída
slug: dispositivos-de-entrada-e-saida
disciplina: introducao-a-computacao
tipo: conceito
aka: [periféricos, entrada e saída, E/S, I/O]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 23_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 24_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [23, 24]
atualizado_em: 2026-09-22
---

Dispositivos de entrada e saída são os componentes que fazem a ponte entre o computador e o mundo externo. Dispositivos de entrada — teclado, mouse, câmera, microfone, scanner, sensores — trazem dados para dentro do sistema; dispositivos de saída — monitor, caixa de som, impressora, projetor — devolvem o resultado do processamento. Alguns dispositivos, como tela touch, placa de rede e armazenamento externo, cumprem os dois papéis ao mesmo tempo.

## Em uma frase

Dispositivos de entrada trazem dados para o computador; dispositivos de saída devolvem o resultado processado.

## O que precisa saber

Nenhum dispositivo de entrada/saída conversa diretamente com a [[cpu]] em todos os seus detalhes elétricos e mecânicos: essa tradução é feita por um [[controlador-de-dispositivo|controlador]] específico, que recebe comandos gerais do sistema e os converte em ações concretas no hardware. Os dados trocados com esses dispositivos trafegam pelo [[barramento]] que liga periféricos ao restante do computador. No fluxo básico de um programa — entrada, processamento, memória, armazenamento, saída — os dispositivos de entrada/saída marcam o início e o fim visível do percurso: é o que o usuário aciona e o que o usuário vê, ouve ou recebe como resultado.

## Erros comuns

- Achar que a CPU processa diretamente cada evento de teclado, pixel de tela ou byte de impressão — o controlador do dispositivo cuida desses detalhes.
- Reduzir "entrada e saída" só a teclado e monitor, ignorando que rede, sensores e armazenamento externo também são periféricos de E/S.
- Ignorar que um mesmo dispositivo pode ser entrada e saída ao mesmo tempo (tela touch, placa de rede).

## Onde aparece

- Aula 23 — *Introdução à Arquitetura de Computadores - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/23-introducao-a-arquitetura-de-computadores-parte-1/canonica.md`
- Aula 24 — *Introdução à Arquitetura de Computadores - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/24-introducao-a-arquitetura-de-computadores-parte-2/canonica.md`
- Conceitos vizinhos: [[controlador-de-dispositivo]], [[barramento]], [[cpu]], [[arquitetura-de-computadores]]

## Fontes

- Classificação de dispositivos de entrada e saída, exemplos e papel no fluxo básico de informação: slides SEED da Aula 23.
- Dispositivos como parte do trânsito interno de dados e da relação com controladores: slides SEED da Aula 24.
