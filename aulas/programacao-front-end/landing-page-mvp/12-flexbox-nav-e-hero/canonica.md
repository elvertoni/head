---
titulo: "Flexbox: alinhar de verdade o topo e o hero"
tema: Layout com Flexbox
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Landing page com cores e tipografia aplicadas na Aula 11]
objetivos:
  - Distinguir o papel do container flex do papel dos itens
  - Explicar o que são eixo principal e eixo cruzado e como flex-direction os inverte
  - Usar justify-content, align-items e gap para montar uma barra de navegação
  - Centralizar o conteúdo do hero nos dois sentidos
  - Diagnosticar por que align-items parece não fazer efeito quando o container não tem altura
trilha: landing-page-mvp
ordem: 12
slug: flexbox-nav-e-hero
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-08-18
---

Sua página tem cor, tem tipografia decente e continua com um problema óbvio: **tudo está empilhado**. O nome do produto em cima, o menu embaixo dele, cada link numa linha, o botão do hero jogado à esquerda. Nenhum site que você usa é assim, e o motivo é que o HTML, sozinho, só sabe empilhar — ele coloca uma caixa embaixo da outra e pronto. Colocar coisas **lado a lado**, com espaço parelho entre elas e alinhadas de verdade, é um trabalho que já foi um dos mais penosos da profissão. Hoje é uma propriedade só. Hoje o seu topo passa a parecer o topo de um site.

## Objetivos

Ao final desta aula, você será capaz de:

- Separar quem manda (**o container**) de quem obedece (**os itens**).
- Explicar **eixo principal** e **eixo cruzado** — e por que eles trocam de lugar quando a direção muda.
- Montar uma barra de navegação com nome à esquerda e links à direita.
- Centralizar o hero **nos dois sentidos**, horizontal e vertical.
- Descobrir sozinho por que `align-items` às vezes parece não funcionar.

## Pré-requisitos

A página das aulas 10 e 08, com a estrutura semântica e o `estilo.css` ligado. Vamos escrever CSS novo em cima do que já existe, sem apagar nada.

## Desenvolvimento

### Quem manda é o elemento de fora

O primeiro e maior tropeço com Flexbox é achar que ele se aplica na coisa que você quer mover. Não é. Ele se aplica no **pai** — no elemento que contém as coisas.

:::conceito Container e itens
Quando você escreve `display: flex` num elemento, ele vira **container flex** e passa a mandar em como seus **filhos diretos** se organizam. Os filhos, chamados de **itens**, não precisam de nenhuma propriedade especial: eles se comportam diferente porque **o pai mudou**, não porque eles mudaram.
:::

É essa a virada mental da aula. Você não empurra cada link para o lugar dele — você declara, no `<nav>`, como os filhos devem se distribuir, e eles se distribuem. Só os **filhos diretos** obedecem: um neto, dentro de outra caixa, não é item daquele container.

```css
nav {
  display: flex;   /* o nav manda */
}
/* os links dentro dele viram itens automaticamente */
```

### Os dois eixos — e a armadilha de decorar

Todo container flex tem dois eixos, e cada um tem sua própria propriedade de alinhamento. Aqui mora a confusão que persegue a maioria das pessoas por anos, porque quase todo mundo aprende errado do jeito mais conveniente.

```diagrama-progressivo
titulo: Os dois eixos, e por que decorar horizontal e vertical te trai
camadas:
  - rotulo: O eixo principal é a direção em que as coisas se enfileiram
    conteudo: "Por padrão, um container flex enfileira os filhos da esquerda para a direita. Essa direção da fila é o eixo principal. O outro sentido, perpendicular a ela, é o eixo cruzado."
  - rotulo: justify-content trabalha no eixo principal
    conteudo: "É ele que decide como sobra o espaço ao longo da fila — tudo junto no começo, tudo no fim, tudo no centro, ou o espaço dividido entre os itens com space-between."
  - rotulo: align-items trabalha no eixo cruzado
    conteudo: "É ele que decide como os itens se posicionam na outra direção — encostados no início, no fim, ou centralizados. Com a fila horizontal, isso significa alinhar de cima a baixo."
  - rotulo: A troca que derruba quem decorou
    conteudo: "Escreva flex-direction column e a fila passa a ser vertical. O eixo principal virou o de cima para baixo, e o cruzado virou o da esquerda para a direita. Ou seja, justify-content agora alinha na vertical e align-items na horizontal — exatamente o contrário do que decorou quem memorizou justify igual horizontal."
  - rotulo: O jeito que não trai
    conteudo: "Não guarde direções, guarde papéis. justify-content sempre cuida de como o espaço se distribui ao longo da fila. align-items sempre cuida de como os itens se assentam na direção perpendicular. Isso continua verdadeiro em qualquer direção."
```

Os valores que resolvem 90% dos casos:

| Propriedade | Valor | Efeito |
|---|---|---|
| `justify-content` | `flex-start` | tudo no começo da fila (padrão) |
| | `center` | tudo no centro da fila |
| | `space-between` | primeiro na ponta, último na outra, espaço dividido no meio |
| `align-items` | `center` | itens centralizados na direção perpendicular |
| | `stretch` | itens esticam para preencher (padrão) |

`space-between` é o valor que constrói barra de navegação do mundo inteiro: nome do produto de um lado, menu do outro, sem você calcular margem nenhuma.

### `gap`: o fim das margens contadas na mão

Antes existia um ritual: dar `margin-right` em todos os links, menos no último — e alguém sempre esquecia o "menos no último", deixando um espaço sobrando na ponta.

`gap` acabou com isso. Ele define o espaço **entre** os itens, e só entre eles: não sobra margem nas bordas.

```css
nav {
  display: flex;
  gap: 24px;
}
```

:::atencao Quando align-items parece não fazer nada
Você escreve `align-items: center` esperando centralizar verticalmente, recarrega, e nada acontece. O CSS está certo. O que falta é **altura**: por padrão o container tem exatamente a altura do conteúdo dele, então não existe espaço vertical sobrando para centralizar coisa alguma — é como pedir para centralizar um quadro numa parede do tamanho exato do quadro. Diagnóstico: dê ao container uma altura (`min-height: 80vh`, por exemplo) e o mesmo `align-items: center` que "não funcionava" passa a funcionar na hora. É a causa número um de aluno concluindo que Flexbox está bugado.
:::

:::curiosidade Centralizar era piada da profissão
Antes do Flexbox, alinhar coisas na web era feito com propriedades pensadas para outra finalidade — `float`, criado para fazer texto contornar imagem, e até tabelas de layout. Centralizar uma caixa **verticalmente** era tão trabalhoso que virou piada interna entre programadores: era o exemplo canônico de "coisa que parece trivial e não é". O Flexbox chegou e transformou isso em duas linhas. Você está aprendendo em quinze minutos o que custou anos de gambiarra a uma geração inteira.
:::

:::dica Flex é para uma dimensão
No mercado, a regra de bolso é essa: **Flexbox para uma direção** — uma barra, uma fila de botões, um item com conteúdo dos dois lados — e **Grid para duas**, quando você precisa de linhas e colunas ao mesmo tempo. Não são rivais; times usam os dois no mesmo arquivo, o tempo todo. É por isso que a próxima aula é sobre Grid: seus três cards de benefício são um caso de duas dimensões, e Flex faria aquilo com mais esforço e menos controle.
:::

## Prática

**Alinhar o topo e o hero (~15 min).** Acrescente ao `estilo.css`, sem apagar o que já existe.

**1. A barra de navegação** — nome à esquerda, links à direita:

```css
header {
  display: flex;
  justify-content: space-between;  /* separa as duas pontas */
  align-items: center;             /* alinha na mesma linha de base visual */
  padding: 16px 24px;
  border-bottom: 1px solid var(--cor-apoio);
}

nav {
  display: flex;
  gap: 24px;
}

nav a {
  color: var(--cor-texto);
  text-decoration: none;
}
```

Note que existem **dois** containers flex aninhados, e cada um resolve um problema: o `header` afasta as duas pontas, o `nav` distribui os links entre si.

**2. O hero centralizado nos dois sentidos:**

```css
#hero {
  display: flex;
  flex-direction: column;    /* a fila agora é de cima para baixo */
  justify-content: center;   /* no eixo principal, que agora é o vertical */
  align-items: center;       /* no eixo cruzado, que agora é o horizontal */
  gap: 16px;
  min-height: 80vh;          /* sem altura não há o que centralizar */
  text-align: center;
}

#hero a {
  background-color: var(--cor-destaque);
  color: #ffffff;
  padding: 14px 28px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
}
```

Este é o bloco em que a troca de eixos acontece de verdade: com `column`, `justify-content` passou a agir na vertical. Compare com o `header` acima, onde o mesmo `justify-content` agia na horizontal. Mesma propriedade, direções opostas — porque a **fila** mudou de sentido.

**3. Teste do wrap (1 min).** Estreite a janela do navegador até os links do menu se espremerem. Agora acrescente `flex-wrap: wrap;` no `nav` e estreite de novo: em vez de espremer, eles passam para a linha de baixo. Guarde isso — é o primeiro passo do responsivo, que é a aula 14.

**Entrega:** página republicada, com topo alinhado e hero centralizado. Confira **no celular**.

## Avaliação

```quiz
- pergunta: Onde se escreve display flex para colocar os links de um menu lado a lado?
  alternativas:
    - texto: Em cada link do menu
    - texto: "No elemento que contém os links, porque é o container que manda em como os filhos diretos se organizam"
      correta: true
    - texto: No body, para valer na página inteira
    - texto: "Nos links e no container, nos dois"
  feedback: >
    Flexbox se aplica ao pai. Os filhos mudam de comportamento sem receber
    propriedade nenhuma — e só os filhos diretos, um neto dentro de outra caixa
    não é item daquele container.
- pergunta: Num container com flex-direction column, o que justify-content passa a controlar?
  alternativas:
    - texto: O alinhamento horizontal, como sempre
    - texto: "O alinhamento vertical, porque com column o eixo principal passou a ser de cima para baixo"
      correta: true
    - texto: Nada, porque justify-content só funciona na direção padrão
    - texto: O espaçamento entre linhas do texto
  feedback: >
    justify-content nunca significou horizontal — significa "ao longo da fila". Com
    column a fila é vertical, então ele age na vertical. Quem decorou a direção em
    vez do papel erra exatamente aqui.
- pergunta: Você escreveu align-items center num container e nada mudou. Qual é a causa mais provável?
  alternativas:
    - texto: A propriedade precisa vir antes de display flex
    - texto: "O container não tem altura definida, então não sobra espaço no eixo cruzado para centralizar"
      correta: true
    - texto: align-items só funciona com flex-direction column
    - texto: Falta aplicar align-items também nos itens filhos
  feedback: >
    Sem altura, o container mede exatamente o conteúdo — não há folga para
    distribuir. Definir min-height faz o mesmo align-items passar a funcionar
    sem trocar mais nada.
```

## Fechamento

O que ficou de hoje:

- **`display: flex` vai no pai.** Os filhos diretos viram itens sem receber nada.
- **`justify-content` age ao longo da fila; `align-items` age na direção perpendicular.** Guarde os papéis, não as direções — `flex-direction: column` inverte tudo.
- **`space-between`** monta barra de navegação do mundo inteiro em uma linha.
- **`gap`** substitui margens contadas na mão e não sobra espaço nas pontas.
- **Sem altura não há centralização vertical.** É o falso bug mais comum do Flexbox.

**Próxima aula:** o topo e o hero estão resolvidos, mas os três benefícios continuam empilhados um debaixo do outro, como uma lista. Eles precisam virar **três cards lado a lado** — e é aí que Flexbox deixa de ser a ferramenta certa. Entra o **Grid**, com um truque que faz os cards se reorganizarem sozinhos em telas estreitas, sem uma linha de código extra.

:::roteiro
Comece pelo problema, não pela ferramenta: mostre o topo empilhado da página deles no projetor e pergunte como colocariam o menu à direita. Vai aparecer sugestão de margem gigante e de espaço em branco no HTML — deixe aparecer, é o contraste que faz `space-between` valer.

Insista na regra do pai. Vai ter aluno escrevendo `display: flex` no `<a>`. Corrija sempre com a mesma frase: "quem manda é quem contém".

O diagrama dos eixos é o miolo da aula. Faça ao vivo: monte a fila horizontal, aplique `justify-content: center`, e então troque para `column` na frente da turma **sem mexer em mais nada** — o conteúdo pula para o outro sentido e a sala reage. É esse susto que impede o vício do "justify é horizontal".

O falso bug do `align-items` vai acontecer sozinho na Prática. Não avise antes: deixe o primeiro aluno chamar e resolva no projetor, para todos, adicionando `min-height`. Aprendido assim, não esquece.

O teste do `flex-wrap` no fim é rápido e planta a aula 14. Se o tempo apertar, corte a estilização do botão, nunca o wrap.

Circule cobrando o teste no celular. Menu que cabe no monitor da sala frequentemente não cabe em 360 pixels.
:::
