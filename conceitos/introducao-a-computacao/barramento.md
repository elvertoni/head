---
conceito: Barramento
slug: barramento
disciplina: introducao-a-computacao
tipo: conceito
aka: [barramentos, bus]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 23_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 24_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [23, 24]
atualizado_em: 2026-09-22
---

Barramento é o conjunto de linhas de comunicação que permite a troca de dados, endereços e sinais de controle entre os componentes de um computador — [[cpu]], [[memoria-ram]], [[armazenamento-secundario]] e [[dispositivos-de-entrada-e-saida]]. Funciona como uma avenida interna: por ele passam as informações que mantêm as partes do sistema sincronizadas, e sua organização determina o quanto o fluxo entre componentes fica rápido ou congestionado.

## Em uma frase

Barramento é o caminho de comunicação por onde dados, endereços e sinais de controle circulam entre os componentes do computador.

## O que precisa saber

Nem todo tráfego interno tem a mesma prioridade, por isso os barramentos costumam ser organizados de forma hierárquica: a comunicação entre CPU e RAM precisa ser muito rápida, enquanto a comunicação com periféricos pode operar em ritmo mais lento — separar esses fluxos melhora o desempenho geral. Um barramento mal planejado ou congestionado é o equivalente, na cidade que é o computador, a ruas mal desenhadas: as peças existem, mas o fluxo de dados entre elas fica ruim. É por meio do barramento que um [[controlador-de-dispositivo|controlador]] entrega ao restante do sistema os dados vindos de um dispositivo periférico.

## Erros comuns

- Achar que o barramento guarda dados (isso é função de [[memoria-ram]] ou [[armazenamento-secundario]]) — ele apenas transporta.
- Ignorar que barramentos são hierarquizados: nem todo caminho de comunicação tem a mesma velocidade ou prioridade.
- Reduzir "arquitetura lenta" só a CPU ou memória fraca, sem considerar que um barramento congestionado também é gargalo de comunicação.

## Onde aparece

- Aula 23 — *Introdução à Arquitetura de Computadores - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/23-introducao-a-arquitetura-de-computadores-parte-1/canonica.md`
- Aula 24 — *Introdução à Arquitetura de Computadores - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/24-introducao-a-arquitetura-de-computadores-parte-2/canonica.md`
- Conceitos vizinhos: [[cpu]], [[memoria-ram]], [[dispositivos-de-entrada-e-saida]], [[controlador-de-dispositivo]]

## Fontes

- Barramentos como caminhos de comunicação entre componentes: slides SEED da Aula 23.
- Hierarquia de barramentos (CPU↔memória, CPU↔armazenamento, CPU↔periféricos) e sua relação com desempenho: slides SEED da Aula 24.
