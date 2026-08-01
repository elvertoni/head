---
conceito: NPM
slug: npm
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: entidade
aka: [Node Package Manager, gerenciador de pacotes do Node.js]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/09 - Aula 9 - Fundamentos da Plataforma NodeJS I - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/12 - Aula 12 - Sistema de Módulos do NodeJS I - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/14 - Aula 14 - Sistema de Módulos do NodeJS III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

NPM é o gerenciador de pacotes e a CLI do ecossistema Node.js. Ele inicializa projetos, instala dependências e registra metadados e scripts que tornam a montagem do ambiente reproduzível.

## Em uma frase

NPM organiza dependências, scripts e distribuição de projetos Node.js.

## O que precisa saber

O manifesto [[package-json]] descreve o projeto e suas dependências; o NPM resolve versões e instala o grafo de pacotes. O gerenciador complementa [[nodejs]], mas não substitui revisão de dependências, lockfiles, auditoria e controle de versões.

## Erros comuns

- Confundir NPM com o runtime [[nodejs]]: um instala e organiza pacotes; o outro executa JavaScript.
- Tratar qualquer pacote instalado como confiável sem revisar origem, permissões e atualizações.

## Onde aparece

Relaciona-se a [[package-json]], [[commonjs]], [[modulos-esm]], [[nodejs]] e [[expressjs]]. Ainda não há aula canônica registrada em `aulas`.

## Fontes

- Aulas 9, 12 e 14 de Arquitetura e Programação, slides indicados no frontmatter.

