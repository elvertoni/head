---
conceito: Módulos ESM
slug: modulos-esm
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [ECMAScript Modules, ES modules]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/03 - Aula 3 - Funções - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/12 - Aula 12 - Sistema de Módulos do NodeJS I - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/13 - Aula 13 - Sistema de Módulos do NodeJS II - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/14 - Aula 14 - Sistema de Módulos do NodeJS III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Módulos ESM são o sistema padrão de módulos do JavaScript baseado em import e export. Eles delimitam escopos, tornam dependências explícitas e permitem composição entre arquivos e pacotes.

## Em uma frase

ESM organiza JavaScript por imports e exports explícitos.

## O que precisa saber

O ambiente determina resolução, extensão, execução e suporte a top-level await. Módulos têm escopo próprio e devem expor uma interface pequena e estável.

## Erros comuns

- Misturar CommonJS e ESM sem entender a interoperabilidade.
- Criar ciclos de dependência difíceis de inicializar.
- Exportar detalhes internos como contrato público.

## Onde aparece

- JavaScript e Aplicações Práticas, Aula 3, páginas 1–2.
- Relaciona-se a [[javascript]], [[funcoes-em-javascript]] e [[framework]].

## Fontes

- Aula 3, páginas 1–2 dos slides: módulos JavaScript.
