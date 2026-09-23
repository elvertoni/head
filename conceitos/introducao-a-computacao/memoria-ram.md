---
conceito: Memória RAM
slug: memoria-ram
disciplina: introducao-a-computacao
tipo: conceito
aka: [RAM, memória principal, memória de acesso aleatório]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 23_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 24_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 27_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 30_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 31_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 32_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA_RETOMADA_2_ INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/rco/2tri/37-o-que-e-um-sistema-operacional.md"
aulas: [2, 23, 24, 27, 30, 31, 32, 37]
atualizado_em: 2026-09-22
---

A memória RAM (Memória de Acesso Aleatório) guarda temporariamente os dados e instruções que estão em uso ativo pela [[cpu]] naquele momento. É rápida, para a CPU acessar sem espera, mas volátil: seu conteúdo desaparece quando o computador desliga. Por isso um programa precisa subir do [[armazenamento-secundario]] para a RAM antes de ser executado, e um arquivo aberto só se torna permanente quando salvo de volta no armazenamento.

## Em uma frase

A RAM guarda, de forma rápida e temporária, o que o computador está usando agora.

## O que precisa saber

Na [[hierarquia-de-memoria]], a RAM fica entre a [[memoria-cache]] (ainda mais rápida e menor, dentro da CPU) e o armazenamento secundário (mais lento, porém permanente): quanto mais alto na hierarquia, mais rápida, menor e mais cara é a memória. Quando muitos [[processo|processos]] estão abertos ao mesmo tempo, a RAM pode lotar — esse é um dos sintomas mais comuns de "computador lento", diferente do disco cheio. É o [[sistema-operacional]], por meio da [[gerencia-de-memoria|gerência de memória]], que divide o espaço da RAM entre os programas, evitando que um invada o espaço do outro e liberando a área quando um processo termina.

## Erros comuns

- Confundir "estar aberto" com "estar salvo": enquanto você digita, o conteúdo vive só na RAM; sem salvar, ele some se a energia acabar.
- Achar que o programa "roda direto do disco" sem passar pela RAM — o disco é permanente, mas lento demais para a CPU trabalhar nele diretamente o tempo todo.
- Atribuir à RAM qualquer lentidão: disco cheio e RAM cheia são problemas em lugares diferentes, embora os dois pareçam "computador lento".

## Onde aparece

- Aula 2 — *Retomada - Entendendo a Execução de Programas* `aulas/introducao-a-computacao/nivelamento-e-retomada/02-retomada-execucao-de-programas/canonica.md`
- Aula 23 — *Introdução à Arquitetura de Computadores - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/23-introducao-a-arquitetura-de-computadores-parte-1/canonica.md`
- Aula 24 — *Introdução à Arquitetura de Computadores - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/24-introducao-a-arquitetura-de-computadores-parte-2/canonica.md`
- Aula 27 — *Memória e Armazenamento - o Temporário e o Permanente* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/27-memoria-e-armazenamento-temporario-e-permanente/canonica.md`
- Aula 30 — *Vários Programas ao Mesmo Tempo - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/30-varios-programas-ao-mesmo-tempo-parte-2/canonica.md`
- Aula 31 — *A Memória do Computador - Parte 1 - a Cache* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/31-memoria-do-computador-parte-1-a-cache/canonica.md`
- Aula 32 — *A Memória do Computador - Parte 2 - a Hierarquia* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/32-memoria-do-computador-parte-2-a-hierarquia/canonica.md`
- Aula 37 — *O Que o Sistema Operacional Faz por Você* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/37-o-que-o-sistema-operacional-faz-por-voce/canonica.md`
- Conceitos vizinhos: [[cpu]], [[armazenamento-secundario]], [[memoria-cache]], [[hierarquia-de-memoria]], [[gerencia-de-memoria]]

## Fontes

- RAM como parte do sistema computacional: slides SEED das Aulas 23 e 24.
- Volatilidade da RAM versus armazenamento permanente: slides SEED da Aula 27.
- RAM como recurso disputado entre processos: slides SEED da Aula 30.
- RAM na hierarquia de memória, entre cache e disco: slides SEED das Aulas 31 e 32.
- Gerência de memória pelo sistema operacional: `lake/introducao-a-computacao/rco/2tri/37-o-que-e-um-sistema-operacional.md` (Aula 37).
- Fluxo integrado disco → RAM → CPU: slides SEED da retomada (`AULA_RETOMADA_2_ INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da Aula 2.
