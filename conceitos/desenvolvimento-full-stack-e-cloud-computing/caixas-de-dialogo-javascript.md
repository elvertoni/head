---
conceito: Caixas de diálogo JavaScript
slug: caixas-de-dialogo-javascript
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [alert, confirm e prompt]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Padrões Web - HTML e CSS/05 - Aula 5 - Criando Soluções WEB - Resumo (Aula em PDF).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Caixas de diálogo JavaScript são interfaces nativas do navegador para informar, confirmar ou solicitar um valor. alert exibe uma mensagem, confirm oferece uma escolha e prompt solicita texto, interrompendo o fluxo até a resposta ou cancelamento.

## Em uma frase

alert, confirm e prompt são interações nativas simples entre script e pessoa usuária.

## O que precisa saber

Essas funções pertencem ao ambiente do navegador e são um recurso de [[entrada-e-saida-em-javascript]]. O resultado de prompt costuma ser texto e pode exigir [[conversao-de-tipos]]. Para experiências mais integradas, a [[manipulacao-do-dom]] permite construir mensagens dentro da própria página.

## Erros comuns

- Usar diálogos bloqueantes em fluxos longos ou repetitivos.
- Não tratar cancelamento de confirm e prompt.
- Mostrar mensagens técnicas sem contexto para a pessoa usuária.

## Onde aparece

- Aula 5 — Criando Soluções WEB.
- Conecta [[javascript]], [[entrada-e-saida-em-javascript]], [[conversao-de-tipos]] e [[manipulacao-do-dom]].

## Fontes

- Resumo da Aula 5, páginas 3–5 e 8: alert, confirm, prompt e interação.
