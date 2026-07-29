---
titulo: "GitHub Pages: transformando seu repositório num site que qualquer pessoa acessa"
tema: Publicação de site estático com GitHub Pages
disciplina: programacao-front-end
serie: 3ª
prerequisitos: ["Repositório no GitHub com Pull Requests (Aulas 3 e 4)"]
objetivos:
  - Explicar o que o GitHub Pages faz e para que tipo de projeto ele serve direto, sem configuração extra
  - Ativar o GitHub Pages num repositório e obter um link público funcionando
  - Diagnosticar o erro mais comum de deploy — caminho de arquivo que funciona local mas quebra publicado
  - Saber quando GitHub Pages via GitHub Actions é necessário, para projetos com etapa de build
trilha: controle-de-versao-git-github
ordem: 6
slug: deploy-com-github-pages
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 2
atualizado_em: 2026-07-29
---

Até agora, seu Petfinder só existe pra quem abre o VSCode, baixa os arquivos ou recebe eles por WhatsApp. Hoje ele ganha um **link de verdade** — um endereço que qualquer pessoa, no celular dela, na casa dela, clica e vê seu projeto rodando, sem instalar nada e sem você mandar arquivo nenhum. É o primeiro momento em que "meu projeto de curso" vira "coisa que existe na internet".

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que o **GitHub Pages** faz e para que tipo de projeto ele serve direto, sem configuração extra.
- Ativar o GitHub Pages num repositório e obter um link público funcionando.
- Diagnosticar o erro mais comum de deploy — um caminho de arquivo que funciona no seu computador mas quebra depois de publicado.
- Saber quando GitHub Pages via **GitHub Actions** é necessário, para projetos que têm uma etapa de build.

## Pré-requisitos

Você precisa ter um repositório no GitHub com seu projeto (o Petfinder serve perfeitamente) e já ter passado pelas Aulas 3 e 4 — remoto e Pull Request.

## Desenvolvimento

### O que o GitHub Pages faz

:::conceito GitHub Pages
**GitHub Pages** é um serviço gratuito do GitHub que pega os arquivos estáticos de um repositório (HTML, CSS, JavaScript) e os coloca no ar, servidos como um site de verdade, num endereço público — sem você precisar contratar hospedagem nem configurar servidor nenhum.
:::

O detalhe importante está na palavra **estáticos**: o Petfinder é HTML, CSS e JavaScript que rodam **direto no navegador**, sem nenhuma etapa de "compilar" antes. Pra esse tipo de projeto, o GitHub Pages funciona exatamente assim: pega os arquivos como estão no repositório e os publica. Não tem meio-termo pra configurar.

### Ativando o GitHub Pages pro Petfinder

O caminho é todo pela interface do site, sem comando de terminal:

1. No repositório do Petfinder, abra **Settings** (Configurações).
2. No menu lateral, clique em **Pages**.
3. Em "Build and deployment", escolha a fonte **Deploy from a branch**.
4. Selecione a branch `main` e a pasta `/ (root)` — ou a pasta onde está o `index.html`, se ele não estiver na raiz.
5. Clique em **Save**. Depois de cerca de um minuto, o GitHub mostra o link público no topo da mesma página — algo como `https://seu-usuario.github.io/petfinder/`.

A partir daí, **todo `push` na branch escolhida atualiza o site sozinho**, em torno de um minuto depois. Você não "reenvia" o site — ele é sempre um reflexo automático do que está na `main`.

```diagrama-progressivo
titulo: O que acontece entre o push e o site atualizado
camadas:
  - rotulo: Você dá push
    conteudo: "Um commit novo chega na branch configurada como fonte do GitHub Pages (geralmente main)."
  - rotulo: GitHub Pages detecta
    conteudo: "O serviço percebe a mudança automaticamente, sem você precisar avisar nada em lugar nenhum."
  - rotulo: Publicação
    conteudo: "Em cerca de um minuto, os arquivos atualizados substituem os antigos no endereço público — o link continua o mesmo, só o conteúdo muda."
```

### O erro mais comum: um caminho que funciona local e quebra publicado

Existe um erro clássico que pega quase todo mundo na primeira publicação, e ele não tem nada a ver com HTML errado.

:::atencao Erro comum
No seu computador (Windows ou Mac), o sistema de arquivos **não diferencia** maiúscula de minúscula: `logo.png` e `Logo.PNG` apontam pro **mesmo arquivo**. Um `<img src="Logo.png">` funciona local mesmo que o arquivo se chame `logo.png` de verdade. Só que o servidor do GitHub Pages roda em Linux, que **diferencia** maiúscula de minúscula rigorosamente — `logo.png` e `Logo.png` são dois arquivos diferentes pra ele. Resultado: a imagem aparece perfeitamente enquanto você testa local, e vira um ícone quebrado assim que o site vai pro ar. Pra diagnosticar, confira se o nome do arquivo no seu `src=""` ou `href=""` bate **letra por letra, maiúscula por maiúscula** com o nome real do arquivo na pasta.
:::

Esse é o tipo de erro que só existe **por causa do deploy** — é por isso que testar local nunca garante 100% que vai funcionar publicado.

### Quando isso deixa de ser suficiente

O Petfinder não tem build step — por isso "Deploy from a branch" resolve tudo sozinho. Mas nem todo projeto de front-end é assim.

:::dica Onde isso muda no seu futuro como dev
Frameworks modernos (React, Vue, e outros que você vai encontrar depois do curso) não rodam os arquivos `.jsx`/`.vue` direto no navegador — eles passam por uma etapa de **build**, que transforma o código-fonte em HTML/CSS/JS final. Pra esses casos, a opção correta no GitHub Pages não é mais "Deploy from a branch": é configurar o **GitHub Actions**, que roda o build automaticamente a cada `push` e só então publica o resultado. Você não precisa disso hoje — mas quando seu próximo projeto tiver um comando `npm run build`, é esse o motivo de "Deploy from a branch" não bastar mais.
:::

## Prática

**No repositório do Petfinder, pelo navegador (~10 min):**

1. Ative o GitHub Pages seguindo os 5 passos da seção anterior.
2. Espere cerca de um minuto e abra o link gerado — confirme que o Petfinder está no ar.
3. Abra o mesmo link no celular (dado ou Wi-Fi, sem estar na mesma rede do computador que criou) e confirme que funciona fora do ambiente da escola.
4. **Provoque o erro de propósito**: mude, só no HTML, o `src` de uma imagem pra uma grafia com letra maiúscula diferente do arquivo real (ex.: se o arquivo é `pet1.jpg`, escreva `src="Pet1.jpg"`). Suba com `git add`, `commit`, `push` e confira: local a imagem pode continuar aparecendo (dependendo do navegador), mas no link publicado ela quebra.
5. Corrija o nome pra bater exatamente com o arquivo real, suba de novo e confirme que voltou a funcionar.

## Avaliação

```quiz
- pergunta: Por que o GitHub Pages consegue publicar o Petfinder sem nenhuma configuração de build?
  alternativas:
    - texto: "Porque o GitHub Pages sempre faz build de qualquer projeto automaticamente"
    - texto: "Porque o Petfinder é HTML/CSS/JS que já roda direto no navegador, sem etapa de compilação"
      correta: true
    - texto: "Porque o Petfinder está numa branch especial chamada gh-pages"
    - texto: "Porque o navegador do celular compila o código sozinho"
  feedback: >
    Deploy from a branch serve exatamente projetos sem build step — os arquivos
    do repositório são publicados como estão, sem transformação nenhuma.
- pergunta: Uma imagem aparece certinho no seu computador mas fica quebrada depois de publicada no GitHub Pages. Qual é a causa mais provável, segundo a aula?
  alternativas:
    - texto: "O GitHub Pages não suporta imagens"
    - texto: "A internet do celular estava lenta"
    - texto: "Diferença entre maiúscula e minúscula no nome do arquivo — o servidor Linux diferencia, seu computador não"
      correta: true
    - texto: "A imagem é grande demais para a internet"
  feedback: >
    Windows e Mac ignoram maiúscula/minúscula em nomes de arquivo; o servidor
    Linux do GitHub Pages não. Um src="Logo.png" que aponta pra logo.png
    funciona local e quebra publicado.
- pergunta: Quando "Deploy from a branch" deixa de ser suficiente para publicar um projeto no GitHub Pages?
  alternativas:
    - texto: "Nunca — sempre funciona para qualquer projeto"
    - texto: "Quando o projeto tem uma etapa de build (ex.: React, Vue), que precisa rodar antes de publicar — aí entra o GitHub Actions"
      correta: true
    - texto: "Quando o repositório é privado"
    - texto: "Quando o projeto tem mais de um arquivo HTML"
  feedback: >
    Projetos com build step (npm run build, por exemplo) precisam que esse
    processo rode antes da publicação — isso é o que o GitHub Actions automatiza.
```

## Fechamento

Hoje você viu que:

- **GitHub Pages** publica arquivos estáticos (HTML/CSS/JS) direto do repositório, sem hospedagem paga.
- Ativar é configuração pura de interface: Settings → Pages → Deploy from a branch → escolher `main`.
- Todo `push` depois disso **atualiza o site sozinho**, em cerca de um minuto.
- O erro mais comum é maiúscula/minúscula divergente no nome de arquivo — funciona local, quebra publicado, porque o servidor é Linux.
- Projetos com etapa de build (React, Vue) precisam de **GitHub Actions** em vez de "Deploy from a branch".

Com isso, fecha o módulo de Git e GitHub: você saiu de "arquivo salvo no meu computador" pra "histórico versionado, hospedado, revisado por Pull Request e publicado com link público" — o fluxo real usado por qualquer time profissional de front-end.

:::roteiro
Guardar esse momento como o "grande final" do módulo — é a primeira vez que o trabalho do aluno vira algo clicável e mostrável pra família/amigos, e isso rende engajamento real. Fazer questão de que todo mundo mande o link do próprio GitHub Pages no grupo da turma ou mostre no celular do colega ao vivo. No erro de maiúscula/minúscula, vale reforçar bem que é um erro **invisível localmente** — ninguém vai ver o problema até publicar, o que é uma lição sobre confiar demais no "funcionou aqui". Se sobrar tempo, mostrar rapidamente (sem aprofundar) como seria a tela de configuração do GitHub Actions, só pra desmistificar — não é assunto da aula, é só o "próximo capítulo" que a turma vai encontrar fora do curso.
:::
