---
conceito: GitHub Pages
slug: github-pages
disciplina: programacao-front-end
tipo: entidade
aka: [GH Pages]
status: rascunho
fontes: []
aulas: [6]
atualizado_em: 2026-09-24
---

GitHub Pages é um serviço gratuito do [[github|GitHub]] que pega os arquivos estáticos de um repositório (HTML, CSS, JavaScript) e os coloca no ar, servidos como um site de verdade, num endereço público — sem contratar hospedagem nem configurar servidor. Funciona direto para projetos sem etapa de build: pega os arquivos como estão no repositório e publica.

## Em uma frase

GitHub Pages publica os arquivos estáticos de um repositório num link público, sem hospedagem paga.

## O que precisa saber

A ativação é toda por interface — Settings → Pages → Deploy from a branch → escolher `main` — e a partir daí todo `push` atualiza o site sozinho em cerca de um minuto. Projetos com etapa de build (React, Vue) não usam "Deploy from a branch": precisam de **GitHub Actions**, que roda o build a cada push e só então publica o resultado.

## Erros comuns

- Confiar em `src`/`href` com maiúscula/minúscula diferente do nome real do arquivo. Windows e Mac ignoram a diferença; o servidor Linux do GitHub Pages não — a imagem aparece local e quebra publicada.

## Onde aparece

- Aula 6 — *GitHub Pages: transformando seu repositório num site que qualquer pessoa acessa* `aulas/programacao-front-end/controle-de-versao-git-github/06-deploy-com-github-pages/canonica.md`
- Conceitos vizinhos: [[github]], [[github-flow]]

## Fontes

- Conteúdo autoral da Aula 6 (modo_origem: tema), sem fonte externa direta — ativação do GitHub Pages e o erro de maiúscula/minúscula no deploy.
