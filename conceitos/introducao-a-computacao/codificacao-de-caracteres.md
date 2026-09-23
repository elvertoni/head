---
conceito: Codificação de caracteres
slug: codificacao-de-caracteres
disciplina: introducao-a-computacao
tipo: conceito
aka: [ASCII, Unicode]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 33_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [33]
atualizado_em: 2026-09-22
---

Codificação de caracteres é o padrão que atribui um número a cada caractere, número esse guardado como qualquer outro em binário. A tabela ASCII, por exemplo, associa a letra 'A' ao número 65; o Unicode é uma tabela muito maior, que cobre praticamente todos os alfabetos, símbolos e emojis do mundo.

## Em uma frase

Codificação de caracteres é a tabela que converte cada letra ou símbolo em um número, guardado depois em binário.

## O que precisa saber

Um mesmo padrão de [[bit]]s — por exemplo `01000001` — pode significar o número 65 ou a letra 'A'. Quem decide qual dos dois é não é o bit, é a interpretação: o programa define se aquela posição da memória deve ser lida como número ou como caractere, e só então consulta a tabela de codificação para traduzir. A tabela ASCII usa 1 [[byte]] por caractere no exemplo trabalhado em aula; ela é suficiente para o alfabeto latino básico, mas pequena demais para outros alfabetos, símbolos técnicos e emojis — daí a necessidade do Unicode, muito mais amplo. A codificação é, portanto, mais uma convenção de leitura sobre o [[sistema-binario]] do que uma técnica de armazenamento em si.

## Erros comuns

- Achar que um bloco de bits "sabe" sozinho se é número ou letra — a interpretação depende do tipo de dado esperado pelo programa naquela posição, não do bit.
- Ignorar que texto pode ser salvo com uma tabela e lido com outra: é essa incompatibilidade que produz caracteres quebrados como "Ã§" no lugar de "ç", erro comum em sites, bancos de dados e arquivos.
- Supor que ASCII basta para qualquer idioma ou símbolo — ela cobre só o alfabeto latino básico; alfabetos maiores, acentuação ampla e emojis exigem Unicode.

## Onde aparece

- Aula 33 — *Como os Dados Viram Binário - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/33-como-os-dados-viram-binario-parte-1/canonica.md`
- Conceitos vizinhos: [[bit]], [[byte]], [[sistema-binario]]

## Fontes

- Definição de codificação de caracteres, exemplo ASCII ('A' = 65) e o alerta sobre choque de codificação ("Ã§"/"ç"): slides SEED da aula 33 (`lake/introducao-a-computacao/AULA 33_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da aula 33 (blocos `:::conceito Codificação de caracteres (ASCII e Unicode)` e `:::dica Por que isso aparece quando você menos espera`).
