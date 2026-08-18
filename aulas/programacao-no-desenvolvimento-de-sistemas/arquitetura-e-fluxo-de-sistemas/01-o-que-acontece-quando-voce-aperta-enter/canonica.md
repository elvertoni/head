---
titulo: O que acontece quando você aperta Enter
tema: Arquitetura e fluxo de uma requisição
disciplina: programacao-no-desenvolvimento-de-sistemas
serie: 3ª
prerequisitos: [Ter escrito alguma tela ou formulário, Noção de o que é um banco de dados]
objetivos:
  - Descrever o caminho de uma requisição desde o clique até a resposta na tela, nomeando cada camada
  - Distinguir o que é responsabilidade do front-end, do back-end e do banco de dados
  - Explicar por que a validação precisa existir dos dois lados
  - Desenhar o fluxograma de uma função, incluindo o caminho de erro
trilha: arquitetura-e-fluxo-de-sistemas
ordem: 1
slug: o-que-acontece-quando-voce-aperta-enter
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-08-18
---

Você abre o app do banco, digita a senha e aperta **Entrar**. Meio segundo depois aparece o seu saldo. Parece uma coisa só, um bloco maciço de mágica. Não é. Nesse meio segundo o seu clique atravessou umas seis fronteiras diferentes, passou por pelo menos três programas escritos por gente diferente, em máquinas diferentes, e voltou. Hoje a gente vai desenhar esse caminho inteiro no quadro — sem computador, sem código rodando — porque quem enxerga o caminho antes de programar escreve muito menos código errado. E, no fim, você vai desenhar o caminho de uma função do **seu TCC**.

## Objetivos

Ao final desta aula, você será capaz de:

- **Descrever** o caminho de uma requisição do clique até a resposta, nomeando cada camada por onde ela passa.
- **Separar** o que é trabalho do front-end, do back-end e do banco de dados.
- **Explicar** por que a mesma validação aparece duas vezes no sistema — e por que isso não é burrice.
- **Desenhar** o fluxograma de uma função incluindo o caminho de erro, não só o caminho feliz.

## Pré-requisitos

Você já montou alguma tela ou formulário e já ouviu falar em banco de dados. Não precisa saber nenhuma linguagem específica: hoje o trabalho é de **quadro e papel**.

## Desenvolvimento

### O seu clique não fala com o banco

Existe uma intuição errada muito comum, e ela aparece no desenho de quase todo mundo na primeira vez: o aluno desenha a **tela** ligada direto no **banco de dados**, com uma setinha só. É como se o botão "Entrar" fosse até o banco, olhasse a tabela de usuários e voltasse.

Se fosse assim, qualquer pessoa com o app instalado teria a chave do banco no bolso. Bastaria abrir o aplicativo, achar onde está guardada a senha do banco de dados e pronto: acesso a **todas** as contas de todos os clientes. O sistema inteiro cairia numa tarde.

:::conceito Arquitetura cliente-servidor
Na [[arquitetura-cliente-servidor|arquitetura cliente-servidor]], quem você segura na mão é o **cliente**: ele só sabe **pedir** e **mostrar**. Quem decide, calcula e guarda é o **servidor**, que roda numa máquina que você nunca vê e cujo endereço você nem precisa conhecer. O cliente nunca toca o banco de dados. Ele pede; o servidor responde.
:::

:::exemplo O restaurante
Pense num restaurante. Você (cliente) não entra na cozinha pra pegar o prato. Você fala com o garçom, que leva o pedido, e a cozinha decide o que fazer. Se todo cliente pudesse entrar na cozinha, em cinco minutos alguém estaria comendo a sobremesa dos outros e mexendo no fogão. A **separação** é o que mantém o negócio de pé — e o cardápio é a lista do que você **pode** pedir.
:::

Esse "cardápio" tem nome em software: é a **API**. É a lista fechada de pedidos que o servidor aceita. `POST /login`, `GET /saldo`, `POST /transferencia`. Nada fora do cardápio existe.

:::conceito API
Uma **API** é o contrato entre cliente e servidor: quais pedidos existem, o que cada um exige de informação e o que devolve de resposta. Numa [[api-rest|API REST]], cada pedido é um verbo ([[metodos-http|método HTTP]] como GET ou POST) mais um endereço. O cliente não sabe **como** o servidor faz — só o que pedir e o que esperar de volta.
:::

### O caminho completo, camada por camada

Agora o desenho de verdade. Cada camada abaixo é uma parada obrigatória do seu clique. Vá revelando uma de cada vez e tentando adivinhar a próxima antes de abrir.

```diagrama-progressivo
titulo: A viagem de um clique no botão Entrar
camadas:
  - rotulo: Você clica
    conteudo: O navegador (ou o app) junta o que você digitou e monta um pacote de dados. Nada saiu da sua máquina ainda — até aqui é só front-end.
  - rotulo: DNS
    conteudo: "O endereço que você conhece é um nome, tipo api.meubanco.com.br. A internet não roteia nomes, roteia números. O [[dns|DNS]] é a agenda telefônica que traduz esse nome para um endereço IP, algo como 200.147.35.149."
  - rotulo: A requisição HTTP viaja
    conteudo: "O pacote sai da sua máquina e atravessa a internet até o servidor. Se o endereço começa com [[https|HTTPS]], ele viaja embaralhado: quem interceptar no meio do caminho vê ruído, não a sua senha."
  - rotulo: Back-end recebe
    conteudo: "O servidor abre o pacote e procura no cardápio quem atende esse pedido. Achou POST /login? Então chama a função responsável. Não achou? Devolve erro 404 e acabou a viagem."
  - rotulo: A regra de negócio decide
    conteudo: "Aqui mora a inteligência. A função valida o que chegou, consulta o que precisa e decide. É este o único lugar do sistema onde a regra vale de verdade."
  - rotulo: Banco de dados
    conteudo: "O back-end pergunta ao banco: existe um usuário com esse e-mail? O banco não decide nada — ele guarda e devolve. Ele responde a pergunta que foi feita, nada além disso."
  - rotulo: A resposta volta
    conteudo: "O servidor monta a resposta (normalmente em [[json|JSON]], um formato de texto que todo mundo lê) e devolve pelo mesmo caminho. O front-end recebe e finalmente pinta o saldo na tela."
```

Repare numa coisa: entre o seu clique e o seu saldo aparecendo, **a maior parte do tempo não é processamento — é viagem**. É por isso que um app parece lento no ônibus e rápido no wi-fi de casa, sem que uma linha de código tenha mudado.

:::curiosidade Meio segundo é uma eternidade
Um servidor resolve o "existe esse usuário?" em poucos milissegundos. Já a viagem de ida e volta pela internet costuma custar dezenas ou centenas de milissegundos, dependendo da distância e da rede. Ou seja: em boa parte dos sistemas, o computador passa a maior parte do tempo **esperando**, não pensando. Otimizar o número de idas e vindas costuma render mais que otimizar o código.
:::

### Onde mora a regra de negócio (e por que validar duas vezes)

Se o cliente é burro de propósito e o banco só guarda, sobra o back-end como o cérebro. É lá que ficam as **regras de negócio**: só transfere quem tem saldo; menor de 18 não abre conta sozinho; cupom vencido não dá desconto.

Aí vem a pergunta que sempre aparece: *"mas eu já validei no formulário, professor. Por que validar de novo no servidor?"*

Porque a validação do formulário não é segurança — é **educação**. Ela existe pra você não esperar dois segundos de viagem só pra descobrir que esqueceu o arroba do e-mail. Quem quer atacar o sistema simplesmente não usa o seu formulário.

:::atencao Erro comum que custa caro
Confiar na [[validacao-de-formulario|validação de formulário]] como se fosse proteção. O atacante não abre a sua tela: ele manda o pedido direto pro endereço da API, com os dados que quiser, usando qualquer ferramenta que faça requisição. Seu `required` no HTML e seu `if` no JavaScript **nem foram carregados** nesse cenário. Regra prática: **validação no cliente é conforto; validação no servidor é a única que conta.**
:::

:::dica Como isso aparece no trabalho
Em entrevista de estágio, "onde você validaria isso?" é pergunta clássica de eliminação. A resposta que passa é: *nos dois lados, por motivos diferentes* — no cliente pela experiência, no servidor pela segurança. E quando você abrir um projeto de verdade, vai ver a mesma regra escrita duas vezes em lugares distantes. Não é bagunça: é intencional.
:::

### O caminho que ninguém desenha: o erro

Chegou a hora do fluxograma. Quase todo aluno desenha o **caminho feliz**: entra o dado, dá tudo certo, sai a resposta. Uma linha reta, bonita, do começo ao fim.

Só que em sistema de verdade o caminho feliz é a minoria dos casos. O usuário digita e-mail errado. O cupom já venceu. A internet cai no meio. O banco de dados demora e estoura o tempo. Cada uma dessas situações é um **caminho de exceção** — e cada caminho de exceção que você não desenhou vira uma tela travada, um botão que não responde ou, pior, um "sucesso!" mentiroso.

Fluxograma é a ferramenta mais barata do mundo pra achar esses buracos: um losango é uma pergunta, e **toda pergunta tem duas saídas**. Se você desenhou um losango com uma saída só, você esqueceu um caminho.

```text
              ┌─────────────────┐
              │  Recebe e-mail  │
              │    e senha      │
              └────────┬────────┘
                       ▼
                 ╱───────────╲        não
                ╱ Campos      ╲───────────────► 400  "preencha tudo"
                ╲ preenchidos? ╱
                 ╲───────────╱
                       │ sim
                       ▼
                 ╱───────────╲        não
                ╱  Usuário    ╲───────────────► 401  "e-mail ou senha inválidos"
                ╲  existe?     ╱
                 ╲───────────╱
                       │ sim
                       ▼
                 ╱───────────╲        não
                ╱   Senha     ╲───────────────► 401  "e-mail ou senha inválidos"
                ╲   confere?   ╱
                 ╲───────────╱
                       │ sim
                       ▼
              ┌─────────────────┐
              │  Gera sessão e  │
              │  devolve 200    │
              └─────────────────┘
```

Repare em dois detalhes desse desenho, que são decisões de projeto e não enfeite:

1. **"Usuário não existe" e "senha errada" devolvem a mesma mensagem.** Se a resposta fosse *"esse e-mail não está cadastrado"*, qualquer um poderia usar o seu login como uma máquina de descobrir quem tem conta no sistema. A mensagem vaga é proposital.
2. **Cada saída tem um número.** Esses são os [[codigos-de-status-http|códigos de status HTTP]]: `200` deu certo, `400` você mandou errado, `401` você não provou quem é, `404` não existe, `500` o erro foi nosso. Quem programa a tela usa esse número pra decidir o que mostrar.

:::importante O que separa quem projeta de quem só codifica
Quem só codifica escreve o caminho feliz e depois passa semanas apagando incêndio. Quem projeta **desenha primeiro as perguntas** — cada losango, cada saída, cada mensagem — e só então abre o editor. O desenho custa dez minutos de papel. O incêndio custa a entrega do TCC na véspera.
:::

## Prática

**Atividade "raio-X do seu TCC" (desplugada, ~15 min).** Em duplas ou trios, com papel e caneta. Peguem **uma** função do sistema de vocês — a que mais importa: cadastrar, agendar, publicar, comprar.

**Rodada 1 — o caminho (5 min).** Desenhem a viagem da requisição, do clique até a resposta, marcando com uma linha vertical onde termina o front-end e começa o back-end. Escrevam ao lado de cada camada **o que ela decide** (e o banco não decide nada).

**Rodada 2 — os losangos (5 min).** Agora o fluxograma da função no servidor. A meta é chegar a **pelo menos três losangos**, cada um com as duas saídas escritas. Para cada saída de erro, escrevam a mensagem que o usuário vai ler e o código de status.

**Rodada 3 — o ataque (5 min).** Troquem o papel com a dupla ao lado. A missão agora é **quebrar o desenho do colega**: achem uma situação real que o fluxograma não cobre. Vale campo vazio, valor negativo, usuário já cadastrado, data no passado, dois cliques seguidos no botão. Escrevam o furo no rodapé da folha e devolvam.

Vence a dupla que **encontrar** mais furos, não a que tiver menos. Achar furo no papel é de graça; achar em produção, não.

**Extensão no VSCode (opcional, se sobrar tempo em casa):** escreva só o esqueleto da função, com os `if` de cada losango e um comentário no lugar do corpo. Sem lógica ainda — só a estrutura das perguntas.

```javascript
function login(email, senha) {
  if (!email || !senha) return { status: 400, msg: "Preencha e-mail e senha" };

  const usuario = buscarUsuarioPorEmail(email);
  if (!usuario) return { status: 401, msg: "E-mail ou senha inválidos" };

  if (!senhaConfere(senha, usuario)) return { status: 401, msg: "E-mail ou senha inválidos" };

  return { status: 200, sessao: criarSessao(usuario) };
}
```

## Avaliação

```quiz
- pergunta: No caminho de uma requisição, quem toma a decisão de permitir ou negar uma transferência?
  alternativas:
    - texto: O front-end, porque é onde o usuário clica
    - texto: O back-end, onde ficam as regras de negócio
      correta: true
    - texto: O banco de dados, porque é ele que guarda o saldo
    - texto: O DNS, que autoriza a conexão
  feedback: >
    O cliente só pede e mostra; o banco só guarda e devolve o que foi perguntado.
    A decisão mora no back-end — é o único lugar onde a regra vale de verdade.
- pergunta: Por que a mesma validação aparece no formulário e no servidor?
  alternativas:
    - texto: Por descuido da equipe, é código duplicado que deveria ser removido
    - texto: Porque o formulário melhora a experiência, mas só a do servidor é segurança de fato
      correta: true
    - texto: Porque o servidor não consegue validar campos de texto
    - texto: Para o sistema ficar mais rápido
  feedback: >
    Um atacante manda a requisição direto pra API e nunca carrega a sua tela.
    Validação no cliente é conforto; a do servidor é a única que impede o dado ruim de entrar.
- pergunta: Você desenhou um losango "cupom é válido?" com uma única seta saindo dele. O que isso indica?
  alternativas:
    - texto: Que o fluxograma está correto e enxuto
    - texto: Que falta desenhar o caminho de exceção — toda pergunta tem duas saídas
      correta: true
    - texto: Que o losango deveria ser um retângulo
    - texto: Que a validação deve ser feita no banco de dados
  feedback: >
    Losango é decisão, e decisão sempre bifurca. Uma saída só significa que o
    caso de cupom vencido não foi previsto — e ele vai aparecer em produção.
- pergunta: Um usuário digita a senha errada. Qual código de status a API deve devolver?
  alternativas:
    - texto: "200, porque a requisição chegou ao servidor"
    - texto: "401, porque ele não provou quem é"
      correta: true
    - texto: "500, porque houve um erro"
    - texto: "404, porque a senha não foi encontrada"
  feedback: >
    401 é "não autenticado". O 500 seria culpa do servidor, e o 200 diria ao
    front-end que deu tudo certo — fazendo a tela liberar o acesso.
```

## Fechamento

Hoje a gente desenhou o que normalmente fica invisível:

- O cliente **pede e mostra**, o back-end **decide**, o banco **guarda**. Seu clique nunca toca o banco de dados.
- A **API** é o cardápio: a lista fechada de pedidos que o servidor aceita.
- Validar no formulário é **conforto**; validar no servidor é **segurança**. As duas coisas existem por motivos diferentes.
- Todo losango tem **duas saídas**. O caminho de erro que você não desenhou é o bug que o seu usuário vai encontrar primeiro.

**Próxima aula:** se toda função precisa de tantas perguntas e caminhos, como é que a gente organiza isso sem virar um arquivo de dois mil `if`? Vamos separar responsabilidades em camadas de código — rota, serviço e repositório — e ver por que o profissional divide o que o iniciante amontoa.

:::roteiro
Aula de quadro, do começo ao fim — não abrir slide.

**Abertura (5 min).** Pergunte de cara: "quem aqui já usou o app do banco hoje?". Peça a UM aluno que venha ao quadro e desenhe o que ele acha que acontece quando aperta Entrar. Nove em cada dez desenham tela → banco, com uma seta só. Não corrija: circule a seta e pergunte à turma "se é assim, quem tem a senha do banco de dados?". Deixe o silêncio trabalhar. É esse desenho errado que a aula inteira vai consertar.

**Camadas (12 min).** Construa o caminho no quadro da esquerda pra direita, uma parada por vez, e **não revele a próxima**: pergunte sempre "e agora, pra onde vai?". Numere as paradas conforme desenha. No DNS, use a analogia da agenda de contatos do celular (você salva o nome, mas o que disca é o número). Deixe o desenho no quadro até o fim da aula — a prática vai apontar pra ele.

**Validação dupla (8 min).** Espere a pergunta "mas eu já validei no formulário" aparecer sozinha; se não aparecer em dois minutos, provoque: "então posso apagar o if do servidor, né?". A frase que gruda: *validação no cliente é conforto, no servidor é segurança*. Escreva ela no canto do quadro e deixe.

**Fluxograma (8 min).** Desenhe o fluxo do login losango por losango, perguntando a cada um "e se der errado?". Só depois revele o detalhe da mensagem igual pros dois erros — costuma render um "ahhh" audível. Se a turma for rápida, pergunte por que 401 e não 400.

**Prática (15 min).** Circule nos grupos e faça UMA pergunta em cada mesa: "e se o usuário clicar duas vezes no botão?". Na rodada do ataque, deixe a competição esquentar — é a parte que fixa. Feche lendo em voz alta dois ou três furos que as duplas acharam, sem citar quem errou, e ligue de volta ao desenho do quadro.

**Se o tempo apertar:** corte a extensão em JavaScript e o quiz vira dever de casa. Não corte a rodada do ataque — é ela que ensina.
:::
