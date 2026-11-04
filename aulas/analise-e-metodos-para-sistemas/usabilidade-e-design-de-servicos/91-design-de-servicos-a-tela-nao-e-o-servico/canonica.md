---
titulo: "Design de Serviços: a tela não é o serviço"
tema: Usabilidade e Design de Serviços
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: ["Leis de UX: Hick, Fitts, Jakob e Miller"]
objetivos:
  - Diferenciar a interface de um aplicativo do serviço completo do qual ela faz parte
  - Identificar pessoas, processos, tecnologias e evidências que compõem um serviço
  - Explicar os princípios do Design de Serviços
  - Investigar o serviço antes de propor uma mudança no software
trilha: usabilidade-e-design-de-servicos
ordem: 91
slug: design-de-servicos-a-tela-nao-e-o-servico
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/seed-87-95/90-design-de-servicos-introducao.pptx
  - lake/analise-e-metodos-para-sistemas/seed-87-95/91-design-de-servicos-aplicacao.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-11-04
---

Você pede um lanche pelo aplicativo de delivery. A tela é linda, o pagamento passa em dois toques, aparece "Pedido confirmado". Quarenta minutos depois o lanche chega frio, faltando a batata, e o entregador não sabe de nada. Você dá uma estrela para... quem, exatamente? O app funcionou do primeiro ao último toque. O que falhou estava fora da tela: na cozinha que se atrasou, na conferência que não aconteceu, no entregador que pegou três pedidos de uma vez. Nas últimas aulas você aprendeu a deixar telas fáceis de usar. Hoje você vai descobrir que **a tela é só a ponta** de algo muito maior, e que muitas vezes é nesse "algo maior" que mora o problema.

## Objetivos

Ao final desta aula, você será capaz de:

- Diferenciar a **interface** de um aplicativo do **serviço** completo do qual ela faz parte.
- Identificar **pessoas, processos, tecnologias e evidências** que compõem um serviço.
- Explicar os **princípios** do Design de Serviços.
- **Investigar o serviço** antes de propor uma mudança no software.

## Pré-requisitos

Ter visto as **Aulas 87 a 90**: usabilidade, heurísticas e leis de UX. Hoje a gente amplia o olhar: da tela para tudo o que está em volta dela.

## Desenvolvimento

### O serviço é maior que o aplicativo

Um **produto** você leva para casa: um caderno, um fone. Um **serviço** é algo que acontece **ao longo do tempo**, com várias partes trabalhando juntas para alguém atingir um objetivo: comer o lanche, pegar o livro emprestado, conseguir o documento na secretaria. O aplicativo costuma ser só **uma** dessas partes.

```diagrama-progressivo
titulo: O que existe por trás de "Pedido confirmado"
camadas:
  - rotulo: O que você vê
    conteudo: O cardápio no app, o botão de pagar, a mensagem de confirmação e, depois, o mapinha do entregador chegando.
  - rotulo: As pessoas
    conteudo: Atendente do restaurante que recebe o pedido, cozinheiro que prepara, quem confere e embala, entregador, suporte que atende reclamação.
  - rotulo: Os processos
    conteudo: Receber o pedido, preparar na ordem certa, conferir os itens, chamar o entregador, entregar, resolver problema quando algo dá errado.
  - rotulo: As tecnologias
    conteudo: O app do cliente, o tablet da cozinha, o sistema de pagamento, o serviço de mapas, o banco de dados de pedidos e o app do entregador.
  - rotulo: Onde quebrou
    conteudo: A batata faltou porque a etapa de conferir não existe no processo da cozinha. Nenhuma tela nova resolve isso. O conserto é no serviço.
```

:::conceito Design de Serviços
É uma abordagem para **compreender, planejar e melhorar serviços** olhando para a experiência de quem usa **e** para tudo o que é necessário para entregá-la: **pessoas**, **processos**, **tecnologias** e as **evidências** que a pessoa encontra pelo caminho (telas, mensagens, comprovantes, o balcão, a embalagem).
:::

### Os princípios do Design de Serviços

Os autores de referência da área (Marc Stickdorn e colegas, no livro *This is Service Design Doing*, de 2018) resumem a abordagem em seis princípios:

| Princípio | Em uma frase |
|---|---|
| **Centrado no ser humano** | Considera a experiência de todas as pessoas envolvidas, não só do cliente: também de quem atende, prepara e entrega. |
| **Colaborativo** | Usuários, desenvolvedores, atendentes e gestores constroem a solução juntos. |
| **Iterativo** | Testa cedo, aprende com o erro e melhora em ciclos, em vez de apostar tudo numa versão final. |
| **Sequencial** | O serviço é uma sequência de momentos (antes, durante e depois), e cada um precisa ser pensado. |
| **Real** | Decide com base em pesquisa e observação do mundo real, não em suposição da equipe. |
| **Holístico** | Olha para o serviço inteiro e para o contexto em volta, não para uma tela isolada. |

:::curiosidade Cinco ou seis princípios?
Talvez você encontre por aí uma lista com **cinco** princípios: centrado no usuário, cocriativo, sequencial, evidente (ou tangível) e holístico. Ela vem da primeira edição do livro, de 2011. Em 2018 os mesmos autores revisaram a lista: o "tangível" foi absorvido e entraram **iterativo** e **real**. A ideia central não mudou; a versão nova só deixa mais claro que design de serviço se faz testando e pesquisando.
:::

### A pergunta muda

Para quem desenvolve sistemas, o efeito prático do Design de Serviços é trocar a pergunta inicial do projeto. Sai **"qual funcionalidade vamos programar?"** e entra **"qual problema precisamos resolver, e que papel o software tem nesse serviço?"**. Às vezes a resposta é uma tela nova. Às vezes é integrar dois sistemas que não conversam. E às vezes é mudar um processo, sem uma linha de código.

:::atencao Erro comum: consertar a tela quando o problema é o serviço
A escola criou um app para agendar atendimento na secretaria, mas a fila continua enorme. A reação mais comum de uma equipe de desenvolvimento é mexer no que ela controla: refazer o layout, trocar as cores, mudar a linguagem de programação. Nada disso adianta, porque o atraso vem dos **atendimentos anteriores que demoram** e da secretaria, que **não atualiza** os horários no sistema. O sinal de alerta é fácil de reconhecer: se o app "funciona" e a reclamação continua, investigue o serviço antes de abrir o editor de código.
:::

:::dica Na profissão
Essa troca de pergunta é o começo de um bom **levantamento de requisitos**. Quem só pergunta "quais telas você quer?" escreve requisitos para o problema errado. Quem olha o serviço descobre [[requisito-funcional|requisitos funcionais]] que ninguém tinha pedido, como "a cozinha deve ver o pedido assim que ele é pago", e evita programar funções que ninguém vai usar.
:::

## Prática

**Atividade "raio-X de um serviço da escola" (grupos de 4, sem computador, ~15 min).** Cada grupo escolhe um serviço da própria escola: **cantina**, **biblioteca**, **secretaria**, **merenda** ou **empréstimo de equipamentos** (notebook, projetor).

1. **Desmontem o serviço (7 min).** Numa folha dividida em quatro, listem:
   - **Pessoas:** quem participa, inclusive quem o aluno não vê.
   - **Processos:** as etapas que acontecem do começo ao fim.
   - **Tecnologias:** sistemas, planilhas, papéis, telefones usados.
   - **Evidências:** o que o aluno vê ou recebe (fila, balcão, ficha, mensagem).
2. **Achem a falha invisível (5 min).** Escrevam **um problema real** desse serviço que **não seria resolvido** só com um aplicativo bonito. Em uma frase, digam onde ele nasce: em qual pessoa, processo ou tecnologia.
3. **Princípio (3 min).** Qual dos seis princípios a escola mais está esquecendo nesse serviço? Justifiquem.

Cada grupo apresenta a falha invisível em 30 segundos.

## Avaliação

```quiz
- pergunta: O app de agendamento da secretaria funciona sem erros, mas os alunos continuam pegando fila porque os atendimentos anteriores atrasam e ninguém atualiza os horários. Qual atitude está mais alinhada ao Design de Serviços?
  alternativas:
    - texto: Trocar a linguagem de programação do app
    - texto: Deixar a interface mais colorida
    - texto: Mapear a experiência do aluno e investigar também os processos internos da secretaria
      correta: true
    - texto: Comprar computadores mais potentes para a secretaria
  feedback: >
    O problema nasce no processo da secretaria, não no código. Design de Serviços
    olha para o que o usuário vê e para os bastidores que sustentam o serviço.
- pergunta: Qual destas opções descreve melhor um serviço?
  alternativas:
    - texto: Uma tela de aplicativo bem desenhada
    - texto: Um objeto que o cliente compra e leva para casa
    - texto: Um conjunto de pessoas, processos, tecnologias e evidências que, ao longo do tempo, ajudam alguém a atingir um objetivo
      correta: true
    - texto: O banco de dados de um sistema
  feedback: >
    O serviço acontece no tempo e envolve várias partes. O app é só uma delas.
- pergunta: No delivery, o lanche chega sem a batata porque a cozinha não tem uma etapa de conferência. Esse problema está em qual componente do serviço?
  alternativas:
    - texto: Na tecnologia, porque o app está com defeito
    - texto: No processo, porque falta uma etapa no trabalho da cozinha
      correta: true
    - texto: Na evidência, porque a embalagem é feia
    - texto: Não é um problema de serviço, é culpa do cliente
  feedback: >
    O app registrou o pedido certinho. A falha está numa etapa que não existe no
    processo de preparo.
- pergunta: Uma equipe decide ouvir alunos, atendentes e a direção antes de redesenhar o serviço da biblioteca, e montar a solução junto com eles. Quais princípios ela está aplicando?
  alternativas:
    - texto: Centrado no ser humano e colaborativo
      correta: true
    - texto: Sequencial e iterativo
    - texto: Holístico e tangível
    - texto: Nenhum, porque princípio de design é só sobre a tela
  feedback: >
    Considerar todas as pessoas envolvidas é ser centrado no ser humano; construir
    junto com elas é ser colaborativo.
- pergunta: Para quem desenvolve sistemas, qual é a principal mudança de pergunta que o Design de Serviços propõe?
  alternativas:
    - texto: De "qual linguagem usar?" para "qual framework usar?"
    - texto: De "qual funcionalidade programar?" para "qual problema resolver e qual o papel do software no serviço?"
      correta: true
    - texto: De "quanto custa?" para "quanto tempo leva?"
    - texto: De "quem é o cliente?" para "qual é a cor da marca?"
  feedback: >
    Entender o serviço antes de programar evita construir uma solução correta para
    o problema errado.
```

## Fechamento

Hoje você descobriu que:

- A **tela é só uma parte** do serviço; o resto são pessoas, processos, tecnologias e evidências.
- **Design de Serviços** olha para a experiência de quem usa e para os bastidores que a tornam possível.
- Seus **seis princípios**: centrado no ser humano, colaborativo, iterativo, sequencial, real e holístico.
- Quando o app funciona e a reclamação continua, **investigue o serviço** antes de mexer no código.

**Próxima aula:** você vai aprender a ferramenta mais usada para enxergar um serviço no tempo: o **mapa da jornada**, com seus pontos de contato e a separação entre o que o usuário vê (*frontstage*) e o que acontece nos bastidores (*backstage*).

:::roteiro
Abrir pedindo um relato real: "quem já teve pedido de delivery que deu errado? de quem foi a culpa?". As respostas espalham a culpa entre app, restaurante e entregador, que é exatamente o ponto. No diagrama, antes de cada camada, pergunte "quem mais está envolvido aqui?". A tabela de princípios não é para decorar: peça que cada aluno escolha o princípio que mais faz falta na escola. Correções em relação à origem: (1) no deck 90 da SEED, a resposta do desafio da secretaria aparece como "Alternativa C — Lei de Hick", copiada do deck 89; a alternativa C está certa, mas a explicação certa é a do quiz 1 desta aula. (2) O deck lista os 5 princípios da edição de 2011; a aula traz os 6 da edição de 2018 e explica a diferença no :::curiosidade. Os decks 90 e 91 repetiam o mesmo caso da cantina; aqui o caso é o delivery, e a cantina fica para o projeto das aulas 95 a 97. Na prática, ajude grupos que travarem no "pessoas invisíveis": quem lava, quem compra o estoque, quem cadastra no sistema.
:::
