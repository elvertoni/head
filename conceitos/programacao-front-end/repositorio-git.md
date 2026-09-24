---
conceito: Repositório (repo)
slug: repositorio-git
disciplina: programacao-front-end
tipo: conceito
aka: [repo, repositório Git]
status: rascunho
fontes: []
aulas: [2]
atualizado_em: 2026-09-24
---

Um repositório Git é uma pasta de projeto com uma "caixa-preta" de histórico escondida dentro (a pasta `.git`, criada por `git init`). A partir do momento em que existe, o [[git|Git]] consegue guardar fotografias completas do estado dos arquivos — os commits — sempre que alguém mandar.

## Em uma frase

Uma pasta comum vira repositório quando ganha, dentro dela, um histórico de fotografias do próprio conteúdo.

## O que precisa saber

`git init` transforma a pasta atual num repositório em instantes, sem mexer nos arquivos existentes. Daí em diante, cada commit é uma fotografia inteira do projeto — não um diff — carimbada com data, autor e mensagem. Um repositório pode viver só localmente ou também existir num remoto como o [[github]], e as duas cópias não precisam estar sincronizadas o tempo todo.

## Erros comuns

- Rodar `git add .` sem olhar `git status` antes, marcando pra dentro do histórico arquivos que nunca deveriam entrar (capturas de tela, notas pessoais, pastas de dependências).
- Achar que "arquivo com nome de versão" (`v1`, `v2`, `final`) é o mesmo que ter um repositório — sem `.git`, não existe histórico real, só cópias soltas.

## Onde aparece

- Aula 2 — *Controle de versão: Git local* `aulas/programacao-front-end/controle-de-versao-git-github/02-controle-de-versao-git-local/canonica.md`
- Conceitos vizinhos: [[git]], [[github]]

## Fontes

- Conteúdo autoral da Aula 2 (modo_origem: tema), sem fonte externa direta — ciclo `init` / `add` / `commit` / `log` e papel do `.gitignore`.
