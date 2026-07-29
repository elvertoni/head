---
titulo: "Branches: testando uma ideia arriscada sem bagunçar o que já funciona"
tema: Branches e merge no Git
disciplina: programacao-front-end
serie: 3ª
prerequisitos: ["Ciclo local do Git (Aula 1 — init, add, commit, log, .gitignore)"]
objetivos:
  - Explicar o que é uma branch e por que ela evita bagunçar o histórico principal
  - Criar e alternar entre branches com git switch
  - Fazer merge de uma branch e diferenciar fast-forward de merge commit
  - Resolver um conflito de merge de verdade, reconhecendo os marcadores de conflito
trilha: controle-de-versao-git-github
ordem: 3
slug: branches-modernas-e-merge
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 2
atualizado_em: 2026-07-29
---

Imagina que você está com o Petfinder funcionando perfeitamente, entregável amanhã, e bate aquela vontade de testar um modo escuro novo. Se você mexer direto nos arquivos de sempre, sua única versão estável fica **exposta** ao risco de o experimento dar errado. Hoje você aprende como criar uma linha do tempo paralela pra testar qualquer loucura — sem tocar num pixel da versão que já funciona.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que é uma **branch** e por que ela evita bagunçar o histórico principal.
- Criar e alternar entre branches usando `git switch`.
- Fazer **merge** de uma branch e diferenciar *fast-forward* de *merge commit*.
- Resolver um **conflito de merge** de verdade, reconhecendo os marcadores que o Git deixa no arquivo.

## Pré-requisitos

Você precisa ter feito a Aula 1 — Controle de versão: Git local — e ter um repositório com pelo menos dois commits pra praticar em cima.

## Desenvolvimento

### O problema: testar sem arriscar o que funciona

No fim da aula passada, seu histórico era uma linha reta: um commit atrás do outro. Isso é ótimo enquanto você só adiciona coisa que **já sabe** que vai funcionar. Mas todo projeto real chega numa hora em que você quer **experimentar** — um layout novo, uma função arriscada — sem comprometer a versão que já está pronta pra entregar.

A solução do Git pra isso não é copiar a pasta pra testar em outro lugar. É criar uma **branch**.

### Branch: um ponteiro que se move, não uma cópia da pasta

:::conceito Branch
Uma **branch** é só um **rótulo móvel** apontando pra um commit específico. Quando você cria uma branch nova, o Git não duplica nenhum arquivo — ele só cria um segundo rótulo, no mesmo ponto do histórico onde você está agora. A partir daí, cada rótulo (cada branch) anda **independente**: os commits que você faz numa branch não aparecem na outra, até você decidir juntar as duas.
:::

Por padrão, todo repositório novo nasce com uma branch chamada `main` — é nela que mora a versão estável do projeto. Quando você quer experimentar algo, você cria uma branch nova a partir dela.

```bash
git switch -c modo-escuro   # cria a branch "modo-escuro" E já muda pra ela
git branch                  # lista todas as branches, com * marcando a atual
git switch main             # volta pra branch principal a qualquer momento
```

O `-c` de `git switch -c` significa *create*: cria a branch e já te leva pra ela num único comando. Sem o `-c`, `git switch nome-da-branch` só troca pra uma branch que já existe.

:::dica Onde isso vira hábito profissional
Em qualquer equipe, cada funcionalidade nova nasce numa branch com nome descritivo: `feature/modo-escuro`, `fix/botao-quebrado`, `feature/login-google`. Isso é o chamado **feature branch workflow** — a branch `main` só recebe código já testado, nunca experimento cru. Quando você ouvir um dev falando "abri uma branch pra isso", é exatamente isso que ele fez.
:::

### Merge: juntando duas linhas de história

Depois que o experimento em `modo-escuro` está bom, você quer trazer esse trabalho de volta pra `main`. Isso é um **merge**: pegar os commits de uma branch e incorporá-los em outra.

```bash
git switch main            # vá para a branch que vai RECEBER as mudanças
git merge modo-escuro       # traz os commits da branch modo-escuro para main
```

O Git resolve isso de duas formas, dependendo do que aconteceu enquanto você estava fora:

```diagrama-progressivo
titulo: Fast-forward ou merge commit?
camadas:
  - rotulo: Ninguém mexeu em main
    conteudo: "Se main não recebeu nenhum commit novo enquanto você trabalhava em modo-escuro, o Git só empurra o rótulo main pra frente, até o último commit da outra branch. Isso é um fast-forward — não cria nenhum commit extra, é só mover o ponteiro."
  - rotulo: Alguém mexeu em main também
    conteudo: "Se main ganhou commits novos enquanto você trabalhava em modo-escuro, o Git precisa costurar as duas histórias. Ele cria um commit especial, o merge commit, que tem DOIS pais — um de cada branch — marcando o ponto exato onde as linhas se juntaram."
  - rotulo: E se as duas mexeram no mesmo lugar?
    conteudo: "Se as duas branches mudaram a MESMA linha do mesmo arquivo de jeitos diferentes, o Git não sabe qual versão manter sozinho. Isso é o conflito de merge — o próximo assunto desta aula."
```

### Quando o Git não consegue decidir sozinho: o conflito

Um conflito de merge não é um erro seu, nem um bug do Git. É o Git sendo **honesto**: duas versões diferentes da mesma linha existem, e só um humano sabe qual delas (ou se as duas) deve sobreviver. Quando isso acontece, o Git para o merge no meio e marca o arquivo com esses símbolos:

```html
<<<<<<< HEAD
<p>Bem-vindo ao Petfinder!</p>
=======
<p>Encontre seu novo melhor amigo no Petfinder!</p>
>>>>>>> modo-escuro
```

- Tudo entre `<<<<<<< HEAD` e `=======` é a versão da branch em que você está agora.
- Tudo entre `=======` e `>>>>>>> modo-escuro` é a versão da outra branch.
- Resolver o conflito é **editar o arquivo manualmente**: decidir qual trecho fica (ou escrever um terceiro, misturando os dois) e **apagar as três linhas de marcador** — `<<<<<<<`, `=======` e `>>>>>>>` nunca devem sobrar no arquivo final.

Depois de editar, o fluxo é o mesmo de sempre: `git add` no arquivo corrigido e `git commit` pra fechar o merge.

:::atencao Erro comum
O erro mais comum ao ver um conflito pela primeira vez é entrar em pânico e sair apagando trechos aleatórios só pra fazer o marcador sumir. Isso pode apagar código que funcionava. O jeito certo é **ler as duas versões com calma**, entender o que cada uma faz, e só então decidir — o conflito só existe porque humano precisa decidir, não porque algo quebrou.
:::

## Prática

**No terminal do VSCode, dentro do seu repositório do Petfinder (~15 min):**

1. Confirme que está na `main`: `git branch`.
2. Crie e mude para uma branch nova: `git switch -c modo-escuro`.
3. Edite uma linha de texto em `index.html` (ex.: mude o parágrafo de boas-vindas) e commite: `git add .` + `git commit -m "Ajusta texto de boas-vindas"`.
4. Volte pra `main`: `git switch main`.
5. Edite a **mesma linha**, com um texto diferente, e commite também na `main`.
6. Rode `git merge modo-escuro` — o Git vai avisar sobre um conflito.
7. Abra o arquivo, encontre os marcadores `<<<<<<<` / `=======` / `>>>>>>>`, escolha o texto final e apague os marcadores.
8. Finalize com `git add .` e `git commit` (o Git já sugere uma mensagem de merge — pode aceitar).
9. Rode `git log --oneline --graph` e observe o ponto onde as duas linhas se juntam.

## Avaliação

```quiz
- pergunta: O que uma branch realmente é, por dentro do Git?
  alternativas:
    - texto: "Uma cópia completa de todos os arquivos do projeto"
    - texto: "Um rótulo móvel apontando para um commit, que anda independente das outras branches"
      correta: true
    - texto: "Um backup automático feito na nuvem"
    - texto: "Uma pasta separada dentro do repositório"
  feedback: >
    Criar uma branch não duplica arquivo nenhum — é só um ponteiro novo no mesmo
    ponto do histórico, que passa a se mover sozinho a partir dali.
- pergunta: Quando acontece um fast-forward em vez de um merge commit?
  alternativas:
    - texto: "Sempre que você usa git merge"
    - texto: "Quando a branch main não recebeu nenhum commit novo enquanto a outra branch era desenvolvida"
      correta: true
    - texto: "Quando há um conflito de merge"
    - texto: "Nunca — todo merge cria um commit novo"
  feedback: >
    Fast-forward só acontece quando não há divergência: o Git apenas empurra o
    rótulo da branch para frente, sem precisar costurar duas histórias.
- pergunta: O que fazer quando o Git marca um arquivo com <<<<<<< ======= >>>>>>>?
  alternativas:
    - texto: "Apagar tudo entre os marcadores sem ler, para o erro sumir rápido"
    - texto: "Ler as duas versões, decidir o texto final e remover os três marcadores antes de commitar"
      correta: true
    - texto: "Deletar a branch e desistir do merge"
    - texto: "Ignorar os marcadores — eles somem sozinhos no próximo commit"
  feedback: >
    O conflito existe porque só um humano sabe qual versão (ou combinação) deve
    sobreviver. Os marcadores precisam ser removidos manualmente após a decisão.
```

## Fechamento

Hoje você viu que:

- Uma **branch** é um rótulo móvel, não uma cópia de arquivos — criar uma é praticamente instantâneo.
- `git switch -c` cria e já troca pra branch nova; `git switch nome` troca pra uma que já existe.
- **Merge** junta duas linhas de história: sem divergência vira *fast-forward*; com divergência vira um *merge commit* com dois pais.
- **Conflito** não é erro — é o Git pedindo uma decisão humana quando duas branches mudam a mesma linha de jeitos diferentes.

**Próxima aula:** até agora, tudo isso viveu só no seu computador. A próxima aula leva esse repositório pro **GitHub** — como colocar seu código na nuvem e trazer o de outra pessoa pro seu computador.

:::roteiro
Abrir com a analogia do modo escuro no Petfinder — pedir pra turma imaginar que a entrega é amanhã, e perguntar "vocês mexeriam direto no arquivo que já funciona?". Deixa a resposta ("não, dava medo") preparar o terreno pra branch como solução. No trecho de fast-forward vs merge commit, não entregar o diagrama-progressivo de uma vez — pedir pra turma prever o que acontece antes de revelar cada camada. A prática do conflito é o coração da aula: force o conflito de propósito (passo 5, editar a MESMA linha) — não deixe pra sorte, porque um conflito "que não acontece" na prática esvazia a aula inteira. Reforçar visualmente com git log --oneline --graph no final, o "Y" do merge no gráfico costuma ser o momento em que a ficha cai de verdade. Fechar com o quiz.
:::
