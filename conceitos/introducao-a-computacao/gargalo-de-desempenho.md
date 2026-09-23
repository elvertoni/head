---
conceito: Gargalo de desempenho
slug: gargalo-de-desempenho
disciplina: introducao-a-computacao
tipo: conceito
aka: [bottleneck]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 30_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [30]
atualizado_em: 2026-09-22
---

Gargalo de desempenho é o recurso que está no limite e por isso restringe a velocidade do sistema como um todo — o "pescoço estreito da garrafa". Pode ser a [[cpu]] sem [[nucleo-de-processador|núcleos]] suficientes para as threads pesadas em execução, a [[memoria-ram|RAM]] lotada ou um disco de [[armazenamento-secundario]] lento; diagnosticar um travamento é descobrir qual desses recursos está saturado.

## Em uma frase

Gargalo de desempenho é o recurso saturado que está limitando a velocidade do sistema — CPU, RAM ou disco.

## O que precisa saber

O gargalo aparece quando a demanda por um recurso ultrapassa sua capacidade de resposta naquele instante. É o que explica o caso clássico do vídeo que trava enquanto a música continua tocando: a tarefa leve e contínua cabe nas brechas de [[escalonamento-de-processos|escalonamento]] mesmo com a CPU ocupada, mas a [[thread]] pesada de edição de vídeo precisa de mais tempo de CPU do que está disponível e engasga. Raciocinar em termos de gargalo transforma um diagnóstico vago ("está travando") em um diagnóstico específico: qual recurso — CPU, RAM ou disco — está no limite. Esse raciocínio orienta decisões práticas, como saber se vale mais a pena adicionar RAM, trocar o disco ou reduzir o número de tarefas pesadas simultâneas.

## Erros comuns

- Parar em "o programa travou" sem investigar qual recurso específico está saturado.
- Achar que um travamento pontual significa que o sistema inteiro parou, quando na prática tarefas leves continuam avançando enquanto só a tarefa pesada é penalizada.
- Presumir que o gargalo é sempre a CPU, ignorando RAM e disco como causas igualmente comuns.

## Onde aparece

- Aula 30 — *Vários Programas ao Mesmo Tempo - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/30-varios-programas-ao-mesmo-tempo-parte-2/canonica.md`
- Conceitos vizinhos: [[thread]], [[escalonamento-de-processos]], [[cpu]], [[memoria-ram]], [[armazenamento-secundario]]

## Fontes

- Definição de gargalo de desempenho e o caso do vídeo travando enquanto a música toca: slides SEED da Aula 30 (`lake/introducao-a-computacao/AULA 30_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da Aula 30.
