---
conceito: Pull Request (PR)
slug: pull-request
disciplina: programacao-front-end
tipo: conceito
aka: [PR, pedido de pull]
status: rascunho
fontes: []
aulas: [5, 6]
atualizado_em: 2026-09-24
---

Um Pull Request é um pedido formal para que os commits de uma [[branch]] sejam trazidos para outra (geralmente para `main`) — mas, ao contrário de um [[merge]] direto, o PR abre um espaço de conversa antes disso acontecer. O [[github|GitHub]] mostra o diff automaticamente, permite comentários em linhas específicas do código, e só depois de aprovado alguém aperta o botão de merge.

## Em uma frase

O Pull Request cria um espaço de revisão e conversa antes do merge acontecer, em vez de empurrar a mudança direto para a branch principal.

## O que precisa saber

Um bom PR tem título e descrição claros — o quê mudou e por quê — porque PR sem descrição obriga quem revisa a adivinhar a intenção lendo código frio. Mensagens de commit no padrão **Conventional Commits** (`feat:`, `fix:`, `docs:`, `chore:`...) tornam o histórico legível em vez de uma lista de "ajustes". Hoje a revisão de código já conta com apoio de IA (Copilot), que adianta parte do trabalho repetitivo, mas a aprovação final continua humana.

## Erros comuns

- Fazer merge direto na `main` sem passar por revisão, deixando erro de digitação, lógica errada ou `console.log` esquecido entrar sem ninguém ver antes.
- Escrever `fix: corrigido` ou `feat: mudanças` — o prefixo classifica a intenção, mas a frase ainda precisa dizer o quê mudou.

## Onde aparece

- Aula 5 — *Pull Request: como propor uma mudança sem simplesmente sobrescrever o código de alguém* `aulas/programacao-front-end/controle-de-versao-git-github/05-pull-request-e-revisao-de-codigo/canonica.md`
- Aula 6 — *GitHub Pages: transformando seu repositório num site que qualquer pessoa acessa* `aulas/programacao-front-end/controle-de-versao-git-github/06-deploy-com-github-pages/canonica.md`
- Conceitos vizinhos: [[github]], [[branch]], [[merge]], [[github-flow]]

## Fontes

- Conteúdo autoral da Aula 5 (modo_origem: tema), sem fonte externa direta — abertura de PR, Conventional Commits e revisão de código assistida por IA.
