---
conceito: Cross-Site Scripting
slug: xss
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [XSS, injeção de script]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/05 - Aula 5 - Imersão JavaScript - Coleções e Funções - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Cross-Site Scripting é a execução de script controlado por atacante em um contexto confiável do usuário, geralmente por conteúdo inserido sem escape ou sanitização. O impacto pode incluir roubo de sessão, alteração de interface e ações em nome do usuário.

## Em uma frase

XSS transforma entrada não confiável em código executável no navegador.

## O que precisa saber

Contexto de saída, escape, sanitização, cookies e [[content-security-policy]] formam camadas de defesa. O servidor continua responsável por validar e autorizar operações.

## Erros comuns

- Inserir string externa com innerHTML sem sanitização.
- Confiar apenas em filtro de palavras.
- Usar CSP como substituto de codificação correta.

## Onde aparece

- JavaScript e Aplicações Práticas, Aula 5, página 3.
- Relaciona-se a [[seguranca-da-informacao]], [[content-security-policy]], [[cookies]] e [[acessibilidade]].

## Fontes

- Aula 5, página 3 dos slides: riscos de script e segurança Web.
