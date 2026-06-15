---
titulo: RAG — Recuperação com Geração Aumentada
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [Context Engineering, Treino, Fine-tuning e Cutoff]
objetivos:
  - Explicar o que é RAG e o problema que ele resolve
  - Diferenciar RAG de fine-tuning
  - Reconhecer as duas metades do RAG - ingestão e consulta
trilha: fundamentos-de-ia
ordem: 16
modo_origem: material
fontes:
  - lake/inteligencia-artificial/ia-master
  - lake/inteligencia-artificial/elite-wiki/arquitetura/blueprint-sistema-rag-para-suporte-a-alunos.md
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Imagine um assistente de estudos que respondesse dúvidas dos alunos com base **no material da sua escola** — as apostilas, os PDFs, o regulamento. O problema da Aula 12 já apareceu: o [[llm]] não conhece esse material (ele parou no [[cutoff]] e nunca viu os seus documentos). E a Aula 15 deu a pista: é preciso **colocar o material no contexto**. Mas se a apostila tem 300 páginas, você não cola tudo. A solução elegante para isso é a estrela deste módulo: **RAG**. Ela busca só os trechos certos e entrega ao modelo na hora da pergunta.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que é **RAG** e o **problema** que ele resolve.
- Diferenciar **RAG de fine-tuning**.
- Reconhecer as duas metades do RAG: **ingestão** e **consulta**.

## Pré-requisitos

Ter visto a **Aula 15** (context engineering) e a **Aula 12** (cutoff).

## Desenvolvimento

### O que é RAG

:::conceito RAG (Retrieval-Augmented Generation)
É a técnica de **buscar os trechos certos** de um acervo (apostilas, PDFs, documentação) e **entregá-los ao [[llm]] junto com a pergunta**, para ele responder com base nesse material — e não só pela memória do treino. "Recuperação com geração aumentada": primeiro **recupera** o trecho relevante, depois o modelo **gera** a resposta apoiado nele.

:::

RAG resolve as duas dores que você já conhece: o modelo não sabe o que é recente (cutoff) e não conhece o **seu** conteúdo específico. Em vez de esperar que ele "saiba", você entrega o que ele precisa, na hora.

:::atencao Erro comum
"RAG treina o modelo / ensina coisas novas pra ele." Não. O RAG **não muda** nada nos pesos do modelo — ele apenas **monta o contexto** com o trecho certo na hora da pergunta. É a diferença da Aula 12: [[fine-tuning]] muda o modelo (treino); RAG só fornece informação no contexto. Por isso o RAG é **barato**, rápido de atualizar e **auditável** — você sabe de qual documento veio a resposta.

:::

### As duas metades

```diagrama-progressivo
titulo: Como o RAG funciona
camadas:
  - rotulo: 1. Ingestão (uma vez, antes)
    conteudo: O acervo é preparado - quebrado em pedaços, transformado em vetores e guardado num banco de busca. É a engenharia da próxima aula (chunking, embeddings, vector store).
  - rotulo: 2. Pergunta chega
    conteudo: O aluno pergunta "qual o prazo do trabalho?". A pergunta também vira vetor.
  - rotulo: 3. Recuperação
    conteudo: O sistema busca no banco os trechos mais parecidos com a pergunta (por significado, não por palavra exata) e pega os melhores.
  - rotulo: 4. Geração aumentada
    conteudo: Esses trechos entram no contexto junto com a pergunta. O LLM gera a resposta apoiado neles - e pode até citar a fonte.
```

:::dica Por que RAG e não fine-tuning?
Para a maioria dos casos de "dar conhecimento ao modelo", o RAG ganha: o fine-tuning é caro, lento e, toda vez que o material muda, você teria que retreinar. Com RAG, basta atualizar o acervo — a resposta acompanha. E você sempre sabe **de onde** veio a informação, o que é essencial em educação, saúde e direito. É uma das arquiteturas de IA mais usadas no mercado hoje; entendê-la abre muitas portas.

:::

## Prática

**Atividade "RAG humano" (em grupos de 4, sem computador, ~15 min).** O grupo vai simular um assistente RAG.

1. **Ingestão:** preparem **8 fichas** de papel, cada uma com um fato sobre a escola (um por ficha): horário, prazo de trabalhos, regra de atraso, uniforme, cantina, biblioteca, recuperação, transporte.
2. Um aluno é o **"usuário"** e faz uma pergunta (ex.: "posso entregar atrasado?").
3. Outro é o **"recuperador"**: sem decorar nada, ele **busca** entre as 8 fichas a(s) mais relevante(s) à pergunta e entrega.
4. Um terceiro é o **"LLM"**: responde a pergunta usando **só** as fichas recebidas, e **cita** de qual ficha tirou.
5. Repitam com uma pergunta cuja resposta **não** está em nenhuma ficha. O que o "LLM" deve fazer? (resposta: dizer que não há informação — não inventar.)

Discussão: o que mudou em relação a responder "de cabeça"? Por que citar a ficha é tão valioso?

## Avaliação

```quiz
- pergunta: O que o RAG faz?
  alternativas:
    - texto: Retreina o modelo com dados novos
    - texto: Busca trechos relevantes de um acervo e os entrega ao modelo junto com a pergunta
      correta: true
    - texto: Aumenta a velocidade do computador
    - texto: Apaga o conhecimento antigo do modelo
  feedback: >
    RAG recupera o trecho certo e o injeta no contexto. O modelo gera a resposta
    apoiado nele — sem mudar seus pesos.
- pergunta: Qual a diferença entre RAG e fine-tuning?
  alternativas:
    - texto: São a mesma coisa
    - texto: Fine-tuning muda o modelo (treino); RAG só fornece informação no contexto
      correta: true
    - texto: RAG é mais caro e lento que fine-tuning
    - texto: Fine-tuning busca trechos de documentos
  feedback: >
    RAG não altera o modelo — monta o contexto com o trecho certo. É barato, atualizável
    e auditável; fine-tuning retreina o modelo.
- pergunta: Por que RAG é considerado "auditável"?
  alternativas:
    - texto: Porque é caro
    - texto: Porque você sabe de qual documento veio a resposta
      correta: true
    - texto: Porque ninguém consegue ver como funciona
    - texto: Porque não usa documentos
  feedback: >
    Como a resposta se apoia em trechos recuperados, dá pra citar a fonte e conferir —
    essencial em educação, saúde e direito.
```

## Fechamento

Hoje você descobriu que:

- **[[rag|RAG]]** busca os trechos certos de um acervo e os entrega ao [[llm]] junto com a pergunta.
- Ele resolve o **[[cutoff]]** e o desconhecimento do **seu** material — sem retreinar.
- **RAG ≠ [[fine-tuning]]**: RAG fornece contexto; fine-tuning muda o modelo.
- RAG é **barato, atualizável e auditável** (você sabe a fonte da resposta).

**Próxima aula:** falamos que a ingestão "quebra, vetoriza e guarda" o acervo. Como isso funciona por dentro? Fechamos o módulo com **chunking, embeddings e vector stores** — a engrenagem do RAG.

:::roteiro
Vem de material do ia-master + blueprint da elite-wiki (modo Material). Abrir com o assistente de estudos da própria escola — concreto e desejável. Amarre forte com aulas 12 (cutoff) e 15 (contexto): RAG é a automação de "colocar o material certo no contexto". O erro "RAG treina o modelo" é o conceito-chave; contraste com fine-tuning. A prática "RAG humano" com fichas é excelente — o passo 5 (pergunta sem resposta) ensina a não alucinar (gancho aula 23). Citar a fonte = auditabilidade. 8 min pro quiz.
:::
