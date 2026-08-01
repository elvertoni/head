---
conceito: Hypervisor
slug: hypervisor
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: entidade
aka: [hipervisor, virtual machine monitor, monitor de máquina virtual]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Estratégias de Cloud Computing/18 - Aula 18 - Conceitos de Virtualização e Conteinerização II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Hypervisor é a camada de software que abstrai o hardware físico, distribui recursos às máquinas virtuais e mantém o isolamento entre sistemas convidados. Ele controla a fronteira entre o ambiente físico e os ambientes virtualizados.

## Em uma frase

Hypervisor administra recursos físicos para executar máquinas virtuais isoladas.

## O que precisa saber

O hypervisor sustenta [[virtualizacao]] e pode hospedar várias [[maquina-virtual|máquinas virtuais]]. A qualidade do isolamento depende da implementação, da configuração e da segurança do host; o hypervisor não transforma automaticamente qualquer ambiente em confiável.

## Erros comuns

- Confundir hypervisor com a própria máquina virtual ou com o sistema operacional convidado.
- Ignorar atualizações e controles do host porque os convidados parecem isolados.

## Onde aparece

Depende de [[virtualizacao]] e [[maquina-virtual]] e se conecta a [[conteinerizacao]] e [[computacao-em-nuvem]]. Ainda não há aula canônica registrada em `aulas`.

## Fontes

- Aula 18 de Estratégias de Cloud Computing, slides indicados no frontmatter.

