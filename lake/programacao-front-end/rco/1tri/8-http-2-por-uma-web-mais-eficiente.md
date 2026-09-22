---
titulo: "HTTP/2 – Por uma Web Mais Eficiente"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 1
ordem_rco: 8
serie: 2
aula_rco: "Aula 08"
slides: 21
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/8-http-2-por-uma-web-mais-eficiente/8-http-2-por-uma-web-mais-eficiente.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/8-http-2-por-uma-web-mais-eficiente/AULA 08_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/8-http-2-por-uma-web-mais-eficiente/AULA 08_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# HTTP/2 – Por uma Web Mais Eficiente

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO FRONT-END
- 2ª Série
- HTTP/2 – Por uma Web Mais Eficiente
- Aula 08

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Prestar apoio técnico na elaboração da documentação de sistemas.
- Estruturar arquitetura dos elementos de conteúdo de websites.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Aprender sobre mais detalhes de uma comunicação HTTP2
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store

_3 imagem(ns) no slide._

### Slide 5 (oculto)

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!
- Como funciona o HTTP/2 e o que ele muda na sua vida:
- https://tecnoblog.net/especiais/http-2-como-funciona/
- Editor HTML on line:
- https://html5-editor.net/

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Você já aprendeu tanta coisa sobre o HTTP, recurso, requisição, método, portas, enfim, já tem noção sobre o comportamento da comunicação web, agora vamos ver uma evolução que está vindo aos poucos e que tem tudo para mudar ainda mais.

_2 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- A primeira versão do HTTP, a HTTP 0.9, foi publicada em 1991. Desde então, o protocolo tem evoluído e a versão atualmente utilizada é a HTTP/2, que foi publicada em 2015. O HTTP/2 introduziu vários recursos e melhorias em comparação com a HTTP 1.1, incluindo suporte a requisições múltiplas e compressão de cabeçalhos, tornando a transferência de dados mais eficiente e rápida. O que você acha que isso irá impactar na internet como a conhecemos?
- 3 minutos
- Conversem e apresentem suas visões

_3 imagem(ns) no slide._

### Slide 8

- Conceituando
- HTTP/2 é a segunda versão do protocolo HTTP (Hypertext Transfer Protocol), que é amplamente utilizado na internet para transferir dados. Ele foi publicado em 2015 e é uma atualização significativa em comparação com a primeira versão, o HTTP 1.1.
- Fonte https://upload.wikimedia.org/wikipedia/commons/8/80/Qu%C3%A9_es_http2.jpg

_2 imagem(ns) no slide._

### Slide 9

- Conceituando
- O HTTP/2 introduz várias melhorias em comparação com o HTTP 1.1, incluindo:
- Transferência mais rápida: O HTTP/2 permite que múltiplas requisições sejam enviadas e recebidas simultaneamente, tornando a transferência de dados mais rápida.
- Compressão de cabeçalhos: O HTTP/2 permite que os cabeçalhos sejam comprimidos antes de serem enviados, tornando a transferência de dados mais eficiente.
- Fonte https://blog.apiki.com/http2/

_2 imagem(ns) no slide._

### Slide 10

- Conceituando
- Multiplexamento: O HTTP/2 permite que várias requisições sejam enviadas em paralelo, sem que haja a necessidade de abrir novas conexões para cada requisição.
- Priorização de requisições: O HTTP/2 permite que as requisições sejam priorizadas, permitindo que os dados mais importantes sejam transferidos primeiro.
- Fonte https://www.escueladeinternet.com/protocolo-http2-novedades-empezar-usarlo/

_2 imagem(ns) no slide._

### Slide 11

- Conceituando
- Em geral, o HTTP/2 torna a transferência de dados mais eficiente e rápida, melhorando a velocidade e desempenho da web. A maioria dos navegadores modernos já suporta o HTTP/2, tornando-o a versão padrão para a transferência de dados na web.
- Fonte https://upload.wikimedia.org/wikipedia/commons/8/80/Qu%C3%A9_es_http2.jpg

_2 imagem(ns) no slide._

### Slide 12

- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/http-fundamentos

_2 imagem(ns) no slide._

### Slide 13

- HTTP2 - Dados binários, GZIP ativo e TLS
- Até agora sempre usamos o browser para realizar uma requisição.
- Mas podemos realizar fora dele usando a linha de comando por exemplo.
- Link para tarefa: https://cursos.alura.com.br/course/http-fundamentos/task/25737
- Um programa famoso para isso é o CURL. No Linux e MacOS ele já vem instalado por padrão.
- 10 minutos
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 14

- HTTP2 - Cabeçalhos Stateful
- No código abaixo, estamos fazendo uma requisição através do método GET, que já conhecemos. Essa requisição está sendo feita para a raiz, bem parecido com o que fizemos no CURL no vídeo anterior.
- Link para tarefa: https://cursos.alura.com.br/course/http-fundamentos/task/25738
- GET /
- Host: www.caelum.com.br
- User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:34.0)
- Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
- Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3
- Accept-Encoding: gzip, deflate
- 6 minutos
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 15

- HTTP2 - Server Push
- Temos o cliente e um servidor sendo representados. Podemos imaginar que estamos fazendo uma requisição para uma página principal, a index.html.
- Link para tarefa: https://cursos.alura.com.br/course/http-fundamentos/task/25739
- Então, ao receber esse conteúdo, o browser tem que sair fazendo requisições de tudo o que é necessário para que ele renderize a página. O navegador interpreta esse conteúdo HTML de cima para baixo, verifica que o primeiro recurso necessário é o estilo.css, aí ele vai lá buscar.
- 6 minutos
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 16

- HTTP2 - Multiplexação
- Outra coisa importante de requisição é que temos o conceito de request e response. Cada requisição e cada resposta no HTTP1.1 são únicos.
- Link para tarefa: https://cursos.alura.com.br/course/http-fundamentos/task/25740
- “Por baixo dos panos”, antes dessa requisição de fato ser feita, há uma conexão, comunicação entre cliente e servidor, que chamamos de TCP. Para que consigamos realizar uma requisição via HTTP, antes existe um modelo de TCP, que é um protocolo de transporte.
- 6 minutos
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 17

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 18

- O que vimos na aula de hoje:
- O que é o HTTP/2
- Finalidade do protocolo HTTP/2
- Funcionamento do protocolo HTTP/2

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

_Fonte: AULA 08_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 08

Questão 1

O que é o HTTP/2?

A) Uma nova versão do protocolo HTTP com suporte a transferência de dados binários

B) Uma evolução do protocolo FTP para a web

C) Uma nova versão do protocolo FTP com suporte a transferência de dados binários

D) Uma evolução do protocolo HTTP para a web

Resposta correta: D) Uma evolução do protocolo HTTP para a web

Questão 2

Qual é a principal vantagem do uso do HTTP/2 em relação ao HTTP 1.1?

A) Permite a transferência de múltiplos recursos em paralelo com uma única conexão

B) Oferece suporte a transferência de dados binários

C) Permite a transferência de dados mais rapidamente do que o HTTP 1.1

D) Todas as alternativas são corretas

Resposta correta: A) Permite a transferência de múltiplos recursos em paralelo com uma única conexão

## Prática

_Fonte: AULA 08_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 08

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender o que é o protocolo HTTP/2 e por que ele representa uma evolução do HTTP/1.1.
- Identificar as principais melhorias do HTTP/2, como multiplexação, compressão de cabeçalhos e priorização.
- Analisar, de forma prática, o impacto do HTTP/2 no desempenho de sites.
- Relacionar o uso do HTTP/2 com a eficiência e experiência do usuário em websites modernos.
Produto final esperado:

- Análise comparativa simples do comportamento de carregamento de páginas, destacando benefícios do HTTP/2.

##### 2. Ferramentas Recomendadas

###### Navegador Web (Google Chrome, Edge ou Firefox)

- Para que serve: acessar sites e observar o protocolo utilizado.
- Por que é adequada: navegadores modernos já utilizam HTTP/2 automaticamente.
- Como facilita o aprendizado: permite visualizar, na prática, a eficiência do protocolo.

###### Ferramentas de Desenvolvedor do Navegador

- Para que serve: identificar se o site utiliza HTTP/2 e analisar requisições simultâneas.
- Por que é adequada: ferramenta padrão no ambiente profissional.
- Como facilita o aprendizado: torna visível o funcionamento do HTTP/2 sem exigir código.

###### Editor HTML Online

- Para que serve: visualizar páginas simples e seus recursos.
- Por que é adequada: permite observar como múltiplos recursos são carregados.
- Como facilita o aprendizado: simplifica a visualização do impacto no carregamento.
Link sugerido: https://html5-editor.net/

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Computador ou notebook
- Navegador web atualizado
- Conexão com a internet
- Acesso às Ferramentas de Desenvolvedor do navegador
- Ambiente: laboratório de informática ou sala multimídia
Link de apoio: https://cursos.alura.com.br/course/http-fundamentos

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações necessárias

- Testar previamente o acesso à internet.
- Selecionar um site moderno que utilize HTTP/2.
- Manter o navegador aberto com as Ferramentas de Desenvolvedor.

###### Condução da aula

1. Contextualização inicial (5 min)

- Retomar a evolução do HTTP.
- Propor a reflexão: “Por que sites modernos precisam ser mais rápidos?”
2. Demonstração do professor (15 min)

- Acessar um site atual.
- Abrir as Ferramentas de Desenvolvedor.
- Mostrar:
- Protocolo HTTP/2 em uso
- Várias requisições ocorrendo simultaneamente
- Explicar, de forma conceitual:
- Multiplexação
- Compressão de cabeçalhos
- Prioridade de recursos
3. Prática guiada dos alunos (20 min)

- Alunos acessam sites indicados.
- Identificam se utilizam HTTP/2.
- Observam o carregamento de múltiplos recursos.
4. Discussão e fechamento (10 min)

- Compartilhamento das observações.
- Relacionar desempenho com experiência do usuário.

###### Pontos de atenção

- Não aprofundar em comandos de linha (curl).
- Manter foco no conceito e na observação visual.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá analisar o funcionamento do HTTP/2 em um site real, observando como múltiplos recursos são carregados de forma eficiente.

Problema real simulado: Garantir melhor desempenho e velocidade em um website.

Habilidade desenvolvida: Análise técnica básica de desempenho em comunicação web.

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
- Acesse um site moderno indicado pelo professor.
- Abra as Ferramentas de Desenvolvedor.
- Atualize a página.
- Verifique o protocolo utilizado (HTTP/2).
- Observe várias requisições sendo carregadas ao mesmo tempo.
- Registre suas observações.
- Responda: “Por que o HTTP/2 torna a web mais rápida?”

##### 8. Exemplo ou Demonstração

Exemplo conceitual:

- HTTP/1.1 → requisições sequenciais
- HTTP/2 → múltiplas requisições simultâneas
Resultado: Menor tempo de carregamento e melhor desempenho.

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Identificação de um site que utilize HTTP/2.
- Descrição simples das melhorias percebidas.
- Compreensão do impacto do protocolo no desempenho web.
O professor verifica o aprendizado pela clareza da análise.

##### 10. Formato de Entrega da Atividade

- Formato: resposta escrita (caderno, formulário ou AVA).
- Conteúdo: identificação do site + observações sobre HTTP/2.
- Entrega: ao final da aula ou como atividade complementar.
- Prazo sugerido: até a próxima aula.

##### 11. Encerramento e Reflexão

O professor encerra com perguntas orientadoras:

- Por que a evolução do HTTP é necessária?
- Como o HTTP/2 melhora a experiência do usuário?
- O que isso impacta no desenvolvimento front-end?
