---
conceito: Hooks do React
slug: hooks-react
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [React Hooks]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/25 - Aula 25 - Gerenciamento Ciclos de Vida de Componentes_ Classes e Hooks I - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/27 - Aula 27 - Gerenciamento Ciclos de Vida de Componentes_ Classes e Hooks III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Hooks do React são APIs que permitem a componentes funcionais acessar estado, efeitos, contexto e outros recursos do modelo React. Eles organizam lógica reutilizável sem depender de classes, mas obedecem regras de chamada e não são funções genéricas para qualquer ambiente.

## Em uma frase

Hooks conectam componentes funcionais a estado, efeitos e contexto do React.

## O que precisa saber

[[use-state]] declara estado local; [[use-effect]] sincroniza o componente com efeitos externos; [[use-context]] lê um valor compartilhado na árvore. Hooks devem ser chamados no topo de componentes ou hooks customizados, em ordem estável. O efeito não deve substituir modelagem de dados ou eventos do domínio.

## Erros comuns

- Chamar hook dentro de condição, loop ou função comum.
- Usar `use-effect` para calcular valor derivável.
- Criar hook customizado que apenas renomeia uma linha sem encapsular comportamento.

## Onde aparece

- Projeto Front-End e Desenvolvimento Web, Aulas 25 e 27, páginas 2–5.
- Relaciona-se a [[react]], [[use-state]], [[use-effect]], [[use-context]] e [[ciclo-de-vida-de-componente]].

## Fontes

- Projeto Front-End e Desenvolvimento Web, Aulas 25 e 27, slides sobre classes, ciclo de vida e hooks.
