---
conceito: Ciclo de vida do documento
slug: ciclo-de-vida-do-documento
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [document lifecycle]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/05 - Aula 5 - Imersão JavaScript - Coleções e Funções - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Ciclo de vida do documento descreve estados e eventos desde o carregamento inicial do HTML até o documento estar pronto e interativo. Código que manipula o DOM precisa respeitar quando elementos e recursos existem.

## Em uma frase

O documento passa por estados de carregamento antes de estar pronto para interação.

## O que precisa saber

DOMContentLoaded e load indicam marcos diferentes; scripts defer e async mudam ordem de execução. Componentes também precisam remover listeners e liberar recursos no encerramento.

## Erros comuns

- Acessar elemento antes de ele existir.
- Esperar load para toda interação e atrasar comportamento útil.
- Registrar inicialização repetida em navegação parcial.

## Onde aparece

- JavaScript e Aplicações Práticas, Aula 5, página 4.
- Relaciona-se a [[modelo-de-eventos-do-dom]], [[delegacao-de-eventos]] e [[navegador-web]].

## Fontes

- Aula 5, página 4 dos slides: ciclo de vida do documento.
