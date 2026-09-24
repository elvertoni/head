---
conceito: Autenticação
slug: autenticacao
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [authentication]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/28 - Aula 28 - Mecanismo de Segurança_ Cors, Autenticação e Autorização - Apostila (Slides).pdf"
aulas: [4]
atualizado_em: 2026-09-24
---

Autenticação é o processo de verificar a identidade declarada por uma pessoa, serviço ou dispositivo. Ela responde “quem é?”; depois, autorização decide quais ações essa identidade pode realizar.

## Em uma frase

Autenticação verifica identidade; autorização controla permissão.

## O que precisa saber

Credenciais, sessões, tokens e fatores precisam ser protegidos e revogados quando necessário. [[cookies]] e [[gerenciamento-de-sessao]] podem participar do fluxo; [[jwt]] é uma representação de token, não uma política completa de segurança.

## Erros comuns

- Confundir login com autorização.
- Armazenar senha em texto ou usar hash inadequado.
- Não tratar expiração, recuperação e revogação.

## Onde aparece

- Aulas 28–31 — Segurança, CORS, Autenticação e Autorização.
- Aula 4 — *GitHub: tirando seu repositório do seu notebook e colocando na nuvem* `aulas/programacao-front-end/controle-de-versao-git-github/04-github-do-local-ao-remoto/canonica.md` — desde 2021 o GitHub exige SSH ou GitHub CLI em vez de usuário/senha em operações de linha de comando.
- Conecta [[gerenciamento-de-sessao]], [[cookies]], autorização, JWT, [[api]] e [[github]].

## Fontes

- Aula 28, páginas 1–6 dos slides: segurança Web e autenticação.
