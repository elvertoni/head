---
conceito: Branch
slug: branch
disciplina: programacao-front-end
tipo: conceito
aka: [ramificação, branch do Git]
status: rascunho
fontes: []
aulas: [3, 4, 5]
atualizado_em: 2026-09-24
---

Uma branch é um rótulo móvel apontando para um commit específico do [[git|Git]] — não uma cópia da pasta. Criar uma branch nova não duplica nenhum arquivo: o Git só cria um segundo rótulo no mesmo ponto do histórico, que a partir daí anda independente do original.

## Em uma frase

Branch é um ponteiro que se move, não uma cópia de arquivos.

## O que precisa saber

Todo repositório nasce com uma branch padrão (`main`), onde mora a versão estável. `git switch -c nome` cria e já troca para uma branch nova; `git switch nome` troca para uma que já existe. Trazer os commits de uma branch de volta para outra é um [[merge]] — sem divergência, o Git só empurra o rótulo (*fast-forward*); com divergência, cria um *merge commit* com dois pais. Quando as duas branches mudam a mesma linha do mesmo arquivo, o resultado é um [[conflito-de-merge]].

## Erros comuns

- Achar que criar uma branch copia o projeto inteiro — na prática é quase instantâneo, porque é só um ponteiro novo.
- Misturar experimento e versão estável na mesma branch em vez de isolar o risco numa branch nova.

## Onde aparece

- Aula 3 — *Branches: testando uma ideia arriscada sem bagunçar o que já funciona* `aulas/programacao-front-end/controle-de-versao-git-github/03-branches-modernas-e-merge/canonica.md`
- Aula 4 — *GitHub: tirando seu repositório do seu notebook e colocando na nuvem* `aulas/programacao-front-end/controle-de-versao-git-github/04-github-do-local-ao-remoto/canonica.md`
- Aula 5 — *Pull Request: como propor uma mudança sem simplesmente sobrescrever o código de alguém* `aulas/programacao-front-end/controle-de-versao-git-github/05-pull-request-e-revisao-de-codigo/canonica.md`
- Conceitos vizinhos: [[git]], [[merge]], [[conflito-de-merge]]

## Fontes

- Conteúdo autoral da Aula 3 (modo_origem: tema), sem fonte externa direta — `git switch -c`, fast-forward vs. merge commit e marcadores de conflito.
