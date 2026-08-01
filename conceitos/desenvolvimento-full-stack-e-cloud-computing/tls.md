---
conceito: TLS
slug: tls
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Transport Layer Security]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/01 - Aula 1 - Arquitetura de Uma Aplicação Web e o Formato Json - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

TLS é um protocolo criptográfico que autentica pares, negocia chaves e protege dados em trânsito. Em aplicações Web, é a camada de segurança normalmente usada pelo [[https]].

## Em uma frase

TLS cria um canal autenticado, confidencial e íntegro para a comunicação.

## O que precisa saber

O handshake negocia versão, algoritmos e chaves; certificados sustentam a autenticação do servidor. A segurança depende de configuração, cadeia de confiança e versões modernas do protocolo.

## Erros comuns

- Confundir criptografia de transporte com criptografia ponta a ponta do dado.
- Aceitar qualquer certificado em produção.
- Usar versões ou cifras obsoletas.

## Onde aparece

- Arquitetura e Programação, Aula 1, página 4.
- Fundamenta [[https]] e relaciona-se a [[criptografia]].

## Fontes

- Aula 1, página 4 dos slides: TLS na comunicação Web.
