---
conceito: Server Actions
slug: server-actions
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [ações de servidor]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks, Programação e Estratégias/07 - Aula 7 - Busca de Dados e Roteamento Dinâmico I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Server Actions são funções assíncronas executadas no servidor e acionáveis por componentes da interface. Elas aproximam mutações de dados da UI sem transferir ao navegador credenciais ou lógica de persistência.

## Em uma frase

Server Actions executam operações de servidor a partir de uma interface declarativa.

## O que precisa saber

Entradas precisam ser validadas e autorizadas como qualquer endpoint. A técnica se relaciona a [[componentes-de-servidor-nextjs]], [[busca-de-dados-no-servidor]] e revalidação.

## Erros comuns

- Tratar a action como função privada sem validar o chamador.
- Retornar dados sensíveis à interface.
- Misturar mutação, autorização e apresentação sem limites claros.

## Onde aparece

- Frameworks, Programação e Estratégias, Aula 7, página 3.
- Relaciona-se a [[componentes-de-servidor-nextjs]], [[busca-de-dados-no-servidor]] e [[revalidacao-de-dados]].

## Fontes

- Aula 7, página 3 dos slides: ações de servidor.
