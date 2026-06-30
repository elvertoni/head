---
titulo: Blueprint · A.N.N Beauty
tema: Blueprints de TCC
disciplina: tcc
serie: 3a-serie
prerequisitos: []
objetivos:
  - Compreender a arquitetura e os requisitos do projeto A.N.N Beauty
trilha: blueprint-tcc
ordem: 1
slug: blueprint-a-n-n-beauty
status: aprovada
versao: 1
atualizado_em: 2026-06-30
---

# Blueprint · A.N.N Beauty

Plataforma web (e-commerce + tutoriais + social) · Anny Isabely Coradassi, Nicoly Holtz da Silva e Nivea Caroline da Silva Matos

## Objetivos

Ao final desta leitura, você será capaz de compreender a arquitetura e os requisitos do projeto A.N.N Beauty.

## Problema e Contexto

No cenário atual, entusiastas e profissionais de maquiagem enfrentam desafios significativos ao buscar inspiração, aprender novas técnicas e adquirir produtos. A fragmentação de informações é um problema central: tutoriais de maquiagem estão espalhados por diversas plataformas de vídeo, as informações sobre os produtos utilizados nem sempre são claras ou facilmente acessíveis, e a compra desses itens frequentemente exige a navegação por múltiplos e-commerces.

Isso resulta em uma experiência de usuário desarticulada, perda de tempo na pesquisa e dificuldade em replicar looks desejados devido à falta de identificação precisa dos produtos. Além disso, a interação social e o compartilhamento de experiências são limitados, impedindo uma comunidade engajada em torno do universo da maquiagem.

A ausência de uma plataforma unificada que integre conteúdo educacional, identificação de produtos e e-commerce, com um componente social, gera frustração e ineficiência para quem busca aprimorar suas habilidades e consumir produtos de beleza.

## Público-Alvo

O público-alvo do AnnyvvMake é diversificado, abrangendo desde iniciantes até profissionais da área de maquiagem. Cada perfil terá interações específicas com o sistema:

- Entusiastas de Maquiagem (iniciantes e intermediários): buscarão tutoriais para aprender novas técnicas, descobrir produtos e se inspirar em looks. Poderão assistir a vídeos, identificar os produtos usados, salvar favoritos e realizar compras diretamente na plataforma. Também interagirão com a comunidade através da aba social.
- **Profissionais de Maquiagem**: utilizarão a plataforma para se manter atualizados sobre tendências, descobrir novos produtos e, potencialmente, compartilhar seus próprios trabalhos e tutoriais. A identificação de produtos será valiosa para recomendações a clientes e para a gestão de seus kits.
- Criadores de Conteúdo (influenciadores e maquiadores): poderão hospedar tutoriais, marcar os produtos utilizados e monetizar suas criações através de vendas diretas ou comissões. A aba social servirá como portfólio e canal de engajamento com seus seguidores.
- **Consumidores em Geral**: pessoas interessadas em comprar maquiagem de forma conveniente, com a vantagem de ver os produtos em uso e receber recomendações baseadas em tutoriais e na comunidade.

## Solução Proposta

O AnnyvvMake propõe uma plataforma web inovadora que integra a experiência de compra de maquiagem com conteúdo educacional e social. A ideia central é criar um ecossistema onde usuários possam assistir a tutoriais em vídeo, identificar instantaneamente os produtos de maquiagem utilizados neles e adquiri-los diretamente.

Complementarmente, a plataforma oferecerá uma aba social inspirada no Instagram, permitindo que a comunidade compartilhe looks, interaja e descubra novas tendências, tudo em um ambiente coeso e focado em beleza.

## Requisitos Funcionais

- RF01 — O sistema deve permitir que usuários assistam a vídeos tutoriais de maquiagem.
- RF02 — O sistema deve exibir os produtos de maquiagem utilizados em cada tutorial, com links diretos para compra.
- RF03 — O sistema deve possibilitar a compra de produtos através de um carrinho de compras e processo de checkout.
- RF04 — O sistema deve oferecer uma aba social (feed) onde usuários podem postar fotos de maquiagens, seguir outros usuários e interagir (curtir, comentar).
- RF05 — O sistema deve permitir que usuários criem e gerenciem seus perfis, incluindo informações pessoais e histórico de compras.
- RF06 — O sistema deve disponibilizar busca e filtragem para tutoriais e produtos.
- RF07 — O sistema deve permitir que criadores de conteúdo façam upload de seus próprios vídeos tutoriais e marquem os produtos utilizados.

## Requisitos Não Funcionais

- **RNF01 — Usabilidade**: a interface deve ser intuitiva e de fácil navegação, garantindo que usuários de diferentes níveis de familiaridade com tecnologia possam utilizá-la sem dificuldades. O tempo de aprendizado das funcionalidades principais deve ser mínimo.
- **RNF02 — Desempenho**: o sistema deve carregar páginas e vídeos em no máximo 3 segundos, mesmo em horários de pico, e o checkout deve ser concluído em menos de 5 segundos para garantir uma experiência de compra fluida.
- **RNF03 — Segurança**: o sistema deve proteger os dados pessoais e financeiros dos usuários através de criptografia (SSL/TLS) e seguir as melhores práticas de prevenção de acessos não autorizados e vazamento de informações. As transações de pagamento devem ser PCI DSS compliant.
- **RNF04 — Disponibilidade**: o sistema deve estar disponível 99,9% do tempo, minimizando interrupções e garantindo acesso contínuo.
- **RNF05 — Escalabilidade**: a arquitetura deve suportar aumento significativo no número de usuários e no volume de dados (vídeos, produtos, posts) sem degradação perceptível do desempenho.

## Arquitetura e Tecnologias

Padrão arquitetural: Microsserviços (com API Gateway).

Linguagem: HTML, JavaScript e CSS.

Banco de dados: SQLite — justificativa: leveza, simplicidade e facilidade de integração, especialmente em projetos acadêmicos; diferente de MySQL ou PostgreSQL, não necessita de um servidor separado para funcionar.

Front-end / Interface: React.js com Next.js — justificativa: React.js permite interfaces dinâmicas e reativas, essenciais para a experiência de e-commerce e feed social. Next.js adiciona Server-Side Rendering (SSR) e geração de sites estáticos, melhorando o SEO (crucial para descoberta de produtos e tutoriais) e o desempenho inicial, além de simplificar o roteamento e a gestão de APIs.

Hospedagem / Deploy: GitHub e Google Drive — GitHub para hospedagem e versionamento eficiente do código, permitindo controle de versões e acompanhamento de todas as alterações.

Outras ferramentas: Google Drive — adotado como armazenamento, oferece praticidade no compartilhamento de arquivos e segurança no armazenamento em nuvem, evitando perda de dados.

## Fluxo Principal do Usuário

Cenário: usuário busca um tutorial de maquiagem, identifica os produtos e realiza uma compra.

1. Login/Cadastro: o usuário acessa a plataforma AnnyvvMake e faz login com suas credenciais ou cria uma nova conta.
2. Navegação/Busca de Tutorial: após o login, é direcionado à página inicial, onde pode navegar por tutoriais em destaque, comprar maquiagem à sua escolha ou usar a barra de busca para encontrar um tutorial específico ou produtos (ex.: "tutorial de delineado").
3. Visualização do Tutorial: o usuário seleciona um tutorial e começa a assistir. Durante a reprodução, uma interface lateral ou sobreposta exibe os produtos utilizados no momento ou em pontos específicos do vídeo.
4. Identificação e Seleção de Produtos: ao ver um produto de interesse, o usuário clica para ver detalhes (marca, preço, descrição, avaliações) e pode adicioná-lo ao carrinho.
5. Adição ao Carrinho e Continuação da Compra: o usuário adiciona um ou mais produtos ao carrinho; pode continuar navegando por outros tutoriais/produtos ou prosseguir para o checkout.
6. Checkout e Pagamento: no carrinho, o usuário revisa os itens, informa o endereço de entrega, seleciona a forma de pagamento e finaliza a compra, recebendo confirmação do pedido.
7. Confirmação e Acompanhamento: após a compra, recebe e-mail de confirmação e acompanha o status do pedido pelo seu perfil na plataforma.

## Autoavaliação do Escopo

Acredito que este projeto é viável dentro do prazo de um TCC, considerando o tempo disponível, a equipe (com divisão clara de tarefas) e a dificuldade técnica, pelos seguintes motivos:

Foco nas funcionalidades essenciais: o escopo inicial pode se concentrar no core — visualização de tutoriais com identificação de produtos, fluxo de compra simplificado e funcionalidade básica da aba social (postar e visualizar). Recursos mais avançados, como sistemas de recomendação complexos ou ferramentas de edição de vídeo integradas, ficam para fases futuras.

[A FAZER] Complementar a autoavaliação em prosa: detalhar viabilidade no prazo, MVP x extras, riscos técnicos e mitigação, e divisão de responsabilidades entre as três integrantes.
