---
titulo: Blueprint · Alexandria
tema: Blueprints de TCC
disciplina: tcc
serie: 3a-serie
prerequisitos: []
objetivos:
  - Compreender a arquitetura e os requisitos do projeto Alexandria
trilha: blueprint-tcc
ordem: 3
slug: blueprint-brvpn
status: aprovada
versao: 1
atualizado_em: 2026-06-30
---

# Blueprint · Alexandria

Aplicativo mobile (Android) + web · Gabriella Gomes de Almeida Miranda, Marlon Gabriel Perissute e Nathalia Elisa Prestes Fujikawa

## Objetivos

Ao final desta leitura, você será capaz de compreender a arquitetura e os requisitos do projeto Alexandria.

## Problema e Contexto

Nos últimos dias eu notei a falta de sites e apps de leitura de mangás/manhwas/webtoons.
Muitos dos sites que tinham antes foram derrubados pela falta de licenciamento, e atualmente já
não há mais nenhum site ou aplicativo disponível, os que têm são gringos, sem tradução para o
português e ainda pagos, ou sites piratas cheio de anuncios. Isso dificulta a acessibilidade para
os leitores brasileiros que gostam desse conteúdo, e desvaloriza o trabalho dos autores dessas
obras, que .
É extremamente frustrante se interessar por um conteúdo ou obra e ter o acesso limitado,
sabendo que em outros lugares fora do Brasil o acesso é facilitado e ilimitado.

## Público-Alvo

- Leitores brasileiros de mangás, manhwas e webtoons — utilizarão o aplicativo para ler
obras gratuitamente, comentar capítulos e acompanhar lançamentos.
- Criadores e tradutores autorizados — poderão publicar obras próprias ou conteúdos
licenciados/autorizados no aplicativo.
- Moderadores e apoiadores da comunidade — irão ajudar na organização do conteúdo,
denúncias e gerenciamento da comunidade.
- Usuários menores de idade — terão acesso apenas a conteúdos apropriados para sua
faixa etária.
- Usuários premium ou ativos — poderão desbloquear conteúdos especiais usando
moedas adquiridas no aplicativo.

## Solução Proposta

A nossa proposta é criar um aplicativo com leituras completamente gratuitas, onde os
usuários vão poder upar um manhwa de sua autoridade ou um que você recebeu permissão
para registrar no app.
O nosso aplicativo vai ter um sistema de comentários e perfis personalizados, onde nossos
usuários poderão personalizar seus perfis, com molduras, balões de comentários ou fontes
especiais. Terá um sistema de moedinhas que os usuários poderão receber ao assistir anúncios,
ou completar missões como “ler 3 capítulos”, e assim poder desbloquear obras ou capítulos
especiais. Cada manhwa/mangá/webtoon terá sua tag e classificação, menores de idade não
poderão ter acesso a conteúdos para maiores de idade.
Será uma comunidade toda se ajudando a promover esse conteúdo, então também terá
apoiadores que irão nos ajudar a upar as obras no app e a gerenciar a comunidade dos
usuários.

## Requisitos Funcionais

- RF01 — O sistema deve permitir que usuários criem e personalizem suas contas.
- RF02 — O sistema deve permitir a leitura online de mangás, manhwas e webtoons.
- RF03 — O sistema deve permitir que usuários publiquem obras autorizadas.
- RF04 — O sistema deve possuir um sistema de comentários em capítulos e obras.
- RF05 — O sistema deve possuir classificação indicativa para restringir conteúdos
impróprios para menores de idade.
- RF06 — O sistema deve permitir que usuários ganhem moedas virtuais ao assistir
anúncios ou completar missões.
- RF07 — O sistema deve permitir desbloquear capítulos especiais utilizando moedas
virtuais.
- RF08 — O sistema deve permitir denúncias de conteúdos inadequados ou usuários
ofensivos.

## Requisitos Não Funcionais

- RNF01 — O sistema deve possuir interface intuitiva e fácil de usar em dispositivos
móveis.
- RNF02 — O aplicativo deve carregar capítulos e imagens em até 3 segundos em
conexões comuns de internet.
- RNF03 — O sistema deve proteger os dados dos usuários por meio de autenticação
segura e criptografia de senhas.
- RNF04 — O aplicativo deve possuir disponibilidade mínima de 95% do tempo.
- RNF05 — O sistema deve ser compatível com Android e navegadores web modernos.

## Arquitetura e Tecnologias

Linguagem / Framework back-end: Node.js
Banco de dados: MongoDB
Front-end / Interface: React Native
Hospedagem / Deploy: Firebase
Outras ferramentas: Figma e GitHub
Padrão arquitetural (MVC, microsserviços, etc.): MVC (Model-View-Controller)

## Fluxo Principal do Usuário

1. O usuário instala o aplicativo e cria uma conta.
2. O sistema solicita confirmação de idade e preferências de leitura.
3. O usuário acessa a página inicial e pesquisa uma obra.
4. O usuário seleciona um mangá/manhwa/webtoon para leitura.
5. O sistema exibe os capítulos disponíveis.
6. O usuário lê o capítulo e pode comentar ou reagir.
7. O usuário ganha moedas ao concluir missões ou assistir anúncios.
8. O usuário utiliza moedas para desbloquear conteúdos especiais.

## Autoavaliação do Escopo

Acreditamos que o projeto é viável dentro do prazo do TCC porque a equipe possui uma
proposta organizada e funcionalidades bem definidas. O sistema poderá começar com recursos
principais, como leitura, login e comentários, deixando funções mais avançadas para versões
futuras.

As tecnologias escolhidas possuem bastante documentação e suporte na internet, facilitando o
aprendizado e desenvolvimento. Apesar de envolver desafios como armazenamento de imagens
e gerenciamento de usuários, o projeto é possível de ser desenvolvido em etapas ao longo do
período disponível.
