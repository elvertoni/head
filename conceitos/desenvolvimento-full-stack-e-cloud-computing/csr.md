---
conceito: Client-side rendering
slug: csr
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [renderização no cliente, Client-Side Rendering]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks, Programação e Estratégias/02 - Aula 2 - Introdução Ao Desenvolvimento Front - end Com o Next.js II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

CSR é o modelo em que o navegador executa JavaScript para montar ou atualizar a interface depois de receber a aplicação e seus dados. Ele favorece interatividade, mas desloca trabalho e dependências para o cliente.

## Em uma frase

CSR renderiza a interface principalmente no navegador.

## O que precisa saber

O modelo contrasta com [[ssr]], [[ssg]] e [[isr]]. SEO, tempo até conteúdo, tamanho do JavaScript, cache e acessibilidade precisam ser avaliados para cada tela.

## Erros comuns

- Escolher CSR para tudo sem medir carregamento inicial.
- Expor segredo no código enviado ao navegador.
- Confundir hidratação com renderização completa no servidor.

## Onde aparece

- Frameworks, Programação e Estratégias, Aula 2, páginas 2–4.
- Relaciona-se a [[componentes-de-cliente-nextjs]], [[ssr]], [[nextjs]] e [[seo]].

## Fontes

- Aula 2, páginas 2–4 dos slides: renderização no cliente.
