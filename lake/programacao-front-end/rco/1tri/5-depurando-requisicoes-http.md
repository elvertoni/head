---
titulo: "Depurando Requisições HTTP"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 1
ordem_rco: 5
serie: 2
aula_rco: "Aula 05"
slides: 19
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/5-depurando-requisicoes-http/5-depurando-requisicoes-http.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/5-depurando-requisicoes-http/AULA 05_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/5-depurando-requisicoes-http/AULA 05_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Depurando Requisições HTTP

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO FRONT-END
- 2ª Série
- Depurando Requisições HTTP
- Aula 05

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Realizar prospecções, testes e avaliações de ferramentas.
- Interpretar briefing para projetos de websites.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Aprender sobre mais detalhes de uma comunicação HTTP
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
- Você já aprendeu como é feito o acesso a um site, como é feito a conexão, acesso a portas, protocolo HTTP e HTTPS, agora chegou a hora de ver mais sobre isso, adentrar mais ao processo, a isso chamamos de depuração.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Você já viu como um motor de um carro funciona por dentro? No âmbito lógico não é possível visto que ele é fechado para garantir pressão e temperatura do óleo e seus componentes. Mas se surgisse um defeito, seria possível ver isso com ele fechado? Seguindo esse exemplo, e uma conexão HTTP? Você tem noção de como funciona esse processo? Como você imagina que seria possível verificar algum possível erro em uma conexão HTTP?
- Quem pode me ajudar a responder essas perguntas?

_1 imagem(ns) no slide._

### Slide 8

- Conceituando
- Uma depuração HTTP é o processo de verificação de erros e solução de problemas relacionados ao protocolo HTTP (Hypertext Transfer Protocol) durante a comunicação entre um servidor e um cliente. Isso envolve o uso de ferramentas e técnicas para verificar a integridade e a consistência dos dados transmitidos durante uma requisição HTTP.
- Fonte https://publicdomainvectors.org/pt/vetorial-gratis/Conex%C3%A3o-de-Internet/40080.html

_1 imagem(ns) no slide._

### Slide 9

- Conceituando
- Alguns erros comuns que podem surgir em uma conexão HTTP incluem:
- Códigos de status HTTP: como 404 (Não encontrado), 500 (Erro interno do servidor), 401 (Não autorizado), etc.
- Problemas de CORS (Compartilhamento de Recursos de Origem Cruzada): ocorre quando o navegador bloqueia o acesso a dados em outro domínio.
- Fonte https://publicdomainvectors.org/pt/vetorial-gratis/Conex%C3%A3o-de-Internet/40080.html

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- Problemas de autenticação: quando o servidor requer autenticação antes de permitir o acesso ao recurso.
- Problemas de SSL/TLS: quando o certificado SSL/TLS não é válido ou não corresponde ao nome do host.
- Timeouts: ocorre quando a conexão demora muito tempo para ser estabelecida ou para receber uma resposta.
- Fonte https://publicdomainvectors.org/pt/vetorial-gratis/Conex%C3%A3o-de-Internet/40080.html

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- Erros de parsing: quando o servidor retorna dados mal formatados ou não podem ser interpretados pelo cliente.
- Problemas de cache: quando o cliente está recebendo dados antigos armazenados em cache em vez de dados atualizados.
- Estes são apenas alguns dos erros comuns que podem surgir em uma conexão HTTP e a depuração é necessária para identificar e corrigir esses problemas.
- Fonte https://publicdomainvectors.org/pt/vetorial-gratis/Conex%C3%A3o-de-Internet/40080.html

_1 imagem(ns) no slide._

### Slide 12

- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/http-fundamentos

_2 imagem(ns) no slide._

### Slide 13

- Depurando o método HTTP
- Uma depuração HTTP é o processo de verificação de erros e solução de problemas relacionados ao protocolo HTTP (Hypertext Transfer Protocol) durante a comunicação entre um servidor e um cliente.
- Link para tarefa: https://cursos.alura.com.br/course/http-fundamentos/task/25395
- Aqui está um exemplo de depuração HTTP:
- Verificar código de status HTTP: Verifique se o código de status HTTP retornado pelo servidor é o esperado. Por exemplo, se o código de status for 404 (Não encontrado), significa que o recurso solicitado não pôde ser encontrado no servidor.
- 2 minutos
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 14

- Depurando os códigos de respostas
- Uma depuração HTTP é o processo de verificação de erros e solução de problemas relacionados ao protocolo HTTP (Hypertext Transfer Protocol) durante a comunicação entre um servidor e um cliente.
- Link para tarefa: https://cursos.alura.com.br/course/http-fundamentos/task/25399
- Os códigos de resposta HTTP são números de três dígitos retornados pelo servidor em resposta a uma requisição HTTP e fornecem informações sobre o resultado da requisição. Por exemplo, o código 200 significa "OK" e indica que a requisição foi bem-sucedida, enquanto o código 404 significa "Não encontrado" e indica que o recurso solicitado não foi encontrado no servidor.
- 2 minutos
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 15

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 16

- O que vimos na aula de hoje:
- O que é depuração HTTP;
- Finalidade da depuração;
- O que podemos entender com a depuração web.

_1 imagem(ns) no slide._

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
- <a href="https://www.flaticon.com/br/icones-gratis/antivirus" title="antivirus ícones">Antivirus ícones criados por shmai - Flaticon</a>

### Slide 19

_(sem texto)_

## Atividade

_Fonte: AULA 05_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 05

Questão 1

Qual é o principal objetivo da depuração de requisições HTTP?

a) Identificar erros em códigos HTML

b) Otimizar o tempo de resposta da página

c) Monitorar o tráfego de rede

d) Identificar erros na comunicação entre cliente e servidor

Resposta correta: d) Identificar erros na comunicação entre cliente e servidor

A depuração de requisições HTTP visa identificar problemas na comunicação entre o cliente e o servidor, como problemas de sincronização, solicitações mal formadas, erros de resposta, entre outros. Isso ajuda a garantir que a comunicação entre os dois seja suave e eficiente, evitando problemas para o usuário final.

Questão 2

Qual é a principal ferramenta utilizada na depuração de requisições HTTP?

a) Wireshark

b) Telnet

c) FTP

d) Ping

Resposta correta: a) Wireshark

Wireshark é uma das principais ferramentas utilizadas na depuração de requisições HTTP. Ele permite que você capture e analise pacotes de rede, permitindo identificar problemas na comunicação entre cliente e servidor, incluindo a análise de cabeçalhos HTTP, corpo da mensagem, tempo de resposta, entre outros aspectos importantes.

## Prática

_Fonte: AULA 05_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 05

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender o conceito de depuração de requisições HTTP e sua importância no desenvolvimento web.
- Identificar erros comuns em comunicações HTTP, como códigos de status e falhas de conexão.
- Analisar respostas do servidor, interpretando códigos HTTP básicos.
- Desenvolver habilidade prática de investigação técnica, simulando a análise de problemas em acessos a sites.
Produto final esperado:

- Registro explicativo de uma requisição HTTP analisada, contendo código de resposta e interpretação do erro ou sucesso.

##### 2. Ferramentas Recomendadas

###### Navegador Web (Google Chrome, Edge ou Firefox)

- Para que serve: acessar sites e gerar requisições HTTP.
- Por que é adequada: atua como cliente no processo de comunicação web.
- Como facilita o aprendizado: permite simular acessos reais e erros comuns.

###### Ferramentas de Desenvolvedor do Navegador

- Para que serve: visualizar requisições, respostas e códigos HTTP.
- Por que é adequada: ferramenta profissional utilizada para depuração.
- Como facilita o aprendizado: torna visíveis erros que normalmente ficam ocultos.

###### Plataforma Alura

- Para que serve: reforçar o conteúdo com exercícios guiados.
- Por que é adequada: apresenta exemplos introdutórios e contextualizados.
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
- Abrir um site funcional e um endereço inválido para demonstração.
- Manter abertas as Ferramentas de Desenvolvedor.

###### Condução da aula

1. Contextualização inicial (5 min)

- Retomar o conceito de requisição–resposta.
- Utilizar a analogia do motor do carro apresentada no material.
2. Demonstração do professor (15 min)

- Acessar um site válido (retorno 200).
- Acessar uma página inexistente (retorno 404).
- Mostrar onde visualizar:
- Código de status
- Tipo de requisição
- Resposta do servidor
3. Prática guiada dos alunos (20 min)

- Alunos acessam diferentes páginas.
- Observam os códigos de resposta.
- Identificam erros ou sucessos nas requisições.
4. Discussão e fechamento (10 min)

- Compartilhamento das análises.
- Reforço da importância da depuração no desenvolvimento web.

###### Pontos de atenção

- Não aprofundar em configurações avançadas de servidor.
- Manter o foco na leitura e interpretação dos códigos HTTP.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá analisar uma comunicação HTTP real, identificando o código de resposta retornado pelo servidor e explicando seu significado.

Problema real simulado: Identificar por que um site não carrega corretamente.

Habilidade desenvolvida: Análise técnica básica e interpretação de erros em aplicações web.

##### 6. Metodologia Ativa Utilizada

- Ensino por descoberta
- Experimentação
- Aprendizagem baseada em problemas
- Elementos de Lemov aplicados:
- Estabelecer propósito
- Prática guiada
- Checagem de compreensão
- Feedback imediato

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Abra o navegador web.
- Acesse um site funcional.
- Abra as Ferramentas de Desenvolvedor.
- Atualize a página.
- Identifique o código de status HTTP retornado.
- Acesse um endereço inexistente.
- Observe o novo código de resposta.
- Registre:
- URL acessada
- Código HTTP
- Significado do código
- Finalize respondendo: “Por que a depuração é importante?”

##### 8. Exemplo ou Demonstração

Exemplo de análise:

- URL: https://www.google.com
- Código HTTP: 200
- Significado: Requisição realizada com sucesso
- URL: https://www.siteinexistente.com/pagina
- Código HTTP: 404
- Significado: Página não encontrada

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Pelo menos uma requisição analisada com sucesso (200).
- Pelo menos uma requisição com erro (ex.: 404).
- Explicação simples e correta sobre o significado dos códigos.
O professor verifica o aprendizado pela coerência da análise.

##### 10. Formato de Entrega da Atividade

- Formato: resposta escrita (caderno, formulário ou AVA).
- Conteúdo: tabela ou lista com URL, código HTTP e explicação.
- Entrega: ao final da aula ou como atividade complementar.
- Prazo sugerido: até a próxima aula.

##### 11. Encerramento e Reflexão

O professor encerra com perguntas orientadoras:

- O que os códigos HTTP nos dizem sobre um site?
- Como a depuração ajuda a resolver problemas?
- Por que essa habilidade é importante para desenvolvedores?
