---
conceito: Software
slug: software
disciplina: introducao-a-computacao
tipo: conceito
aka: []
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 23_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 35_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 38_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [23, 35, 38]
atualizado_em: 2026-09-22
---

Software é o conjunto de programas e instruções que dizem ao [[hardware]] o que fazer. Enquanto o hardware oferece capacidade física — processamento, memória, armazenamento, dispositivos —, o software organiza essa capacidade em tarefa útil: é o que "dá vida" a um computador desligado ou parado, pedindo recursos e coordenando o funcionamento de tudo.

## Em uma frase

Software é o conjunto de instruções que transforma a capacidade física do hardware em tarefa útil.

## O que precisa saber

Os programas se dividem em duas categorias: software de aplicação — o que o usuário abre diretamente, como navegador, editor de texto ou jogo — e [[software-de-base]], cuja função é controlar o hardware e dar suporte aos demais programas. O [[sistema-operacional]] é o principal software de base: todo software de aplicação roda em cima dele, e sem essa camada intermediária os aplicativos não teriam onde funcionar. Um programa, antes de ser executado, precisa ser traduzido para [[linguagem-de-maquina]] — pelo trabalho de um [[compilador]] ou [[interpretador]] — e depois sobe do [[armazenamento-secundario]] para a [[memoria-ram]], de onde a [[cpu]] o executa.

## Erros comuns

- Achar que hardware bom garante um sistema útil sozinho — sem software, nenhuma capacidade física vira tarefa.
- Confundir "os programas que vêm instalados" (aplicações) com o sistema operacional: aplicações rodam em cima do SO, não são o SO.
- Tratar software como algo abstrato demais, esquecendo que ele sempre depende de tradução (compilação ou interpretação) para virar instruções executáveis pela CPU.

## Onde aparece

- Aula 23 — *Introdução à Arquitetura de Computadores - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/23-introducao-a-arquitetura-de-computadores-parte-1/canonica.md`
- Aula 35 — *Sistema Operacional - Conceito e Estrutura* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/35-sistema-operacional-conceito-e-estrutura/canonica.md`
- Aula 38 — *O Que é um Sistema Operacional - Definição e Onde Vivem* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/38-o-que-e-um-sistema-operacional/canonica.md`
- Conceitos vizinhos: [[hardware]], [[software-de-base]], [[sistema-operacional]], [[compilador]], [[interpretador]]

## Fontes

- Definição de software e sua dependência do hardware: slides SEED da Aula 23.
- Software como camada acima do sistema operacional: slides SEED da Aula 35.
- Definição madura de software de base versus software de aplicação: slides SEED da Aula 38.
