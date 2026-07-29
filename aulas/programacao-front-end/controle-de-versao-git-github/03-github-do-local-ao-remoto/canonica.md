---
titulo: "GitHub: tirando seu repositório do seu notebook e colocando na nuvem"
tema: GitHub — repositório remoto, clone e autenticação
disciplina: programacao-front-end
serie: 3ª
prerequisitos: ["Ciclo local do Git e branches (Aulas 1 e 2 — init, add, commit, switch, merge)"]
objetivos:
  - Explicar a diferença entre Git (ferramenta local) e GitHub (serviço remoto)
  - Conectar um repositório local a um repositório remoto e enviar commits com git push
  - Trazer um repositório existente para o computador com git clone
  - Explicar por que o GitHub não aceita mais senha em operações Git e escolher entre SSH e GitHub CLI para autenticar
trilha: controle-de-versao-git-github
ordem: 3
slug: github-do-local-ao-remoto
modo_origem: tema
fontes: []
revisao: false
status: rascunho
versao: 1
atualizado_em: 2026-07-29
---

Até agora, todo o histórico do seu projeto existe num lugar só: o SSD do seu notebook. Se ele quebrar, for roubado ou você simplesmente for trabalhar de outro computador na escola, todo aquele histórico de commits fica pra trás. Hoje seu repositório sai do seu computador e vai pra um servidor que qualquer colega, professor ou recrutador consegue acessar — e você aprende a trazer de volta um repositório que nem começou no seu computador.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar a diferença entre **Git** (a ferramenta que roda no seu computador) e **GitHub** (o serviço que hospeda repositórios na nuvem).
- Conectar um repositório local a um repositório remoto e enviar commits com `git push`.
- Trazer um repositório que já existe no GitHub pro seu computador com `git clone`.
- Explicar por que o GitHub não aceita mais senha em operações Git, e escolher entre SSH e GitHub CLI pra autenticar.

## Pré-requisitos

Você precisa ter feito as Aulas 1 e 2 — ciclo local do Git (`init`, `add`, `commit`, `log`) e branches (`switch`, `merge`). Ter uma conta no GitHub ajuda, mas criar uma leva menos de 2 minutos.

## Desenvolvimento

### Git é a ferramenta, GitHub é o prédio onde ela mora

Essa confusão é tão comum que vale resolver logo de cara: **Git** e **GitHub** não são a mesma coisa.

:::conceito GitHub
**GitHub** é um serviço na nuvem que hospeda repositórios Git, dá uma interface visual pra eles e adiciona ferramentas de colaboração (Pull Requests, Issues, revisão de código). Ele **usa** o Git por baixo dos panos, mas não é o único jeito de usar Git — existem alternativas como GitLab e Bitbucket. Pense assim: Git é a linguagem; GitHub é um dos lugares onde essa linguagem é falada.
:::

Tudo o que você fez nas duas últimas aulas — `init`, `add`, `commit`, branches, merge — acontece **inteiramente no seu computador**, sem internet nenhuma. GitHub só entra quando você decide que aquele histórico deve existir em algum outro lugar também.

### Subindo um repositório local pela primeira vez

Quando o repositório **nasceu no seu computador** (como o do Petfinder, que você já vem versionando), o caminho é: criar um repositório vazio no GitHub, e depois avisar ao seu Git local que aquele endereço remoto existe.

```bash
git remote add origin https://github.com/seu-usuario/petfinder.git
git push -u origin main
```

- `git remote add origin <url>` cadastra o endereço do GitHub com o apelido `origin` — é assim que o Git vai chamar aquele remoto a partir de agora.
- `git push -u origin main` envia os commits da sua branch `main` local pra branch `main` no GitHub. O `-u` (de *upstream*) faz o Git lembrar dessa ligação, então da próxima vez basta `git push`, sem repetir `origin main`.

### Trazendo um repositório que já existe no GitHub

Quando o repositório **já existe no GitHub** — o projeto de um colega, um material do curso, um repositório que você criou direto pelo site — você não usa `init`. Você usa `clone`:

```bash
git clone https://github.com/algum-usuario/algum-projeto.git
```

`git clone` faz três coisas de uma vez: cria a pasta, baixa **todo o histórico** de commits (não só os arquivos da versão mais recente) e já deixa configurado o remoto `origin` apontando pra onde você clonou. É por isso que, logo depois de um clone, `git log` já mostra o histórico inteiro do projeto — ele não precisa ser reconstruído, ele **vem junto**.

```diagrama-progressivo
titulo: Duas portas de entrada pro GitHub
camadas:
  - rotulo: Repositório nasceu no seu computador
    conteudo: "Você já tem commits locais (com git init). Cria um repositório vazio no GitHub, cadastra o endereço com git remote add origin, e envia tudo com git push -u origin main."
  - rotulo: Repositório já existe no GitHub
    conteudo: "Não existe nada no seu computador ainda. Você usa git clone <url>, que baixa o histórico inteiro e já deixa o remoto origin configurado sozinho."
  - rotulo: No dia a dia
    conteudo: "Depois da primeira conexão, os dois casos convergem: git push envia seus commits novos, git pull traz os commits que outra pessoa (ou você, de outro computador) enviou."
```

### Autenticação: como o GitHub sabe que é você

Aqui está uma pegadinha real que vai te confundir se ninguém explicar antes: **o GitHub não aceita mais login com usuário e senha** em operações de linha de comando (`git push`, `git clone` de repositório privado) — essa porta foi fechada em 2021, por segurança. Você precisa de uma destas duas formas:

- **SSH** — você gera um par de chaves no seu computador (uma fica só com você, a outra vai pro seu perfil do GitHub) e o Git usa isso pra provar quem você é, sem digitar nada a cada operação. É a forma clássica, usada por devs profissionais há anos.
- **GitHub CLI** (`gh auth login`) — um programa oficial do GitHub que abre o navegador, você faz login normalmente (inclusive com 2FA), e ele guarda a credencial de forma segura no seu computador. É o caminho mais direto pra quem está começando, porque não exige entender chave pública/privada ainda.

:::importante O ponto-chave
Antes de 2021, dava pra usar sua senha normal do GitHub direto no terminal. Hoje isso é **bloqueado por design** — nem que você tente. A senha da sua conta só serve pra logar no site; qualquer operação de linha de comando (`push`, `pull`, `clone` privado) exige SSH ou um token/credencial gerenciado por uma ferramenta como o GitHub CLI.
:::

:::atencao Erro comum
Um erro sério e comum: copiar um token de acesso pessoal e colar ele **direto dentro da URL remota** (`https://TOKEN@github.com/...`) ou, pior, deixá-lo esquecido dentro de um arquivo que depois vai num `git add .`. Um token vazado em um commit **continua no histórico pra sempre**, mesmo que você apague o arquivo depois — porque a fotografia antiga já foi tirada. Prefira sempre `gh auth login` ou SSH, que guardam a credencial fora do seu código.
:::

:::dica Onde isso vira hábito profissional
Em qualquer empresa, o primeiro passo de um dev novo no time é configurar autenticação com o GitHub da empresa — geralmente SSH, às vezes GitHub CLI. É configuração que você faz **uma vez por computador**, não a cada projeto. Vale fazer isso com calma agora, porque é a mesma configuração que você vai usar no seu primeiro emprego.
:::

## Prática

**No terminal do VSCode (~15 min):**

1. Crie um repositório vazio no site do GitHub (sem README, sem `.gitignore` — só o nome).
2. No repositório local do Petfinder que você já vem usando, rode `git remote add origin <a-url-que-o-github-te-deu>`.
3. Rode `git push -u origin main` — se pedir autenticação, use `gh auth login` (se o GitHub CLI estiver instalado) ou configure uma chave SSH seguindo o passo a passo que o professor vai mostrar.
4. Atualize a página do repositório no navegador e confirme que seus arquivos e commits apareceram.
5. Em outra pasta (fora da do Petfinder), rode `git clone` no endereço de um repositório de um colega (com permissão dele) e confira, com `git log --oneline`, que o histórico completo veio junto.

## Avaliação

```quiz
- pergunta: Qual afirmação descreve corretamente a diferença entre Git e GitHub?
  alternativas:
    - texto: "São a mesma ferramenta, só com nomes diferentes"
    - texto: "Git é a ferramenta que roda no computador; GitHub é um serviço na nuvem que hospeda repositórios Git"
      correta: true
    - texto: "GitHub substitui completamente a necessidade de usar Git"
    - texto: "Git só funciona depois que o repositório é criado no GitHub"
  feedback: >
    Todo o histórico de commits, branches e merges acontece localmente com Git,
    sem depender de internet. GitHub entra quando você decide hospedar esse
    histórico na nuvem.
- pergunta: Você quer trazer para o seu computador um projeto que já existe no GitHub, sem nenhum arquivo local ainda. Qual comando usar?
  alternativas:
    - texto: "git init"
    - texto: "git push"
    - texto: "git clone"
      correta: true
    - texto: "git switch"
  feedback: >
    git clone baixa o histórico completo de um repositório existente e já
    configura o remoto origin — é o ponto de partida quando o projeto nasceu
    no GitHub, não no seu computador.
- pergunta: Por que o GitHub não aceita mais usuário e senha em operações de linha de comando como git push?
  alternativas:
    - texto: "Porque senha é mais lenta que token"
    - texto: "Por segurança — desde 2021, é exigido SSH ou um token/credencial gerenciado (ex.: GitHub CLI)"
      correta: true
    - texto: "Porque o GitHub não usa mais senha nem no site"
    - texto: "Isso nunca foi verdade, senha sempre funcionou"
  feedback: >
    Desde 2021 o GitHub bloqueou autenticação por senha em operações Git via
    linha de comando, exigindo SSH ou token — o site continua aceitando senha
    normalmente para login.
```

## Fechamento

Hoje você viu que:

- **Git** roda local e não depende de internet; **GitHub** é um serviço que hospeda esses repositórios na nuvem, com interface e ferramentas de colaboração.
- Repositório que **nasceu local**: `git remote add origin` + `git push -u origin main`. Repositório que **já existe no GitHub**: `git clone`.
- Depois da primeira conexão, o dia a dia é `git push` (enviar) e `git pull` (trazer o que outra pessoa enviou).
- O GitHub não aceita mais senha em operações de linha de comando — a autenticação hoje é por **SSH** ou por uma ferramenta como o **GitHub CLI**.

**Próxima aula:** agora que seu código está no GitHub, como um colega **sugere** uma mudança no seu projeto sem simplesmente sobrescrever o que você fez? A próxima aula é sobre **Pull Requests** — o fluxo real que times profissionais usam pra revisar código antes dele entrar na `main`.

:::roteiro
Abrir perguntando quem já perdeu trabalho por pen-drive corrompido ou notebook que travou — ancora bem a motivação de "seu código só existe num lugar". Reforçar a distinção Git/GitHub com a analogia "linguagem x lugar onde ela é falada" antes de qualquer comando — sem isso, boa parte da turma passa o resto do curso achando que são sinônimos. Na parte de autenticação, ser direto sobre o bloqueio de senha desde 2021: não é frescura do GitHub, é resposta a um problema real de segurança (senha reaproveitada, vazamento). Se o laboratório tiver o GitHub CLI instalado, priorizar gh auth login na prática — é o caminho com menos passos pra travar a aula toda pela autenticação. Reservar tempo extra pra essa etapa: autenticação é sempre onde a aula trava mais no tempo real, mesmo com o passo a passo pronto.
:::
