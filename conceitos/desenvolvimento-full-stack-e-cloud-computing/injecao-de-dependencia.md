---
conceito: Injeção de dependência
slug: injecao-de-dependencia
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [dependency injection, DI]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/30 - Aula 30 - Evolução e Gestão do Ciclo de Vida de uma API - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Injeção de dependência entrega a um componente os serviços de que ele precisa, em vez de fazê-lo instanciá-los diretamente. Isso separa política de construção e uso.

## Em uma frase

Injeção de dependência fornece colaboradores de fora do componente.

## O que precisa saber

Dependências podem ser passadas por construtor, função ou mecanismo do framework. A técnica melhora substituição em testes e composição, mas exige limites e ciclo de vida claros.

## Erros comuns

- Injetar um contêiner global e esconder dependências reais.
- Criar grafos circulares difíceis de inicializar.
- Usar mocks que não respeitam o contrato do colaborador.

## Onde aparece

- Arquitetura e Programação, Aula 30, páginas 3–4.
- Relaciona-se a [[inversao-de-controle]], [[backend]] e [[expressjs]].

## Fontes

- Aula 30, páginas 3–4 dos slides: injeção de dependência em APIs.
