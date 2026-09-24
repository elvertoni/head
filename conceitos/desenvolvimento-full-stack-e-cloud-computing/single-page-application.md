---
conceito: Single-page application
slug: single-page-application
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [SPA, aplicação de página única]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/04 - Aula 4 - Primeiros Passos com React I - Apostila (Slides).pdf"
aulas: [6, 8]
atualizado_em: 2026-09-24
---

Single-page application é uma aplicação Web que mantém uma entrada carregada no navegador e atualiza vistas e dados no cliente sem recarregar todo o documento a cada navegação. Ela pode melhorar a fluidez, mas transfere decisões de estado, roteamento, carregamento e acessibilidade para o frontend.

## Em uma frase

Uma SPA atualiza a interface no cliente sem reconstruir toda a página a cada rota.

## O que precisa saber

Uma SPA usa componentes, estado e roteamento para trocar a vista; [[react]] é uma tecnologia comum nesse modelo. A escolha pode ser combinada com [[ssr]], [[ssg]] ou [[csr]], conforme SEO, carregamento e dados. O navegador ainda precisa tratar histórico, acessibilidade e falhas de rede.

## Erros comuns

- Supor que SPA elimina requisições ao servidor.
- Ignorar carregamento inicial, histórico, acessibilidade e SEO.
- Colocar toda a lógica de dados e estado no componente da tela.

## Onde aparece

- Projeto Front-End e Desenvolvimento Web, Aula 4, página 3.
- Aula 6 — *Blueprint · HealthSync* `aulas/tcc/blueprint-tcc/06-blueprint-healthsync/canonica.md` — SPA responsiva com roteamento dinâmico sem recarga, rodando inteiramente no cliente.
- Aula 8 — *Blueprint · Lumina* `aulas/tcc/blueprint-tcc/08-blueprint-lumina/canonica.md` — SPA com arquitetura cliente-servidor via BaaS.
- Relaciona-se a [[react]], [[frontend]], [[csr]] e [[roteamento]].

## Fontes

- Projeto Front-End e Desenvolvimento Web, Aula 4, slide sobre aplicações React de página única.
