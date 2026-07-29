---
titulo: "Controle de versão: por que <code>projeto-final-VERSAO-2-agora-vai.html</code> não escala"
tema: Controle de versão com Git (local)
disciplina: programacao-front-end
serie: 3ª
prerequisitos: [Usar o terminal integrado do VSCode, Ter um projeto em pastas/arquivos como o Petfinder]
objetivos:
  - Explicar por que guardar cópias manuais de arquivo (v1, v2, final) não escala e cria risco
  - Explicar o que é um repositório Git e o que um commit realmente guarda
  - Executar o ciclo local completo — git init, git add, git commit, git log
  - Usar .gitignore para excluir arquivos que nunca devem ser versionados
trilha: controle-de-versao-git-github
ordem: 1
slug: controle-de-versao-git-local
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-07-29
---

Você já teve uma pasta com `projeto.html`, `projeto-2.html`, `projeto-final.html` e `projeto-final-agora-vai.html`? Cada arquivo é uma tentativa de responder a mesma pergunta: "qual dessas versões é a boa?" — e depois de duas semanas, nem quem escreveu lembra mais. O problema não é falta de organização sua. É que arquivo comum não foi feito pra guardar **história**. Existe uma ferramenta feita exatamente pra isso, e hoje você aprende a base dela.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar por que múltiplas cópias manuais de arquivo não escalam e escondem risco.
- Explicar o que é um repositório Git e o que um **commit** realmente guarda.
- Rodar o ciclo local completo: `git init`, `git add`, `git commit`, `git log`.
- Criar um `.gitignore` pra manter arquivos indesejados fora do repositório.

## Pré-requisitos

Você precisa saber abrir o terminal integrado do VSCode (`` Ctrl+` ``) e ter algum projeto em pastas — o próprio Petfinder que você já construiu serve perfeitamente como campo de testes.

## Desenvolvimento

### O problema que toda cópia manual esconde

`projeto-v1.html`, `projeto-v2.html`, `projeto-final.html` resolve por uns dias, mas quebra rápido:

- Você não sabe **o que mudou** entre `v1` e `v2` sem abrir os dois e comparar linha a linha.
- Se dois colegas mexem no mesmo projeto ao mesmo tempo, alguém sobrescreve o trabalho do outro sem nem perceber.
- Não existe "voltar pro que funcionava ontem" — só existe o arquivo que sobrou.

Git resolve isso trocando "arquivo com nome diferente" por **histórico dentro do próprio projeto**, sem multiplicar arquivo nenhum.

### Um commit é uma fotografia, não um "diff"

:::conceito Repositório (repo)
Um **repositório Git** é uma pasta do seu projeto com uma "caixa-preta" de histórico escondida dentro (a pasta `.git`, criada por você em instantes). A partir do momento em que existe, o Git consegue **guardar fotografias** do estado inteiro dos arquivos, sempre que você mandar.
:::

Cada vez que você salva um ponto da história, o Git tira uma **fotografia completa** de como os arquivos estão naquele momento — chamada de **commit**. Não é "só a linha que mudou": é o estado inteiro do projeto, carimbado com data, autor e uma mensagem que você escreve explicando o porquê daquela mudança.

```diagrama-progressivo
titulo: O que acontece quando você dá um commit
camadas:
  - rotulo: Você edita
    conteudo: "Você muda o HTML, o CSS, adiciona uma imagem — qualquer coisa dentro da pasta do projeto."
  - rotulo: git add
    conteudo: "Você avisa ao Git quais mudanças entram nesta fotografia. Isso é a área de stage — um rascunho do que vai ser fotografado."
  - rotulo: git commit
    conteudo: "O Git bate a foto de verdade: grava o estado dos arquivos marcados, com sua mensagem explicando o porquê, e guarda isso pra sempre no histórico do repositório."
  - rotulo: git log
    conteudo: "A qualquer momento, você pode listar todas as fotografias já tiradas — o histórico completo do projeto, em ordem."
```

### Por que existe uma etapa "add" antes do "commit"?

Isso costuma confundir quem começa: por que não existe só um comando que já salva tudo de uma vez?

:::importante O ponto-chave
`git add` existe porque **nem toda mudança que você fez precisa entrar na mesma fotografia**. Talvez você tenha mexido no CSS *e* começado um experimento no JavaScript que ainda não terminou. `add` deixa você escolher exatamente o que entra no commit — o resto continua ali, esperando o próximo.
:::

Na prática, o ciclo básico é sempre o mesmo:

```bash
git init                  # transforma a pasta atual num repositório (só uma vez)
git add index.html        # marca este arquivo pra entrar na próxima fotografia
git add .                 # ou marca TODOS os arquivos modificados de uma vez
git commit -m "Cria estrutura inicial da página"   # bate a foto, com mensagem
git log --oneline         # lista o histórico, uma linha por commit
```

:::atencao Erro comum
Rodar `git add .` sem pensar é o hábito mais comum de quem começa — e o mais perigoso. Ele marca **literalmente tudo** que mudou na pasta, inclusive arquivo que você esqueceu ali (uma captura de tela de teste, um `notas.txt` pessoal, uma pasta inteira de dependências). O resultado: esses arquivos entram no histórico do projeto pra sempre, mesmo que você delete depois — porque a fotografia antiga continua guardada. Antes de commitar, rode `git status` pra ver exatamente o que está marcado.
:::

### .gitignore — dizendo ao Git o que nunca fotografar

Todo projeto real tem arquivos que **nunca** deveriam entrar no histórico: pastas geradas automaticamente, senhas e chaves de configuração, arquivos temporários do seu editor. Em vez de lembrar de excluir isso manualmente toda vez, você cria um arquivo chamado `.gitignore` na raiz do projeto, listando o que o Git deve ignorar:

```
# .gitignore
node_modules/
.env
*.log
.DS_Store
```

A partir daí, mesmo que você rode `git add .`, esses arquivos e pastas são pulados automaticamente — o Git age como se eles não existissem.

:::dica Onde isso vira hábito profissional
Em qualquer projeto de front-end que usa Node (React, Vite, o que for), a pasta `node_modules/` pode ter **centenas de megabytes** de dependências que qualquer pessoa recria com um comando. Subir isso pro repositório deixaria o histórico gigante e lento à toa. Todo projeto profissional que você abrir no GitHub tem um `.gitignore` logo na raiz — é a primeira coisa que devs experientes conferem antes do primeiro commit.
:::

## Prática

**No terminal do VSCode, dentro de uma cópia da pasta do Petfinder (~15 min):**

1. Rode `git init` e confira que apareceu a mensagem de repositório criado.
2. Rode `git status` — repare que todos os arquivos aparecem como não rastreados.
3. Crie um `.gitignore` com pelo menos uma linha (ex.: `*.log`).
4. Rode `git add .` e depois `git status` de novo — veja a diferença: agora os arquivos aparecem em verde, prontos pra fotografia.
5. Rode `git commit -m "Primeiro commit do Petfinder"`.
6. Edite qualquer arquivo (mude um texto no `index.html`), depois repita `add` + `commit` com uma mensagem nova descrevendo o que mudou.
7. Rode `git log --oneline` e confira: você deve ver **duas** linhas, uma pra cada commit, na ordem em que foram feitos.

## Avaliação

```quiz
- pergunta: Qual é a diferença principal entre guardar "projeto-v1.html, projeto-v2.html" e usar Git?
  alternativas:
    - texto: "Não tem diferença, os dois guardam histórico do mesmo jeito"
    - texto: "Git guarda o histórico dentro do próprio projeto, com data, autor e mensagem — sem multiplicar arquivos"
      correta: true
    - texto: "Git só funciona se o projeto estiver no GitHub"
    - texto: "Arquivos com nome de versão são mais rápidos de abrir"
  feedback: >
    Git substitui a multiplicação manual de arquivos por um histórico estruturado
    guardado na pasta .git, sem precisar renomear nada.
- pergunta: Por que o comando git add existe antes do git commit?
  alternativas:
    - texto: "Porque o Git exige dois comandos para tudo, sem motivo real"
    - texto: "Para permitir escolher exatamente quais mudanças entram na próxima fotografia (commit)"
      correta: true
    - texto: "Porque git add é o comando que realmente salva o histórico"
    - texto: "Para deixar o computador mais rápido"
  feedback: >
    add monta a área de stage — um rascunho do que vai ser fotografado — permitindo
    deixar de fora mudanças que ainda não devem entrar no commit.
- pergunta: Para que serve o arquivo .gitignore?
  alternativas:
    - texto: "Para apagar arquivos indesejados do computador"
    - texto: "Para listar arquivos e pastas que o Git nunca deve incluir no histórico"
      correta: true
    - texto: "Para esconder o projeto do GitHub"
    - texto: "Para acelerar o comando git commit"
  feedback: >
    .gitignore diz ao Git quais arquivos/pastas pular mesmo com git add . — como
    node_modules, .env e arquivos temporários.
```

## Fechamento

Hoje você viu que:

- Cópias manuais de arquivo (`v1`, `v2`, `final`) não escalam e escondem risco de sobrescrever trabalho.
- Um **repositório Git** guarda **commits** — fotografias completas do projeto, com data, autor e mensagem.
- O ciclo básico local é sempre `git init` → `git add` → `git commit` → `git log`.
- `.gitignore` mantém arquivos indesejados (dependências, senhas, temporários) fora do histórico pra sempre.

**Próxima aula:** hoje seu histórico foi uma linha reta, um commit atrás do outro. Mas e se você quiser testar uma ideia arriscada sem bagunçar o que já funciona? A próxima aula é sobre **branches** — como manter linhas de trabalho paralelas dentro do mesmo repositório.

:::roteiro
Abrir perguntando quem já teve arquivo "final-final-agora-vai" — quase toda mão levanta, é ótimo gancho de riso + identificação. Não entregar a definição de commit de cara: perguntar "o que vocês acham que o Git guarda quando vocês salvam?" antes de revelar que é uma fotografia completa, não só a diferença. No erro comum do git add ., se der tempo, provocar de propósito: peça pra um aluno criar um arquivo "besteira.txt" na pasta e rodar git add . sem cuidado — deixe a turma perceber ao vivo que ele entrou junto. Reforçar que .git é uma pasta oculta (mostrar com ls -la ou o explorador de arquivos do VSCode) — muita gente esquece que ela existe e se assusta quando aparece. Reservar uns 15 min pra prática — o aluno só entende add/commit/log fazendo de verdade, não ouvindo. Fechar com o quiz.
:::
