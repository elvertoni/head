---
titulo: "Parâmetros de Requisição e Resposta"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 1
ordem_rco: 6
serie: 2
aula_rco: "Aula 06"
slides: 21
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/6-parametros-de-requisicao-e-resposta/6-parametros-de-requisicao-e-resposta.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/6-parametros-de-requisicao-e-resposta/AULA 06_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/6-parametros-de-requisicao-e-resposta/AULA 06_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Parâmetros de Requisição e Resposta

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO FRONT-END
- 2ª Série
- Parâmetros de Requisição e Resposta
- Aula 06

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
- Compreender sobre parâmetros de requisição.
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
- Parâmetros na URL:
- https://cursos.alura.com.br/course/http-fundamentos/task/25587
- Outros métodos HTTP e Web Services:
- https://cursos.alura.com.br/course/http-fundamentos/task/25588

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Você compreendeu como fazer uma depuração de requisição HTTP, por isso hoje iremos aprender mais sobre os parâmetros da requisição.

_2 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Você já compreender coo funciona a comunicação HTTP, agora precisamos compreender quais são os parâmetros que permite que essa conexão seja realizada. Quando você realiza uma avaliação, quais são os parâmetros que são passados para a realização da prova? Conseguiria listar eles? Lembre-se que parâmetro é uma informação adicional necessária para a realização ou conclusão de algum processo.
- 3 minutos
- Conversem e apresentem suas visões

_3 imagem(ns) no slide._

### Slide 8

- Conceituando
- Um parâmetro é uma variável que é passada para uma função, procedimento ou algoritmo, com o objetivo de fornecer informações adicionais necessárias para o cálculo ou execução correta daquele processo.
- Fonte https://www.publicdomainpictures.net/pictures/230000/nahled/computer-user.jpg

_2 imagem(ns) no slide._

### Slide 9

- Conceituando
- Em outras palavras, os parâmetros são valores que são utilizados para personalizar o comportamento de uma função ou algoritmo para atender às necessidades específicas da tarefa que está sendo executada.
- Fonte: https://blog.ida.cl/marketing-digital/parametros-utm-google-analytics/

_2 imagem(ns) no slide._

### Slide 10

- Conceituando
- Os parâmetros de requisição HTTP são valores adicionais que são enviados pelo cliente para o servidor com a finalidade de fornecer informações adicionais ou especificar o comportamento desejado para a requisição HTTP. Esses parâmetros são enviados na URL ou no corpo da mensagem HTTP e são usados pelo servidor para determinar como processar a requisição.
- Fonte: https://fator.ag/blog/como-utilizar-tracking-de-utm-para-rastrear-campanhas-de-facebook-no-analytics/

_2 imagem(ns) no slide._

### Slide 11

- Conceituando
- Por exemplo, os parâmetros de requisição podem ser usados para especificar os dados a serem incluídos em uma consulta de banco de dados, ou para fornecer informações adicionais para personalizar o conteúdo retornado pelo servidor.
- Fonte https://neetwork.com/metricas-de-google-analytics/

_1 imagem(ns) no slide._

### Slide 12

- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/http-fundamentos

_2 imagem(ns) no slide._

### Slide 13

- Revendo a aula anterior
- Uma depuração HTTP é o processo de verificação de erros e solução de problemas relacionados ao protocolo HTTP (Hypertext Transfer Protocol) durante a comunicação entre um servidor e um cliente.
- Link para tarefa: https://cursos.alura.com.br/course/http-fundamentos/task/25401
- Aqui está um exemplo de depuração HTTP:
- Verificar código de status HTTP: Verifique se o código de status HTTP retornado pelo servidor é o esperado. Por exemplo, se o código de status for 404 (Não encontrado), significa que o recurso solicitado não pôde ser encontrado no servidor.
- 2 minutos
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 14

- Parâmetros na requisição com métodos GET e POST
- Um parâmetro em uma requisição é uma informação adicional enviada pelo cliente para o servidor, a fim de especificar ou personalizar a ação que o servidor deve realizar.
- Link para tarefa: https://cursos.alura.com.br/course/http-fundamentos/task/25396
- Por exemplo, em uma requisição HTTP, um parâmetro pode ser usado para especificar o ID de um recurso que o cliente deseja obter do servidor, ou para filtrar os resultados de uma consulta de banco de dados. Os parâmetros são geralmente enviados na URL ou no corpo da mensagem da requisição e são usados pelo servidor para processar a requisição de maneira adequada.
- 2 minutos
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 15

- Conceituando
- O método GET é um dos métodos HTTP (Hypertext Transfer Protocol) utilizados para requisitar recursos em um servidor. Ele é o método mais comum e amplamente utilizado para obter informações de um servidor, geralmente através da URL.
- Fonte https://www.computersciencemaster.com.br/get-e-post-com-php/

_2 imagem(ns) no slide._

### Slide 16

- Conceituando
- O método POST é um dos métodos HTTP (Hypertext Transfer Protocol) utilizados para enviar informações para o servidor. Ele é usado principalmente para submeter dados de formulários ou enviar dados em formatos como JSON ou XML.
- Fonte https://dev.to/death2k/artigo-curl-api-get-post-put-delete-fn9

_2 imagem(ns) no slide._

### Slide 17

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 18

- O que vimos na aula de hoje:
- O que é parâmetro de requisição
- O que é o método GET
- O que é o método POST

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

_Fonte: AULA 06_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 06

Questão 1

Qual é o objetivo principal dos parâmetros de requisições HTTP?

a) Armazenar dados permanentemente no servidor

b) Fornecer informações adicionais para o servidor

c) Permitir a transferência de arquivos

d) Garantir a segurança das informações

Resposta correta: b) Fornecer informações adicionais para o servidor

Os parâmetros de requisições HTTP são utilizados para fornecer informações adicionais para o servidor. Eles são enviados na URL ou no corpo da mensagem e permitem ao servidor entender o que o cliente está solicitando e como ele deseja que a informação seja retornada. Isso é importante porque permite que o servidor ajuste a resposta de acordo com as especificações do cliente.

Questão 2

Qual é a diferença entre parâmetros enviados na URL e parâmetros enviados no corpo da mensagem?

a) Parâmetros enviados na URL são mais seguros que os parâmetros enviados no corpo da mensagem

b) Parâmetros enviados no corpo da mensagem são mais seguros que os parâmetros enviados na URL

c) Parâmetros enviados na URL são limitados em tamanho, enquanto os parâmetros enviados no corpo da mensagem não são

d) Parâmetros enviados no corpo da mensagem são limitados em tamanho, enquanto os parâmetros enviados na URL não são

Resposta correta: c) Parâmetros enviados na URL são limitados em tamanho, enquanto os parâmetros enviados no corpo da mensagem não são

Os parâmetros enviados na URL são geralmente limitados em tamanho devido às restrições do tamanho da URL. Isso significa que eles não são adequados para envio de grandes quantidades de dados. Por outro lado, os parâmetros enviados no corpo da mensagem não são limitados em tamanho, o que os torna uma opção melhor para o envio de grandes quantidades de dados. Além disso, os parâmetros enviados no corpo da mensagem também podem ser codificados de maneira diferente, o que significa que eles podem ser usados para enviar tipos de dados diferentes, como arquivos binários.

## Prática

_Fonte: AULA 06_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 06

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender o que são parâmetros de requisição HTTP e sua função na comunicação cliente-servidor.
- Identificar parâmetros enviados em URLs, especialmente em requisições do tipo GET.
- Diferenciar, em nível conceitual, os métodos GET e POST, reconhecendo quando cada um é utilizado.
- Desenvolver habilidade de interpretação técnica, essencial para análise de requisitos de websites.
Produto final esperado:

- Análise simples de URLs com parâmetros, identificando informações enviadas do cliente para o servidor.

##### 2. Ferramentas Recomendadas

###### Navegador Web (Google Chrome, Edge ou Firefox)

- Para que serve: acessar URLs com parâmetros e observar seu comportamento.
- Por que é adequada: permite visualizar parâmetros diretamente na barra de endereços.
- Como facilita o aprendizado: torna o conceito de parâmetro visível e concreto.

###### Ferramentas de Desenvolvedor do Navegador

- Para que serve: visualizar detalhes da requisição HTTP.
- Por que é adequada: ferramenta padrão no ambiente profissional.
- Como facilita o aprendizado: possibilita observar parâmetros sem necessidade de programação.

###### Plataforma Alura

- Para que serve: reforçar o conteúdo com atividades guiadas.
- Por que é adequada: conteúdo introdutório e alinhado ao tema da aula.
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
- Separar exemplos de URLs com parâmetros.
- Manter o navegador aberto para demonstração.

###### Condução da aula

1. Contextualização inicial (5 min)

- Retomar a aula anterior sobre depuração HTTP.
- Utilizar a analogia da avaliação escolar e seus parâmetros.
2. Demonstração do professor (15 min)

- Mostrar uma URL simples sem parâmetros.
- Em seguida, apresentar uma URL com parâmetros (ex.: filtros de busca).
- Explicar:
- O que é um parâmetro
- Onde ele aparece na URL
- Qual informação ele carrega
3. Prática guiada dos alunos (20 min)

- Alunos acessam sites que utilizam parâmetros.
- Identificam os parâmetros presentes.
- Relacionam o parâmetro com a ação realizada no site.
4. Discussão e fechamento (10 min)

- Compartilhamento das análises.
- Reforço da diferença conceitual entre GET e POST.

###### Pontos de atenção

- Evitar aprofundar em código ou backend.
- Manter foco na interpretação da URL e da requisição.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá analisar requisições HTTP que utilizam parâmetros, identificando quais informações são enviadas pelo cliente ao servidor.

Problema real simulado: Entender como filtros, buscas e formulários simples funcionam em sites.

Habilidade desenvolvida: Leitura técnica básica de parâmetros de requisição HTTP.

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
- Acesse um site que possua busca ou filtros.
- Realize uma busca ou aplique um filtro.
- Observe a URL gerada.
- Identifique os parâmetros presentes após o símbolo ?.
- Anote:
- Nome do parâmetro
- Valor enviado
- Repita o processo com outro site.
- Responda: “Para que servem os parâmetros em uma requisição?”

##### 8. Exemplo ou Demonstração

Exemplo de URL com parâmetros:

- https://www.exemplo.com/busca?produto=notebook&ordem=preco
- produto → parâmetro
- notebook → valor
- ordem → parâmetro
- preco → valor
Explicação: Os parâmetros informam ao servidor o que o usuário deseja visualizar.

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Pelo menos 2 URLs com parâmetros identificados.
- Identificação correta do nome e valor dos parâmetros.
- Explicação simples do papel dos parâmetros na requisição.
O professor verifica o objetivo pela clareza da análise.

##### 10. Formato de Entrega da Atividade

- Formato: resposta escrita (caderno, formulário ou AVA).
- Conteúdo: lista de URLs + identificação dos parâmetros.
- Entrega: ao final da aula ou como atividade complementar.
- Prazo sugerido: até a próxima aula.

##### 11. Encerramento e Reflexão

O professor encerra com perguntas orientadoras:

- O que acontece se um parâmetro for alterado?
- Por que o método GET expõe os parâmetros na URL?
- Como esse conceito ajuda no desenvolvimento de websites?
