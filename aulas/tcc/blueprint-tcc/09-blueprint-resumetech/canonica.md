---
titulo: Blueprint · ResumeTech
tema: Blueprints de TCC
disciplina: tcc
serie: 3a-serie
prerequisitos: []
objetivos:
  - Compreender a arquitetura e os requisitos do projeto ResumeTech
trilha: blueprint-tcc
ordem: 9
slug: blueprint-resumetech
status: aprovada
versao: 1
atualizado_em: 2026-06-30
---

# Blueprint · ResumeTech

Plataforma web · Flávia Juliane Lemos, Isabela Silva de Meira e Maria Luiza Aguiar da Cunha

## Objetivos

Ao final desta leitura, você será capaz de compreender a arquitetura e os requisitos do projeto ResumeTech.

## Problema e Contexto

Hoje em dia, muitas pessoas enfrentam dificuldades na hora de elaborar um currículo adequado, seja por falta de conhecimento, experiência ou acesso a ferramentas digitais. A construção de um currículo exige organização, clareza, e conhecimento sobre o que o mercado de trabalho espera, o que nem todos possuem. Além disso, existem poucas plataformas simples e acessíveis que atendam pessoas de diferentes idades e níveis de escolaridade.
O problema afeta principalmente os jovens em busca do primeiro emprego, pessoas com baixa familiaridade com tecnologia, adultos que estão retornando ao mercado de trabalho, pessoas com dificuldade de organizar suas informações profissionais.
Esse problema aparece quando a pessoa precisa se candidatar a uma vaga de emprego e não sabe como montar um currículo direito ou não tem um atualizado, isso pode fazer a pessoa perder uma oportunidade profissional, isso acontece no começo da vida profissional, quando alguém está procurando o primeiro emprego.

## Público-Alvo

O público-alvo do sistema são pessoas de diferentes idades que precisam criar um currículo de forma rápida e fácil.
Jovens em busca do primeiro emprego: Vão preencher seus dados básicos, e gerar um currículo simples para se candidatar às primeiras vagas.
Adultos em busca de recolocação profissional: Vão atualizar suas informações, incluir experiências antigas e gerar um currículo mais completo para voltar ao mercado de trabalho.

## Solução Proposta

A proposta é o desenvolvimento de uma plataforma web que facilita a criação de currículos de forma automática e guiada, o usuário apenas preenche suas informações pessoais e profissionais, e o sistema organiza esses dados em um formato de currículo pronto, dessa forma, o processo se torna mais simples, rápido e acessível para qualquer pessoa.

## Requisitos Funcionais

O sistema deve: permitir que o usuário cadastre suas informações pessoais, como nome, contato e endereço.
Inserir sua formação acadêmica.
Registrar experiências profissionais.
Adicionar cursos, habilidades e competências.
O usuário deve visualizar o currículo antes de finalizar.
Editar as informações inseridas
O usuário pode baixar o currículo em formato PDF.

## Requisitos Não Funcionais

Qualidade: O sistema vai ter um interface simples, intuitiva e fácil de usar, garantindo que qualquer usuário consiga criar seu currículo sem dificuldades.
Segurança: O sistema vai gerar o currículo de forma rápida, mesmo com várias informações inseridas, sem travamentos, ou demora excessiva.
Disponibilidade: O sistema vai estar disponível para uso na maior parte do tempo, permitindo que os usuários acessem e criem seus currículos sempre que precisarem.

## Arquitetura e Tecnologias

Linguagem: Será utilizado Node.js com Express.js, pois permite a criação de uma aplicação web leve, rápida e escalável, além disso, é muito usado no mercado, o que facilita manutenção e integração com outras tecnologias.
Banco de Dados: Será utilizado MongoDB, por ser um banco de dados NoSQL flexível, ideal para armazenar dados de usuários e currículos de forma estruturada e sem necessidade de tabelas fixas, facilitando futuras alterações no sistema.
Front-end: Será utilizado HTML, CSS e JavaScript, possivelmente com React, pois permite criar uma interface moderna, responsiva e fácil de usar, garantindo uma boa experiência para o usuário.
Hospedagem: Será utilizada uma plataforma como Vercel ou Render, pois oferecem facilidade de deploy, integração com projetos web e permitem que o sistema fique acessível online de forma simples.
Outras ferramentas: Vai ser utilizadas ferramentas como Git e GitHub para controle de versão, além de bibliotecas para geração de PDF do currículo, garantindo funcionalidade prática no sistema
Padrão de arquitetura: Será adotado o padrão MVC (Model-View-Controller), pois ajuda a organizar melhor o sistema separando lógica, interface e dados, facilitando a manutenção e escalabilidade do projeto.

## Fluxo Principal do Usuário

O usuário acessa o site e realiza o login ou cadastro, caso ainda não tenha uma conta. Após entrar no sistema, o usuário é direcionado para uma página onde começa a preencher suas informações pessoais, como nome, contato e endereço.
Em seguida, adiciona dados como formação acadêmica, experiência profissional, cursos e habilidades. Depois de preencher todas as informações, o usuário avança para a etapa de visualização, onde pode conferir como o currículo está ficando, caso queira, pode voltar e editar qualquer informação. Por fim, o sistema gera automaticamente o currículo pronto e formatado, e o usuário pode baixar o arquivo em PDF ou salvar para uso posterior.

## Autoavaliação do Escopo

Esse projeto é viável dentro prazo do TCC, pois possui um escopo bem definido e não tem um complexidade técnica grande, as funcionalidades principais como cadastro de informações e geração automática de currículo, pode ser desenvolvidas utilizando tecnologias já conhecidas e bem documentadas, o que facilita o desenvolvimento do site.
Além disso, o projeto vai ser realizado por uma equipe de 3 pessoas, o tempo disponível é suficiente para planejar, desenvolver, testar e ajustar o sistema.
