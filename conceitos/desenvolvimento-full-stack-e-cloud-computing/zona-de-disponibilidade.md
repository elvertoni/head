---
conceito: Zona de disponibilidade
slug: zona-de-disponibilidade
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [availability zone, AZ]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Estratégias de Cloud Computing/10 - Aula 10 - Arquitetura e Serviço de Computação em Nuvem - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Zona de disponibilidade é um domínio físico isolado dentro de uma região de nuvem, com infraestrutura e falhas parcialmente independentes. Distribuir componentes entre zonas reduz o impacto de uma falha local, desde que aplicação, dados, rede e recuperação também sejam projetados para isso.

## Em uma frase

Uma zona de disponibilidade separa fisicamente recursos para aumentar resiliência dentro de uma região.

## O que precisa saber

Alta disponibilidade entre zonas exige replicação, balanceamento, dados consistentes e testes de failover. Zonas não são regiões e não protegem automaticamente contra falhas regionais. A arquitetura deve definir RTO, RPO e dependências críticas.

## Erros comuns

- Confundir várias zonas com várias regiões.
- Distribuir servidores sem distribuir estado e dependências.
- Declarar alta disponibilidade sem testar a queda de uma zona.

## Onde aparece

- Estratégias de Cloud Computing, Aula 10, página 3.
- Relaciona-se a [[alta-disponibilidade]], [[tolerancia-a-falhas]], [[nuvem-publica]] e [[arquitetura-de-nuvem]].

## Fontes

- Estratégias de Cloud Computing, Aula 10, slide sobre regiões e zonas.
