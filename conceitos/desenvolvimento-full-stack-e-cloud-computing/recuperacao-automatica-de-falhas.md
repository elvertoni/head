---
conceito: Recuperação automática de falhas
slug: recuperacao-automatica-de-falhas
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [self-healing]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/09 - Aula 9 - Kubernetes II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Recuperação automática de falhas substitui, reinicia ou realoca workloads quando o sistema detecta que o estado atual diverge do desejado. Ela reduz intervenção manual, mas depende de sinais e políticas corretos.

## Em uma frase

Self-healing tenta restaurar automaticamente workloads que falharam.

## O que precisa saber

Probes, réplicas, controllers e limites definem quando agir. A automação deve ser observável para não mascarar falhas sistêmicas.

## Erros comuns

- Reiniciar sem corrigir a causa raiz.
- Configurar probe que mata uma aplicação saudável.
- Confundir reinício com recuperação de dados persistentes.

## Onde aparece

- Desenvolvimento Web, Aulas 9–10, páginas indicadas.
- Relaciona-se a [[kubernetes]], [[tolerancia-a-falhas]], [[deployment]] e [[observabilidade]].

## Fontes

- Aula 9, página 4, e Aula 10, página 5 dos slides: recuperação automática.
