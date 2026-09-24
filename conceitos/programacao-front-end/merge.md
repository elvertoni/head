---
conceito: Merge
slug: merge
disciplina: programacao-front-end
tipo: conceito
aka: [mesclagem]
status: rascunho
fontes: []
aulas: [3, 4, 5]
atualizado_em: 2026-09-24
---

Merge é a operação do [[git|Git]] que traz os commits de uma [[branch]] para dentro de outra. Quando a branch de destino não recebeu nenhum commit novo enquanto a origem era desenvolvida, o Git só empurra o rótulo para a frente — um *fast-forward*, sem commit extra. Quando as duas divergiram, ele cria um *merge commit* com dois pais, um de cada branch.

## Em uma frase

Merge junta duas linhas de história: sem divergência vira fast-forward, com divergência vira um commit com dois pais.

## O que precisa saber

Quando as duas branches mudaram a mesma linha do mesmo arquivo de jeitos diferentes, o Git não sabe decidir sozinho e para o merge no meio — isso é um [[conflito-de-merge]]. Resolver exige ler as duas versões, editar manualmente o resultado e remover os marcadores (`<<<<<<<`, `=======`, `>>>>>>>`) antes de fechar com `git add` e `git commit`.

## Erros comuns

- Entrar em pânico ao ver um conflito e apagar trechos aleatórios só para o marcador sumir, em vez de ler as duas versões com calma.
- Achar que todo merge cria um commit extra — sem divergência, o Git só move o ponteiro (fast-forward).

## Onde aparece

- Aula 3 — *Branches: testando uma ideia arriscada sem bagunçar o que já funciona* `aulas/programacao-front-end/controle-de-versao-git-github/03-branches-modernas-e-merge/canonica.md`
- Aula 4 — *GitHub: tirando seu repositório do seu notebook e colocando na nuvem* `aulas/programacao-front-end/controle-de-versao-git-github/04-github-do-local-ao-remoto/canonica.md`
- Aula 5 — *Pull Request: como propor uma mudança sem simplesmente sobrescrever o código de alguém* `aulas/programacao-front-end/controle-de-versao-git-github/05-pull-request-e-revisao-de-codigo/canonica.md`
- Conceitos vizinhos: [[branch]], [[conflito-de-merge]], [[git]]

## Fontes

- Conteúdo autoral da Aula 3 (modo_origem: tema), sem fonte externa direta — fast-forward, merge commit e resolução de conflito.
