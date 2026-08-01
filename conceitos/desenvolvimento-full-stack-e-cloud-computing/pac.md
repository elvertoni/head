---
conceito: PAC
slug: pac
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Presentation-Abstraction-Control]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/17 - Aula 17 - Uso de MVC como Padrão de Projeto II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

PAC é um padrão que separa apresentação, abstração e controle, organizando comunicação entre a interface, o conhecimento do domínio e a coordenação. Ele oferece uma alternativa de decomposição para sistemas interativos.

## Em uma frase

PAC separa interface, conhecimento e coordenação em agentes colaborativos.

## O que precisa saber

O controlador coordena relações entre apresentação e abstração, e a estrutura pode ser hierárquica. A escolha deve ser comparada com [[mvc]] e [[arquitetura-em-camadas]].

## Erros comuns

- Confundir PAC com simples divisão de pastas.
- Criar controladores que concentram toda a regra do sistema.
- Ignorar custo de sincronização entre agentes.

## Onde aparece

- Frameworks e Aplicações, Aula 17, página 2.
- Relaciona-se a [[mvc]], [[arquitetura-em-camadas]] e [[padroes-arquiteturais]].

## Fontes

- Aula 17, página 2 dos slides: padrão PAC.
