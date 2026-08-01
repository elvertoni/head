---
conceito: Registro de imagens de containers
slug: registro-de-imagens-de-containers
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [container registry]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/05 - Aula 5 - Docker e Desenvolvimento de Aplicações II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Registro de imagens de containers é o serviço que armazena, versiona e distribui imagens para execução em ambientes de desenvolvimento ou produção. Ele participa da cadeia de entrega e da confiança do artefato.

## Em uma frase

Registry publica e distribui imagens versionadas de containers.

## O que precisa saber

Tags, digest, autenticação, varredura e política de retenção devem ser definidos. O registro precisa ser tratado como parte da superfície de segurança e supply chain.

## Erros comuns

- Sobrescrever tag de produção sem rastreabilidade.
- Publicar imagem com segredo embutido.
- Baixar imagem sem verificar origem ou integridade.

## Onde aparece

- Desenvolvimento Web, Aula 5, páginas 9–10.
- Relaciona-se a [[imagem-docker]], [[docker]], [[seguranca-em-nuvem]] e [[pipeline-ci-cd]].

## Fontes

- Aula 5, páginas 9–10 dos slides: registro de imagens.
