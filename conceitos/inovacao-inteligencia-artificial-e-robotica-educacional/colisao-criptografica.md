---
conceito: Colisão criptográfica
slug: colisao-criptografica
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [hash collision, colisão de hash]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/22 - Aula 22 - Hashing, Integridade e Segurança das Transações no Blockchain - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Colisão criptográfica ocorre quando duas entradas diferentes produzem a mesma saída de uma função hash. Sistemas de hash voltados à segurança procuram tornar a descoberta intencional de colisões computacionalmente inviável, pois uma colisão pode enfraquecer verificações de integridade e identificação de conteúdo.

## Em uma frase

Colisão é a coincidência de um mesmo hash para entradas diferentes.

## O que precisa saber

Como as entradas possíveis são maiores que o conjunto de saídas de tamanho fixo, colisões são possíveis em princípio; a propriedade desejada é a resistência prática à sua descoberta. A análise deve ser feita em conjunto com [[hashing]], [[sha-256]] e [[md5]], não com a ideia de unicidade absoluta.

## Erros comuns

- Dizer que uma função hash segura torna colisões impossíveis.
- Confundir colisão com duas cópias idênticas do mesmo arquivo.
- Usar MD5 sem considerar ataques conhecidos contra sua resistência a colisões.

## Onde aparece

- Aula 22 — Hashing, Integridade e Segurança das Transações, no Módulo II.
- É uma propriedade de segurança analisada em [[hashing]], [[sha-256]], [[md5]] e [[raiz-de-merkle]].

## Fontes

- Slides da Aula 22, páginas 2–8: colisões e resistência a colisões em funções hash.
