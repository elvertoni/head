---
conceito: Depuração
slug: depuracao
disciplina: introducao-a-computacao
tipo: conceito
aka: [debugging, debug]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 26_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [26]
atualizado_em: 2026-09-22
---

Depuração é o processo de encontrar e corrigir erros (bugs) em um programa. Quanto mais rápido é o ciclo entre alterar o código e ver o resultado da execução, mais rápida fica a depuração — é por isso que a estratégia de tradução escolhida para um programa afeta diretamente a velocidade com que seus erros são localizados e corrigidos.

## Em uma frase

Depuração é o ciclo de achar e corrigir erros num programa, tão rápido quanto o ciclo editar-rodar permitir.

## O que precisa saber

O [[interpretador]] favorece a depuração porque elimina a etapa de recompilar antes de testar de novo: muda uma linha, roda na hora, vê o efeito imediatamente. Um [[compilador]] não impede a depuração, mas encarece cada rodada de teste, já que qualquer alteração exige recompilar o programa inteiro antes de executar de novo. Por isso a escolha entre compilador e interpretador não é só sobre desempenho final — é também sobre quão caro fica repetir o ciclo de depuração durante o desenvolvimento. Essa é uma das razões pelas quais protótipos e código em fase de aprendizado tendem a rodar sob interpretadores, enquanto software já estabilizado é entregue compilado.

## Erros comuns

- Achar que só é possível depurar código interpretado — programas compilados também são depurados, só que com um ciclo editar-recompilar-rodar mais longo a cada tentativa.
- Confundir "depuração rápida" com "programa mais correto" — a velocidade do ciclo de teste ajuda a achar erros mais cedo, mas não elimina a necessidade de raciocinar sobre a causa do bug.

## Onde aparece

- Aula 26 — *Como o Computador Lê o seu Código - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/26-como-o-computador-le-o-codigo-parte-2/canonica.md`
- Conceitos vizinhos: [[interpretador]], [[compilador]]

## Fontes

- Slides SEED da aula 26 (`lake/introducao-a-computacao/AULA 26_INTRODUÇÃO A COMPUTAÇÃO.pptx`), slide 12: depuração como vantagem do interpretador por identificação mais rápida de erros.
- Base da canônica aprovada da aula 26, bloco :::conceito Depuração.
