---
titulo: "Usabilidade e as heurísticas de Nielsen (1 a 5)"
tema: Usabilidade e Design de Serviços
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: [Noção de protótipo de tela]
objetivos:
  - Diferenciar um sistema que funciona de um sistema fácil de usar
  - Explicar o que é uma heurística de usabilidade e para que ela serve
  - Reconhecer as heurísticas 1 a 5 de Nielsen em telas de aplicativos
  - Apontar a heurística violada num problema de tela e propor uma correção
trilha: usabilidade-e-design-de-servicos
ordem: 1
slug: usabilidade-e-heuristicas-de-nielsen
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/seed-87-95/87-heuristicas-de-nielsen-introducao.pptx
  - lake/analise-e-metodos-para-sistemas/seed-87-95/87-exercicios-1.docx
  - lake/analise-e-metodos-para-sistemas/seed-87-95/88-heuristicas-de-usabilidade-avancado.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-11-04
---

Você manda a atividade pelo aplicativo da escola, toca em **Enviar** e... nada. A tela fica igual. Foi? Não foi? Você toca de novo, só por garantia. E aí a professora recebe o mesmo arquivo duas vezes, ou nenhuma, e ninguém sabe dizer qual. Repare numa coisa: o envio pode ter funcionado perfeitamente lá no servidor. O código está certo. Mesmo assim, você saiu da tela inseguro, e a culpa não é sua. A aula de hoje é sobre essa diferença entre **funcionar** e **ser fácil de usar**, e sobre as cinco primeiras regras práticas que os profissionais usam para encontrar esse tipo de problema antes do usuário.

## Objetivos

Ao final desta aula, você será capaz de:

- Diferenciar um sistema que **funciona** de um sistema **fácil de usar**.
- Explicar o que é uma **heurística de usabilidade** e para que ela serve.
- Reconhecer as **heurísticas 1 a 5 de Nielsen** em telas de aplicativos.
- Apontar a heurística violada num problema de tela e **propor uma correção**.

## Pré-requisitos

Ter visto, nas aulas anteriores, o que é um **protótipo de tela**. Não precisa saber programar: hoje a gente analisa telas, não código.

## Desenvolvimento

### Funcionar não é o mesmo que ser fácil de usar

Todo sistema responde a duas perguntas diferentes. A primeira é **"faz o que deveria?"**: o botão envia, o cálculo dá certo, o dado é salvo. A segunda é **"a pessoa consegue usar sem tropeçar?"**: ela entende o que está vendo, sabe o que acontece depois de tocar, consegue voltar atrás. Dá para acertar a primeira e errar feio a segunda. O app da atividade do início é exatamente isso.

:::conceito Usabilidade
É o quanto uma pessoa consegue usar um sistema para atingir o objetivo dela **com eficácia** (chega lá), **com eficiência** (sem esforço desperdiçado) e **com satisfação** (sem sair irritada ou insegura). Usabilidade é qualidade de verdade, não "enfeite" que entra no fim do projeto.
:::

Para avaliar usabilidade, o jeito mais completo é observar pessoas reais usando o sistema. Só que isso custa tempo, e muitos problemas são tão comuns que dá para encontrá-los antes, só olhando com atenção. É para isso que existem as heurísticas.

:::conceito Heurística de usabilidade
É uma **regra prática**: uma diretriz geral, nascida da experiência, que ajuda a encontrar problemas de interface. Não é lei, não é checklist que garante aprovação, e não substitui o teste com usuários. É um par de óculos: você olha a mesma tela e passa a enxergar coisas que antes passavam batido.
:::

:::curiosidade De onde vêm as dez
O dinamarquês **Jakob Nielsen** publicou em 1990, junto com Rolf Molich, uma lista de princípios para avaliar interfaces. Em 1994 ele analisou centenas de problemas reais de usabilidade e refinou a lista nas **10 heurísticas** usadas até hoje. Elas nasceram na época do computador de mesa e continuam valendo no celular: o que mudou foi a tela, não a cabeça de quem usa.
:::

### Fale com o usuário: heurísticas 1 e 2

**1. Visibilidade do status do sistema.** O sistema deve sempre contar o que está acontecendo, rápido e de um jeito que a pessoa perceba. É o caso do envio da atividade: faltou um "Enviando..." seguido de "Atividade enviada às 14h32". Exemplos do seu dia a dia que acertam: a barra de progresso de um download, o "digitando..." numa conversa, os dois risquinhos de mensagem entregue.

**2. Correspondência entre o sistema e o mundo real.** O sistema deve falar a língua de quem usa, com palavras, ícones e ordem de informação que a pessoa já conhece. Não basta estar em português. Um botão escrito **"Persistir registro"** está em português e mesmo assim não comunica nada para um estudante; **"Salvar"** comunica. Uma lixeira para apagar e um carrinho para compras funcionam porque imitam objetos do mundo real.

:::exemplo O teste da avó
Leia o texto de um botão ou de um aviso em voz alta e imagine sua avó (ou alguém que nunca programou) ouvindo. Se ela perguntar "o que é isso?", provavelmente a heurística 2 foi violada. "Sincronizar entidades" reprova. "Atualizar suas notas" passa.
:::

### Deixe o usuário no comando: heurísticas 3 e 4

**3. Controle e liberdade do usuário.** Todo mundo toca no lugar errado às vezes. O sistema precisa oferecer uma **saída de emergência** clara: cancelar, voltar, fechar, **desfazer**. O exemplo clássico é o "Desfazer" que aparece por alguns segundos depois de apagar um e-mail ou arquivar uma conversa: você erra, corrige e segue a vida.

**4. Consistência e padrões.** Coisas iguais devem parecer iguais e se comportar igual, dentro do próprio sistema e em relação aos outros apps que a pessoa já usa. Se o ícone de lixeira **exclui** numa tela e **arquiva** em outra, o usuário aprende uma regra e é traído por ela. Se todos os apps põem a busca numa lupa e o seu inventa um desenho novo, a pessoa precisa reaprender algo que já sabia.

:::importante A diferença entre 3 e 4
A heurística 3 é sobre **sair de uma situação** que a pessoa não queria (o erro já aconteceu ou está acontecendo). A heurística 4 é sobre **não confundir** a pessoa para começo de conversa (o mesmo símbolo sempre significa a mesma coisa). Um botão "Voltar" que some numa tela viola a 3; um botão "Voltar" que em cada tela fica num canto diferente viola a 4.
:::

### Evite o erro antes que ele aconteça: heurística 5

**5. Prevenção de erros.** Melhor do que uma boa mensagem de erro é um projeto que não deixa o erro acontecer. Na prática: separar o botão perigoso dos outros, desabilitar o botão **Enviar** enquanto o envio está em andamento (o que resolve o envio duplicado do início), oferecer uma lista de opções em vez de um campo livre onde a pessoa pode digitar errado, e pedir confirmação para o que não tem volta.

```diagrama-progressivo
titulo: Enviando uma atividade pelo app da escola
camadas:
  - rotulo: Você toca em Enviar
    conteudo: A tela não muda. Você não sabe se o sistema recebeu o toque. Problema de visibilidade do status (heurística 1).
  - rotulo: Você toca de novo
    conteudo: Como nada impedia, o arquivo foi enviado duas vezes. Faltou prevenção de erros (heurística 5), por exemplo desabilitar o botão enquanto envia.
  - rotulo: Aparece um aviso
    conteudo: "O texto diz \"Entidade persistida com sucesso\". Você até deduz que deu certo, mas o sistema não fala a sua língua (heurística 2)."
  - rotulo: Você percebe que mandou o arquivo errado
    conteudo: Não existe botão de desfazer nem de substituir o envio. Você fica preso a um erro que percebeu em dois segundos (heurística 3).
  - rotulo: A versão corrigida
    conteudo: "Botão bloqueado com \"Enviando...\", depois \"Atividade enviada às 14h32\" e um link \"Trocar arquivo\" por alguns minutos. Mesmo código no servidor, experiência completamente diferente."
```

:::atencao Erro comum: confirmação para tudo
Quem descobre a heurística 5 costuma sair colocando "Tem certeza?" em **todas** as ações. Resultado real e fácil de observar: em poucos dias a pessoa clica em "Sim" sem ler, por reflexo, e a confirmação para de proteger justamente na hora em que importava. Confirmação é para ação **destrutiva e sem volta** (excluir a conta, apagar o projeto). Para o resto, um "Desfazer" depois da ação protege mais e incomoda menos.
:::

:::dica Na hora de programar
Essas heurísticas viram linhas de código bem concretas no Front-End: mostrar um indicador de carregamento enquanto espera a resposta (1), desabilitar o botão durante o envio (5), escrever a mensagem do `alert` pensando no usuário e não no programador (2). Em empresa, o pessoal de QA e de UX abre chamado citando a heurística pelo nome, e quem desenvolve precisa entender o que ela quer dizer.
:::

## Prática

**Atividade "caça às violações" (duplas, sem computador, ~15 min).** Cada dupla recebe (ou copia do quadro) a descrição de cinco telas. Para cada uma, escreva no caderno: **qual heurística (1 a 5) foi violada**, em uma frase **por quê**, e **uma correção**.

| Tela | O que acontece |
|---|---|
| A — Cantina | Você confirma o pedido do lanche e volta para a tela inicial, sem nenhum aviso. |
| B — Biblioteca | O botão de reservar livro diz **"Efetuar alocação de exemplar"**. |
| C — Cadastro | Depois de preencher 12 campos, não existe botão para voltar e corrigir o e-mail digitado errado; só "Concluir". |
| D — Agenda escolar | Na tela de tarefas, o ícone de lápis edita; na tela de provas, o mesmo lápis apaga a prova. |
| E — Fotos da turma | O botão **"Apagar álbum"** fica colado no **"Compartilhar"**, do mesmo tamanho e cor, e apaga na hora. |

Depois, cada dupla escolhe a tela que achou mais grave e explica a correção para a turma. Se duas duplas apontarem heurísticas diferentes para a mesma tela, ótimo: discutam, porque um problema pode violar mais de uma.

**Extensão (opcional, com celular e autorização do professor):** encontre num app que você usa um exemplo que **acerta** uma das cinco heurísticas e mostre para a dupla.

## Avaliação

```quiz
- pergunta: Um app de pedidos calcula o valor certinho e grava o pedido no banco, mas metade dos usuários faz o pedido duas vezes porque não percebe que o primeiro foi enviado. O que isso mostra?
  alternativas:
    - texto: O sistema tem um erro de programação no cálculo
    - texto: O sistema funciona, mas tem um problema de usabilidade
      correta: true
    - texto: Os usuários precisam de treinamento antes de usar
    - texto: O problema é só de estética da tela
  feedback: >
    A funcionalidade está correta; quem falha é a comunicação com a pessoa.
    Funcionar e ser fácil de usar são perguntas diferentes.
- pergunta: O que melhor define uma heurística de usabilidade?
  alternativas:
    - texto: Uma lei obrigatória que todo app precisa cumprir para ser publicado
    - texto: Um teste automático que encontra todos os erros de uma tela
    - texto: Uma regra prática que ajuda a encontrar problemas de interface
      correta: true
    - texto: Um padrão de cores definido pelo Google e pela Apple
  feedback: >
    Heurística é diretriz geral nascida da experiência. Ajuda a enxergar
    problemas, mas não garante nada sozinha e não substitui o teste com usuários.
- pergunta: "Um sistema da escola mostra o botão \"Persistir registro\" para o estudante salvar a ficha. Qual heurística foi violada?"
  alternativas:
    - texto: Visibilidade do status do sistema
    - texto: Correspondência entre o sistema e o mundo real
      correta: true
    - texto: Prevenção de erros
    - texto: Controle e liberdade do usuário
  feedback: >
    O texto usa a linguagem do programador, não a do usuário. "Salvar" resolveria.
- pergunta: Depois de arquivar uma conversa por engano, aparece por alguns segundos o botão "Desfazer". Qual heurística esse botão atende?
  alternativas:
    - texto: Consistência e padrões
    - texto: Correspondência entre o sistema e o mundo real
    - texto: Controle e liberdade do usuário
      correta: true
    - texto: Visibilidade do status do sistema
  feedback: >
    Desfazer é a saída de emergência: a pessoa errou e consegue voltar sem prejuízo.
- pergunta: O botão "Excluir projeto" fica ao lado de "Editar projeto", igual a ele, e exclui sem pedir confirmação. Qual a melhor correção?
  alternativas:
    - texto: Trocar a fonte de todos os botões da tela
    - texto: Afastar e diferenciar o botão perigoso e pedir confirmação antes de excluir
      correta: true
    - texto: Colocar "Tem certeza?" em todos os botões do aplicativo
    - texto: Escrever no manual que o usuário deve tomar cuidado
  feedback: >
    É prevenção de erros: impedir a ação destrutiva acidental. Confirmar tudo
    banaliza a confirmação; avisar no manual joga a culpa no usuário.
```

## Fechamento

Hoje você descobriu que:

- **Funcionar** e **ser fácil de usar** são coisas diferentes, e o usuário sente as duas.
- **Heurísticas** são regras práticas para encontrar problemas de interface, não leis nem garantias.
- As cinco primeiras de Nielsen: **visibilidade do status**, **correspondência com o mundo real**, **controle e liberdade**, **consistência e padrões** e **prevenção de erros**.
- Um mesmo problema pode violar mais de uma heurística, e a correção quase sempre é pequena perto do estrago que evita.

**Próxima aula:** as heurísticas 6 a 10, incluindo a que transforma o temido "Erro 504" numa mensagem que realmente ajuda alguém.

:::roteiro
Abrir com a pergunta "quem já tocou duas vezes num botão porque não sabia se tinha ido?". Quase todo mundo levanta a mão; peça um ou dois relatos rápidos e só depois nomeie a diferença entre funcionar e ser usável. Não liste as cinco heurísticas no quadro logo de cara: apresente pelo problema, nome por último. No diagrama progressivo, antes de revelar cada camada, pergunte à turma "o que deu errado aqui?". Correção em relação à origem: o comentário da questão 1 do docx da SEED (aula 87) diz que as heurísticas "não tratam de estética"; isso está errado, a heurística 8 é justamente "Estética e design minimalista" (vem na próxima aula). Se algum aluno trouxer o exercício da SEED, a resposta (C, "Diversão e estética") continua certa, só a justificativa é que estava errada. Gabarito da prática: A=1, B=2, C=3, D=4, E=5 (E também toca na 3, pela falta de desfazer). Celular só na extensão e com sua autorização. Os vídeos da Alura citados no deck 87 ficam como apoio opcional.
:::
