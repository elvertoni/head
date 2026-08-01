---
conceito: CDN
slug: cdn
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Content Delivery Network, rede de distribuição de conteúdo]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/08 - Aula 8 - Projeto Mão na Massa - Bootstrap - Resumo (Aula em PDF).pdf"
aulas: []
atualizado_em: 2026-07-31
---

CDN é uma rede de servidores distribuídos que entrega arquivos estáticos, como CSS, JavaScript, imagens e fontes, a partir de pontos próximos das pessoas usuárias. Em um projeto front-end, ela pode fornecer os arquivos do [[bootstrap]] sem copiá-los para o repositório.

## Em uma frase

CDN distribui recursos estáticos para reduzir distância e tempo de entrega.

## O que precisa saber

Referenciar uma CDN cria dependência de disponibilidade, versão e integridade do provedor. A escolha entre CDN e empacotamento local deve considerar cache, desempenho, privacidade e resiliência. No uso de [[bootstrap]], a versão carregada precisa ser controlada.

## Erros comuns

- Usar URL sem versão e permitir mudanças inesperadas.
- Não considerar falha de rede ou política de segurança.
- Confundir CDN com hospedagem da aplicação inteira.

## Onde aparece

- Aula 8 — Projeto Mão na Massa — Bootstrap, na trilha JavaScript e Aplicações Práticas.
- É um mecanismo de distribuição usado para carregar [[bootstrap]].

## Fontes

- Resumo da Aula 8, páginas 2–4: CDN e carregamento de CSS e JavaScript.
