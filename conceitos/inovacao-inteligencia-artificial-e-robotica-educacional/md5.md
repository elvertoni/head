---
conceito: MD5
slug: md5
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: entidade
aka: [Message-Digest Algorithm 5]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/22 - Aula 22 - Hashing, Integridade e Segurança das Transações no Blockchain - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

MD5 é um algoritmo de hash que produz um resumo de 128 bits. Embora ainda apareça em sistemas legados e verificações não adversariais, sua resistência a colisões foi quebrada e ele não deve ser escolhido para garantias críticas de integridade ou segurança.

## Em uma frase

MD5 é um hash legado inadequado para usos que dependem de resistência a colisões.

## O que precisa saber

MD5 ilustra que um algoritmo pode continuar popular depois de deixar de ser apropriado para segurança. A escolha precisa considerar o adversário e o objetivo: resumir dados não é o mesmo que autenticar dados. Ele deve ser comparado a [[sha-256]] no contexto de [[hashing]] e [[colisao-criptografica]].

## Erros comuns

- Usar MD5 para senhas, assinaturas ou integridade contra adulteração.
- Confundir checksum para detectar erro acidental com proteção criptográfica.
- Avaliar segurança apenas pela velocidade ou pela popularidade histórica.

## Onde aparece

- Aula 22 — Hashing, Integridade e Segurança das Transações, no Módulo II.
- É um algoritmo legado de [[hashing]] com problemas de [[colisao-criptografica]], comparado com [[sha-256]].

## Fontes

- Slides da Aula 22, páginas 2–8: MD5 e comparação entre algoritmos hash.
