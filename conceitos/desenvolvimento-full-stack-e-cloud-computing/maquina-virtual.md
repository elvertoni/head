---
conceito: Máquina virtual
slug: maquina-virtual
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [VM, virtual machine, máquinas virtuais]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Estratégias de Cloud Computing/11 - Aula 11 - Arquitetura e Serviço de Computação em Nuvem II - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Estratégias de Cloud Computing/18 - Aula 18 - Conceitos de Virtualização e Conteinerização II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Máquina virtual é um ambiente computacional isolado que emula recursos de hardware e executa um sistema operacional convidado sobre uma camada de virtualização. Ela permite empacotar e administrar ambientes distintos no mesmo hardware físico.

## Em uma frase

Máquina virtual executa um sistema convidado isolado sobre hardware abstraído.

## O que precisa saber

O [[hypervisor]] distribui CPU, memória, armazenamento e rede para as máquinas virtuais. Elas são uma aplicação de [[virtualizacao]] diferente de [[conteinerizacao]]: normalmente incluem um sistema operacional convidado completo, com custo e isolamento próprios.

## Erros comuns

- Assumir que uma VM elimina toda disputa por recursos ou torna falhas de hardware invisíveis.
- Confundir VM com container: os níveis de isolamento, inicialização e consumo de recursos são diferentes.

## Onde aparece

Relaciona-se a [[hypervisor]], [[virtualizacao]], [[conteinerizacao]] e [[computacao-em-nuvem]]. Ainda não há aula canônica registrada em `aulas`.

## Fontes

- Aulas 11 e 18 de Estratégias de Cloud Computing, slides indicados no frontmatter.

