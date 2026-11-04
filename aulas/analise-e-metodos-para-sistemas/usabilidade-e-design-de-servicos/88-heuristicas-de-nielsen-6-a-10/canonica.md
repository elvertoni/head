---
titulo: "Heurísticas de Nielsen (6 a 10) e a boa mensagem de erro"
tema: Usabilidade e Design de Serviços
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: ["Usabilidade e as heurísticas de Nielsen (1 a 5)"]
objetivos:
  - Reconhecer as heurísticas 6 a 10 de Nielsen em telas de aplicativos
  - Explicar por que reconhecer é mais fácil do que lembrar e aplicar isso a uma interface
  - Diferenciar design minimalista de interface vazia ou escondida
  - Reescrever uma mensagem de erro dizendo o que aconteceu, por quê e como resolver
trilha: usabilidade-e-design-de-servicos
ordem: 88
slug: heuristicas-de-nielsen-6-a-10
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/seed-87-95/88-heuristicas-de-usabilidade-avancado.pptx
  - lake/analise-e-metodos-para-sistemas/seed-87-95/87-exercicios-1.docx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-11-04
---

"Erro 504 — operação inválida." Se você já viu uma mensagem assim, lembra da sensação: o que eu fiz de errado? Perdi o que tinha digitado? Tento de novo ou chamo alguém? A mensagem existe, está na tela, é tecnicamente verdadeira para quem programou... e não serve para nada a quem está usando. Na aula passada você conheceu cinco heurísticas que evitam boa parte dos tropeços. Hoje vêm as outras cinco, e elas cuidam de três coisas que todo app precisa acertar: não exigir que você decore nada, não encher a tela de distração e, quando algo der errado (porque sempre dá), ajudar em vez de assustar.

## Objetivos

Ao final desta aula, você será capaz de:

- Reconhecer as **heurísticas 6 a 10 de Nielsen** em telas de aplicativos.
- Explicar por que **reconhecer é mais fácil do que lembrar** e aplicar isso a uma interface.
- Diferenciar **design minimalista** de interface vazia ou escondida.
- Reescrever uma mensagem de erro dizendo **o que aconteceu, por quê e como resolver**.

## Pré-requisitos

Ter visto a **Aula 87**: a diferença entre funcionar e ser fácil de usar, e as heurísticas 1 a 5.

## Desenvolvimento

### Mostre em vez de exigir memória: heurística 6

**6. Reconhecimento em vez de memorização.** A pessoa não deveria precisar guardar na cabeça uma informação de uma tela para usar em outra. O sistema deve deixar à vista as opções, os comandos e os dados de que ela precisa naquele momento.

Pense numa prova. Questão de múltipla escolha costuma parecer mais fácil do que questão aberta sobre o mesmo assunto, e não é impressão: **reconhecer** a resposta certa entre opções exige muito menos da memória do que **lembrar** dela do zero. Interfaces boas fazem do usuário um aluno de prova de múltipla escolha.

Na prática, isso aparece como: histórico de buscas recentes, sugestões enquanto você digita, menus visíveis, ícone acompanhado de texto, e o resumo do pedido mostrado na tela de pagamento (em vez de esperar que você lembre o que pôs no carrinho).

:::exemplo O código do pedido
Um app de cantina mostra "Seu código de retirada é 4827" e muda de tela. No balcão, pede o código. Quem não anotou fica travado. A versão que respeita a heurística 6 deixa o código fixo na tela de "Meus pedidos", visível a qualquer momento, sem depender da memória de ninguém.
:::

### Sirva o novato e o veterano: heurística 7

**7. Flexibilidade e eficiência de uso.** O mesmo sistema é usado por quem abriu pela primeira vez e por quem usa todo dia. O novato precisa de caminhos claros e visíveis; o veterano quer **atalhos** que o deixem mais rápido, sem atrapalhar o novato.

Exemplos: o `Ctrl+C` / `Ctrl+V` do computador (quem não conhece usa o menu "Editar"; quem conhece nem pensa), o gesto de arrastar para o lado para arquivar uma mensagem, os "favoritos" que levam direto ao que você mais usa, e o "pedir de novo" de um app de comida.

### Menos distração, mais clareza: heurística 8

**8. Estética e design minimalista.** Cada informação a mais na tela disputa a atenção com as informações que importam. Minimalismo **não** é deixar tudo branco nem tirar funções: é retirar o que **compete à toa** pela atenção, para que o essencial apareça.

:::importante Estética é, sim, heurística
Algumas atividades que circulam por aí dizem que as heurísticas de Nielsen "não tratam de estética". Não é verdade: a heurística 8 se chama justamente **Estética e design minimalista**. O que ela não trata é de gosto pessoal ("essa cor é feia"). Ela trata de **ruído**: tudo o que está na tela e não ajuda a pessoa a fazer o que veio fazer.
:::

:::atencao Erro comum: minimalismo que esconde
Na tentativa de "limpar" a tela, muita equipe troca todos os textos por ícones sem rótulo ou esconde funções importantes dentro de um menu ☰. A tela fica bonita na apresentação e o uso piora: a pessoa passa a **adivinhar** o que cada ícone faz, o que viola a heurística 6. Dá para diagnosticar fácil: peça para alguém de fora achar uma função e conte quantos toques "de tentativa" ele dá. Minimalista é a tela com **menos ruído**, não com **menos informação útil**.
:::

### Quando algo dá errado: heurísticas 9 e 10

**9. Ajudar o usuário a reconhecer, diagnosticar e se recuperar de erros.** A heurística 5 tenta evitar o erro; a 9 cuida de quando ele acontece mesmo assim. Uma boa mensagem de erro usa linguagem simples (nada de código técnico), diz **o que aconteceu**, **por que** (quando dá para saber) e **como resolver**.

```diagrama-progressivo
titulo: Consertando a mensagem "Erro 504 — operação inválida"
camadas:
  - rotulo: A mensagem original
    conteudo: "\"Erro 504 — operação inválida.\" O estudante não sabe se a atividade foi enviada, se perdeu o arquivo nem o que fazer agora."
  - rotulo: O que aconteceu
    conteudo: "Primeiro, dizer o fato em linguagem humana: \"Não conseguimos enviar sua atividade.\""
  - rotulo: Por que aconteceu
    conteudo: "Depois, a causa provável, sem jargão. O código 504 significa que o servidor demorou demais para responder. Para o usuário isso vira: \"O sistema da escola demorou para responder.\""
  - rotulo: Como resolver
    conteudo: "Por fim, a saída concreta: \"Seu arquivo continua salvo aqui. Tente enviar de novo em alguns minutos.\" De preferência com um botão \"Tentar novamente\" logo abaixo."
  - rotulo: A mensagem completa
    conteudo: "\"Não conseguimos enviar sua atividade porque o sistema da escola demorou para responder. Seu arquivo continua salvo. Tente de novo em alguns minutos.\" Mesma falha, pessoa tranquila."
```

**10. Ajuda e documentação.** O ideal é que o sistema seja usável sem manual, mas às vezes a pessoa precisa de apoio. Quando precisar, a ajuda deve ser **fácil de encontrar**, **ligada à tarefa** que ela está fazendo, curta e prática. O "?" ao lado de um campo explicando o que é a matrícula vale mais do que um PDF de 40 páginas escondido no rodapé.

:::dica Na hora de programar
Quem programa costuma mostrar na tela o mesmo texto que vai para o log: `Error: ECONNRESET`, um *stack trace*, um código HTTP. Profissionalmente, separe as duas mensagens: a **técnica** vai para o log, onde a equipe investiga; a **humana** vai para a tela, onde alguém precisa decidir o que fazer. Em revisão de código de Front-End, mensagem técnica exposta ao usuário é apontamento comum.
:::

## Prática

**Atividade "o plantão de UX" (duplas, sem computador, ~15 min).**

**Parte 1 — identifique (5 min).** Para cada situação, escreva qual heurística de 6 a 10 foi violada e por quê, em uma frase.

| Situação | O que acontece |
|---|---|
| A — Boletim online | Para ver a nota de uma matéria, você precisa digitar o código dela ("MAT-1A-03"), que só aparece em outra tela. |
| B — Rede social da escola | A tela inicial tem 4 banners piscando, 3 pop-ups e o feed só aparece depois de rolar. |
| C — Inscrição em evento | Aparece apenas "Falha: código 0x0004" e o formulário volta vazio. |
| D — App de horários | Quem usa todo dia precisa abrir três menus para ver a aula de hoje; não existe atalho nem tela inicial personalizável. |
| E — Secretaria digital | Não há nenhuma explicação sobre o que é "Número de RA" no campo que o exige. |

**Parte 2 — reescreva (10 min).** Escolham **duas** mensagens abaixo e reescrevam seguindo o modelo *o que aconteceu + por quê + como resolver*.

```text
1. "Erro 401."
2. "Campo inválido."
3. "NullPointerException at Cadastro.salvar()"
4. "Upload falhou."
```

Cada dupla lê uma das suas mensagens para a turma. A turma avalia: dá para saber o que fazer depois de ouvir?

## Avaliação

```quiz
- pergunta: Um app de pagamento mostra, na tela final, o resumo dos itens que você colocou no carrinho. Qual heurística isso atende?
  alternativas:
    - texto: Reconhecimento em vez de memorização
      correta: true
    - texto: Flexibilidade e eficiência de uso
    - texto: Ajuda e documentação
    - texto: Estética e design minimalista
  feedback: >
    O sistema mostra a informação em vez de exigir que você lembre o que escolheu
    em outra tela.
- pergunta: O gesto de arrastar uma mensagem para o lado para arquivá-la, enquanto o botão "Arquivar" continua no menu, é exemplo de quê?
  alternativas:
    - texto: Prevenção de erros
    - texto: Flexibilidade e eficiência de uso
      correta: true
    - texto: Consistência e padrões
    - texto: Visibilidade do status do sistema
  feedback: >
    É um atalho para quem já usa bastante, sem tirar o caminho visível de quem
    está começando.
- pergunta: Uma equipe "limpou" a tela trocando todos os botões com texto por ícones sem rótulo. O que provavelmente aconteceu com a usabilidade?
  alternativas:
    - texto: Melhorou, porque menos texto é sempre melhor
    - texto: Não mudou, porque as funções continuam lá
    - texto: Piorou, porque o usuário passa a adivinhar o que cada ícone faz
      correta: true
    - texto: Melhorou, porque atende à heurística de ajuda e documentação
  feedback: >
    Minimalismo é tirar ruído, não informação útil. Ícones sem rótulo obrigam a
    lembrar ou adivinhar, o que viola o reconhecimento em vez de memorização.
- pergunta: Qual destas mensagens de erro segue melhor a heurística 9?
  alternativas:
    - texto: "\"Erro 500 — falha interna.\""
    - texto: "\"Ops! Algo deu errado.\""
    - texto: "\"Não foi possível salvar porque a internet caiu. Suas respostas estão guardadas; tente de novo quando a conexão voltar.\""
      correta: true
    - texto: "\"Operação inválida. Contate o administrador.\""
  feedback: >
    Ela diz o que aconteceu, por que aconteceu e o que fazer, e ainda tranquiliza
    sobre os dados. As outras ou usam jargão ou não dão saída.
- pergunta: As heurísticas de Nielsen tratam de estética?
  alternativas:
    - texto: Não, elas tratam só de funcionalidade
    - texto: Sim, a heurística 8 trata de estética e design minimalista, no sentido de evitar ruído na tela
      correta: true
    - texto: Sim, elas definem quais cores cada app deve usar
    - texto: Não, estética é assunto só de designer gráfico
  feedback: >
    A heurística 8 é "Estética e design minimalista". Ela não é sobre gosto, e sim
    sobre tirar da tela o que compete à toa pela atenção.
```

## Fechamento

Hoje você descobriu que:

- **Reconhecer é mais fácil do que lembrar**: boas telas mostram o que a pessoa precisa, em vez de exigir memória (heurística 6).
- O mesmo sistema deve atender o **novato e o veterano**, com caminhos visíveis e atalhos (7).
- **Minimalismo** é tirar ruído, não esconder informação útil (8).
- Erro acontece; uma boa mensagem diz **o que, por quê e como resolver** (9), e a ajuda fica **perto da tarefa** (10).

**Próxima aula:** com as dez heurísticas na mão, você vai fazer o que um profissional de UX faz: uma **avaliação heurística** completa, com registro de problema, gravidade e recomendação.

:::roteiro
Abrir projetando ou escrevendo "Erro 504 — operação inválida" no quadro e perguntar "o que vocês fariam se vissem isso enviando um trabalho?". Recolher as reações (medo de ter perdido, tentar de novo, chamar alguém). No diagrama, pare em cada camada e peça que a turma proponha o texto antes de revelar. Nota técnica: no deck 88 da SEED o exemplo junta "504" com "operação inválida", mas 504 é Gateway Timeout (servidor demorou para responder), não operação inválida; o diagrama usa o significado correto e isso vira bom gancho ("a mensagem nem descreve o próprio erro"). Correção da origem: o comentário da Q1 do docx da SEED (aula 87) afirma que as heurísticas não tratam de estética; o :::importante corrige. Gabarito da Parte 1: A=6, B=8, C=9 (também toca na 3, pelo formulário apagado), D=7, E=10. Na Parte 2, aceite reescritas que tenham as três partes; se faltar "como resolver", essa é a falha mais comum, aponte.
:::
