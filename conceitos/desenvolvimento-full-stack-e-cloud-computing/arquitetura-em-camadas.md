---
conceito: Arquitetura em camadas
slug: arquitetura-em-camadas
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [layered architecture]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/17 - Aula 17 - Uso de MVC como Padrão de Projeto II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Arquitetura em camadas separa um sistema em níveis com responsabilidades e dependências controladas. Cada camada oferece serviços à camada acima e protege detalhes internos quando o desenho é respeitado.

## Em uma frase

Camadas organizam responsabilidades e direção de dependências.

## O que precisa saber

Apresentação, aplicação, domínio e persistência são divisões possíveis, não uma lista universal. [[mvc]] e [[injecao-de-dependencia]] podem apoiar a separação.

## Erros comuns

- Criar camadas que apenas repassam chamadas sem responsabilidade.
- Permitir que a apresentação acesse diretamente a persistência.
- Confundir separação física com baixo acoplamento.

## Onde aparece

- Frameworks e Aplicações, Aula 17, página 2.
- Relaciona-se a [[mvc]], [[injecao-de-dependencia]] e [[padroes-arquiteturais]].

## Fontes

- Aula 17, página 2 dos slides: arquitetura em camadas.
