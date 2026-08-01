---
conceito: package.json
slug: package-json
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: entidade
aka: [manifesto de pacote Node.js, package manifest]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/09 - Aula 9 - Fundamentos da Plataforma NodeJS I - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/12 - Aula 12 - Sistema de Módulos do NodeJS I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

`package.json` é o manifesto de um projeto ou pacote Node.js. Ele registra identidade, scripts, dependências, ponto de entrada e a forma de resolução de módulos que o projeto espera.

## Em uma frase

`package.json` declara como um projeto Node.js se identifica, executa e depende de pacotes.

## O que precisa saber

O arquivo é consumido por [[npm]] e participa da escolha entre [[commonjs]] e [[modulos-esm]]. Campos como scripts e dependências são contrato operacional; mudanças neles devem ser revisadas junto com o lockfile e o código que os consome.

## Erros comuns

- Confundir `package.json` com o lockfile: o manifesto declara intenção; o lockfile fixa a resolução concreta.
- Alterar o modo de módulos sem revisar imports, exports e ferramentas do projeto.

## Onde aparece

Depende de [[npm]], [[nodejs]], [[commonjs]] e [[modulos-esm]]. Ainda não há aula canônica registrada em `aulas`.

## Fontes

- Aulas 9 e 12 de Arquitetura e Programação, slides indicados no frontmatter.

