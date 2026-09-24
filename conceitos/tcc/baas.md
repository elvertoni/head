---
conceito: Backend as a Service
slug: baas
disciplina: tcc
tipo: conceito
aka: [BaaS, backend gerenciado]
status: rascunho
fontes: []
aulas: [7, 8]
atualizado_em: 2026-09-24
---

Backend as a Service (BaaS) é um modelo em que o time de desenvolvimento não escreve nem opera o servidor: contrata serviços gerenciados (autenticação, banco de dados, armazenamento, funções) de uma plataforma como o Firebase, e o aplicativo cliente fala diretamente com esses serviços.

## Em uma frase

BaaS troca "escrever um back-end" por "assinar um back-end pronto".

## O que precisa saber

Num TCC com prazo curto e equipe pequena, BaaS reduz drasticamente o que precisa ser construído: [[autenticacao|autenticação]], persistência e hospedagem já vêm prontas, restando o app cliente para desenvolver. A arquitetura ainda é [[arquitetura-cliente-servidor|cliente-servidor]] — só que o "servidor" é operado por terceiros, não pelo time do projeto. A contrapartida é menos controle sobre a lógica de negócio no servidor e dependência do plano e dos limites do provedor escolhido.

## Erros comuns

- Tratar BaaS como "sem backend" — o backend existe, só não é seu para operar; regras de segurança e validação ainda precisam ser configuradas no provedor.
- Escolher BaaS só pela gratuidade inicial sem avaliar o que acontece quando o uso crescer além do limite do plano gratuito.

## Onde aparece

- Aula 7 — *Blueprint · HobbyQuest* `aulas/tcc/blueprint-tcc/07-blueprint-hobbyquest/canonica.md` — Cliente-Servidor com BaaS (Firebase) para autenticação, banco de dados, armazenamento e funções.
- Aula 8 — *Blueprint · Lumina* `aulas/tcc/blueprint-tcc/08-blueprint-lumina/canonica.md` — SPA com arquitetura cliente-servidor via BaaS (Firebase Authentication e Realtime Database).
- Conceitos vizinhos: [[arquitetura-cliente-servidor]], [[autenticacao]], [[banco-de-dados-nao-relacional]]

## Fontes

- Conteúdo autoral dos blueprints de TCC (modo_origem: tema/projeto), sem fonte externa direta — BaaS como escolha arquitetural que reduz o escopo de backend em projetos de prazo curto.
