---
titulo: Blueprint · HobbyQuest
tema: Blueprints de TCC
disciplina: tcc
serie: 3a-serie
prerequisitos: []
objetivos:
  - Compreender a arquitetura e os requisitos do projeto HobbyQuest
trilha: blueprint-tcc
ordem: 7
slug: blueprint-hobbyquest
status: aprovada
versao: 1
atualizado_em: 2026-06-30
---

# Blueprint · HobbyQuest

Aplicativo mobile gamificado (Android/iOS) · Maysa Rogaleski Rodrigues, Raquel Heloize Kutz de Bastos e Victor Gabriel Silvestre Melo

## Objetivos

Ao final desta leitura, você será capaz de compreender a arquitetura e os requisitos do projeto HobbyQuest.

## Problema e Contexto

No cenário atual, muitas pessoas enfrentam dificuldades em manter a motivação e a disciplina para aprender e praticar novos hobbies — estão perdendo a vontade de fazer coisas novas que estimulem sua criatividade. A rotina agitada, a falta de um método estruturado e a ausência de um objetivo real são alguns dos fatores que contribuem para que novos interesses sejam rapidamente abandonados.

Frequentemente, a busca por desenvolvimento pessoal através de novas habilidades se torna uma tarefa solitária e desestimulante, resultando em tempo perdido ou não produtivo e na perda de oportunidades de crescimento pessoal e social.

A falta de um sistema que transforme esse processo em uma experiência divertida e recompensadora é um problema que afeta indivíduos que desejam expandir seus horizontes, mas se veem presos à vida agitada e ao vício tecnológico.

## Público-Alvo

O sistema é direcionado a jovens adolescentes e adultos que buscam aprender novas habilidades de forma lúdica e bem organizada. Os perfis de usuário incluem:

- **Usuário Aprendiz**: indivíduos que desejam explorar novos hobbies (como desenho, crochê, culinária, leitura) e buscam um método gamificado para manter a motivação. Interagem com a narrativa, completam desafios práticos e registram sua conclusão por meio de interações simples no sistema (marcação de tarefas e pequenos relatos textuais), acompanhando seu progresso através de níveis e recompensas conquistados pouco a pouco.
- **Administrador do Sistema**: responsável por gerenciar o conteúdo da plataforma, incluindo a criação e atualização de desafios, moderação de evidências enviadas pelos usuários e manutenção da narrativa e dos personagens.

## Solução Proposta

A solução proposta é uma plataforma interativa e gamificada, denominada HobbyQuest, que transforma o aprendizado e a prática de novos passatempos em uma experiência envolvente e social.

Através de uma narrativa de "Visual Novel" ambientada em um cenário escolar, o sistema estimula o usuário a desenvolver habilidades focadas em três áreas principais — arte (desenho), leitura e atividade física leve — representadas por personagens, por meio de desafios práticos e um sistema de progressão baseado em níveis e recompensas.

O objetivo é converter o tempo "livre" em aprendizado produtivo, ajudando o usuário a aperfeiçoar sua disciplina e a descobrir novos talentos de forma lúdica.

## Requisitos Funcionais

- RF01 — O sistema deve permitir que o usuário realize login e mantenha a persistência dos dados e do progresso individual.
- RF02 — O sistema deve apresentar um tutorial animado para introduzir a mecânica do jogo e os personagens/hobbies disponíveis.
- RF03 — O sistema deve propor desafios práticos personalizados para a evolução do nível de proficiência em cada hobby.
- RF04 — O sistema deve permitir que o usuário marque desafios como concluídos e registre um breve relato opcional.
- RF05 — O sistema deve atualizar automaticamente o progresso do usuário após a conclusão de um desafio.
- RF06 — O sistema deve exibir uma linha do tempo visual com todas as atividades concluídas pelo usuário.
- RF07 — O sistema deve atribuir pontos (XP) ao usuário com base na complexidade dos desafios concluídos.
- RF08 — O sistema deve conceder conquistas e medalhas digitais ao usuário por marcos importantes alcançados.
- RF09 — O sistema deve exibir o nível atual do usuário e seu progresso no perfil.
- RF10 — O sistema deve exibir mensagens motivacionais internas (sem push notification).

## Requisitos Não Funcionais

- **RNF01 — Desempenho**: o sistema deve apresentar tempos de resposta inferiores a 3 segundos para a maioria das interações do usuário, garantindo uma experiência fluida e sem atrasos perceptíveis.
- **RNF02 — Usabilidade**: a interface deve ser intuitiva e de fácil aprendizado, permitindo que usuários com diferentes níveis de familiaridade com aplicativos gamificados naveguem e interajam sem dificuldades.
- **RNF03 — Segurança**: o sistema deve implementar protocolos de segurança robustos para proteger os dados pessoais dos usuários e as evidências enviadas (fotos/textos), garantindo conformidade com a LGPD e prevenindo acessos não autorizados.
- **RNF04 — Disponibilidade**: o sistema deve estar disponível durante o período de testes e apresentação, com funcionamento estável.
- **RNF05 — Escalabilidade**: o sistema deve suportar múltiplos usuários simultâneos em ambiente de teste.

## Arquitetura e Tecnologias

Padrão arquitetural: Cliente-Servidor com Backend as a Service (BaaS) — o frontend (aplicativo mobile) atua como cliente, interagindo diretamente com os serviços do Firebase (BaaS) para autenticação, banco de dados, armazenamento e funções de backend, simplificando o desenvolvimento e a manutenção da infraestrutura.

Linguagem / Framework back-end: Firebase Cloud Functions — permite executar código de backend sem gerenciar servidores, ideal para lógica de notificações e validações automáticas, com integração nativa aos demais serviços Firebase.

Banco de dados: Firestore (NoSQL) — banco escalável e flexível, adequado para armazenar dados de progresso, níveis e pontos, com sincronização em tempo real e fácil integração com o frontend mobile.

Front-end / Interface: Flutter ou React Native — desenvolvimento de apps móveis nativos para iOS e Android a partir de uma única base de código, garantindo interface intuitiva, animações fluidas e feedback visual constante, essenciais para a experiência gamificada.

Hospedagem / Deploy: Firebase Hosting e Cloud Storage — o Hosting oferece hospedagem rápida e segura para o frontend (versão web ou assets estáticos); o Cloud Storage armazena as mídias (fotos e vídeos) enviadas pelos usuários, ambos com alta escalabilidade.

Outras ferramentas: Firebase Authentication — gerencia o acesso e a autenticação de usuários, com diversas opções de login e segurança robusta.

## Fluxo Principal do Usuário

O fluxo principal segue um caminho gamificado, da autenticação à conclusão da jornada de aprendizado de hobbies:

1. Autenticação e Acesso: o usuário inicia a experiência realizando login, garantindo acesso ao seu progresso e dados personalizados.
2. Onboarding e Introdução: após o login, é guiado por um tutorial animado que apresenta a narrativa do jogo, a mecânica de progressão e os personagens que representam os diferentes hobbies.
3. Seleção de Hobby e Interação: o usuário escolhe um dos personagens/hobbies disponíveis; a interação inicial pode ser limitada pelo nível de proficiência necessário para desbloquear diálogos.
4. Aceitação de Desafio: para progredir no hobby escolhido e desbloquear novas interações, o usuário visualiza e aceita um desafio prático proposto pelo sistema.
5. Conclusão do Desafio: o usuário marca o desafio como concluído.
6. Atualização Automática: o sistema atualiza automaticamente o XP e o progresso.
7. Acompanhamento e Recompensa: o usuário acompanha seu progresso pela linha do tempo e pelo perfil, visualizando conquistas e medalhas. O ciclo se repete com novos desafios até atingir o nível máximo em todos os hobbies, concluindo a jornada da protagonista.

## Autoavaliação do Escopo

O projeto HobbyQuest, embora ambicioso em sua proposta de gamificação e narrativa, é considerado viável dentro do prazo de um TCC, pelos seguintes aspectos:

Foco em MVP: o tempo disponível exige concentrar esforços na criação de um Produto Mínimo Viável. A estratégia prioriza as funcionalidades essenciais que sustentam a proposta central — gamificação do aprendizado por meio de desafios práticos, progressão por níveis e feedback ao usuário. Funcionalidades mais complexas (interações sociais avançadas, personalização aprofundada da narrativa) ficam como expansões futuras.

Equipe e divisão de trabalho: com três integrantes, o projeto pode ser gerenciado com eficiência dividindo responsabilidades entre desenvolvimento, design e estruturação de conteúdo. Flutter/React Native no frontend permitem desenvolvimento multiplataforma com base de código única, otimizando o tempo, e o Firebase como BaaS reduz a necessidade de gerenciar infraestrutura, banco de dados e autenticação.

Viabilidade de execução: com planejamento adequado e priorização das funcionalidades críticas, a equipe concentra esforços em um sistema funcional de desafios, progressão e narrativa interativa simplificada. A conclusão das atividades é registrada diretamente pelo usuário (marcação de tarefas e relatos textuais opcionais), eliminando mecanismos complexos de validação.

Dificuldade técnica gerenciável: as ferramentas escolhidas reduzem a complexidade. Progressão por níveis, atribuição de XP e desbloqueio de conteúdo são conceitos consolidados e amplamente documentados, com curva de aprendizado acessível e suporte de comunidade.

Em síntese, a definição de um MVP, a escolha adequada de tecnologias e a delimitação clara das funcionalidades tornam o HobbyQuest um projeto viável, coerente e plenamente executável no contexto de um Trabalho de Conclusão de Curso.
