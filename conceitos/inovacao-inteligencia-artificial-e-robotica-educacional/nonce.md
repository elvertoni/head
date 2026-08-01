---
conceito: Nonce
slug: nonce
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [number used once, número usado uma vez]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/20 - Aula 20 - Criptografia de Chave Pública II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Nonce é um valor usado como tentativa em um processo criptográfico para produzir uma saída que satisfaça uma condição da rede. Na [[prova-de-trabalho]], mineradores variam o nonce e recalculam o [[hashing|hash]] até encontrar um resultado dentro do alvo definido pelo protocolo.

## Em uma frase

Nonce é o valor variável que permite tentar novas saídas de hash até atender ao critério do protocolo.

## O que precisa saber

O nonce não é uma chave secreta nem uma prova isolada de validade. Ele faz parte do trabalho computacional usado para encontrar um bloco aceitável e deve ser analisado junto de [[prova-de-trabalho]], [[mecanismos-de-consenso]] e [[hashing]].

## Erros comuns

- Confundir nonce com senha ou chave privada.
- Achar que qualquer nonce válido dispensa a validação do bloco e das transações.
- Tratar a busca do nonce como uma operação criptográfica reversível.

## Onde aparece

- Aula 20 — Criptografia de Chave Pública II, no Módulo II.
- É um componente operacional de [[prova-de-trabalho]] e [[mecanismos-de-consenso]] que usa [[hashing]] na [[mineracao-de-criptomoedas]].

## Fontes

- Slides da Aula 20, página 4: nonce na busca de um hash que atenda ao critério da rede.
