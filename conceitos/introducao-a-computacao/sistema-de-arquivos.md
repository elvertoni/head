---
conceito: Sistema de arquivos
slug: sistema-de-arquivos
disciplina: introducao-a-computacao
tipo: conceito
aka: [file system]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/rco/2tri/37-o-que-e-um-sistema-operacional.md"
aulas: [37]
atualizado_em: 2026-09-22
---

É a forma como o [[sistema-operacional]] organiza o armazenamento em arquivos e pastas, com nomes, locais e permissões. Sem ele, o disco seria um mar de bits sem nenhuma ordem; com ele, o usuário localiza um arquivo pelo nome, dentro de uma pasta, em segundos.

## Em uma frase

A camada do sistema operacional que organiza o disco em arquivos e pastas com nome e localização.

## O que precisa saber

É uma das quatro funções que fazem o [[sistema-operacional]] transformar [[hardware]] bruto em algo usável, ao lado da [[gerencia-de-memoria]], do escalonamento de [[processo|processos]] e dos [[driver|drivers]]. Na prática, toda vez que o usuário cria uma pasta, renomeia um arquivo, salva um documento ou o move para a lixeira, é o sistema de arquivos trabalhando por baixo. A distinção importante é entre o disco físico — o [[armazenamento-secundario]], que só guarda sequências de bits — e o sistema de arquivos, que é a abstração lógica organizada por cima dele; um mesmo dispositivo de armazenamento pode ser formatado com sistemas de arquivos diferentes, cada um com suas próprias regras de nomes, locais e permissões.

## Erros comuns

- Confundir "sistema de arquivos" com o disco em si: o disco é o hardware; o sistema de arquivos é a organização lógica que o SO impõe sobre ele.
- Achar que um arquivo "desapareceu magicamente": na maioria dos casos é um problema de localização (pasta errada, permissão, exclusão) dentro do sistema de arquivos, não perda física de dados.

## Onde aparece

- Aula 37 — *O Que o Sistema Operacional Faz por Você* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/37-o-que-o-sistema-operacional-faz-por-voce/canonica.md`
- Conceitos vizinhos: [[sistema-operacional]], [[armazenamento-secundario]], [[gerencia-de-memoria]]

## Fontes

- Definição da função e exemplos cotidianos (criar pasta, salvar arquivo): base da canônica aprovada da Aula 37, apoiada na extração RCO (`lake/introducao-a-computacao/rco/2tri/37-o-que-e-um-sistema-operacional.md`), que cita "organizar os arquivos e pastas" entre as funções do SO no estudo de caso da prática.
