---
titulo: Alucinações — Causas, Tipos e Mitigação
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [O que é um LLM, RAG — Recuperação com Geração Aumentada]
objetivos:
  - Explicar o que é uma alucinação e por que ela acontece
  - Reconhecer tipos comuns de alucinação
  - Aplicar estratégias para reduzir e detectar alucinações
trilha: fundamentos-de-ia
ordem: 23
slug: alucinacoes-causas-tipos-e-mitigacao
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Lá na Aula 09 ficou um aviso no ar: o [[llm]] pode dizer uma coisa **errada com toda a confiança do mundo**. Ele inventa um livro que não existe, cita uma lei falsa, dá uma data errada — tudo com a mesma cara segura de quando acerta. Já houve advogado que entregou ao juiz processos com casos **inventados** pela IA, e alunos que entregaram trabalhos com fontes que nunca existiram. Esse fenômeno tem nome — **alucinação** — e saber lidar com ele é, talvez, a habilidade mais importante de toda esta trilha. Porque não adianta usar IA se você não sabe quando **não** confiar nela.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que é uma **alucinação** e **por que** ela acontece.
- Reconhecer **tipos comuns** de alucinação.
- Aplicar **estratégias** para reduzir e detectar alucinações.

## Pré-requisitos

Ter visto a **Aula 09** (o LLM prevê texto) e a **Aula 16** (RAG).

## Desenvolvimento

### Por que a IA "alucina"

:::conceito Alucinação
É quando um [[llm]] gera uma informação **falsa ou inventada** apresentando-a como verdadeira, com total confiança. Não é "mentira" (não há intenção) nem defeito: é uma **consequência direta** de como o modelo funciona. Lembra da Aula 09? Ele **prevê o texto mais provável**, não consulta um banco de fatos. Quando não "sabe" algo, ele não para — completa com o que **soa** plausível. Às vezes o plausível é verdadeiro; às vezes é pura invenção convincente.

:::

As causas se encadeiam com tudo que você já viu: o modelo prevê probabilidade (não verdade); o conhecimento dele para no [[cutoff]]; e, sem o **contexto** certo, ele preenche o buraco com um chute bem-acabado.

### Tipos comuns

:::importante Onde a alucinação costuma aparecer
- **Fatos inventados:** datas, números, estatísticas que soam certos mas são falsos.
- **Fontes falsas:** livros, artigos, leis ou links que **não existem** — um clássico perigoso.
- **Citações erradas:** atribuir a alguém uma frase que a pessoa nunca disse.
- **Falsa confiança:** o tom é sempre seguro, mesmo quando o conteúdo é inventado — por isso engana.
:::

:::atencao Erro comum
Confiar cegamente porque "a resposta parece certa e bem escrita". A boa escrita do LLM **não** é garantia de verdade — ele é ótimo em soar convincente, lembra? Quanto mais técnico ou específico o assunto (uma lei, um dado, uma fonte), **maior** a chance de alucinação e mais importante **conferir**. Texto bonito não é prova.

:::

### Como reduzir e detectar

Você já aprendeu as ferramentas certas ao longo da trilha — agora elas se juntam:

```diagrama-progressivo
titulo: Estratégias contra alucinação
camadas:
  - rotulo: 1. Dar contexto (RAG)
    conteudo: Forneça o material certo no contexto, ou use RAG (Aula 16). Com a fonte real à mão, o modelo não precisa inventar.
  - rotulo: 2. Pedir a fonte
    conteudo: Peça que ele cite de onde tirou a informação - e então confira se a fonte existe e diz aquilo mesmo.
  - rotulo: 3. Usar ferramentas
    conteudo: Para contas, uma calculadora; para fatos recentes, uma busca (Aula 19). Ferramentas trazem a verdade que o modelo não tem.
  - rotulo: 4. Verificar sempre
    conteudo: A regra de ouro: trate a resposta como um rascunho de um colega esperto, mas distraído. Confira o que importa antes de usar.
```

:::dica Verificar é a habilidade profissional do futuro
Aqui está o que separa quem usa IA com competência de quem se dá mal: **nunca entregar uma saída de IA sem revisar**. Médicos, advogados, engenheiros e programadores que usam IA com responsabilidade têm todos o mesmo hábito — confiar, mas verificar. Essa disciplina de revisão é, provavelmente, a habilidade mais valiosa que esta trilha te dá. A IA é uma estagiária brilhante e veloz, mas que às vezes inventa: você é quem assina embaixo.

:::

## Prática

**Atividade "caça à alucinação" (em duplas, sem computador, ~15 min).**

Aqui estão 4 "respostas de IA". Para cada uma, a dupla decide: **confiável** ou **suspeita de alucinação**? E **como verificariam**?

1. "A capital da França é Paris."
2. "Segundo o livro *Redes Quânticas Aplicadas* (2019), de Maria Albertina Souza, o 5G usa entrelaçamento."
3. "A fórmula da água é H₂O."
4. "O time X venceu o campeonato deste mês por 3 a 1." (sobre um evento recentíssimo)

Para cada uma:
- É o tipo de coisa que o modelo **sabe bem** ou que costuma **alucinar**?
- Que **estratégia** da aula vocês usariam para conferir?

Discussão: qual resposta é a **mais perigosa** — a obviamente errada ou a que parece certíssima mas é inventada? Por quê?

## Avaliação

```quiz
- pergunta: Por que um LLM alucina?
  alternativas:
    - texto: Porque está com defeito
    - texto: Porque prevê o texto mais provável, não consulta fatos — e completa o que soa plausível
      correta: true
    - texto: Porque mente de propósito
    - texto: Porque ficou sem memória RAM
  feedback: >
    Alucinação é consequência de como o LLM funciona: ele gera o provável, não o
    verdadeiro. Sem saber, completa com algo que soa convincente.
- pergunta: Qual tipo de alucinação é especialmente perigoso?
  alternativas:
    - texto: Erros óbvios e absurdos
    - texto: Fontes e citações falsas que parecem reais (livros, leis, links que não existem)
      correta: true
    - texto: Respostas muito curtas
    - texto: Respostas em outro idioma
  feedback: >
    Fontes falsas são perigosas porque soam legítimas. Já houve advogados punidos por
    citar casos inventados pela IA. Sempre confira se a fonte existe.
- pergunta: Qual destas NÃO é uma boa estratégia contra alucinação?
  alternativas:
    - texto: Confiar porque a resposta está bem escrita
      correta: true
    - texto: Fornecer contexto/usar RAG
    - texto: Pedir a fonte e conferir
    - texto: Usar ferramentas (busca, calculadora) e verificar
  feedback: >
    Texto bem escrito não é prova de verdade — o LLM é ótimo em soar convincente. As
    outras três (contexto, fonte, ferramentas + verificação) reduzem alucinação.
```

## Fechamento

Hoje você descobriu que:

- **[[alucinacoes|Alucinação]]** é o LLM gerar informação falsa com confiança — consequência de **prever o provável**, não consultar fatos.
- Tipos comuns: **fatos inventados, fontes falsas, citações erradas** — sempre com tom seguro.
- Reduz-se com **contexto/[[rag|RAG]], pedir a fonte, usar ferramentas** — e **verificar sempre**.
- **Texto bonito não é prova.** Confiar, mas verificar, é a habilidade-chave.

**Próxima aula:** se a IA pode errar, como **medir** se ela está boa o bastante? E como controlar o **custo** de usá-la? Na Aula 24: **evals e economia de tokens**.

:::roteiro
Esta é, talvez, a aula mais importante da trilha para a vida real. Abrir com o caso do advogado que citou processos inventados (real e marcante). O conceito-chave: alucinação não é bug, é consequência de "prever o provável" (volta à aula 9). O erro "está bem escrito, logo é verdade" é o alvo central. O diagrama amarra as ferramentas da trilha (RAG, fonte, tools) como mitigações — mostre que tudo se conecta. A `:::dica` "confiar mas verificar" é a lição que eles devem levar para a vida. A caça à alucinação (item 2, fonte falsa convincente) é o ápice. 8 min pro quiz.
:::
