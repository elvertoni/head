---
conceito: Autorrelacionamento
slug: autorrelacionamento
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [relacionamento recursivo]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/13 - Aula 13 - Relacionamentos II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Autorrelacionamento é um relacionamento que liga instâncias da mesma entidade, usando papéis diferentes para distinguir a participação de cada lado. Uma entidade Funcionário pode, por exemplo, relacionar-se consigo mesma para representar quem supervisiona quem.

## Em uma frase

Autorrelacionamento conecta instâncias de uma entidade por papéis distintos.

## O que precisa saber

Os papéis tornam explícita a direção e o significado de cada participação; sem eles, o diagrama pode ser ambíguo. Cardinalidade e [[multiplicidade]] continuam necessárias para expressar quantas instâncias podem participar. Ao mapear para o [[modelo-relacional]], a chave estrangeira costuma referenciar a própria tabela.

## Erros comuns

- Desenhar a ligação sem nomear os papéis.
- Confundir autorrelacionamento com entidade associativa.
- Omitir condição de término em hierarquias recursivas.

## Onde aparece

- Modelagem de Banco de Dados, Aula 13, páginas 2–3.
- Relaciona-se a [[relacionamento]], [[cardinalidade]], [[multiplicidade]] e [[modelo-relacional]].

## Fontes

- Modelagem de Banco de Dados, Aula 13, slides sobre relacionamentos recursivos.
