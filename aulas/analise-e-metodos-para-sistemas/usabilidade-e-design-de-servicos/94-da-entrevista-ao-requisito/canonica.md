---
titulo: "Da entrevista ao requisito: analisando o que os usuários disseram"
tema: Usabilidade e Design de Serviços
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: ["Entrevistas com usuários: perguntar para descobrir"]
objetivos:
  - Separar a fala do usuário da interpretação da equipe
  - Agrupar falas por afinidade para encontrar padrões
  - Formular um insight a partir de um padrão, sem confundir frequência com importância
  - Transformar uma necessidade identificada em um requisito do sistema
trilha: usabilidade-e-design-de-servicos
ordem: 94
slug: da-entrevista-ao-requisito
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/seed-87-95/93-analise-das-entrevistas.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-11-04
---

Depois de uma semana de entrevistas, a equipe tem trinta páginas de anotação, quatro áudios e uma sensação estranha: ouviu muita coisa, e não sabe o que fazer com nada. Um colega diz que "todo mundo reclamou da cor", outro jura que "o problema é a senha", e cada um lembra do que mais o marcou. É como voltar de uma viagem com 800 fotos no celular: elas só viram lembrança útil quando alguém separa, agrupa e escolhe. Na aula passada você aprendeu a colher as falas. Hoje você vai aprender a **analisá-las**, transformando conversa em decisão de projeto.

## Objetivos

Ao final desta aula, você será capaz de:

- Separar a **fala** do usuário da **interpretação** da equipe.
- **Agrupar** falas por afinidade para encontrar padrões.
- Formular um **insight** a partir de um padrão, sem confundir frequência com importância.
- Transformar uma **necessidade** identificada em um **requisito** do sistema.

## Pré-requisitos

Ter visto a **Aula 93**: planejamento de entrevistas e perguntas abertas.

## Desenvolvimento

### Fala não é interpretação

Entrevistas geram **dados qualitativos**: relatos, experiências, dificuldades, expectativas. Não são números que se somam numa planilha; são frases que precisam ser lidas, comparadas e entendidas. O primeiro cuidado ao organizá-las é não misturar duas coisas:

- **Fala:** o que a pessoa **realmente disse**, de preferência com as palavras dela. "Eu nunca sei se meu pedido foi aceito."
- **Interpretação:** o significado que a **equipe** atribui. "Falta retorno do sistema depois do envio."

:::importante Por que separar
Quando a interpretação é anotada como se fosse a fala, a equipe passa a "lembrar" de usuários dizendo coisas que eles nunca disseram, e a opinião do time vira falsa evidência. Mantenha sempre as duas colunas: a fala original, intocada, e ao lado a sua leitura. Assim qualquer pessoa consegue conferir se a interpretação faz sentido.
:::

### Agrupar para enxergar

:::conceito Diagrama de afinidade
É uma técnica para organizar dados qualitativos: cada fala vai para um papelzinho (ou post-it), e a equipe vai **juntando os parecidos** até formar grupos. Só **depois** de agrupar é que cada grupo ganha um nome. É assim que trinta falas soltas viram quatro ou cinco temas.
:::

Repare na ordem: primeiro agrupar, depois nomear. Se a equipe cria as categorias antes ("cadastro", "login", "notificação") e sai encaixando as falas, ela só encontra o que já esperava. Deixando os grupos surgirem das próprias falas, aparecem temas que ninguém tinha previsto.

### Do padrão ao insight

Quando falas diferentes dizem, no fundo, a mesma coisa, você encontrou um **padrão**. Três alunos dizem: "demoro para descobrir minhas tarefas", "não acho os trabalhos pendentes" e "queria ver rápido o que preciso entregar". Frases diferentes, padrão único: **dificuldade de visualizar o que está pendente**.

:::conceito Insight
É uma **compreensão nova e útil** sobre o usuário, tirada de um padrão. Não é a fala repetida, e sim o "porquê" por trás dela. Padrão: "vários alunos perguntam na secretaria se o documento está pronto". Insight: "o aluno não precisa que o documento saia mais rápido; precisa **saber quando** ele vai ficar pronto, para se planejar".
:::

:::importante Frequência é pista, não sentença
Contar quantas pessoas citaram cada problema ajuda a priorizar: se 7 de 10 reclamaram do cadastro, aquilo merece atenção. Mas **um problema citado por poucos pode ser o mais grave**. Se só 2 de 10 contaram que perderam todas as respostas de uma prova quando a internet caiu, isso pesa mais do que 8 pessoas achando a cor do app sem graça. Pese também o **estrago** de cada problema.
:::

### Da necessidade ao requisito

O caminho completo leva de uma frase solta a algo que a equipe consegue construir:

```diagrama-progressivo
titulo: Do que o usuário disse ao que o sistema vai fazer
camadas:
  - rotulo: Fala
    conteudo: "\"Depois que eu envio a solicitação, não sei o que acontece com ela. Fico perguntando na secretaria.\""
  - rotulo: Problema
    conteudo: Falta de retorno. Depois do envio, o aluno fica no escuro e precisa ir pessoalmente perguntar.
  - rotulo: Necessidade
    conteudo: Acompanhar o andamento da solicitação sem depender de ninguém.
  - rotulo: Insight
    conteudo: A ansiedade não vem da demora, vem da incerteza. Saber em que etapa o pedido está já resolve boa parte do incômodo.
  - rotulo: Requisito
    conteudo: O sistema deve permitir que o aluno consulte o status de cada solicitação (recebida, em análise, pronta para retirada) e deve avisá-lo quando ela estiver pronta.
```

:::atencao Erro comum: copiar a solução que o usuário sugeriu
Um entrevistado diz: "Faz um grupo de WhatsApp pra avisar quando o documento ficar pronto". A equipe anota "requisito: grupo de WhatsApp". Erro clássico: o usuário é especialista no **problema** que vive, não na solução técnica. A pergunta certa é "por que ele pediu isso?". A resposta (ele quer ser avisado) é a **necessidade**; o WhatsApp é só uma das soluções possíveis, e talvez não a melhor para dados de alunos. Anote a sugestão, mas registre como requisito a necessidade que está por trás dela.
:::

:::dica Na profissão
Esse caminho termina exatamente onde começam as ferramentas que você já conhece da trilha de agilidade: a necessidade vira uma [[historia-de-usuario|história de usuário]] ("Como aluno, quero acompanhar minha solicitação para não precisar ir à secretaria perguntar") e entra no backlog como [[requisito-funcional|requisito funcional]]. Em empresa, guardar a fala original junto do requisito é ouro: quando alguém perguntar "quem pediu isso?", a evidência está lá.
:::

## Prática

**Atividade "o mural das falas" (grupos de 4, sem computador, ~15 min).** A equipe que vai criar um sistema de **empréstimo de equipamentos** da escola (notebooks, projetores, caixa de som) entrevistou alunos, professores e a funcionária responsável. Estas foram as falas:

```text
 1. "Nunca sei se o projetor está livre antes de descer até a sala."
 2. "Reservei o notebook e, quando cheguei, outra turma tinha pegado."
 3. "Queria receber uma confirmação de que a reserva deu certo."
 4. "A gente não sabe quem está com a caixa de som agora."
 5. "O caderno de reservas fica na coordenação, e ela vive fechada."
 6. "O notebook voltou sem carregador e ninguém soube quem foi."
 7. "Eu anoto no caderno, mas não entendo a letra do outro professor."
 8. "Faz um app igual ao WhatsApp pra gente combinar entre nós."
 9. "Devolvi o projetor e depois me cobraram dizendo que eu não devolvi."
10. "Perdi metade da aula esperando liberarem um notebook."
11. "Queria ver a lista do que está disponível hoje."
12. "Ninguém confere se o equipamento volta funcionando."
```

1. **Mural (3 min).** Escrevam cada fala num papelzinho (só o número e duas ou três palavras).
2. **Afinidade (5 min).** Sem criar categorias antes, juntem os papéis parecidos até formar de 3 a 4 grupos. **Só então** deem um nome a cada grupo.
3. **Insight e requisitos (7 min).** Para o grupo que vocês consideram **mais grave**, escrevam:
   - um **insight** (o porquê por trás das falas);
   - **dois requisitos** no formato "O sistema deve...".
   - E respondam: o que fazer com a fala 8?

## Avaliação

```quiz
- pergunta: "Várias pessoas disseram \"Depois que envio uma solicitação, não sei o que aconteceu com ela\". Qual interpretação é mais adequada?"
  alternativas:
    - texto: Os usuários querem trocar as cores do aplicativo
    - texto: O aplicativo deve apagar as solicitações automaticamente
    - texto: Existe uma necessidade de acompanhar o status das solicitações
      correta: true
    - texto: A entrevista deve ser descartada porque ninguém sugeriu uma solução técnica
  feedback: >
    A fala revela falta de visibilidade depois do envio. Cabe à equipe interpretar a
    necessidade; o usuário não precisa dizer como o software será programado.
- pergunta: Qual das anotações abaixo é uma FALA, e não uma interpretação?
  alternativas:
    - texto: Falta retorno do sistema depois do envio
    - texto: "\"Eu nunca sei se meu pedido foi aceito.\""
      correta: true
    - texto: Os usuários precisam de notificações
    - texto: O processo de envio é confuso
  feedback: >
    A fala é o que a pessoa disse, com as palavras dela. As outras são leituras da
    equipe, que devem ficar em outra coluna.
- pergunta: No diagrama de afinidade, qual a ordem recomendada?
  alternativas:
    - texto: Criar as categorias primeiro e depois encaixar as falas nelas
    - texto: Juntar as falas parecidas primeiro e só depois dar nome aos grupos
      correta: true
    - texto: Descartar as falas que aparecem só uma vez
    - texto: Ordenar as falas pela quantidade de palavras
  feedback: >
    Deixar os grupos surgirem das falas evita que a equipe só encontre o que já
    esperava encontrar.
- pergunta: Em 10 entrevistas, 8 pessoas acharam a cor do app sem graça e 2 contaram que perderam todas as respostas de uma prova quando a internet caiu. O que priorizar?
  alternativas:
    - texto: A cor, porque foi citada por mais gente
    - texto: Nenhum dos dois, porque não houve unanimidade
    - texto: A perda das respostas, porque frequência é pista mas o estrago também pesa
      correta: true
    - texto: Fazer uma nova rodada de entrevistas só sobre cores
  feedback: >
    Um problema raro pode ser crítico. Perder uma prova inteira é muito mais grave
    do que achar uma cor sem graça.
- pergunta: Um entrevistado diz "Faz um grupo de WhatsApp pra avisar quando o documento ficar pronto". O que a equipe deve registrar como requisito?
  alternativas:
    - texto: O sistema deve ser um grupo de WhatsApp
    - texto: O sistema deve avisar o aluno quando o documento estiver pronto
      correta: true
    - texto: Nada, porque sugestão de usuário não serve para análise
    - texto: O sistema deve ter um botão verde igual ao do WhatsApp
  feedback: >
    A sugestão revela a necessidade (ser avisado). A forma de atender a essa
    necessidade é decisão da equipe, e o WhatsApp é só uma das opções.
```

## Fechamento

Hoje você descobriu que:

- Analisar entrevistas começa separando **fala** (o que foi dito) de **interpretação** (o que a equipe entende).
- O **diagrama de afinidade** agrupa falas parecidas e só depois dá nome aos grupos.
- Um **padrão** leva a um **insight**, o porquê por trás das falas, e **frequência** é pista, não sentença.
- O caminho termina em requisito: **fala → problema → necessidade → requisito**, sem copiar a solução sugerida pelo usuário.

**Próxima aula:** você já sabe descobrir problemas e necessidades. Agora é hora de organizar uma **ideia de solução** inteira numa página só, tratando cada parte dela como hipótese a testar: o **Lean Canvas**.

:::roteiro
Abrir com a comparação das 800 fotos da viagem. Escreva no quadro duas colunas, FALA e INTERPRETAÇÃO, e peça que a turma classifique 3 ou 4 frases rápidas antes de entrar no conteúdo. No diagrama, pare em "Necessidade" e peça que proponham o requisito antes de revelar. Acréscimos em relação ao deck 93 da SEED: o nome da técnica (diagrama de afinidade) e a regra de agrupar antes de nomear; o deck já trazia a separação fala/interpretação e o alerta de frequência, que mantivemos. Gabarito esperado da prática (aceite variações bem justificadas): disponibilidade (1, 5, 10, 11), reserva confiável (2, 3, 7), controle de quem está com o quê e da devolução (4, 6, 9, 12). A fala 8 é uma sugestão de solução: a necessidade por trás é se comunicar e combinar o uso, e ela pode ir para o grupo da reserva. Requisitos esperados no grupo de controle: "O sistema deve registrar quem retirou cada equipamento e quando" e "O sistema deve registrar a devolução e o estado do equipamento".
:::
