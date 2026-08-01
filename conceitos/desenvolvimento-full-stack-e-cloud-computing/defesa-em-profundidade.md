---
conceito: Defesa em profundidade
slug: defesa-em-profundidade
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [defense in depth]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Estratégias de Cloud Computing/14 - Aula 14 - Gerenciamento e Governança em Serviços de Nuvem - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Defesa em profundidade usa camadas complementares de proteção para que a falha de um controle não exponha sozinha o sistema. Identidade, autorização, segmentação, criptografia, monitoramento, backup e resposta podem reduzir impactos diferentes, desde que não sejam apenas cópias do mesmo mecanismo.

## Em uma frase

Defesa em profundidade combina camadas independentes para limitar o impacto de falhas.

## O que precisa saber

Cada camada deve ter propósito, sinal de falha e responsável. Redundância de controles não substitui análise de ameaças; camadas mal configuradas podem criar falsa sensação de segurança. O modelo complementa [[seguranca-em-nuvem]], [[zero-trust]] e [[tolerancia-a-falhas]].

## Erros comuns

- Contar várias ferramentas que dependem da mesma credencial como camadas independentes.
- Configurar controles sem monitorar se funcionam.
- Confundir defesa em profundidade com complexidade sem prioridade.

## Onde aparece

- Estratégias de Cloud Computing, Aula 14, página 4.
- Relaciona-se a [[seguranca-em-nuvem]], [[seguranca-da-informacao]], [[zero-trust]] e [[tolerancia-a-falhas]].

## Fontes

- Estratégias de Cloud Computing, Aula 14, slide sobre camadas de segurança.
