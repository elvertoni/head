---
titulo: "A Web Segura – Introdução ao HTTPS"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 1
ordem_rco: 2
serie: 2
aula_rco: "Aula 02"
slides: 21
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/2-a-web-segura-introducao-ao-https/2-a-web-segura-introducao-ao-https.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/2-a-web-segura-introducao-ao-https/AULA 02_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/2-a-web-segura-introducao-ao-https/AULA 02_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# A Web Segura – Introdução ao HTTPS

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO FRONT-END
- 2ª Série
- A Web Segura – Introdução ao HTTPS
- Aula 02

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
- Conhecer o protocolo HTTPS.
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

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Aprendemos o que é o protocolo HTTP:

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Agora que sabemos a respeito do HTTP, a pergunta que fica é, como é feito a segurança da internet? Será que existe um segurança em todos os acessos perguntando quem é você?
- Claro que não! Então vamos fazer um debate sobre quais as possibilidade de insegurança em acessos na internet.
- 2 minutos
- Conversem e apresentem seo que pensam sobre isto

_2 imagem(ns) no slide._

### Slide 8

- Conceituando
- HTTPS é um protocolo de comunicação seguro na Web que é baseado no protocolo HTTP e adiciona criptografia para proteger as informações transmitidas entre o navegador e o servidor. Isso significa que qualquer informação transmitida usando HTTPS, incluindo dados sensíveis, como senhas e informações financeiras, é cifrada e protegida contra interceptação por terceiros.
- Fonte https://static.imasters.com.br/wp-content/uploads/2018/02/HTTP-vs-HTTPS.png

_1 imagem(ns) no slide._

### Slide 9

- Conceituando
- O HTTPS é identificado por um ícone de cadeado verde na barra de endereços do navegador e pela sigla "https" no início do endereço da página da web. Ele é amplamente usado em sites comerciais, financeiros e governamentais para garantir a segurança das informações transmitidas online.
- Fonte https://static.imasters.com.br/wp-content/uploads/2018/02/HTTP-vs-HTTPS.png

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- A principal diferença entre o protocolo HTTP e HTTPS é a segurança.
- O HTTP é um protocolo não cifrado que transmite dados na clara;
- O HTTPS é uma versão segura do HTTP que adiciona criptografia para proteger as informações transmitidas.
- Outra diferença importante é que o HTTPS usa um certificado SSL/TLS para autenticar o servidor e garantir que as informações estão sendo transmitidas para o destinatário correto
- Fonte https://static.imasters.com.br/wp-content/uploads/2018/02/HTTP-vs-HTTPS.png

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- Além disso, o HTTPS usa o protocolo SSL/TLS* para estabelecer uma conexão segura antes de iniciar a transmissão de dados, enquanto o HTTP não tem um mecanismo de segurança integrado. Em resumo, o HTTPS é recomendado para qualquer site que transmita informações sensíveis, como informações financeiras ou de identificação pessoal, enquanto o HTTP é adequado para sites que não precisam de segurança adicional.
- SSL significa Secure Sockets Layer, um tipo de segurança digital que permite a comunicação criptografada entre um domínio de site e um navegador. Atualmente a tecnologia se encontra depreciada e está sendo completamente substituída pelo TLS.
- TLS é uma sigla que representa Transport Layer Security e certifica a proteção de dados de maneira semelhante ao SSL. Como o SSL não está mais de fato em uso, esse é o termo correto que deveria ser utilizado.

_1 imagem(ns) no slide._

### Slide 12

- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/http-fundamentos

_2 imagem(ns) no slide._

### Slide 13

- HTTPS a Versão segura do HTTP
- HTTPS é um protocolo de comunicação seguro na Web que é baseado no protocolo HTTP e adiciona criptografia para proteger as informações transmitidas entre o navegador e o servidor.
- Link para tarefa: https://cursos.alura.com.br/course/http-fundamentos/task/25380
- Quando acessamos a Alura por exemplo, precisamos fornecer informações de autenticação, essas informações são nosso e-mail e senha, que são enviadas e validadas pela plataforma para que assim consigamos assistir às aulas. Essas informações se não criptografadas ficam expostas.
- 2 minutos
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 14

- Funcionamento do HTTPS
- O protocolo HTTPS funciona usando uma combinação de criptografia, autenticação e integridade de dados. Quando um navegador web faz uma solicitação a um site HTTPS, ele estabelece primeiro uma conexão segura com o servidor usando o protocolo SSL/TLS.
- Link para tarefa: https://cursos.alura.com.br/course/http-fundamentos/task/25370
- Em resumo, o HTTPS garante a segurança e a privacidade das informações transmitidas na Web, tornando-o ideal para aplicações financeiras, comerciais e governamentais.
- 2 minutos
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 15

- Assim…
- Quando precisamos informar nossos dados a algum servidor, queremos ter certeza que este servidor realmente representa a entidade em questão. Queremos confiar em quem está fornecendo nossos dados.
- Um certificado digital prova uma identidade para um site, onde temos informações sobre o seu domínio e a data de expiração desse certificado.
- Fonte https://pxhere.com/pt/photo/1595274

_1 imagem(ns) no slide._

### Slide 16

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 17

- TAREFA PARA CASA!
- Agora que você já sabe o que é o HTTPS, liste 3 sites que fazem uso desse protocolo e que você acessa todos com frequência, além disso, liste um site que não faz uso do protocolo HTTPS.

_2 imagem(ns) no slide._

### Slide 18

- O que vimos na aula de hoje:
- Apenas com HTTPS a Web é segura
- O protocolo HTTPS nada mais é do que o protocolo HTTP mais uma camada adicional de segurança, a TLS/SSL
- Apenas com HTTPS a Web é segura

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

_Fonte: AULA 02_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 02

Questão 1

O que é HTTPS?

A) Uma ferramenta de edição de imagens na web

B) Um protocolo de transferência de arquivos na internet

C) Um protocolo de segurança para transferência de dados na web

D) Uma rede social para compartilhamento de arquivos

Resposta correta: C) Um protocolo de segurança para transferência de dados na web

Comentário: HTTPS (Hypertext Transfer Protocol Secure) é um protocolo de segurança para transferência de dados na web que fornece uma camada adicional de segurança para proteger as informações sensíveis transmitidas entre o servidor e o cliente. Ele é baseado em criptografia e é amplamente utilizado em transações financeiras, login de usuários, compra de produtos e serviços na web, entre outras aplicações que requerem segurança na transferência de dados. A presença do prefixo "https" na URL indica que a conexão é segura e protegida.

Questão 2

Questão: Qual é a importância do HTTPS?

A) Para melhorar a performance do site

B) Para garantir a integridade dos dados transmitidos

C) Para proteger a privacidade dos usuários

D) Para aumentar a visibilidade do site nos resultados de busca

Resposta correta: C) Para proteger a privacidade dos usuários

Comentário: O HTTPS (Hypertext Transfer Protocol Secure) é importante porque garante que as informações sensíveis transmitidas entre o servidor e o cliente sejam criptografadas e, portanto, protegidas contra intercepção por terceiros. Isso é especialmente importante em aplicações que envolvem informações confidenciais, como login de usuários, transações financeiras e compra de produtos e serviços na web. A presença do prefixo "https" na URL indica que a conexão é segura e protegida, o que aumenta a confiança do usuário na segurança do site.

## Prática

_Fonte: AULA 02_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 02

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender, na prática, como o protocolo HTTPS garante a segurança na navegação web.
- Identificar visualmente sites seguros e não seguros, analisando o uso de HTTPS.
- Desenvolver a habilidade de avaliação técnica básica, reconhecendo riscos em acessos sem criptografia.
- Relacionar segurança da informação com o desenvolvimento de websites, entendendo a importância do HTTPS em projetos web.
Produto final esperado:

- Lista comentada de sites com HTTPS e um site sem HTTPS, com explicação simples sobre segurança.

##### 2. Ferramentas Recomendadas

###### Navegador Web (Google Chrome, Edge ou Firefox)

- Para que serve: acessar sites e identificar o uso do HTTPS.
- Por que é adequada: exibe claramente o cadeado de segurança e o protocolo usado.
- Como facilita o aprendizado: torna visível o conceito de segurança na prática.

###### Ferramentas de Desenvolvedor do Navegador

- Para que serve: observar detalhes da conexão segura.
- Por que é adequada: aproxima o aluno do ambiente profissional.
- Como facilita o aprendizado: reforça a análise técnica sem exigir programação.

###### Plataforma Alura

- Para que serve: complementar o conteúdo com atividades guiadas.
- Por que é adequada: possui material introdutório claro e progressivo.
- Como facilita o aprendizado: reforça o conteúdo visto em aula.

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
- Separar exemplos de sites com HTTPS e, se possível, um site sem HTTPS.
- Abrir um navegador com as Ferramentas de Desenvolvedor prontas.

###### Condução da aula

1. Abertura e problematização (5 min)

- Retomar o conteúdo da aula anterior (HTTP).
- Propor a questão: “Como a internet protege nossos dados quando digitamos senhas?”
2. Demonstração do professor (15 min)

- Acessar um site seguro (ex.: Alura, site bancário).
- Mostrar o cadeado e o “https”.
- Explicar, de forma simples:
- Criptografia
- Certificado digital
- Diferença entre HTTP e HTTPS
3. Prática guiada dos alunos (20 min)

- Alunos acessam diferentes sites.
- Identificam se usam HTTPS.
- Registram observações.
4. Discussão e fechamento (10 min)

- Compartilhamento das descobertas.
- Reforço da importância do HTTPS para segurança digital.

###### Pontos de atenção

- Evitar aprofundar em conceitos matemáticos de criptografia.
- Reforçar que HTTPS é padrão profissional atual.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá analisar a segurança de sites que acessa no dia a dia, identificando o uso do protocolo HTTPS.

Problema real simulado: Avaliar se um site é seguro antes de informar dados pessoais.

Habilidade desenvolvida: Análise crítica de segurança básica em navegação web.

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
- Acesse três sites que você utiliza com frequência.
- Verifique se o endereço começa com https.
- Observe se há o cadeado de segurança.
- Anote os nomes dos três sites seguros.
- Encontre um site que não utilize HTTPS (se possível).
- Registre suas observações.
- Finalize respondendo: “Por que o HTTPS é importante?”

##### 8. Exemplo ou Demonstração

Exemplo de análise:

- Site 1: https://www.alura.com.br → seguro
- Site 2: https://www.gov.br → seguro
- Site 3: http://exemplo.com → não seguro
Explicação: Sites com HTTPS utilizam criptografia para proteger os dados transmitidos.

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Lista com 3 sites que usam HTTPS.
- Identificação de 1 site sem HTTPS (quando possível).
- Explicação simples sobre a diferença entre HTTP e HTTPS.
O professor verifica o aprendizado pela coerência das respostas e participação.

##### 10. Formato de Entrega da Atividade

- Formato: resposta escrita (caderno, formulário ou AVA).
- Conteúdo: lista de sites + explicação.
- Entrega: ao final da aula ou como tarefa para casa.
- Prazo sugerido: até a próxima aula.

##### 11. Encerramento e Reflexão

O professor finaliza com perguntas orientadoras:

- Você confiaria em um site sem HTTPS?
- Onde usamos HTTPS no nosso dia a dia?
- Como esse conhecimento ajuda no desenvolvimento de sistemas?
