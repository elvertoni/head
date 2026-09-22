---
titulo: "O Cliente Pede e o Servidor Responde"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 1
ordem_rco: 4
serie: 2
aula_rco: "Aula 04"
slides: 21
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/4-o-cliente-pede-e-o-servidor-responde/4-o-cliente-pede-e-o-servidor-responde.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/4-o-cliente-pede-e-o-servidor-responde/AULA 04_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/4-o-cliente-pede-e-o-servidor-responde/AULA 04_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# O Cliente Pede e o Servidor Responde

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO FRONT-END
- 2ª Série
- O Cliente Pede e o Servidor Responde
- Aula 04

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
- Entender o modelo de requisição cliente servidor.
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
- Link para o curso: https://cursos.alura.com.br/course/http-fundamentos

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Aprendemos o que é o domínio de acesso, como é feito o acesso a sites e seus recursos, agora precisamos entender como funciona essa conversa entre cliente e servidor de acesso.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Na escola quando precisamos fazer algo, requisitamos ao professor ou responsável do local, para acessar um site também é necessário requisitar o acesso a um local específico, chamado de servidor, principalmente quando necessita de usuário e senha de acesso.
- Conversem entre vocês e imaginem como esse processo deve funcionar.

_1 imagem(ns) no slide._

### Slide 8

- Conceituando
- O conceito de cliente-servidor é um modelo de arquitetura de computadores onde o servidor oferece recursos, serviços e informações para um ou mais clientes. O cliente envia uma solicitação para o servidor e o servidor retorna uma resposta. Esse modelo é amplamente utilizado na internet e na rede de computadores.
- Fonte https://upload.wikimedia.org/wikipedia/commons/1/1c/Cliente-Servidor.png

_1 imagem(ns) no slide._

### Slide 9

- Conceituando
- No modelo cliente-servidor, o cliente envia uma requisição ao servidor via rede, geralmente usando protocolos de rede padrão como o HTTP ou o TCP/IP. O servidor, então, processa a solicitação e retorna uma resposta ao cliente.
- Fonte https://upload.wikimedia.org/wikipedia/commons/1/1c/Cliente-Servidor.png

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- Essa resposta pode ser uma página web, dados de uma aplicação ou outro tipo de informação. O cliente exibe a resposta para o usuário final. Esse modelo é escalável, pois permite que vários clientes acessem o mesmo servidor ao mesmo tempo.
- Fonte https://upload.wikimedia.org/wikipedia/commons/1/1c/Cliente-Servidor.png

_1 imagem(ns) no slide._

### Slide 11

- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/http-fundamentos

_2 imagem(ns) no slide._

### Slide 12

- Modelo requisição e resposta
- No modelo requisição-resposta cliente-servidor, o cliente envia uma requisição específica ao servidor, incluindo informações como o endereço da página web desejada ou os parâmetros de uma consulta de banco de dados.
- Link para tarefa: https://cursos.alura.com.br/course/http-fundamentos/task/25394
- O servidor, então, processa a requisição, realiza qualquer ação necessária (como buscar informações em um banco de dados ou gerar uma página web dinâmica) e retorna uma resposta ao cliente. A resposta inclui informações como o conteúdo da página web solicitada ou o resultado de uma consulta de banco de dados.
- 2 minutos
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 13

- Cookies o que são? É de comer?
- Um cookie é um pequeno arquivo de texto armazenado no navegador de um usuário quando ele visita um site.
- Link para tarefa: https://cursos.alura.com.br/course/http-fundamentos/task/25552
- Os cookies são usados para armazenar informações sobre as preferências do usuário, como idioma selecionado, itens no carrinho de compras e informações de login. Isso permite que o site lembre dessas informações na próxima vez que o usuário visitar o site, o que torna a navegação mais fácil e personalizada.
- 2 minutos
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 14

- Conceituando
- Além disso, os cookies também são usados para rastrear as atividades do usuário na web e para exibir anúncios direcionados. É importante que os usuários estejam cientes de que os cookies podem ser usados para rastrear suas atividades na web e que muitos navegadores permitem que eles sejam bloqueados ou excluídos.
- Fonte https://pxhere.com/pt/photo/1595274

_2 imagem(ns) no slide._

### Slide 15

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- TAREFA PARA CASA!
- Agora que você já sabe o que é cookie, faça uma pesquisa e aponte quais as principais modalidades de ataques cibernéticos que fazem uso de acesso ao cookie.
- Desenvolva uma atividade

_3 imagem(ns) no slide._

### Slide 17

- O que vimos na aula de hoje:
- DESENVOLVIMENTO DE SISTEMAS
- O protocolo HTTP segue o modelo Requisição-Resposta.
- Sempre o cliente inicia a comunicação.
- Uma requisição precisa ter todas as informações para o servidor gerar a resposta.

_2 imagem(ns) no slide._

### Slide 18

- O que vimos na aula de hoje:
- Aprendemos que:
- O protocolo HTTP segue o modelo Requisição-Resposta.
- Sempre o cliente inicia a comunicação.
- Uma requisição precisa ter todas as informações para o servidor gerar a resposta.

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

_Fonte: AULA 04_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 04

Questão 1

O que é o modelo cliente-servidor?

A) Uma estrutura de rede na qual vários servidores compartilham informações entre si

B) Uma estrutura de rede na qual um servidor controla e distribui informações para vários clientes

C) Uma estrutura de rede na qual vários clientes compartilham informações entre si

D) Uma estrutura de rede na qual um cliente controla e distribui informações para vários servidores

Resposta correta: B) Uma estrutura de rede na qual um servidor controla e distribui informações para vários clientes

Comentário: O modelo cliente-servidor é uma estrutura de rede na qual um servidor é responsável por armazenar, processar e distribuir informações para vários clientes. Os clientes são dispositivos ou programas que solicitam e recebem informações do servidor, como computadores, smartphones ou navegadores da web. Esse modelo é amplamente utilizado na internet e em muitas outras redes, pois permite a distribuição eficiente de informações para vários usuários.

Questão 2

Quem é responsável pela armazenamento e processamento de informações no modelo cliente-servidor?

A) Clientes

B) Ambos, clientes e servidores

C) Nenhum, as informações são processadas e armazenadas em dispositivos externos

D) Servidores

Resposta correta: D) Servidores

Comentário: No modelo cliente-servidor, o servidor é responsável por armazenar e processar as informações. Os clientes são dispositivos ou programas que solicitam informações ao servidor e as recebem, mas não armazenam ou processam as informações. Esse modelo é eficiente porque permite que as informações sejam processadas e armazenadas em um único lugar e depois distribuídas para vários clientes, o que economiza recursos de hardware e torna a rede mais escalável e flexível.

## Prática

_Fonte: AULA 04_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 04

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender o modelo de comunicação cliente-servidor, identificando o papel de cada elemento.
- Reconhecer o funcionamento do modelo requisição–resposta, base do protocolo HTTP.
- Identificar situações reais em que o cliente envia dados e o servidor responde, como login e acesso a sistemas.
- Desenvolver a habilidade de análise técnica básica, necessária para interpretar requisitos de websites.
Produto final esperado:

- Descrição estruturada do fluxo cliente → servidor → resposta, com exemplos reais de navegação.

##### 2. Ferramentas Recomendadas

###### Navegador Web (Google Chrome, Edge ou Firefox)

- Para que serve: acessar sites e simular requisições ao servidor.
- Por que é adequada: representa o papel do cliente no modelo cliente-servidor.
- Como facilita o aprendizado: permite observar o processo real de requisição e resposta.

###### Ferramentas de Desenvolvedor do Navegador

- Para que serve: visualizar requisições HTTP, respostas e cookies.
- Por que é adequada: aproxima o aluno do ambiente profissional.
- Como facilita o aprendizado: torna visível o fluxo técnico sem exigir programação.

###### Plataforma Alura

- Para que serve: reforçar o conteúdo com atividades práticas guiadas.
- Por que é adequada: conteúdo alinhado ao tema da aula.
- Como facilita o aprendizado: complementa a prática com exemplos didáticos.

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

- Testar acesso à internet.
- Ter um site com área de login para demonstração.
- Abrir previamente as Ferramentas de Desenvolvedor.

###### Condução da aula

1. Contextualização inicial (5 min)

- Retomar domínios e URLs.
- Apresentar a analogia da escola: pedir autorização para acessar algo.
2. Demonstração do professor (15 min)

- Acessar um site com login.
- Mostrar que:
- O navegador envia uma requisição.
- O servidor processa.
- O servidor responde.
- Introduzir o conceito de cookies de forma simples.
3. Prática guiada dos alunos (20 min)

- Alunos acessam sites comuns.
- Observam requisições ao atualizar páginas.
- Identificam cookies armazenados no navegador.
4. Revisão e fechamento (10 min)

- Discussão coletiva.
- Reforço do modelo requisição–resposta.

###### Pontos de atenção

- Evitar detalhar ataques cibernéticos nesta aula.
- Manter o foco no fluxo de comunicação.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá analisar como ocorre a comunicação entre cliente e servidor ao acessar um site, identificando requisição, resposta e uso de cookies.

Problema real simulado: Entender como sistemas web funcionam quando solicitamos acesso a informações.

Habilidade desenvolvida: Interpretação técnica do funcionamento básico de sistemas web.

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
- Acesse um site que você utiliza com frequência.
- Atualize a página observando o carregamento.
- Abra as Ferramentas de Desenvolvedor.
- Identifique uma requisição feita ao servidor.
- Observe a resposta recebida.
- Localize a seção de cookies do site.
- Registre suas observações.
- Responda: “Por que os cookies são usados?”

##### 8. Exemplo ou Demonstração

Exemplo de fluxo:

- Cliente (navegador) → envia requisição
- Servidor → processa dados
- Servidor → envia resposta
- Cliente → exibe o conteúdo ao usuário
Exemplo prático: Login em um site → envio de dados → validação → acesso liberado.

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Explicação clara do modelo cliente-servidor.
- Identificação correta de requisição e resposta.
- Compreensão básica do papel dos cookies.
O professor verifica o aprendizado pela clareza e coerência da explicação.

##### 10. Formato de Entrega da Atividade

- Formato: resposta escrita (caderno, formulário ou AVA).
- Conteúdo: explicação do fluxo cliente-servidor + observações.
- Entrega: ao final da aula ou como tarefa complementar.
- Prazo sugerido: até a próxima aula.

##### 11. Encerramento e Reflexão

O professor finaliza com perguntas orientadoras:

- Por que o cliente sempre inicia a comunicação?
- O que acontece se a requisição estiver incompleta?
- Como esse modelo influencia o desenvolvimento de websites?
