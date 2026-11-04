---
titulo: "Service Blueprint: a planta do serviço"
tema: Usabilidade e Design de Serviços
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: ["Jornada do usuário, pontos de contato, frontstage e backstage", "Lean Canvas: a ideia como hipótese"]
objetivos:
  - Diferenciar o mapa de jornada do Service Blueprint
  - Descrever as cinco camadas e as três linhas do Service Blueprint
  - Montar o blueprint de um serviço simples a partir das etapas do usuário
  - Marcar pontos de falha e de espera e transformá-los em requisitos
trilha: usabilidade-e-design-de-servicos
ordem: 96
slug: service-blueprint
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/seed-87-95/94-lean-canvas-e-blueprint.pptx
  - lake/analise-e-metodos-para-sistemas/seed-87-95/95-lean-canvas-e-blueprint-aplicacao.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-11-04
---

Antes de levantar uma casa, alguém desenha a planta. E não é só a planta da sala bonita que aparece no anúncio: tem a planta hidráulica, com os canos escondidos na parede, e a elétrica, com os fios que ninguém vê. Se o pedreiro só olha a planta da sala, a casa fica linda até o dia em que você liga o chuveiro. Com serviços é igual. O mapa de jornada que você fez na aula 92 é a planta da sala: mostra o que a pessoa vive. Hoje você vai desenhar a planta completa, com os canos e os fios, e descobrir que é lá dentro da parede que muitos requisitos estão escondidos.

## Objetivos

Ao final desta aula, você será capaz de:

- Diferenciar o **mapa de jornada** do **Service Blueprint**.
- Descrever as **cinco camadas** e as **três linhas** do Service Blueprint.
- **Montar o blueprint** de um serviço simples a partir das etapas do usuário.
- Marcar **pontos de falha e de espera** e transformá-los em **requisitos**.

## Pré-requisitos

Ter visto a **Aula 92** (jornada, pontos de contato, frontstage e backstage) e a **Aula 95** (Lean Canvas).

## Desenvolvimento

### Da jornada à planta do serviço

:::conceito Service Blueprint
É um diagrama que mostra, etapa por etapa, **a experiência do usuário junto com tudo o que a organização faz para entregá-la**: o que ele vê, o que ele faz, quem o atende, o que acontece nos bastidores e quais sistemas dão suporte. É a "planta" do serviço.
:::

A diferença para o mapa de jornada está no ponto de vista. O **mapa de jornada** olha **com os olhos do usuário**: o que ele faz, sente e onde sofre. O **blueprint** olha **com os olhos de quem entrega o serviço**: para cada passo do usuário, o que precisa acontecer na frente e atrás da cortina. Um completa o outro, e o blueprint costuma vir depois, quando a equipe já sabe onde a experiência dói e quer entender por quê.

:::curiosidade Uma ideia dos anos 1980
O Service Blueprint foi proposto em 1984 por **G. Lynn Shostack**, uma executiva de banco, num artigo da revista Harvard Business Review. Ela argumentava que serviços falhavam porque ninguém os desenhava com o mesmo cuidado com que se desenha um produto. Quarenta anos depois, a ferramenta é usada para planejar de agências bancárias a aplicativos.
:::

### Cinco camadas e três linhas

O blueprint é uma grade: as **etapas do usuário** formam as colunas, da esquerda para a direita, e cada **camada** é uma linha horizontal. Veja as camadas no exemplo de um paciente que agenda consulta pelo app do posto de saúde:

```diagrama-progressivo
titulo: As camadas do blueprint, na etapa "agendar a consulta"
camadas:
  - rotulo: Evidências
    conteudo: O que a pessoa vê e toca. A tela da agenda com os horários livres e, depois, a mensagem de confirmação no celular.
  - rotulo: Ações do usuário
    conteudo: O que o paciente faz. Escolhe o dia e o horário e toca em Confirmar.
  - rotulo: Frontstage
    conteudo: O que o serviço faz diante do paciente. O app mostra os horários disponíveis e exibe "Consulta marcada".
  - rotulo: Backstage
    conteudo: O que acontece sem o paciente ver. O sistema bloqueia aquele horário na agenda do médico e agenda o envio de um lembrete.
  - rotulo: Processos de suporte
    conteudo: O que sustenta tudo. O banco de dados da agenda, o serviço de envio de mensagens e o cadastro com o telefone do paciente.
```

Entre as camadas passam **três linhas** que contam muito sobre o serviço:

- **Linha de interação:** separa as ações do usuário do frontstage. Toda seta que a cruza é um ponto de contato.
- **Linha de visibilidade:** separa o frontstage do backstage, ou seja, o que o usuário vê do que fica atrás da cortina (você a conheceu na aula 92).
- **Linha de interação interna:** separa o backstage dos processos de suporte. Cada seta que a cruza é uma dependência entre pessoas e sistemas, e muitas vezes uma **integração** a programar.

### O blueprint completo e os pontos de falha

| **F** = falha · **W** = espera | Agendar | Receber lembrete | Chegar ao posto | Ser atendido |
|---|---|---|---|---|
| **Evidências** | tela da agenda | mensagem no celular | recepção, senha | consultório |
| **Ações do usuário** | escolhe horário | lê o lembrete | apresenta documento | conversa com o médico |
| *linha de interação* | | | | |
| **Frontstage** | app confirma | app envia lembrete | recepcionista confirma o nome | médico atende |
| *linha de visibilidade* | | | | |
| **Backstage** | bloqueia o horário | dispara o lembrete na véspera | **W** fila sem previsão; atrasos não são avisados | registra o atendimento |
| *linha de interação interna* | | | | |
| **Suporte** | banco da agenda | serviço de mensagens; **F** telefone desatualizado no cadastro | lista de agendados | prontuário eletrônico |

Esse é o blueprint completo do agendamento. As marcas são os pontos onde o serviço quebra (**F**, de falha) ou trava (**W**, do inglês *wait*, espera). O **F** explica um mistério real dos postos: o paciente não recebe o lembrete porque trocou de número, esquece a consulta e falta. O **W** explica a reclamação de espera. Cada um vira requisito: "o sistema deve pedir que o paciente confirme o telefone ao agendar" e "o sistema deve avisar o paciente quando o atendimento estiver atrasado". Nenhum dos dois apareceria olhando só as telas.

:::atencao Erro comum: desenhar o serviço dos sonhos
Na hora de montar o primeiro blueprint, a equipe tende a desenhar **como o serviço deveria funcionar**, com cada etapa perfeita. O resultado é um diagrama bonito sem nenhum F nem W, que não ensina nada. Desenhe primeiro o serviço **como ele é hoje**, com os papéis impressos, as planilhas e os "aí a gente liga para confirmar". Sinal de que algo está errado: se o seu blueprint não tem nenhum ponto de falha, você provavelmente desenhou o ideal, não o real.
:::

:::dica Na hora de programar
Para quem desenvolve, as duas camadas de baixo são as mais valiosas. Cada item do **backstage** costuma virar uma regra de negócio ou uma tela interna (a tela da recepção, o painel da cozinha), e cada item do **suporte** vira tabela no banco de dados, serviço externo ou integração (envio de mensagens, pagamento, mapas). É no blueprint que aparecem os requisitos que ninguém pediu na entrevista, porque o usuário nem sabe que eles existem.
:::

## Prática

**Atividade "a planta da carteirinha" (grupos de 4, sem computador, ~15 min).** Vocês vão montar o blueprint do serviço de **segunda via da carteirinha estudantil** da escola, que funciona assim hoje:

> O aluno pede a segunda via num formulário online e anexa uma foto. A secretaria confere a foto (às vezes recusa porque está escura, mas só avisa quando o aluno aparece no balcão). Uma vez por semana a secretaria imprime as carteirinhas aprovadas. O aluno não recebe aviso: vai ao balcão perguntar até a carteirinha estar pronta.

1. **Grade (3 min).** Numa folha deitada, desenhem 4 colunas (**Pedir**, **Aguardar**, **Retirar** e mais uma etapa que vocês acharem necessária) e as 5 camadas, com as 3 linhas tracejadas.
2. **Preencham (7 min).** Completem cada célula com o serviço **como é hoje**. Célula vazia é permitida se nada acontece ali.
3. **Marquem e consertem (5 min).** Marquem pelo menos **um F** e **um W**. Para cada um, escrevam **um requisito** no formato "O sistema deve...".

No fim, a turma compara: algum grupo achou um requisito que nenhum outro achou? Em qual camada ele estava?

## Avaliação

```quiz
- pergunta: Uma equipe de app de consultas já definiu o problema, os usuários e a proposta de valor. Agora quer ver as ações do paciente, o que aparece na interface e os processos internos que confirmam cada consulta. Qual ferramenta usar?
  alternativas:
    - texto: Diagrama de classes
    - texto: Lean Canvas
    - texto: Service Blueprint
      correta: true
    - texto: O código-fonte do protótipo
  feedback: >
    O blueprint mostra a experiência do usuário junto com o que acontece nos
    bastidores e nos sistemas de suporte. O Lean Canvas já cumpriu seu papel de
    organizar o problema e a proposta.
- pergunta: Qual é a principal diferença entre o mapa de jornada e o Service Blueprint?
  alternativas:
    - texto: A jornada é feita no papel e o blueprint só no computador
    - texto: A jornada olha com os olhos do usuário; o blueprint mostra também o que a organização faz para entregar cada etapa
      correta: true
    - texto: O blueprint não mostra as ações do usuário
    - texto: Não há diferença, são nomes diferentes para a mesma coisa
  feedback: >
    Os dois se completam. O blueprint acrescenta frontstage, backstage e processos
    de suporte a cada passo da jornada.
- pergunta: No blueprint do agendamento, em que camada fica "o sistema bloqueia o horário na agenda do médico"?
  alternativas:
    - texto: Evidências
    - texto: Ações do usuário
    - texto: Frontstage
    - texto: Backstage
      correta: true
  feedback: >
    É algo que acontece sem o paciente ver, mas é necessário para o serviço
    funcionar. Fica abaixo da linha de visibilidade.
- pergunta: O que a linha de visibilidade separa no blueprint?
  alternativas:
    - texto: As ações do usuário das evidências
    - texto: O que o usuário vê (frontstage) do que acontece nos bastidores (backstage)
      correta: true
    - texto: O backstage dos processos de suporte
    - texto: As etapas boas das etapas ruins
  feedback: >
    Acima dela está o palco; abaixo, os bastidores. As ações do usuário e o
    frontstage são separados pela linha de interação.
- pergunta: O blueprint mostra que pacientes faltam porque o lembrete vai para telefones desatualizados no cadastro. Qual requisito responde a esse ponto de falha?
  alternativas:
    - texto: O app deve ter uma cor mais chamativa
    - texto: O sistema deve pedir que o paciente confirme o telefone ao agendar
      correta: true
    - texto: A equipe deve contratar mais programadores
    - texto: O lembrete deve ser enviado com mais emojis
  feedback: >
    O F está no suporte (cadastro desatualizado). A correção ataca a causa,
    garantindo que a mensagem chegue a quem precisa.
```

## Fechamento

Hoje você descobriu que:

- O **Service Blueprint** é a planta do serviço: a jornada do usuário junto com tudo o que a organização faz para entregá-la.
- Ele tem **cinco camadas** (evidências, ações do usuário, frontstage, backstage e suporte) e **três linhas** (de interação, de visibilidade e de interação interna).
- **Pontos de falha (F)** e **de espera (W)** mostram onde o serviço quebra, e cada um vira requisito.
- Desenhe primeiro o serviço **como é**, não como deveria ser; é nos bastidores que moram os requisitos escondidos.

**Próxima aula:** é hora de juntar tudo. No projeto **FilaZero** você vai usar o Lean Canvas e o Blueprint juntos, sobre o problema mais famoso do intervalo, a fila da cantina, e sair com uma lista de requisitos priorizada.

:::roteiro
Abrir com a analogia da planta da casa: pergunte quem já viu reforma em que "acharam um cano no lugar errado". No diagrama, peça que a turma diga em que camada cada coisa vai antes de revelar. A tabela completa é densa: leia em voz alta só a coluna "Receber lembrete", de cima para baixo, e mostre o F; depois deixe a turma achar o W sozinha. Diferenças em relação à origem: os decks 94 e 95 da SEED listavam as cinco camadas, mas não nomeavam as três linhas nem os pontos de falha e espera, que foram acrescentados; o desafio do agendamento de consultas do deck 94 virou a primeira questão do quiz, e o "reduzir faltas" do deck 95 inspirou o F do telefone desatualizado. A origem histórica (Shostack, 1984, Harvard Business Review) foi acrescentada como curiosidade. Na prática, os requisitos esperados são do tipo "avisar quando a foto for recusada" (F na conferência) e "avisar quando a carteirinha estiver pronta" (W na espera); a quarta etapa costuma ser "conferência da foto" ou "impressão".
:::
