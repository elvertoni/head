---
conceito: GitHub
slug: github
disciplina: programacao-front-end
tipo: entidade
aka: [github.com]
status: rascunho
fontes: []
aulas: [4, 6]
atualizado_em: 2026-09-24
---

GitHub é um serviço na nuvem que hospeda repositórios [[git|Git]], dá interface visual a eles e adiciona ferramentas de colaboração — [[pull-request|Pull Requests]], issues, revisão de código. Ele usa o Git por baixo dos panos, mas não é o único jeito de usar Git: existem alternativas como GitLab e Bitbucket. Git é a linguagem; GitHub é um dos lugares onde ela é falada.

## Em uma frase

GitHub hospeda na nuvem o histórico que o Git já mantinha local.

## O que precisa saber

Tudo o que acontece com `init`, `add`, `commit` e [[branch|branches]] roda inteiramente no computador, sem internet. GitHub entra quando esse histórico precisa existir em outro lugar também: um repositório que nasceu local ganha um remoto com `git remote add origin` + `git push -u origin main`; um repositório que já existe no GitHub chega ao computador com `git clone`, que baixa o histórico inteiro de uma vez. Desde 2021 o GitHub não aceita mais usuário e senha em operações de linha de comando — exige [[autenticacao|autenticação]] por SSH ou por uma ferramenta como o GitHub CLI (`gh auth login`).

## Erros comuns

- Colar um token de acesso direto na URL remota ou deixá-lo esquecido num arquivo que entra num `git add .` — um token vazado continua no histórico para sempre, mesmo apagado depois.
- Achar que Git e GitHub são sinônimos, ou que Git só funciona depois que o repositório existe no GitHub.

## Onde aparece

- Aula 4 — *GitHub: tirando seu repositório do seu notebook e colocando na nuvem* `aulas/programacao-front-end/controle-de-versao-git-github/04-github-do-local-ao-remoto/canonica.md`
- Aula 6 — *GitHub Pages: transformando seu repositório num site que qualquer pessoa acessa* `aulas/programacao-front-end/controle-de-versao-git-github/06-deploy-com-github-pages/canonica.md`
- Conceitos vizinhos: [[git]], [[autenticacao]], [[pull-request]], [[github-pages]], [[github-flow]]

## Fontes

- Conteúdo autoral da Aula 4 (modo_origem: tema), sem fonte externa direta — `remote add`, `push`, `clone` e autenticação SSH/GitHub CLI.
