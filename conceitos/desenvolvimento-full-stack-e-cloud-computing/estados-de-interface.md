---
conceito: Estados de interface
slug: estados-de-interface
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [UI states]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/05 - Aula 5 - Imersão JavaScript - Coleções e Funções - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Estados de interface são condições observáveis de um componente, como vazio, carregando, sucesso, erro, desabilitado ou foco. Explicitá-los torna comportamento e feedback mais previsíveis.

## Em uma frase

Estados de UI descrevem o que uma interface mostra e permite em cada condição.

## O que precisa saber

Cada estado precisa de transições, conteúdo, acessibilidade e ação possível. [[validacao-de-formulario]], [[foco-de-teclado]] e [[renderizacao-condicional]] ajudam a implementar a máquina de estados.

## Erros comuns

- Mostrar tela vazia durante carregamento ou erro.
- Permitir clique repetido em ação em andamento.
- Atualizar visualmente sem atualizar semântica e foco.

## Onde aparece

- JavaScript e Aplicações Práticas, Aula 5, páginas 2 e 4–5.
- Relaciona-se a [[renderizacao-condicional]], [[validacao-de-formulario]], [[foco-de-teclado]] e [[experiencia-do-usuario]].

## Fontes

- Aula 5, páginas 2 e 4–5 dos slides: estados e comportamento de UI.
