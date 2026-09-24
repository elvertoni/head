---
conceito: Armazenamento local do navegador
slug: armazenamento-local-do-navegador
disciplina: tcc
tipo: conceito
aka: [Web Storage API, localStorage, armazenamento local]
status: rascunho
fontes: []
aulas: [6, 8]
atualizado_em: 2026-09-24
---

Armazenamento local do navegador (Web Storage API, geralmente via `localStorage`) guarda dados diretamente no navegador do usuário, em formato chave-valor, sem precisar de um servidor ou banco remoto. Os dados sobrevivem a recarregamentos de página, mas ficam presos àquele navegador e àquele dispositivo.

## Em uma frase

localStorage é um banco de dados de um usuário só, dentro do próprio navegador.

## O que precisa saber

Diferente de um [[banco-de-dados-relacional|banco relacional]] ou [[banco-de-dados-nao-relacional|não relacional]] hospedado num servidor, o armazenamento local não sincroniza entre dispositivos nem entre usuários — cada navegador guarda sua própria cópia isolada. Isso o torna adequado para persistir preferências, estado de sessão ou até um protótipo funcional inteiro (como um sistema [[crud|CRUD]] que simula um banco), mas inadequado sempre que mais de uma pessoa precisa enxergar o mesmo dado.

## Erros comuns

- Usar armazenamento local como se fosse um banco compartilhado — dois usuários em dois navegadores nunca veem os dados um do outro.
- Guardar dados sensíveis (senhas, dados de saúde) em texto puro no localStorage, que qualquer script rodando na página consegue ler.

## Onde aparece

- Aula 6 — *Blueprint · HealthSync* `aulas/tcc/blueprint-tcc/06-blueprint-healthsync/canonica.md` — Web Storage API (LocalStorage) como banco de dados único do sistema, com dados estruturados em JSON.
- Aula 8 — *Blueprint · Lumina* `aulas/tcc/blueprint-tcc/08-blueprint-lumina/canonica.md` — localStorage para persistência leve de preferências (timer, customização) sem dependência de rede.
- Conceitos vizinhos: [[banco-de-dados-relacional]], [[banco-de-dados-nao-relacional]], [[crud]]

## Fontes

- Conteúdo autoral dos blueprints de TCC (modo_origem: tema/projeto), sem fonte externa direta — armazenamento local do navegador como alternativa a banco de dados remoto em projetos client-side.
