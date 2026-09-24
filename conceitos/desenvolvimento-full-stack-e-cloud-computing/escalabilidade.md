---
conceito: Escalabilidade
slug: escalabilidade
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [scalability]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Estratégias de Cloud Computing/04 - Aula 4 - Modelos de Nuvem_ Público, Privado e Híbrido - Apostila (Slides).pdf"
aulas: [1, 5, 7]
atualizado_em: 2026-09-24
---

Escalabilidade é a capacidade de aumentar ou reduzir recursos para acompanhar demanda, mantendo requisitos de desempenho e custo. Pode ocorrer verticalmente, aumentando uma máquina, ou horizontalmente, adicionando instâncias. A mesma ideia vale para um negócio: é escalável quando atende muito mais clientes sem aumentar o custo na mesma proporção — servir 10 ou 10.000 pessoas dá quase o mesmo trabalho.

## Em uma frase

Escalabilidade ajusta capacidade ao crescimento ou à redução da demanda.

## O que precisa saber

Nuvem facilita provisionamento, mas a aplicação precisa tolerar distribuição, estado, filas e limites. Escalabilidade é diferente de [[alta-disponibilidade]]: uma aplicação pode ter capacidade e ainda falhar por dependência única.

## Erros comuns

- Confundir mais máquinas com solução para qualquer gargalo.
- Escalar sem observar custo, consistência e banco de dados.
- Medir capacidade sem definir latência e carga esperadas.

## Onde aparece

- Aulas 4–6 — Modelos de Nuvem.
- Aula 7 — *Startup não é empresa pequena* `aulas/programacao-front-end/landing-page-mvp/07-startup-nao-e-empresa-pequena/canonica.md` — escalabilidade como diferença entre crescer (custo proporcional) e escalar.
- Aula 1 — *Blueprint · A.N.N Beauty* `aulas/tcc/blueprint-tcc/01-blueprint-a-n-n-beauty/canonica.md` — RNF05, arquitetura deve suportar aumento de usuários e dados sem degradar desempenho.
- Aula 5 — *Blueprint · Gold Fit* `aulas/tcc/blueprint-tcc/05-blueprint-gold-fit/canonica.md` — RNF05, suportar ao menos 10.000 usuários simultâneos.
- Aula 7 — *Blueprint · HobbyQuest* `aulas/tcc/blueprint-tcc/07-blueprint-hobbyquest/canonica.md` — RNF05, suportar múltiplos usuários simultâneos em ambiente de teste.
- Conecta [[computacao-em-nuvem]], [[nuvem-publica]], [[alta-disponibilidade]], [[arquitetura-de-nuvem]] e [[startup]].

## Fontes

- Aula 4, páginas 2–5 dos slides: características e benefícios dos modelos de nuvem.
