---
titulo: Blueprint · Gold Fit
tema: Blueprints de TCC
disciplina: tcc
serie: 3a-serie
prerequisitos: []
objetivos:
  - Compreender a arquitetura e os requisitos do projeto Gold Fit
trilha: blueprint-tcc
ordem: 5
slug: blueprint-gold-fit
status: aprovada
versao: 1
atualizado_em: 2026-06-30
---

# Blueprint · Gold Fit

Aplicativo mobile (iOS/Android) de academia e fitness · Lucca Dória Loiola, Victor Emanuel Furtado de Oliveira e Pedro Miguel da Silva

## Objetivos

Ao final desta leitura, você será capaz de compreender a arquitetura e os requisitos do projeto Gold Fit.

## Problema e Contexto

Praticantes de academia enfrentam dificuldades para organizar, registrar e acompanhar a evolução dos treinos de forma sistemática. A ausência de um registro centralizado impede que o usuário visualize o progresso ao longo do tempo, dificulta a aplicação da sobrecarga progressiva e aumenta o risco de lesões por execução incorreta dos exercícios.

Atualmente, muitos alunos usam cadernos de papel, planilhas genéricas ou dependem apenas da memória, o que resulta em treinos inconsistentes, perda de motivação e abandono da prática. No Brasil, a falta de modo offline em apps similares é uma barreira adicional, já que academias frequentemente têm conexão instável ou inexistente.

## Público-Alvo

- **Praticante iniciante**: cria seu perfil, consulta a biblioteca de exercícios com vídeos demonstrativos e segue treinos sugeridos pelo app.
- **Praticante intermediário/avançado**: cria treinos personalizados, registra cargas, séries e RPE, monitora PRs e acompanha gráficos de evolução.
- **Usuário focado em metas**: define objetivos (hipertrofia, emagrecimento, força), recebe sugestões automáticas de ajuste de carga e acompanha o progresso pelo calendário.
- **Usuário de wearables**: sincroniza Apple Watch, Samsung Health, Google Fit ou Strava para enriquecer os dados de treino e saúde.

## Solução Proposta

O Gold Fit é um aplicativo mobile de academia e fitness que centraliza o planejamento, o registro e o acompanhamento de treinos em uma única plataforma. A solução combina uma biblioteca rica de exercícios com vídeos demonstrativos, um motor de personalização que aprende com o histórico do usuário e sugere ajustes de carga automáticos (sobrecarga progressiva), e um painel visual de evolução que transforma dados de treino em motivação concreta.

O app é projetado para funcionar integralmente sem internet, garantindo usabilidade em qualquer academia. Toda a experiência é orientada a manter o usuário consistente, reduzir lesões por técnica inadequada e tornar visível o progresso que costuma passar despercebido sem registro sistemático.

## Requisitos Funcionais

- **RF01** — O sistema deve permitir cadastro e autenticação via e-mail, Google ou Apple ID, com coleta de dados de perfil (peso, altura, nível e objetivo).
- **RF02** — O sistema deve disponibilizar uma biblioteca com no mínimo 300 exercícios, com vídeo/animação de execução, músculos trabalhados e instruções de segurança.
- **RF03** — O sistema deve permitir criar treinos personalizados por grupo muscular, divisão semanal (A/B, PPL, full body) e métodos avançados (superset, drop set, circuito).
- **RF04** — O sistema deve registrar cada série com peso (kg), repetições, tempo de descanso, notas livres e RPE (esforço percebido).
- **RF05** — O sistema deve exibir gráficos de evolução de carga, volume semanal, Personal Records (PRs) e estimativa de 1RM por exercício.
- **RF06** — O sistema deve sugerir automaticamente a carga da próxima sessão com base no histórico, aplicando sobrecarga progressiva.
- **RF07** — O sistema deve disponibilizar um timer de descanso configurável entre séries, com notificação sonora e vibração.
- **RF08** — O sistema deve registrar medidas corporais (braço, peito, cintura, quadril) e fotos de progresso vinculadas a datas.
- **RF09** — O sistema deve sincronizar dados com wearables (Apple Watch, Samsung Health, Google Fit e Strava) quando conectado.
- **RF10** — O sistema deve enviar notificações e lembretes de treino conforme a agenda semanal configurada.

## Requisitos Não Funcionais

- **RNF01** — O sistema deve funcionar completamente offline, sincronizando com o servidor quando houver conexão (disponibilidade e modo offline).
- **RNF02** — O sistema deve carregar as telas principais em no máximo 2 segundos em hardware intermediário (desempenho).
- **RNF03** — O sistema deve armazenar senhas com hash bcrypt e dados sensíveis criptografados em repouso e em trânsito via HTTPS/TLS 1.3 (segurança).
- **RNF04** — A interface deve ser operável com uma mão durante o treino, com botões de ação de no mínimo 48dp de área de toque (usabilidade).
- **RNF05** — O sistema deve suportar ao menos 10.000 usuários simultâneos sem degradação perceptível (escalabilidade).

## Arquitetura e Tecnologias

- **Front-end / Mobile**: React Native + Expo — justificativa: desenvolvimento multiplataforma (iOS e Android) com base de código única, reduzindo custo e prazo do TCC.
- **Back-end**: Node.js + Express — justificativa: ecossistema JavaScript unificado com o front-end, alta performance em I/O e ampla comunidade.
- **Banco de dados**: PostgreSQL — justificativa: relacional robusto, suporta consultas complexas de histórico/séries e é gratuito para deploy em nuvem.
- **Offline / Sync**: SQLite (local) + Sync API — justificativa: armazenamento local nativo para modo offline e sincronização incremental ao reconectar.
- **Hospedagem**: Railway / Render — justificativa: plataformas de deploy gratuitas/low-cost ideais para o escopo de TCC, com suporte a Node.js e PostgreSQL.
- **Autenticação**: Firebase Auth — justificativa: login social (Google/Apple) pronto, segurança gerenciada e SDK para React Native.
- **Padrão arquitetural**: MVC + REST API — justificativa: separação clara de responsabilidades e API REST que facilita integração com wearables e escalabilidade futura.

## Fluxo Principal do Usuário

1. O usuário baixa o app e se cadastra informando nome, e-mail (ou login social), peso, altura, gênero, nível de experiência e objetivo principal (ex.: hipertrofia).
2. O sistema gera uma sugestão inicial de divisão de treino com base no perfil (ex.: A/B para iniciante, PPL para avançado).
3. O usuário personaliza ou aceita o plano, podendo adicionar, remover ou reorganizar exercícios da biblioteca e configurar séries, repetições e cargas iniciais.
4. No dia do treino, abre o app, seleciona o treino do dia e inicia a sessão, registrando carga, repetições e RPE de cada série.
5. O timer de descanso é acionado automaticamente entre séries, alertando com som e vibração ao fim do intervalo.
6. Ao concluir, o sistema calcula o volume total da sessão, detecta novos PRs e exibe um resumo comparativo com a sessão anterior.
7. O sistema atualiza os gráficos de evolução (carga × tempo, volume semanal) e registra a sessão no calendário de treinos.
8. Com base no desempenho, o app sugere ajuste de carga para a próxima sessão do mesmo treino, aplicando sobrecarga progressiva personalizada.

## Autoavaliação do Escopo

O escopo do Gold Fit foi dimensionado para ser viável dentro do prazo de um TCC semestral desenvolvido em grupo. O projeto usa tecnologias amplamente documentadas (React Native, Node.js, PostgreSQL), com grande disponibilidade de tutoriais, bibliotecas prontas e comunidade ativa, reduzindo o risco técnico.

O desenvolvimento em grupo permite divisão de responsabilidades — front-end mobile, back-end/API e banco podem evoluir em paralelo. Funcionalidades mais complexas, como integração com wearables e personalização via IA, foram classificadas como incrementais: o MVP entregável no prazo cobre cadastro, biblioteca de exercícios, registro de treinos, histórico e gráficos de evolução.

O modo offline é suportado por SQLite, tecnologia madura e de integração direta com React Native, sem infraestrutura adicional. O deploy em plataformas gratuitas (Railway/Render) elimina custo operacional durante o desenvolvimento. A equipe avalia o projeto como tecnicamente viável e com escopo compatível com o prazo.
