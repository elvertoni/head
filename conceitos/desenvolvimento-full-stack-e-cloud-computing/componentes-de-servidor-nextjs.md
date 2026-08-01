---
conceito: Componentes de servidor Next.js
slug: componentes-de-servidor-nextjs
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [React Server Components no Next.js]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks, Programação e Estratégias/03 - Aula 3 - Introdução Ao Desenvolvimento Front - end Com o Next.js III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Componentes de servidor Next.js são componentes React renderizados no servidor, capazes de acessar recursos de backend sem enviar toda a lógica ao navegador.

## Em uma frase

Componentes de servidor mantêm parte da renderização e do acesso a dados fora do cliente.

## O que precisa saber

Eles se relacionam a [[nextjs]], [[react]] e [[ssr]], enquanto interações do navegador exigem componentes de cliente. Fronteiras, serialização e latência precisam ser explícitas.

## Erros comuns

- Usar APIs do navegador em componente de servidor.
- Enviar segredo ou dado privado para o bundle do cliente.

## Onde aparece

- Aulas 3–4 — Next.js.

## Fontes

- Aula 3, páginas 2–3 dos slides: componentes de servidor.
