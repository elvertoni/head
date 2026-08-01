---
conceito: Hashing
slug: hashing
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [função hash, função hash criptográfica, hash]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/22 - Aula 22 - Hashing, Integridade e Segurança das Transações no Blockchain - Apostila (Slides).pdf"
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/23 - Aula 23 - Hashing, Integridade e Segurança das Transações no Blockchain II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Hashing é o processo de aplicar uma função que transforma uma entrada de tamanho variável em uma saída de tamanho fixo, de modo determinístico e difícil de inverter. Em blockchain, o resumo ajuda a encadear blocos, detectar alterações e verificar integridade, mas não é uma forma de criptografia reversível.

## Em uma frase

Hashing transforma dados em um resumo fixo usado para comparação, integridade e encadeamento.

## O que precisa saber

Uma pequena alteração na entrada deve produzir uma saída diferente; a resistência a [[colisao-criptografica|colisões]] procura tornar difícil encontrar duas entradas com o mesmo resumo. [[sha-256]] é um algoritmo usado em aplicações de segurança; [[md5]] é historicamente importante, mas inadequado para usos críticos atuais. O hash participa da [[imutabilidade-de-registro]] e da integridade em [[blockchain]].

## Erros comuns

- Confundir hash com criptografia que pode ser decifrada pela chave correta.
- Dizer que hashes são matematicamente únicos, ignorando colisões.
- Usar MD5 para autenticação ou integridade de alta segurança.

## Onde aparece

- Aulas 22–23 — Hashing, Integridade e Segurança das Transações, no Módulo II.
- Conecta [[blockchain]], [[criptografia]], [[integridade-de-dados]], [[imutabilidade-de-registro]], [[colisao-criptografica]], [[sha-256]], [[md5]], [[nonce]], [[mineracao-de-criptomoedas]], [[bloco-de-blockchain]], [[arvore-de-merkle]] e [[raiz-de-merkle]].

## Fontes

- Slides da Aula 22, páginas 2–8: hashing, propriedades, SHA-256 e MD5.
- Slides da Aula 23, páginas 2–4: encadeamento pelo hash anterior e imutabilidade.
