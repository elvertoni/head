---
conceito: Funções construtoras
slug: funcoes-construtoras
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [constructor functions]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/03 - Aula 3 - Funções - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Funções construtoras são funções JavaScript projetadas para serem chamadas com `new`, criando um novo objeto e associando-lhe um protótipo. Elas formam um padrão histórico de instanciação; classes modernas oferecem outra sintaxe para organizar o mesmo modelo prototipal.

## Em uma frase

Funções construtoras criam objetos quando invocadas com `new`.

## O que precisa saber

Ao usar `new`, o JavaScript cria um objeto, liga seu protótipo à propriedade `prototype` da função e executa o corpo com `this` apontando para a nova instância. Uma função de flecha não pode ser usada como construtora. O padrão deve ser aplicado com convenções claras.

## Erros comuns

- Esquecer `new` e alterar o contexto ou produzir resultado inesperado.
- Confundir a propriedade `prototype` da função com o protótipo da instância.
- Criar construtores quando uma abstração simples seria suficiente.

## Onde aparece

- JavaScript e Aplicações Práticas, Aula 3, páginas 5–6.
- Relaciona-se a [[javascript]], [[funcoes-em-javascript]] e [[funcoes-de-flecha]].

## Fontes

- JavaScript e Aplicações Práticas, Aula 3, slides sobre funções e criação de objetos.
