---
titulo: "Leis de UX: Hick, Fitts, Jakob e Miller"
tema: Usabilidade e Design de Serviços
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: ["Avaliação heurística na prática"]
objetivos:
  - Explicar a Lei de Hick e organizar muitas opções em grupos para acelerar a decisão
  - Aplicar a Lei de Fitts ao tamanho e à posição de botões em telas de celular
  - Justificar pela Lei de Jakob o uso de padrões que o usuário já conhece
  - Usar a ideia de Miller e o agrupamento (chunking) sem cair no mito dos 7 itens
trilha: usabilidade-e-design-de-servicos
ordem: 90
slug: leis-de-ux-hick-fitts-jakob-miller
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/seed-87-95/89-leis-de-usabilidade.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-11-04
---

Abra o cardápio de uma lanchonete com 80 itens e repare no que acontece com você: o tempo passa, a fila atrás reclama, e no fim você pede o mesmo de sempre. Agora pense no botão "Pular anúncio", minúsculo, no cantinho da tela, que você erra duas vezes antes de acertar. Nada disso é falta de atenção sua. São limites do corpo e da mente humana, tão previsíveis que viraram **leis**. Na aula passada você avaliou telas com heurísticas. Hoje você vai conhecer quatro leis que explicam **por que** certas telas cansam, e usá-las para redesenhar uma.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar a **Lei de Hick** e organizar muitas opções em grupos para acelerar a decisão.
- Aplicar a **Lei de Fitts** ao tamanho e à posição de botões em telas de celular.
- Justificar pela **Lei de Jakob** o uso de padrões que o usuário já conhece.
- Usar a ideia de **Miller** e o agrupamento (*chunking*) sem cair no mito dos 7 itens.

## Pré-requisitos

Ter visto as **Aulas 87 a 89**: heurísticas de Nielsen e avaliação heurística.

## Desenvolvimento

### Lei de Hick: opção demais trava a decisão

:::conceito Lei de Hick
O tempo para tomar uma decisão **aumenta conforme cresce o número e a complexidade das opções**. Foi descrita por William Hick e Ray Hyman nos anos 1950. Ela não cresce em linha reta (dobrar as opções não dobra o tempo), mas cresce sempre.
:::

Cada opção na tela passa pelo mesmo ciclo na cabeça de quem usa: **ver, entender, comparar, decidir**. Com quatro opções isso é instantâneo. Com trinta, a pessoa trava, desiste ou escolhe errado.

A saída **não** é apagar funções importantes. É **organizar**: agrupar opções parecidas em categorias e mostrar primeiro o que é mais usado. Em vez de `Perfil | Foto | Senha | Tema | Privacidade | Notificações | Idioma | Conta | Bloqueios` na mesma tela, três grupos: **Conta**, **Privacidade** e **Preferências**. As nove funções continuam lá, só que a decisão inicial ficou entre três.

### Lei de Fitts: tamanho e distância importam

:::conceito Lei de Fitts
O tempo para atingir um alvo (com o dedo ou o mouse) depende da **distância** até ele e do seu **tamanho**. Alvos grandes e próximos são rápidos e certeiros; alvos pequenos e distantes são lentos e propensos a erro. Paul Fitts a descreveu em 1954.
:::

No celular, o "cursor" é um dedo, que é largo e impreciso. Por isso as próprias fabricantes recomendam um tamanho mínimo de área de toque: cerca de **44 pontos** nas diretrizes da Apple e **48 dp** nas do Material Design, do Google (mais ou menos a ponta de um dedo). E o lugar também conta: segurando o celular com uma mão, o polegar alcança com conforto a parte de baixo da tela, e é por isso que tantos apps puseram a navegação principal ali.

:::atencao Erro comum: Fitts a favor do erro
Fitts vale para os dois lados. Se o botão **Enviar** é grande e fácil de acertar, ótimo. Mas se o **Excluir**, logo do lado, também é grande e fácil de acertar, você acabou de facilitar o acidente. Em ação perigosa, o certo é **afastar** e às vezes até reduzir o destaque, junto com a prevenção de erros que você viu na heurística 5.
:::

### Lei de Jakob: o usuário já vem treinado

:::conceito Lei de Jakob
As pessoas passam a maior parte do tempo usando **outros** apps e sites, não o seu. Por isso esperam que o seu funcione do mesmo jeito que os que elas já conhecem. A ideia foi formulada por Jakob Nielsen, o mesmo das heurísticas.
:::

A 🔍 é busca, o ☰ é menu, o ⚙ é configuração, o 🛒 é carrinho, o logo no topo leva para o início. Ninguém leu isso num manual: aprendeu usando dezenas de apps. Quando você inventa um símbolo novo para busca, o app pode funcionar perfeitamente e mesmo assim cobrar do usuário um aprendizado desnecessário. É a mesma ideia da heurística 4 (consistência e padrões), olhando para fora do seu sistema.

:::importante Inovar não é reinventar a roda
Seguir padrões não proíbe criar. Invente onde está o **valor** do seu produto (a ideia, o conteúdo, o serviço) e use convenção no resto (login, busca, menu, carrinho). Um app que acerta isso parece "fácil" mesmo na primeira vez.
:::

### Miller e o agrupamento: a memória tem limite

Em 1956, o psicólogo George Miller publicou um artigo famoso sobre a capacidade da **memória de trabalho**, aquela que você usa para segurar um número de telefone enquanto disca. Ele falava em "sete, mais ou menos dois" itens. Pesquisas posteriores indicam que o limite real é ainda menor, perto de **quatro blocos**. O recado para interfaces não é o número exato: é que **a memória de curto prazo é pequena**, e por isso a informação deve vir **agrupada**.

:::conceito Chunking (agrupamento)
É organizar informações em **blocos com significado**. O telefone `41998765432` é difícil de lembrar; `(41) 99876-5432` é fácil, porque virou três blocos. Num formulário, 12 campos soltos cansam; os mesmos 12 em três blocos (**Dados pessoais**, **Endereço**, **Contato**) parecem metade.
:::

```diagrama-progressivo
titulo: Redesenhando a tela inicial do app da escola com as quatro leis
camadas:
  - rotulo: O ponto de partida
    conteudo: A tela inicial tem nove botões do mesmo tamanho, sem ordem, com calendário, notas, tarefas, mensagens, perfil, configurações, arquivos, grupos e avisos. Os colegas demoram e tocam no lugar errado.
  - rotulo: Hick organiza a escolha
    conteudo: As nove funções viram quatro grupos (Hoje, Notas, Mensagens e Mais). A primeira decisão agora é entre quatro, não entre nove.
  - rotulo: Miller agrupa o conteúdo
    conteudo: "Dentro de \"Hoje\", tarefas e avisos aparecem em blocos com título (Para entregar, Avisos da turma), em vez de uma lista corrida."
  - rotulo: Fitts posiciona os botões
    conteudo: Os quatro grupos vão para uma barra na parte de baixo da tela, com botões grandes, onde o polegar alcança com conforto.
  - rotulo: Jakob escolhe os ícones
    conteudo: Cada grupo usa o ícone que o usuário já conhece de outros apps e vem com texto embaixo. Ninguém precisa aprender nada novo.
```

:::dica Na hora de programar
Essas leis viram decisões de código bem concretas: um `min-height: 48px` nos botões do CSS (Fitts), um `<fieldset>` com `<legend>` para agrupar campos do formulário (Miller), um menu com poucas categorias em vez de vinte links (Hick). Em entrevista de estágio de Front-End, justificar uma escolha de layout com o nome da lei mostra que você não decidiu "no olho".
:::

## Prática

**Atividade "a tela que ninguém usa" (duplas, sem computador, ~15 min).** A tela inicial do app **Minha Escola** hoje é assim:

```text
Boletim · Faltas · Horário · Calendário · Provas · Trabalhos · Recados ·
Mensagens · Chat da turma · Perfil · Foto · Senha · Tema · Idioma ·
Biblioteca · Cantina · Secretaria · Documentos · Ajuda · Sair
```

São 20 botões do mesmo tamanho, em ordem alfabética, todos com ícones inventados pela equipe, e o **Sair** fica colado no **Boletim**.

1. **Agrupe (5 min):** organizem os 20 itens em no máximo **5 grupos** com nomes claros.
2. **Desenhe (7 min):** façam o rascunho da nova tela inicial numa folha, em formato de celular. Decidam o que aparece primeiro, onde ficam os botões principais e onde vai o **Sair**.
3. **Justifique (3 min):** anotem no desenho, com setas, **pelo menos uma decisão para cada lei**: Hick, Fitts, Jakob e Miller.

Duas duplas apresentam o rascunho; a turma aponta se alguma lei foi usada contra o usuário.

## Avaliação

```quiz
- pergunta: Um app tem 30 opções na mesma tela inicial e os usuários demoram muito para decidir aonde ir. Qual lei explica melhor o problema?
  alternativas:
    - texto: Lei de Fitts
    - texto: Lei de Jakob
    - texto: Lei de Hick
      correta: true
    - texto: Lei de Miller
  feedback: >
    Hick relaciona o tempo de decisão ao número e à complexidade das opções.
    A correção é agrupar em categorias, não apagar funções.
- pergunta: Pela Lei de Fitts, como deve ser o botão principal de uma tela de celular?
  alternativas:
    - texto: Pequeno e no canto superior, para não ocupar espaço
    - texto: Grande o suficiente para o dedo e numa posição fácil de alcançar
      correta: true
    - texto: Do mesmo tamanho de todos os outros, para manter a consistência
    - texto: Escondido no menu, para deixar a tela minimalista
  feedback: >
    Alvos maiores e mais próximos são atingidos mais rápido e com menos erro. No
    celular, a área de toque recomendada fica perto de 44 a 48 unidades.
- pergunta: Uma equipe trocou a lupa de busca por um desenho original de "olho" para deixar o app diferente. O que a Lei de Jakob diz sobre isso?
  alternativas:
    - texto: Foi uma boa ideia, porque inovação sempre melhora a experiência
    - texto: Não faz diferença, porque a função continua funcionando
    - texto: Atrapalha, porque o usuário já aprendeu em outros apps que a lupa é busca
      correta: true
    - texto: Só atrapalha se o app for para computador
  feedback: >
    As pessoas passam a maior parte do tempo em outros apps e trazem esses padrões.
    Inovar no valor do produto, sim; reinventar o ícone de busca, não.
- pergunta: Um colega diz que, pela Lei de Miller, todo menu precisa ter no máximo 7 itens. O que está errado nessa afirmação?
  alternativas:
    - texto: Nada, é exatamente isso que Miller provou
    - texto: O limite correto é de 12 itens
    - texto: Miller falava da memória de curto prazo, não de opções visíveis na tela; o que a ideia ensina é agrupar a informação
      correta: true
    - texto: A Lei de Miller só vale para números de telefone
  feedback: >
    Itens visíveis não precisam ser decorados (é reconhecimento, não memória). A
    lição útil de Miller é o chunking, organizar em blocos com significado.
- pergunta: O botão "Excluir conta" foi deixado grande e colado no botão "Salvar". Que combinação de ideias explica o risco?
  alternativas:
    - texto: Lei de Hick e ajuda e documentação
    - texto: Lei de Fitts e prevenção de erros
      correta: true
    - texto: Lei de Jakob e visibilidade do status
    - texto: Lei de Miller e flexibilidade de uso
  feedback: >
    Fitts mostra que o alvo grande e próximo é fácil de acertar, inclusive sem
    querer. Ação perigosa deve ficar afastada, o que é prevenção de erros.
```

## Fechamento

Hoje você descobriu que:

- **Hick:** muitas opções atrasam a decisão; a saída é agrupar e priorizar, não apagar.
- **Fitts:** tamanho e distância importam; no celular, botão do tamanho do dedo, onde o polegar alcança, e ação perigosa afastada.
- **Jakob:** o usuário chega treinado pelos outros apps; use os padrões e inove onde está o valor.
- **Miller:** a memória de curto prazo é pequena; agrupar (*chunking*) vale mais do que contar itens.

**Próxima aula:** você vai sair da tela. Um app pode ter interface impecável e mesmo assim entregar uma experiência ruim, porque o problema estava no **serviço** inteiro: na fila, na cozinha, no balcão. Começa o bloco de **Design de Serviços**.

:::roteiro
Abrir com o cardápio gigante: pergunte quem já desistiu de escolher e pediu "o de sempre". Para Fitts, um teste rápido e divertido: peça para alguém tocar, na tela do projetor ou num papel colado na parede, num quadrado de 1 cm do outro lado da sala e depois num de 10 cm; a diferença de tempo aparece sem cronômetro. No diagrama, peça para a turma prever qual lei entra em cada camada antes de revelar. Correções em relação à origem: o deck 89 da SEED já trata bem o mito dos 7 itens; acrescentamos que pesquisas posteriores (Cowan, 2001) apontam algo perto de 4 blocos e o atenção sobre Fitts aplicado a ação perigosa. As medidas 44 pt (Apple) e 48 dp (Material) são das diretrizes oficiais de cada plataforma. Na prática, um bom sinal de entendimento é a dupla mover o Sair para longe e para dentro de "Perfil" ou "Mais"; se ninguém fizer isso, provoque.
:::
