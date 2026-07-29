---
titulo: "Pull Request: como propor uma mudança sem simplesmente sobrescrever o código de alguém"
tema: Pull Requests e revisão de código no GitHub
disciplina: programacao-front-end
serie: 3ª
prerequisitos: ["Git remoto: push, clone, autenticação (Aula 3 — github-do-local-ao-remoto)"]
objetivos:
  - Explicar o que é um Pull Request e por que times não fazem merge direto na branch main
  - Abrir um Pull Request no GitHub a partir de uma branch, com título e descrição claros
  - Escrever mensagens de commit no padrão Conventional Commits (feat, fix, docs, chore)
  - Explicar o papel da revisão de código antes do merge, incluindo o que a IA (Copilot) já faz hoje nesse fluxo
trilha: controle-de-versao-git-github
ordem: 4
slug: pull-request-e-revisao-de-codigo
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-07-29
---

Imagina receber essa mensagem de um colega de equipe: "ah, mudei um pouco o seu código direto na `main`, dá uma olhada depois". Você sente um aperto no estômago, certo? Porque ele pulou a etapa mais importante: **te dar a chance de ver a mudança antes dela virar parte definitiva do projeto**. É exatamente esse aperto que o Pull Request existe pra eliminar — e é o fluxo que praticamente todo time profissional usa, sem exceção.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que é um **Pull Request** e por que times não fazem merge direto na `main`.
- Abrir um Pull Request no GitHub a partir de uma branch, com título e descrição claros.
- Escrever mensagens de commit no padrão **Conventional Commits** (`feat`, `fix`, `docs`, `chore`).
- Explicar o papel da revisão de código antes do merge — incluindo o que a IA (Copilot) já faz hoje nesse fluxo.

## Pré-requisitos

Você precisa ter feito a Aula 3 — conectar repositório ao GitHub, `push`, `clone` e autenticação — e saber criar branches (Aula 2).

## Desenvolvimento

### Por que não fazer merge direto na main

Você já sabe criar uma branch, commitar nela e dar merge na `main` sozinho — tecnicamente, nada te impede de fazer isso sem pedir satisfação a ninguém. O problema não é técnico, é de **processo**: se qualquer pessoa pode jogar código direto na `main` sem ninguém mais ver antes, a branch estável do projeto vira uma aposta. Um erro de digitação, uma lógica errada, um `console.log` esquecido — tudo isso entra sem ninguém ter tido a chance de dizer "espera, olha isso aqui".

### O que é um Pull Request, de verdade

:::conceito Pull Request (PR)
Um **Pull Request** é um **pedido formal** pra que os commits de uma branch sejam trazidos pra outra (geralmente pra `main`) — só que, ao contrário de um `merge` direto, o PR cria um **espaço de conversa** antes disso acontecer. O GitHub mostra automaticamente o diff (o que mudou, linha por linha), permite comentários em linhas específicas do código, e só depois de aprovado alguém aperta o botão de merge.
:::

Repara: o nome já entrega a ideia — *pull request* é literalmente "pedido pra que puxem (trragam) minhas mudanças". Você não está *empurrando* a mudança pra dentro da `main` sozinho; está **pedindo** que ela entre, depois de alguém revisar.

### Abrindo um PR na prática

O fluxo sempre segue essa ordem:

```bash
git switch -c feature/pagina-de-contato   # cria a branch pra funcionalidade
# ... edita arquivos, faz commits normalmente ...
git push -u origin feature/pagina-de-contato   # envia a BRANCH (não a main) pro GitHub
```

Depois do `push`, o GitHub mostra um aviso na tela do repositório: "essa branch teve mudanças recentes, quer abrir um Pull Request?". Ao clicar, você preenche:

- **Título** — resumo de uma linha da mudança (ex.: "Adiciona página de contato com formulário").
- **Descrição** — o quê mudou e **por quê**. PR sem descrição obriga quem revisa a adivinhar sua intenção lendo código frio.

O GitHub monta sozinho a comparação entre a branch e a `main`, mostrando exatamente as linhas adicionadas (verde) e removidas (vermelho) — é a mesma lógica do `diff` que você já viu aparecer num conflito de merge, só que numa interface visual.

:::dica Onde isso vira hábito profissional
Em qualquer vaga de estágio ou primeiro emprego em programação, "saber abrir um PR bem descrito" pesa tanto quanto saber a linguagem em si. Um PR com título vago ("mudanças") e descrição vazia atrasa a revisão de todo mundo; um PR claro é revisado mais rápido e gera menos vai-e-volta.
:::

### Commits que contam uma história: Conventional Commits

Mensagem de commit tipo `"correções"`, `"ajustes"` ou `"wip"` (work in progress) não diz nada pra quem olha o histórico seis meses depois. O padrão **Conventional Commits**, adotado por um número enorme de projetos open source e empresas hoje, resolve isso com um prefixo que classifica a intenção do commit:

| Prefixo | Quando usar |
|---|---|
| `feat:` | uma funcionalidade nova |
| `fix:` | correção de um bug |
| `docs:` | mudança só em documentação/comentários |
| `style:` | formatação, sem mudar comportamento (espaço, ponto e vírgula) |
| `refactor:` | reorganiza código sem mudar o que ele faz |
| `chore:` | tarefa de manutenção (atualizar dependência, configurar ferramenta) |

:::exemplo Antes e depois
```
# Sem padrão — não diz nada
git commit -m "ajustes"

# Com Conventional Commits — diz o quê e a intenção
git commit -m "feat: adiciona validação de e-mail no formulário de contato"
git commit -m "fix: corrige botão de enviar que não respondia no mobile"
```
:::

:::atencao Erro comum
Escrever `fix: corrigido` ou `feat: mudanças` continua sendo tão vago quanto não usar o padrão — o prefixo classifica a **intenção**, mas a frase depois dele ainda precisa dizer **o quê** mudou. `feat: adiciona validação de e-mail` é útil; `feat: mudanças` não é.
:::

### Revisão de código: por que outro par de olhos importa

Depois do PR aberto, alguém revisa antes do merge — comentando dúvidas, apontando problemas, ou aprovando. É aqui que erros bobos (nome de variável errado, lógica que só funciona "no seu computador") são pegos **antes** de virar parte permanente do projeto, não depois.

```diagrama-progressivo
titulo: O que muda com revisão de código por IA (2026)
camadas:
  - rotulo: Revisão só humana
    conteudo: "Um colega lê o diff, comenta linha por linha, aprova ou pede ajuste. É o modelo clássico — continua sendo a base de qualquer time."
  - rotulo: Copilot code review
    conteudo: "O GitHub hoje oferece revisão automática por IA (Copilot) direto no PR: ela lê o diff e já deixa comentários sugerindo correções antes de um humano olhar, adiantando parte do trabalho de revisão."
  - rotulo: Resolução de conflito assistida
    conteudo: "O GitHub também já oferece um recurso pra pedir que a IA resolva conflitos de merge dentro do próprio PR, testando se o build continua passando depois — mas a decisão final de aprovar ainda é humana."
```

:::importante O ponto-chave
IA revisando código não elimina a revisão humana — ela **adianta** parte do trabalho repetitivo (apontar um padrão inconsistente, sugerir um teste faltando), deixando mais tempo pra revisão humana focar no que realmente importa: a lógica de negócio está certa? Essa decisão de projeto faz sentido? Isso nenhuma IA decide sozinha ainda.
:::

## Prática

**No repositório do Petfinder, no VSCode (~15 min):**

1. Crie uma branch nova com um nome descritivo, ex.: `feature/melhoria-no-rodape`.
2. Faça uma pequena mudança (ex.: um texto no rodapé) e commite usando Conventional Commits: `git commit -m "feat: adiciona texto de direitos autorais no rodapé"`.
3. Envie a branch: `git push -u origin feature/melhoria-no-rodape`.
4. No site do GitHub, abra um Pull Request dessa branch pra `main`, preenchendo título e descrição explicando o quê e por quê.
5. Peça pra um colega (ou pro professor) comentar algo no PR antes de aprovar — repare onde o comentário aparece: colado na linha exata do código.
6. Depois de aprovado, clique em "Merge pull request" no site — e confirme, com `git log --oneline --graph` no seu terminal (após um `git pull` na `main`), que o commit de merge apareceu.

## Avaliação

```quiz
- pergunta: Qual é a principal diferença entre um merge direto e um Pull Request?
  alternativas:
    - texto: "Não existe diferença técnica nenhuma"
    - texto: "O Pull Request cria um espaço de revisão e conversa antes do merge acontecer"
      correta: true
    - texto: "Pull Request só existe para repositórios privados"
    - texto: "Merge direto é mais rápido porque não usa Git"
  feedback: >
    Tecnicamente os dois terminam juntando commits de uma branch em outra. A
    diferença é o processo: o PR obriga uma etapa de revisão antes disso virar
    definitivo.
- pergunta: Qual mensagem de commit segue corretamente o padrão Conventional Commits?
  alternativas:
    - texto: "ajustes finais"
    - texto: "correções de bug"
    - texto: "fix: corrige botão de enviar que não respondia no mobile"
      correta: true
    - texto: "mudei umas coisas"
  feedback: >
    O prefixo (fix, feat, docs...) classifica a intenção, e a frase depois dele
    diz especificamente o quê mudou — as outras opções não fazem nenhuma das
    duas coisas.
- pergunta: O que a revisão de código por IA (Copilot) faz hoje, segundo o que a aula descreveu?
  alternativas:
    - texto: "Substitui totalmente a necessidade de um humano revisar o PR"
    - texto: "Adianta parte do trabalho repetitivo de revisão, mas a aprovação final continua sendo humana"
      correta: true
    - texto: "Só funciona em repositórios que não usam Pull Request"
    - texto: "Impede que qualquer conflito de merge aconteça"
  feedback: >
    A IA já revisa diffs e até ajuda a resolver conflitos, mas decisões sobre se
    a lógica de negócio faz sentido continuam exigindo julgamento humano.
```

## Fechamento

Hoje você viu que:

- **Pull Request** cria um espaço de revisão e conversa antes de trazer commits de uma branch pra `main` — não é só um merge com nome bonito.
- Abrir um bom PR exige título e descrição claros: o quê mudou e **por quê**.
- **Conventional Commits** (`feat:`, `fix:`, `docs:`, `chore:`...) transforma o histórico numa história legível, não numa lista de "ajustes".
- Revisão de código pega problema antes dele virar permanente — e hoje a IA (Copilot) já participa disso, adiantando trabalho, sem substituir a decisão humana final.

**Próxima aula:** seu código já está versionado, no GitHub, revisado por Pull Request. Falta uma coisa: mostrar o resultado rodando de verdade, num link que qualquer pessoa acessa. A última aula do módulo é sobre **GitHub Pages** — publicar o Petfinder direto do seu repositório.

:::roteiro
Abrir com a cena do colega que "mudou direto na main" — deixar a turma reagir antes de nomear o problema como "falta de revisão", não "falta de tecnologia". Fazer questão de mostrar um PR real e grande de um projeto open source conhecido (React, VSCode) projetado na tela — ver dezenas de comentários de revisão humana num PR de verdade costuma impressionar mais que qualquer explicação. Na tabela de Conventional Commits, não pedir decoreba dos seis prefixos: focar em feat/fix/docs, que cobrem 90% do uso real de aluno nessa fase. No trecho de IA revisando código, evitar tom de "vai substituir dev" — é tentador exagerar, mas a aula é clara que decisão de negócio continua humana; reforçar isso na fala. Reservar tempo real pra abrir um PR de verdade na prática — sem isso, o conceito fica abstrato.
:::
