---
conceito: Estado desejado do Kubernetes
slug: estado-desejado-kubernetes
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [desired state]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/12 - Aula 12 - Arquitetando Aplicações para Kubernetes II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Estado desejado do Kubernetes é a configuração declarada que descreve quantas réplicas, quais imagens, redes e políticas um recurso deve ter. Controladores comparam esse estado ao estado atual e tentam reconciliá-los.

## Em uma frase

Estado desejado é o contrato que orienta a reconciliação do cluster.

## O que precisa saber

Falhas, atualizações e intervenções manuais podem gerar diferença temporária. [[controller-manager-kubernetes]], [[deployment]] e [[configuracao-declarativa-kubernetes]] participam da convergência.

## Erros comuns

- Achar que estado desejado descreve todos os detalhes de execução.
- Alterar recurso manualmente sem atualizar a fonte declarativa.
- Não observar quando a reconciliação não consegue convergir.

## Onde aparece

- Desenvolvimento Web, Aula 13, páginas 4–5; Aula 14, página 2.
- Relaciona-se a [[kubernetes]], [[deployment]] e [[controller-manager-kubernetes]].

## Fontes

- Aula 13, páginas 4–5, e Aula 14, página 2 dos slides: estado desejado.
