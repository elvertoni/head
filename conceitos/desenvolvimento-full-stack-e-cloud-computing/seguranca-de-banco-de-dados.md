---
conceito: Segurança de banco de dados
slug: seguranca-de-banco-de-dados
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [database security]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/09 - Aula 9 - Sistemas de Gerenciamento de Bancos de Dados e Linguagem SQL - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/11 - Aula 11 - Sistemas de Gerenciamento de Bancos de Dados e Linguagem SQL III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Segurança de banco de dados reúne controles para proteger dados, esquemas e operações contra acesso indevido, alteração, exposição ou indisponibilidade. Ela combina identidade, privilégios, segregação de responsabilidades, proteção de credenciais, auditoria e recuperação, em vez de depender somente do comando de consulta.

## Em uma frase

Segurança de banco de dados controla quem acessa quais dados e o que pode fazer com eles.

## O que precisa saber

O [[dcl]] fornece comandos como `GRANT` e `REVOKE` para administrar privilégios sobre objetos. A aplicação deve combinar menor privilégio, autenticação, parametrização, criptografia, logs e cópias recuperáveis. [[autenticacao]] identifica a parte; autorização e privilégios decidem sua capacidade.

## Erros comuns

- Usar uma conta administrativa em toda a aplicação.
- Confundir autenticação com autorização.
- Conceder acesso amplo e nunca revisar privilégios ou credenciais.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aulas 9, página 3, e 11, páginas 7–8.
- Relaciona-se a [[dcl]], [[autenticacao]], [[seguranca-da-informacao]] e [[banco-de-dados]].

## Fontes

- Linguagens e Aplicações de Banco de Dados, Aula 9, slide de controle de acesso.
- Linguagens e Aplicações de Banco de Dados, Aula 11, slides sobre privilégios e segurança.
