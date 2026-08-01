---
conceito: useEffect
slug: use-effect
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [React useEffect]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/25 - Aula 25 - Gerenciamento Ciclos de Vida de Componentes_ Classes e Hooks I - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/27 - Aula 27 - Gerenciamento Ciclos de Vida de Componentes_ Classes e Hooks III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

`useEffect` é o hook do React para sincronizar um componente com sistemas externos, como rede, temporizadores, assinaturas ou APIs do navegador. Ele pode executar uma função de limpeza e depende de uma lista de dependências que descreve quando a sincronização precisa ser refeita.

## Em uma frase

`useEffect` sincroniza o componente com efeitos que vivem fora da renderização pura.

## O que precisa saber

Um efeito deve representar uma sincronização, não o cálculo de um valor derivável durante a renderização. Dependências corretas evitam leituras obsoletas e loops; a limpeza desfaz inscrições e recursos. O modelo se relaciona ao [[ciclo-de-vida-de-componente]], mas não é apenas uma tradução de métodos de classe.

## Erros comuns

- Omitir dependências para silenciar um aviso.
- Criar efeito para encadear estado derivável.
- Esquecer limpeza de timer, listener ou assinatura.

## Onde aparece

- Projeto Front-End e Desenvolvimento Web, Aulas 25 e 27, páginas 2–5.
- Relaciona-se a [[hooks-react]], [[react]], [[ciclo-de-vida-de-componente]] e [[state]].

## Fontes

- Projeto Front-End e Desenvolvimento Web, Aulas 25 e 27, slides sobre ciclo de vida e efeitos.
