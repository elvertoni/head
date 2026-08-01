---
conceito: Hash de senhas
slug: hash-de-senhas
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [password hashing]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/30 - Aula 30 - Mecanismo de Segurança_ Cors, Autenticação e Autorização III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Hash de senhas transforma uma senha em um valor de verificação usando um algoritmo adaptativo e salt, como bcrypt, para que o sistema não precise armazenar a senha original. O custo configurável dificulta tentativas em massa; isso é diferente de um hash rápido usado para integridade ou identificação.

## Em uma frase

Hash de senha armazena uma verificação resistente a recuperação direta da senha original.

## O que precisa saber

Cada senha deve receber salt único e custo adequado ao ambiente. No login, o sistema aplica o mesmo processo e compara a verificação sem revelar a senha. [[autenticacao]] identifica o usuário; o hash protege um segredo específico e não substitui autorização ou MFA.

## Erros comuns

- Usar MD5 ou SHA-256 puro para armazenar senhas.
- Reutilizar salt ou guardar salt de modo inadequado.
- Comparar senha em texto plano ou registrar credenciais em logs.

## Onde aparece

- Frameworks e Aplicações, Aula 30, páginas 2–5.
- Relaciona-se a [[hashing]], [[autenticacao]], [[seguranca-da-informacao]] e [[autorizacao]].

## Fontes

- Frameworks e Aplicações, Aula 30, slides sobre autenticação e armazenamento de credenciais.
