---
conceito: HTTPS
slug: https
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [HTTP seguro]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/01 - Aula 1 - Arquitetura de Uma Aplicação Web e o Formato Json - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

HTTPS é HTTP transportado sobre uma conexão protegida por [[tls]]. Ele fornece autenticação do servidor, confidencialidade e integridade para requisições e respostas.

## Em uma frase

HTTPS protege a comunicação HTTP contra leitura e alteração indevidas.

## O que precisa saber

O certificado associa uma identidade a uma chave pública; o protocolo negocia chaves de sessão para os dados. HTTPS protege o canal, mas não corrige autorização, validação de entrada ou vazamentos na aplicação.

## Erros comuns

- Considerar HTTPS substituto de autenticação e autorização.
- Ignorar certificados expirados ou nomes incompatíveis.
- Misturar conteúdo HTTP e HTTPS e enfraquecer a página.

## Onde aparece

- Arquitetura e Programação, Aula 1, página 4.
- Relaciona-se a [[http]], [[tls]], [[api]] e [[autenticacao]].

## Fontes

- Aula 1, página 4 dos slides: HTTPS e segurança de transporte.
