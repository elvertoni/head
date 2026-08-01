---
conceito: Loading UI do Next.js
slug: loading-ui-nextjs
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [loading.tsx]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks, Programação e Estratégias/13 - Aula 13 - Roteamento Avançado I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Loading UI do Next.js é a interface de fallback exibida enquanto um segmento de rota carrega dados ou componentes. Ela torna a espera explícita e pode acompanhar streaming e [[suspense-react]].

## Em uma frase

Loading UI comunica o estado de carregamento de uma rota.

## O que precisa saber

O fallback deve preservar contexto, acessibilidade e expectativa de tempo. Limites por segmento combinam com [[layout-nextjs]] e [[streaming-web]].

## Erros comuns

- Exibir carregamento sem informar o que está acontecendo.
- Criar layout que salta ou perde foco durante a troca.
- Usar spinner infinito para erros ou ausência de dados.

## Onde aparece

- Frameworks, Programação e Estratégias, Aula 13, páginas 2–4.
- Relaciona-se a [[suspense-react]], [[streaming-web]] e [[layout-nextjs]].

## Fontes

- Aula 13, páginas 2–4 dos slides: loading UI e roteamento avançado.
