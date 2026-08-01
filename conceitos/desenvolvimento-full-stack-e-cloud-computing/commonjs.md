---
conceito: CommonJS
slug: commonjs
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [CommonJS Modules, CJS]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/12 - Aula 12 - Sistema de Módulos do NodeJS I - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/13 - Aula 13 - Sistema de Módulos do NodeJS II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

CommonJS é um sistema de módulos usado pelo Node.js baseado em `require`, `exports` e `module.exports`. Ele define como um arquivo importa dependências e publica valores para outros módulos.

## Em uma frase

CommonJS organiza módulos Node.js com `require` e `module.exports`.

## O que precisa saber

O contrato de importação e exportação do CommonJS é diferente do de [[modulos-esm]]; a escolha deve ser coerente com o runtime e com o campo correspondente em [[package-json]]. A interoperabilidade entre os dois modelos pode exigir convenções explícitas.

## Erros comuns

- Misturar `require` e `import` sem verificar o modo de módulos configurado.
- Exportar uma forma e importar outra, criando valores `undefined` ou contratos inconsistentes.

## Onde aparece

Relaciona-se a [[nodejs]], [[npm]], [[package-json]] e [[modulos-esm]]. Ainda não há aula canônica registrada em `aulas`.

## Fontes

- Aulas 12 e 13 de Arquitetura e Programação, slides indicados no frontmatter.

