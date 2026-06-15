---
titulo: Planejamento em Scrum — visão integrada
tema: Metodologias Ágeis
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: [Planejamento de Releases]
objetivos:
  - Relacionar papéis, eventos e artefatos numa visão integrada do Scrum
  - Explicar os três pilares — transparência, inspeção e adaptação
  - Reconhecer benefícios e desafios reais de adotar o Scrum
trilha: metodologias-ageis
ordem: 39
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/AULA 39_ANÁLISE E MÉTODO PARA SISTEMAS.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Até agora você viu as peças do Scrum separadas: os papéis, as cerimônias, os artefatos, os épicos, a priorização, as releases. É como ter aprendido cada peça de um quebra-cabeça sozinha. Hoje a gente monta a imagem inteira — e, mais importante, faz uma pergunta que pouca aula faz: o Scrum é tão perfeito assim? Resposta honesta: não. Ele resolve muita coisa, mas tem desafios reais. Saber os dois lados é o que separa quem decora o Scrum de quem entende o Scrum.

## Objetivos

Ao final desta aula, você será capaz de:

- Relacionar **papéis, eventos e artefatos** numa visão integrada do Scrum.
- Explicar os **três pilares**: transparência, inspeção e adaptação.
- Reconhecer **benefícios e desafios** reais de adotar o Scrum.

## Pré-requisitos

Ter visto as **Aulas 34 a 38** (papéis, cerimônias, artefatos, épicos, backlog e releases).

## Desenvolvimento

### O Scrum em uma foto

O Scrum se sustenta sobre três tipos de peça, que você já conhece separadas:

| Tipo | Peças | Para quê |
|---|---|---|
| **Papéis** | Product Owner, Scrum Master, Equipe | quem faz |
| **Eventos** | Sprint, Planning, Daily, Review, Retrospectiva | quando e como o time se organiza |
| **Artefatos** | Product Backlog, Sprint Backlog, incremento | o que guia e o que se entrega |

Juntas, essas peças formam um ciclo que se repete a cada sprint: planeja-se, executa-se acompanhando de perto, entrega-se um incremento e reflete-se para melhorar.

### Os três pilares

Por baixo de tudo, o Scrum se apoia em três pilares. São eles que explicam **por que** o framework funciona:

```diagrama-progressivo
titulo: Os três pilares do Scrum
camadas:
  - rotulo: 1. Transparência
    conteudo: Todos enxergam o mesmo: o backlog é aberto, o progresso é visível. Sem informação escondida, ninguém decide no escuro.
  - rotulo: 2. Inspeção
    conteudo: O time examina com frequência tanto o produto quanto o próprio processo (na Review e na Retrospectiva). Olha de verdade para o que está acontecendo.
  - rotulo: 3. Adaptação
    conteudo: Com base no que inspecionou, ajusta o rumo — muda o backlog, as prioridades, as práticas. É a resposta à mudança que define a agilidade.
```

Repare: é o mesmo ciclo de mostrar → olhar → corrigir que apareceu desde a primeira aula. Os pilares são a alma; as cerimônias e artefatos são só o corpo que os sustenta.

### Os dois lados da moeda

:::importante Scrum não é bala de prata
**Benefícios:** adapta-se rápido à mudança, promove melhoria contínua, entrega valor com frequência e melhora a colaboração. **Desafios:** há resistência de quem está acostumado ao jeito tradicional; a falta de experiência leva a aplicar o Scrum errado; estimar e planejar a longo prazo fica mais difícil; e tudo depende de um time **comprometido e autogerenciado**. O Scrum dá o esqueleto — o sucesso depende das pessoas que o vestem.

:::

:::atencao Erro comum
Achar que "adotar o Scrum resolve tudo sozinho". Empresas implantam Scrum esperando mágica e se frustram quando os problemas continuam. O framework só funciona se o time abraçar os pilares de verdade — transparência exige honestidade, inspeção exige tempo, adaptação exige humildade para mudar. Sem isso, vira teatro de reuniões.

:::

:::dica Pensamento crítico vale mais que decoreba
Numa entrevista, qualquer um recita "PO, SM, Dev". Quem impressiona é quem sabe dizer **quando o Scrum não é a melhor escolha** e quais desafios esperar. Entender os dois lados mostra maturidade profissional — e é isso que esta aula te dá.

:::

## Prática

**Atividade "diagnóstico do time" (em duplas, sem computador, ~15 min).** Leiam estes três casos de times com problemas e, para cada um, identifiquem **qual pilar está sendo violado** (transparência, inspeção ou adaptação) e o que fazer:

1. *"O time descobre os problemas só no fim da sprint, nunca durante."*
2. *"O Product Backlog fica num caderno do PO; ninguém mais sabe o que vem por aí."*
3. *"Toda Retrospectiva aponta os mesmos erros, mas nada muda na sprint seguinte."*

Para cada caso: qual pilar falhou? Que prática do Scrum corrigiria?

Cada dupla apresenta o diagnóstico de um caso. A turma confere: o pilar identificado bate?

## Avaliação

```quiz
- pergunta: Quais são os três pilares do Scrum?
  alternativas:
    - texto: Velocidade, lucro e documentação
    - texto: Transparência, inspeção e adaptação
      correta: true
    - texto: Planning, Daily e Review
    - texto: PO, SM e Equipe
  feedback: >
    Transparência (todos enxergam), inspeção (olhar com frequência) e adaptação
    (ajustar o rumo) são a base que faz o Scrum funcionar.
- pergunta: Qual destes é um DESAFIO real de adotar o Scrum?
  alternativas:
    - texto: Resistência de quem está acostumado ao método tradicional
      correta: true
    - texto: Entregar valor com frequência
    - texto: Melhorar a colaboração do time
    - texto: Adaptar-se rápido à mudança
  feedback: >
    Os outros são benefícios. A resistência à mudança, a falta de experiência e a
    dificuldade de estimar a longo prazo são desafios reais do Scrum.
- pergunta: Um time faz Retrospectivas, mas nunca muda nada depois. Qual pilar está falhando?
  alternativas:
    - texto: Transparência
    - texto: Adaptação
      correta: true
    - texto: Nenhum, está tudo certo
    - texto: Velocidade
  feedback: >
    Inspecionar sem adaptar é inútil. O time vê os problemas (inspeção) mas não ajusta
    o rumo (adaptação) — o ciclo fica quebrado.
```

## Fechamento

Hoje você descobriu que:

- O Scrum integra **papéis** (quem faz), **eventos** (como se organiza) e **artefatos** (o que guia/entrega) num ciclo que se repete.
- Tudo se apoia em três pilares: **transparência, inspeção e adaptação**.
- O Scrum traz **benefícios** (adaptação, melhoria contínua, entregas frequentes) e **desafios** reais (resistência, falta de experiência, estimativa difícil).
- Scrum **não é bala de prata** — depende de um time comprometido.

**Próxima aula:** vamos descer ao trabalho concreto do time: como escrever o que o usuário precisa de um jeito claro, usando **histórias de usuário**.

:::roteiro
Esta aula corre o risco de repetir 34/35 — o foco É o "porquê" (pilares) e a honestidade dos dois lados, não recontar as peças. A tabela serve só para amarrar o que já viram; não gaste tempo nela. O coração é o "Scrum não é bala de prata": adolescentes adoram a postura crítica, use isso. A prática de diagnóstico por pilar é a avaliação real — o caso 3 (inspeção sem adaptação) é o mais rico. Reforce a `:::dica`: saber quando NÃO usar Scrum impressiona mais que decorar papéis. Alura ("História de usuário") já aponta pra próxima. 8 min pro quiz.
:::
