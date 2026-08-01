---
conceito: Mapeamento de portas
slug: mapeamento-de-portas
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [port mapping]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/07 - Aula 7 - Docker e Desenvolvimento de Aplicações IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Mapeamento de portas associa uma porta do host a uma porta exposta por um container para permitir que clientes alcancem o serviço. A associação é parte da configuração de rede, não da aplicação em si.

## Em uma frase

Mapeamento publica uma porta do container por uma porta do host.

## O que precisa saber

Porta publicada, endereço de escuta, rede interna e firewall formam o caminho. Expor somente o necessário reduz superfície de ataque.

## Erros comuns

- Publicar banco ou painel administrativo para toda a rede.
- Confundir porta interna com porta acessível externamente.
- Ignorar colisão de portas e regras de firewall.

## Onde aparece

- Desenvolvimento Web, Aula 7, página 3.
- Relaciona-se a [[docker]], [[rede-de-containers]], [[seguranca-em-nuvem]] e [[http]].

## Fontes

- Aula 7, página 3 dos slides: mapeamento de portas.
