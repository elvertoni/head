---
titulo: "O que é HTTP?"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 1
ordem_rco: 1
serie: 2
aula_rco: "Aula 01"
slides: 19
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PFE/1TRI/1-o-que-e-http/1-o-que-e-http.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/1-o-que-e-http/AULA 01_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/1-o-que-e-http/AULA 01_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# O que é HTTP?

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO FRONT-END
- 2ª Série
- O que é HTTP?
- Aula 01

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Prestar apoio técnico na elaboração da documentação de sistemas.
- Identificar requisitos técnicos para projetos de websites.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Aprender o que é o HTTP no acesso a sites.
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store

_5 imagem(ns) no slide._

### Slide 5 (oculto)

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!

_2 imagem(ns) no slide._

### Slide 6

- Para pensarmos juntos...
- Acessar páginas na internet é algo comum hoje em dia, mas você tem ideia de como é feito tal acesso? Qualquer computador pode acessar qualquer página, e páginas restritas? Como é feito o acesso? Para todas essas perguntas temos apenas uma resposta.
- O que vocês pensam sobre isso?

_1 imagem(ns) no slide._

> **Notas do apresentador:** Em caso de falta ou indisponibilidade de acesso a internet no local de aula, você poderá utilizar os seguintes artigo para criação de material complementar para auxiliar na aula: Para saber mais: Peer-To-Peer: https://cursos.alura.com.br/course/http-fundamentos/task/25442 Arquitetura do site Alura: https://cursos.alura.com.br/course/http-fundamentos/task/25444

### Slide 7

- Conceituando
- HTTP é um protocolo de comunicação para transferência de hipertexto na World Wide Web. Ele define como mensagens são formatadas e transmitidas, e o que acontece quando um navegador web solicita uma página da web a um servidor web.
- Fonte https://upload.wikimedia.org/wikipedia/commons/8/83/Internet1.svg

_1 imagem(ns) no slide._

### Slide 8

- Conceituando
- A principal finalidade do protocolo HTTP é permitir a transferência de dados (normalmente hipertexto) na World Wide Web, permitindo que navegadores web acessem e exibam páginas da web em sistemas cliente.
- Fonte https://upload.wikimedia.org/wikipedia/commons/8/83/Internet1.svg

_1 imagem(ns) no slide._

### Slide 9

- Conceituando
- HTTP é importante porque é o protocolo padrão para a transferência de dados na World Wide Web e é usado por milhões de pessoas a cada dia para acessar e compartilhar informações online. Além disso, ele permite a integração de diversos tipos de mídia, como texto, imagens, vídeos e som, em uma única página da web.
- Fonte https://upload.wikimedia.org/wikipedia/commons/8/83/Internet1.svg

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- Existem alguns serviços na web que não usam o protocolo HTTP, mas eles são minoria. Alguns exemplos incluem aplicações de comunicação em tempo real, como jogos online, bate-papo, voz e vídeo, que usam protocolos diferentes, como o WebSockets, RTSP e SIP. Além disso, aplicações de transferência de arquivos de grande porte, como o BitTorrent, também não usam o HTTP. No entanto, a maioria dos sites e aplicativos na web usa o HTTP para transferir dados.
- Fonte https://upload.wikimedia.org/wikipedia/commons/8/83/Internet1.svg

_1 imagem(ns) no slide._

### Slide 11

- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/http-fundamentos

_2 imagem(ns) no slide._

### Slide 12

- O protocolo HTTP
- O protocolo HTTP surgiu no final dos anos 80, quando a Web ainda estava em sua infância. Ele foi criado pelo cientista da computação britânico Tim Berners-Lee, que também é o criador da World Wide Web.
- Link para tarefa: https://cursos.alura.com.br/course/http-fundamentos/task/25368
- A ideia era criar um protocolo simples e eficiente para transferir documentos hipertexto entre sistemas, tornando a Web acessível para usuários comuns. O primeiro servidor HTTP foi implementado em 1991, e desde então o protocolo tem sido amplamente adotado e evoluído para atender às crescentes demandas da Web.
- 2 minutos
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 13

- Como funciona o HTTP?
- O protocolo HTTP funciona como um sistema de solicitação-resposta. Quando um navegador web faz uma solicitação a um servidor web, ele envia uma mensagem HTTP que inclui informações sobre a página da web que está sendo solicitada.
- Link para tarefa: https://cursos.alura.com.br/course/http-fundamentos/task/25367
- O servidor web então processa a solicitação, buscando a página da web especificada, e envia uma resposta HTTP de volta ao navegador. A resposta inclui o conteúdo da página da web, juntamente com informações adicionais, como o tipo de conteúdo, o estado da solicitação e as informações de autenticação.
- 2 minutos
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 14

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 15

- TAREFA PARA CASA!
- Agora que você já sabe o que é o HTTP, pesquise qual a diferença entre o HTTP e o HTTPS, a resposta teremos na próxima aula.
- Desenvolva uma atividade

_2 imagem(ns) no slide._

### Slide 16

- O que vimos na aula de hoje:
- A arquitetura Cliente-Servidor.
- Um protocolo é um conjunto de regras.
- HTTP é um protocolo que define as regras de comunicação entre cliente e servidor na internet.

### Slide 17

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 18

- Referências
- BEAULIEU, Alan. SQL: Guia Prático Para Manipulação de Dados. São Paulo: O'Reilly, 2008.
- CHACON, Scott; STRAUB, Ben. Pro Git. 2ª ed. Berkeley: Apress, 2014.
- DELISLE, Marc. MySQL: Guia do Programador. São Paulo: Novatec, 2010.
- FURGERI, Sérgio. SQL - Curso Prático. São Paulo: Novatec, 2018.
- LOELIGER, Jon; MCCULLOUGH, Matthew. Version Control with Git: Powerful Tools and Techniques for Collaborative Software Development. 2ª ed. Sebastopol: O'Reilly Media, 2012.
- SAMPAIO, Cleuton. Banco de Dados SQL: Aprenda a Construir um Banco de Dados do Zero. São Paulo: Novatec, 2018.
- SANTOS, Rafael. Administração de Banco de Dados: SQL Server 2017. São Paulo: Novatec, 2018.
- SILVERMAN, Richard E. Git Pocket Guide: A Working Introduction. Sebastopol: O'Reilly Media, 2013.
- STANEK, William. SQL Server 2019: Guia Completo do Administrador de Banco de Dados. São Paulo: Novatec, 2019.
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

### Slide 19

_(sem texto)_

## Atividade

_Fonte: AULA 01_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 01

Questão 1

Qual é a principal utilização do HTTP?

A) Armazenar e compartilhar arquivos na internet

B) Executar aplicativos e jogos online

C) Transferir e receber dados entre servidores e clientes na web

D) Enviar e receber e-mails

Resposta correta: C) Transferir e receber dados entre servidores e clientes na web

Questão 2

O HTTP é um protocolo de comunicação:

A) Cliente-servidor

B) Ponto-a-ponto

C) Peer-to-peer

D) Baseado em mensagem

Resposta correta: A) Cliente-servidor

Comentários: HTTP (Hypertext Transfer Protocol) é um protocolo de comunicação cliente-servidor usado para transferir dados, como páginas da web, imagens e arquivos, entre os servidores da web e os navegadores dos clientes. Ele é responsável por estabelecer conexões seguras e confiáveis entre os dispositivos e permite que os usuários da internet acessem e compartilhem informações de maneira eficiente e segura.

## Prática

_Fonte: AULA 01_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 01

##### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante será capaz de:

- Compreender, na prática, como funciona o protocolo HTTP no acesso a páginas da web.
- Identificar o fluxo de comunicação cliente-servidor, reconhecendo o papel do navegador e do servidor.
- Desenvolver a habilidade de análise técnica básica, interpretando requisições e respostas HTTP em situações reais de navegação.
- Relacionar o conceito de protocolo HTTP com o desenvolvimento de websites, conectando teoria e prática profissional.
Produto final esperado do aluno:

- Análise simples do funcionamento do HTTP durante o acesso a um site, com identificação do processo de solicitação e resposta.

##### 2. Ferramentas Recomendadas

###### Navegador Web (Google Chrome ou Firefox)

- Para que serve: acessar páginas web e visualizar a comunicação HTTP.
- Por que é adequada: permite observar o funcionamento real do protocolo.
- Como facilita o aprendizado: torna o conceito abstrato visível na prática.

###### Ferramentas de Desenvolvedor do Navegador

- Para que serve: inspecionar requisições e respostas HTTP.
- Por que é adequada: faz parte do ambiente profissional de desenvolvimento web.
- Como facilita o aprendizado: permite observar status, tipos de requisição e respostas do servidor.

###### Plataforma Alura (acesso gratuito institucional)

- Para que serve: reforçar o conteúdo com atividades guiadas.
- Por que é adequada: apresenta explicações claras e progressivas.
- Como facilita o aprendizado: complementa a aula prática com exercícios contextualizados.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Navegador web atualizado
- Acesso à internet
- Conta institucional para acesso à plataforma Alura
- Laboratório de informática, sala multimídia ou notebook individual
- Acesso ao link do curso: https://cursos.alura.com.br/course/http-fundamentos

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações necessárias

- Testar previamente o acesso à internet.
- Abrir um navegador com as Ferramentas de Desenvolvedor prontas.
- Ter um site simples para demonstração (ex.: portal institucional ou site público).

###### Fluxo da aula

1. Abertura e contextualização (5 min)

- Retomar a pergunta provocadora: “Como o computador consegue acessar uma página da internet?”
- Estimular hipóteses dos alunos.
2. Demonstração pelo professor (15 min)

- Acessar um site ao vivo.
- Abrir as Ferramentas de Desenvolvedor.
- Mostrar o carregamento da página e explicar:
- Cliente (navegador)
- Servidor
- Solicitação (request)
- Resposta (response)
3. Prática guiada dos alunos (20 min)

- Alunos repetem o processo em seus computadores.
- Professor circula orientando e esclarecendo dúvidas.
4. Revisão e fechamento (10 min)

- Discussão coletiva sobre o que foi observado.
- Conexão com o desenvolvimento de sistemas.

###### Pontos de atenção

- Alunos podem confundir internet com site: reforçar a diferença.
- Evitar aprofundar em códigos ou detalhes técnicos avançados nesta aula.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá simular o papel de um analista iniciante, observando como ocorre o acesso a um site e explicando o funcionamento do protocolo HTTP.

Problema real simulado: Compreender como páginas web são acessadas antes de iniciar o desenvolvimento de sistemas web.

Habilidade desenvolvida: Leitura e interpretação do fluxo cliente-servidor via HTTP.

##### 6. Metodologia Ativa Utilizada

- Experimentação
- Ensino por descoberta
- Aprendizagem contextualizada
- Elementos de Lemov aplicados:
- Estabelecer propósito
- Checar compreensão
- Prática guiada
- Feedback imediato

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Abra o navegador web.
- Acesse um site indicado pelo professor.
- Abra as Ferramentas de Desenvolvedor.
- Atualize a página observando o carregamento.
- Identifique:
- Quem faz a solicitação.
- Quem envia a resposta.
- Anote o que acontece durante o acesso.
- Finalize registrando suas observações.

##### 8. Exemplo ou Demonstração

Exemplo ilustrativo:

- Navegador → solicita página (HTTP Request)
- Servidor → envia página (HTTP Response)
- Página é exibida no navegador
Fluxo simplificado:

Cliente → HTTP → Servidor Servidor → HTTP → Cliente

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Explicação simples e correta sobre o que é HTTP.
- Identificação clara do papel do cliente e do servidor.
- Demonstração de compreensão do processo de solicitação e resposta.
O professor verifica o objetivo por meio da explicação oral ou registro escrito.

##### 10. Formato de Entrega da Atividade

- Formato: resposta escrita curta ou registro no caderno / ambiente virtual.
- Conteúdo: explicação do funcionamento do HTTP no acesso a um site.
- Entrega: ao final da aula ou na próxima aula.
- Prazo sugerido: imediato ou até a aula seguinte.

##### 11. Encerramento e Reflexão

O professor conduz a reflexão final com perguntas como:

- O que acontece quando digitamos um endereço no navegador?
- Por que o HTTP é fundamental para a web?
- Como esse conceito se conecta com o desenvolvimento de sites?
