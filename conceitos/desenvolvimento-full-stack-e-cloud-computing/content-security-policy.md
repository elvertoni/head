---
conceito: Content Security Policy
slug: content-security-policy
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [CSP]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/05 - Aula 5 - Imersão JavaScript - Coleções e Funções - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Content Security Policy é uma política HTTP que restringe origens e formas de carregamento ou execução de recursos no navegador. Ela reduz o impacto de classes de ataques como [[xss]] quando configurada em conjunto com outras defesas.

## Em uma frase

CSP limita quais recursos o navegador pode carregar e executar.

## O que precisa saber

Diretivas para scripts, estilos, fontes, imagens, frames e reportes precisam refletir a aplicação real. Nonce, hash e fontes permitidas têm implicações de manutenção.

## Erros comuns

- Liberar unsafe-inline ou wildcard sem necessidade.
- Implantar política que quebra recursos e depois desativá-la.
- Tratar CSP como substituto de escape e sanitização.

## Onde aparece

- JavaScript e Aplicações Práticas, Aula 5, página 3.
- Relaciona-se a [[xss]], [[seguranca-da-informacao]] e [[https]].

## Fontes

- Aula 5, página 3 dos slides: política de segurança de conteúdo.
