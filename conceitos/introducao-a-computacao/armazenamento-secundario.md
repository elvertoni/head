---
conceito: Armazenamento secundário
slug: armazenamento-secundario
disciplina: introducao-a-computacao
tipo: conceito
aka: [armazenamento permanente, disco, HDD, SSD]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 27_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 32_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA_RETOMADA_2_ INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [2, 27, 32]
atualizado_em: 2026-09-22
---

Armazenamento secundário é o conjunto de dispositivos — disco rígido (HDD) ou unidade de estado sólido (SSD) — que guarda programas e arquivos de forma permanente, mesmo com o computador desligado. Ao contrário da [[memoria-ram]], não perde o conteúdo quando falta energia, mas é significativamente mais lento para a [[cpu]] acessar; por isso um programa precisa ser copiado do armazenamento para a RAM antes de ser executado com agilidade.

## Em uma frase

Armazenamento secundário guarda dados e programas de forma permanente, mesmo com o computador desligado.

## O que precisa saber

HDD e SSD cumprem o mesmo papel — memória de longo prazo — por tecnologias diferentes: o HDD usa um disco físico giratório (mais barato, mais lento); o SSD não tem partes móveis (mais rápido, mais caro). Na [[hierarquia-de-memoria]], o armazenamento secundário ocupa uma camada abaixo da RAM: mais lento e maior, mas também mais barato por unidade de espaço. Espaço insuficiente no armazenamento ("disco cheio") é um problema distinto de RAM cheia, embora ambos apareçam ao usuário como "computador lento" — diagnosticar qual dos dois está no limite é parte do trabalho de suporte e desenvolvimento. É também o [[sistema-de-arquivos]], mantido pelo [[sistema-operacional]], que organiza esse espaço em arquivos e pastas navegáveis.

## Erros comuns

- Achar que fechar um programa (que libera RAM) é o mesmo que apagar um arquivo (que libera espaço em disco) — são operações em memórias diferentes.
- Tratar "disco cheio" e "RAM cheia" como o mesmo sintoma: os dois deixam a máquina lenta, mas por causas e em lugares diferentes.
- Achar que um programa "roda direto do disco": ele precisa subir para a RAM antes de a CPU executá-lo com agilidade.

## Onde aparece

- Aula 2 — *Retomada - Entendendo a Execução de Programas* `aulas/introducao-a-computacao/nivelamento-e-retomada/02-retomada-execucao-de-programas/canonica.md`
- Aula 27 — *Memória e Armazenamento - o Temporário e o Permanente* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/27-memoria-e-armazenamento-temporario-e-permanente/canonica.md`
- Aula 32 — *A Memória do Computador - Parte 2 - a Hierarquia* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/32-memoria-do-computador-parte-2-a-hierarquia/canonica.md`
- Conceitos vizinhos: [[memoria-ram]], [[hierarquia-de-memoria]], [[sistema-de-arquivos]], [[cpu]]

## Fontes

- Diferença entre memória volátil e armazenamento permanente, boas práticas de gerência de espaço: slides SEED da Aula 27.
- Posição do armazenamento secundário na hierarquia de memória: slides SEED da Aula 32.
- Fluxo integrado disco → RAM → CPU: slides SEED da retomada (`AULA_RETOMADA_2_ INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da Aula 2.
