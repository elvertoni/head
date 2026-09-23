---
conceito: Memória cache
slug: memoria-cache
disciplina: introducao-a-computacao
tipo: conceito
aka: [cache]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 31_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 32_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [31, 32]
atualizado_em: 2026-09-22
---

Memória cache é uma memória muito rápida e pequena, localizada dentro ou bem perto do processador, que guarda os dados e instruções que a [[cpu]] usa com mais frequência. Funciona como ponte entre a CPU e a [[memoria-ram|RAM]]: como a CPU é rápida demais para esperar a RAM a cada acesso, a cache antecipa o que provavelmente será pedido de novo em breve.

## Em uma frase

Cache é uma memória minúscula e velocíssima, perto da CPU, que guarda o que se usa com mais frequência.

## O que precisa saber

Quando a CPU precisa de um dado, procura primeiro na cache. Se encontra (cache hit), o acesso é quase instantâneo; se não encontra (cache miss), busca na RAM — mais lenta — e costuma copiar o dado para a cache, prevendo reuso próximo. A cache é rápida porque usa tecnologia mais cara, e é justamente esse custo que a mantém pequena de propósito: ela não substitui a RAM nem o disco, trabalha em parceria com eles, guardando só o pouco que é usado muito. O mesmo princípio aparece fora do processador, como na cache de navegador, que acelera o carregamento de páginas já visitadas. A cache ocupa o topo da [[hierarquia-de-memoria]], sendo a camada mais rápida, menor e mais cara de todas.

## Erros comuns

- Achar que a cache substitui a RAM ou o disco, ou que aumentar a cache resolveria qualquer problema de desempenho.
- Ignorar que a cache é pequena por design (é cara), não por limitação técnica superável.
- Não relacionar "limpar o cache" do navegador com o mesmo princípio da cache de CPU — guardar perto o que se usa muito, para não buscar longe toda vez.

## Onde aparece

- Aula 31 — *A Memória do Computador - Parte 1 - a Cache* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/31-memoria-do-computador-parte-1-a-cache/canonica.md`
- Aula 32 — *A Memória do Computador - Parte 2 - a Hierarquia* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/32-memoria-do-computador-parte-2-a-hierarquia/canonica.md`
- Conceitos vizinhos: [[hierarquia-de-memoria]], [[memoria-ram]], [[cpu]]

## Fontes

- Definição de cache, cache hit/cache miss e o exemplo da cache do navegador: slides SEED da Aula 31 (`lake/introducao-a-computacao/AULA 31_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da Aula 31.
- Posição da cache no topo da hierarquia de memória, em contraste com RAM, disco e nuvem: slides SEED da Aula 32 (`lake/introducao-a-computacao/AULA 32_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da Aula 32.
