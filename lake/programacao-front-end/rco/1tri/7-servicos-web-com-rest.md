---
titulo: "Serviços Web com REST"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 1
ordem_rco: 7
serie: 2
aula_rco: "Aula 07"
slides: 21
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/7-servicos-web-com-rest/7-servicos-web-com-rest.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/7-servicos-web-com-rest/AULA 07_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/7-servicos-web-com-rest/AULA 07_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Serviços Web com REST

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO FRONT-END
- 2ª Série
- Serviços Web com REST
- Aula 07

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Codificar aplicações e rotinas utilizando linguagens de programação específicas.
- Estruturar arquitetura dos elementos de conteúdo de websites.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Entender como funciona o serviço web REST
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store

_4 imagem(ns) no slide._

### Slide 5 (oculto)

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!
- Tipos de dados:
- https://cursos.alura.com.br/course/http-fundamentos/task/25398

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Você já sabe como é feita a requisição HTTP, seja ela GET ou POST, onde o método GET utilizado para requisitar recursos em um servidor. Ele é o método mais comum e amplamente utilizado para obter informações de um servidor, geralmente através da URL. O método POST usado para enviar dados a um servidor para processamento.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Já estudamos como o modelo de requisição-resposta funciona usando o browser para esse estudo. Mas será que toda a requisição HTTP sempre tem como origem um navegador? E toda resposta só possui conteúdo que ele entende: HTML, CSS, Javascript e imagens? O que normalmente você faz quando não entende uma solicitação que fizeram a você?
- 3 minutos
- Conversem e apresentem suas visões

_3 imagem(ns) no slide._

### Slide 8

- Conceituando
- Serviços na web com REST (Representational State Transfer) são uma abordagem para criar aplicações distribuídas na web usando o protocolo HTTP. REST é uma arquitetura de software que permite que diferentes sistemas se comuniquem de forma clara e eficiente, tornando-os independentes de plataformas, linguagens e tecnologias.
- Fonte https://gocoding.org/wp-content/uploads/2019/06/Restful-Web-Services.png

_2 imagem(ns) no slide._

### Slide 9

- Conceituando
- Os serviços REST são baseados em recursos, que são representados como URI (Uniform Resource Identifier) e são acessados ​​usando métodos HTTP, como GET, POST, PUT e DELETE. Cada recurso pode ser acessado usando uma URL única e os métodos HTTP determinam a ação a ser realizada no recurso, como obter, criar, atualizar ou excluir.
- Fonte https://gocoding.org/wp-content/uploads/2019/06/Restful-Web-Services.png

_2 imagem(ns) no slide._

### Slide 10

- Conceituando
- Os serviços REST são frequentemente usados ​​para criar APIs (Application Programming Interfaces) que permitem que aplicativos clientes acessem e interajam com dados em um servidor remoto. As respostas são frequentemente fornecidas em formatos como JSON ou XML, facilitando a integração com diferentes aplicativos e plataformas.
- Fonte https://gocoding.org/wp-content/uploads/2019/06/Restful-Web-Services.png

_2 imagem(ns) no slide._

### Slide 11

- Conceituando
- A abordagem REST tem se tornado popular por ser simples, escalável e fácil de ser implementada, tornando-a uma escolha comum para a criação de serviços na web.
- Fonte https://gocoding.org/wp-content/uploads/2019/06/Restful-Web-Services.png

_2 imagem(ns) no slide._

### Slide 12

- Conceituando
- O REST (Representational State Transfer) é amplamente utilizado em vários tipos de aplicações na web, incluindo:
- APIs de terceiros: Muitos sites e aplicativos utilizam APIs REST para obter dados de outras fontes e integrá-los em suas próprias aplicações.
- Aplicativos móveis: As APIs REST são frequentemente usadas para construir aplicativos móveis que precisam acessar dados em um servidor remoto.
- Fonte https://gocoding.org/wp-content/uploads/2019/06/Restful-Web-Services.png

_2 imagem(ns) no slide._

### Slide 13

- Conceituando
- Integração de sistemas: O REST é amplamente utilizado para integrar diferentes sistemas, permitindo que eles se comuniquem de forma eficiente e independente de plataforma.
- Microserviços: O REST é frequentemente usado para criar microserviços, que são pequenos serviços independentes que podem ser combinados para formar aplicações maiores.
- Cloud computing: As APIs REST são amplamente utilizadas em aplicações de nuvem para acessar serviços e recursos em diferentes locais.
- Fonte https://gocoding.org/wp-content/uploads/2019/06/Restful-Web-Services.png

_2 imagem(ns) no slide._

### Slide 14

- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/http-fundamentos

_2 imagem(ns) no slide._

### Slide 15

- Serviços Web -REST
- Nessa aula veremos como as aplicações conseguem se comunicar e responder as questões levantadas anteriormente.
- Link para tarefa: https://cursos.alura.com.br/course/http-fundamentos/task/25371
- Um exemplo clássico é o login via rede social que estamos cada vez mais habituados. Essa conversa acaba sendo transparente para nós, usuários, já que exige uma autorização de acesso às nossas informações.
- 9 minutos
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 16

- Serviços Web -REST
- Nessa aula veremos como as aplicações conseguem se comunicar e responder as questões levantadas anteriormente.
- Link para tarefa: https://cursos.alura.com.br/course/http-fundamentos/task/26032
- Um exemplo clássico é o login via rede social que estamos cada vez mais habituados. Essa conversa acaba sendo transparente para nós, usuários, já que exige uma autorização de acesso às nossas informações.
- 6 minutos
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 17

- O que vimos na aula de hoje:
- O que é web service
- O que é web servisse REST
- Principal finalidade do REST

### Slide 18

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 19

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 20

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

### Slide 21

_(sem texto)_

## Atividade

_Fonte: AULA 07_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 07

Questão 1

O que é o REST (Representational State Transfer)?

A) Um protocolo para transferência de dados entre servidores na Internet

B) Uma linguagem de programação para desenvolvimento de aplicações web

C) Um conjunto de regras para projetar aplicações na web

D) Uma biblioteca de componentes de interface de usuário para a web

Resposta correta: C) Um conjunto de regras para projetar aplicações na web

Questão 2

Qual é a principal vantagem do uso do REST na arquitetura de aplicações da web?

A) Permite a integração de diferentes sistemas através da Internet

B) Oferece uma alta performance na transferência de dados

C) Facilita o desenvolvimento de aplicações web

D) Permite o compartilhamento de recursos em rede

Resposta correta: A) Permite a integração de diferentes sistemas através da Internet

## Prática

_Fonte: AULA 07_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 07

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender o que são serviços web e a arquitetura REST, reconhecendo sua finalidade.
- Identificar recursos, URLs e métodos HTTP utilizados em serviços REST.
- Reconhecer que nem toda requisição HTTP parte de um navegador, entendendo a comunicação entre sistemas.
- Desenvolver visão prática sobre APIs REST, relacionando com aplicações reais (sites, apps e integrações).
Produto final esperado:

- Análise simples de um serviço web REST, identificando recurso, método HTTP e formato de resposta.

##### 2. Ferramentas Recomendadas

###### Navegador Web (Google Chrome, Edge ou Firefox)

- Para que serve: acessar URLs de serviços web REST.
- Por que é adequada: permite visualizar respostas REST diretamente.
- Como facilita o aprendizado: torna visível a comunicação entre sistemas.

###### Ferramentas de Desenvolvedor do Navegador

- Para que serve: visualizar requisições e respostas HTTP.
- Por que é adequada: aproxima o aluno do ambiente profissional.
- Como facilita o aprendizado: permite observar respostas em JSON ou XML.

###### Plataforma Alura

- Para que serve: reforçar o conteúdo com atividades guiadas.
- Por que é adequada: material introdutório alinhado ao tema REST.
- Como facilita o aprendizado: complementa a prática realizada em sala.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Computador ou notebook
- Navegador web atualizado
- Conexão com a internet
- Acesso institucional à plataforma Alura
- Ambiente: laboratório de informática ou sala multimídia
Link de apoio: https://cursos.alura.com.br/course/http-fundamentos

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações necessárias

- Testar previamente o acesso à internet.
- Separar exemplos simples de URLs de APIs públicas.
- Manter o navegador aberto para demonstração.

###### Condução da aula

1. Contextualização inicial (5 min)

- Retomar GET e POST.
- Lançar a questão: “Toda comunicação HTTP vem de um navegador?”
2. Demonstração do professor (15 min)

- Acessar uma URL de serviço REST.
- Mostrar que:
- Não há interface visual tradicional.
- O retorno é em dados (ex.: JSON).
- Explicar:
- Recurso
- URL
- Método HTTP
3. Prática guiada dos alunos (20 min)

- Alunos acessam serviços REST simples.
- Identificam:
- Recurso acessado
- Método HTTP
- Tipo de resposta
4. Discussão e fechamento (10 min)

- Compartilhamento das observações.
- Conexão com exemplos reais (login social, apps).

###### Pontos de atenção

- Evitar implementação de código.
- Manter foco no conceito e na leitura da resposta.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá analisar um serviço web REST, observando como ocorre a comunicação entre aplicações.

Problema real simulado: Entender como aplicativos e sistemas diferentes trocam informações.

Habilidade desenvolvida: Interpretação técnica básica de serviços web REST.

##### 6. Metodologia Ativa Utilizada

- Ensino por descoberta
- Experimentação
- Aprendizagem contextualizada
- Elementos de Lemov aplicados:
- Estabelecer propósito
- Prática guiada
- Checagem de compreensão
- Feedback imediato

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Abra o navegador web.
- Acesse uma URL de serviço web REST indicada pelo professor.
- Observe o conteúdo retornado.
- Identifique:
- O recurso acessado
- O método HTTP utilizado
- Verifique o formato da resposta (JSON ou XML).
- Anote suas observações.
- Responda: “Por que esse serviço não precisa de uma interface visual?”

##### 8. Exemplo ou Demonstração

Exemplo conceitual de serviço REST:

- URL: /usuarios
- Método: GET
- Recurso: lista de usuários
- Resposta: dados estruturados (JSON)
Explicação: O serviço REST fornece dados para outros sistemas, não para usuários finais diretamente.

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Identificação correta de um recurso REST.
- Reconhecimento do método HTTP utilizado.
- Compreensão básica do formato de resposta.
O professor verifica o aprendizado pela clareza da análise.

##### 10. Formato de Entrega da Atividade

- Formato: resposta escrita (caderno, formulário ou AVA).
- Conteúdo: identificação do serviço REST + observações.
- Entrega: ao final da aula ou como atividade complementar.
- Prazo sugerido: até a próxima aula.

##### 11. Encerramento e Reflexão

O professor encerra com perguntas orientadoras:

- Onde usamos serviços REST no dia a dia?
- Por que REST é importante para integração de sistemas?
- Como esse conceito se conecta com front-end e back-end?
