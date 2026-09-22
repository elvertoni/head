---
titulo: "HTML e Leitores de Tela – Parte I"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 58
serie: 2
aula_rco: "Aula 58"
slides: 25
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/58-html-e-leitores-de-tela-parte-i/58-html-e-leitores-de-tela-parte-i.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/58-html-e-leitores-de-tela-parte-i/AULA 58_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/58-html-e-leitores-de-tela-parte-i/AULA 58_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# HTML e Leitores de Tela – Parte I

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- HTML e Leitores de Tela – Parte I
- Aula 58

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Desenvolver interfaces gráficas para aplicações computacionais.
- Aplicar boas práticas de acessibilidade em interfaces web.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Entender como funcionam os interpretadores de tela em páginas HTML.
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
- https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes/task/106566
- Instalando o Git localmente:
- https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes/task/117550

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Concluímos os estudos sobre a utilização do Git criando ramificações e realizando o merge.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- João é um desenvolvedor web iniciante e está trabalhando em seu primeiro projeto de um site de notícias. Ele fez um design atraente, com imagens impressionantes e layout interativo. No entanto, um de seus amigos, que é deficiente visual e utiliza um leitor de tela, lhe informou que tinha problemas para acessar o conteúdo do site. As imagens não tinham descrições e a ordem do conteúdo não fazia sentido quando o leitor de tela narra.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Conversem e apresentem suas visões
- João está confuso e se pergunta: "Como posso tornar o meu site acessível para leitores de tela?"

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- A resposta para o dilema de João envolve a incorporação de práticas de design inclusivo e acessibilidade na web em seu processo de desenvolvimento. Primeiro, ele deve adicionar texto alternativo às suas imagens, que descreva a imagem para aqueles que não podem vê-las. Isso pode ser feito adicionando um atributo 'alt' à tag da imagem.

_1 imagem(ns) no slide._

### Slide 10

- Resposta
- Além disso, João deve garantir que a estrutura de seu conteúdo esteja em uma ordem lógica que faça sentido quando lida por um leitor de tela. Por exemplo, usar corretamente as tags de cabeçalho (h1, h2, h3, etc.) para indicar a hierarquia da informação.

_1 imagem(ns) no slide._

### Slide 11

- Resposta
- Finalmente, qualquer elemento interativo no site, como links ou botões, deve estar corretamente rotulado para que um leitor de tela possa identificá-lo e descrever sua função para o usuário. Ao fazer essas alterações, João pode tornar seu site mais acessível para todos os usuários, incluindo aqueles que utilizam leitores de tela.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Os leitores de tela são programas de software que permitem que pessoas com deficiências visuais ou dificuldades de leitura possam ler o texto que está na tela do computador. Eles são uma ferramenta essencial para garantir a acessibilidade das páginas da web para todos os usuários.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Esses softwares funcionam convertendo o texto em voz sintetizada ou, para usuários com deficiência visual total, em braille. Isso significa que eles podem "ler" o conteúdo da tela para o usuário, permitindo que eles interajam com o seu computador ou dispositivo móvel.

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Na construção de páginas HTML, é importante considerar a compatibilidade com os leitores de tela. Para isso, é essencial seguir as diretrizes de acessibilidade da web, como a inclusão de texto alternativo para imagens (atributo alt), utilização correta das tags de cabeçalho (h1, h2, h3, etc.), uso de listas para conteúdos que possuem uma sequência lógica, entre outros.

_1 imagem(ns) no slide._

### Slide 15

- Conceituando
- Os leitores de tela também são capazes de navegar por links, botões e outros elementos interativos na página. Para que estes sejam acessíveis, deve-se garantir que cada elemento interativo esteja corretamente etiquetado e tenha um nome significativo.

_6 imagem(ns) no slide._

### Slide 16

- Conceituando
- A importância dos leitores de tela está na garantia da inclusão e acessibilidade na web. Ao criar páginas HTML que são compatíveis com os leitores de tela, você está garantindo que seu site ou aplicativo seja acessível a todos, independentemente de suas habilidades visuais.
- Isso não apenas abre o seu conteúdo para um público mais amplo, mas também cumpre as diretrizes de acessibilidade que são uma parte importante do design inclusivo.

_1 imagem(ns) no slide._

### Slide 17

- Ainda sobre HTML e leitores de tela, vamos conhecer praticando?
- Na plataforma Alura, vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/acessibilidade-web-front-end
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 18

- Introdução
- 2 minutos
- Agora você aprenderá um pouco mais sobre acessibilidade web, com um foco maior em Front-end.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36229
- Por isso, é necessário que você tenha algum conhecimento prévio de HTML e CSS. Se você não possui estes pré-requisitos, recomendo os cursos de HTML e CSS da plataforma Alura.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 19

- Testando de verdade
- 11 minutos
- O testes de acessibilidade é algo importante.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36230
- Nessa aula tem se o relato de uma pessoa com um tipo de deficiência onde o leitor de tela se faz extremamente importante.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 20

- Instalando o NVDA
- 15 minutos
- Os chamados leitores de tela, que funcionam indicando e lendo a localização do foco.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36231
- Dentre as opções disponíveis, estão o JAWS, o NVDA e, no caso do Mac, o VoiceOver - leitor que vem integrado ao sistema operacional. Há também o Narrador no Windows, e outros.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 21

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 22

- O que vimos na aula de hoje:
- Conhecemos formas de utilizar inclusão de pessoas com algum tipo de deficiência na utilização de tecnologias e desenvolvimento de produtos para essas pessoas.

_1 imagem(ns) no slide._

### Slide 23

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 24

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

### Slide 25

_(sem texto)_

## Atividade

_Fonte: AULA 58_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 58

Questão 1

O que é um leitor de tela na área de desenvolvimento web?

a) Um software que lê o código HTML e CSS e o converte em uma página web visual.

b) Uma ferramenta que permite aos desenvolvedores ver o código-fonte de uma página da web.

c) Um programa que lê em voz alta o conteúdo de uma página da web para pessoas com deficiência visual ou cegueira.

d) Um plugin de navegador que melhora a velocidade de carregamento de uma página da web.

Resposta correta: c) Um programa que lê em voz alta o conteúdo de uma página da web para pessoas com deficiência visual ou cegueira.

Questão 2

Por que é importante adicionar texto alternativo (alt text) às imagens em um site?

a) Para aumentar a velocidade de carregamento da imagem.

b) Para que o leitor de tela possa descrever a imagem para pessoas que não conseguem vê-la.

c) Para melhorar o posicionamento do site nos motores de busca (SEO).

d) Todas as alternativas acima.

Resposta correta: d) Todas as alternativas acima.

O texto alternativo serve para descrever uma imagem para os usuários que não conseguem vê-la, o que é essencial para a acessibilidade e uma boa prática para os leitores de tela. Além disso, ele também pode contribuir para a otimização do site nos motores de busca.

## Prática

_Fonte: AULA 58_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 58

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender a importância da acessibilidade em páginas web.
- Identificar problemas que dificultam o uso de leitores de tela.
- Aplicar textos alternativos em imagens utilizando o atributo alt.
- Organizar corretamente títulos e subtítulos utilizando tags semânticas.
- Melhorar a navegação de páginas HTML para usuários que utilizam tecnologias assistivas.
- Avaliar a acessibilidade básica de uma página web.

###### Produto Final Esperado

O estudante deverá adaptar uma página HTML para torná-la mais acessível, incluindo:

- Imagens com descrição alternativa.
- Hierarquia correta de títulos.
- Botões e links identificáveis.
- Estrutura organizada para leitores de tela.

##### 2. Ferramentas Recomendadas

###### Visual Studio Code (VS Code)

Para que serve: edição dos arquivos HTML.

Por que é adequado: permite modificar rapidamente a estrutura da página.

Como facilita o aprendizado: possibilita testar e corrigir problemas de acessibilidade.

Site: https://code.visualstudio.com

###### Navegador Web

Para que serve: visualização e teste da página.

Por que é adequado: permite validar as alterações realizadas.

Como facilita o aprendizado: mostra o comportamento real da interface.

###### NVDA (NonVisual Desktop Access)

Para que serve: leitor de tela gratuito para Windows.

Por que é adequado: é uma das ferramentas mais utilizadas para testes de acessibilidade.

Como facilita o aprendizado: permite que os alunos experimentem como pessoas com deficiência visual navegam em páginas web.

Site: https://www.nvaccess.org

###### WAVE Web Accessibility Evaluation Tool

Para que serve: análise automática de acessibilidade.

Por que é adequado: identifica problemas comuns de acessibilidade.

Como facilita o aprendizado: fornece feedback visual imediato.

Site: https://wave.webaim.org

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve possuir:

VS Code instalado

Navegador atualizado

Página HTML para análise

Conexão com internet

NVDA instalado (quando disponível)

Conhecimentos básicos de HTML

###### Materiais de Apoio

Curso Alura:

https://cursos.alura.com.br/course/acessibilidade-web-front-end

NVDA:

https://www.nvaccess.org

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações Necessárias

- Garantir acesso ao laboratório.
- Disponibilizar uma página HTML simples.
- Instalar ou demonstrar o funcionamento do NVDA.
- Testar previamente o navegador.

###### Contextualização (5 minutos)

Apresente o cenário:

João criou um site bonito visualmente, mas seu amigo com deficiência visual não consegue utilizá-lo adequadamente.

Pergunta para a turma:

Um site pode ser considerado bom se apenas algumas pessoas conseguem utilizá-lo?

###### Conceituando Acessibilidade (10 minutos)

Explique:

- O que é acessibilidade digital.
- O que são leitores de tela.
- Quem utiliza essas ferramentas.
- Importância do design inclusivo.
Apresente exemplos reais de uso.

###### Demonstração do Leitor de Tela (10 minutos)

Demonstrar:

- Navegação com NVDA.
- Leitura de títulos.
- Leitura de imagens.
- Leitura de botões.
Mostrar a diferença entre uma página acessível e outra sem acessibilidade.

###### Demonstração das Correções (10 minutos)

Mostrar como:

- Adicionar atributo alt.
- Organizar títulos.
- Melhorar identificação de links.
- Estruturar conteúdo semanticamente.

###### Prática Guiada (10 minutos)

Os alunos deverão:

- Analisar uma página.
- Identificar problemas.
- Corrigir os elementos necessários.

###### Encerramento (5 minutos)

Revisar:

- melhorias realizadas;
- benefícios da acessibilidade;
- impacto social da inclusão digital.

###### Pontos de Atenção

- Evitar descrições genéricas em imagens.
- Manter ordem lógica dos títulos.
- Garantir textos claros em links e botões.
- Pensar na experiência de diferentes usuários.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá atuar como desenvolvedor responsável por tornar uma página web acessível para usuários que utilizam leitores de tela.

A atividade consiste em:

- Analisar uma página HTML.
- Identificar problemas de acessibilidade.
- Corrigir elementos que dificultam a navegação.
- Testar a experiência utilizando ferramentas de acessibilidade.

###### Problema Real Simulado

Adequação de um portal de notícias para usuários com deficiência visual.

###### Habilidade Desenvolvida

Aplicação de boas práticas de acessibilidade em interfaces web.

##### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Problemas (PBL)

Os estudantes solucionam problemas reais de acessibilidade.

###### Aprendizagem por Experimentação

Testam a navegação utilizando leitores de tela.

###### Ensino por Descoberta

Identificam falhas e propõem melhorias.

###### Elementos de Lemov

- Modelagem
- Prática Guiada
- Verificação de Compreensão
- Feedback Imediato
- Revisão

##### 7. Passo a Passo da Atividade Prática (para os alunos)

###### Etapa 1 – Análise Inicial

- Abra a página HTML fornecida pelo professor.
- Observe:
- imagens;
- títulos;
- links;
- botões.
- Identifique possíveis problemas de acessibilidade.

###### Etapa 2 – Melhorar as Imagens

- Localize todas as imagens.
- Verifique se possuem descrição alternativa.
- Adicione descrições adequadas.

###### Etapa 3 – Organizar a Estrutura

- Analise os títulos da página.
- Organize-os em ordem lógica:
- título principal;
- subtítulos;
- seções.

###### Etapa 4 – Melhorar Navegação

- Revise os links.
- Revise os botões.
- Garanta que possuam textos claros e significativos.

###### Etapa 5 – Teste

- Utilize o navegador ou leitor de tela.
- Verifique se o conteúdo pode ser compreendido sem apoio visual.

###### Etapa 6 – Evidências

- Capture prints:
- antes das correções;
- depois das correções;
- resultado final.

##### 8. Exemplo ou Demonstração

###### Exemplo de Imagem Não Acessível

- <img src="noticia.jpg">

###### Exemplo Corrigido

- <img src="noticia.jpg" alt="Jornalista apresentando reportagem sobre tecnologia">

###### Estrutura Correta de Títulos

- H1 - Título Principal
- H2 - Categoria
- H3 - Subcategoria

###### Fluxo de Acessibilidade

- Página HTML
- ↓
- Análise
- ↓
- Correção
- ↓
- Teste
- ↓
- Página Acessível

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Página corrigida.
- Imagens com descrições alternativas.
- Estrutura organizada.
- Melhor experiência para leitores de tela.

###### Critérios de Verificação

O professor deverá verificar:

Uso correto do atributo alt

Hierarquia adequada de títulos

Identificação clara de links e botões

Organização da página

Participação na atividade

##### 10. Formato de Entrega da Atividade

###### O que deve ser enviado

- Arquivo HTML corrigido.
- Prints das melhorias realizadas.
- Relatório simples contendo:
- problemas encontrados;
- soluções aplicadas.

###### Nomeação Sugerida

- Aula58_NomeSobrenome
Exemplo:

- Aula58_MariaOliveira

###### Onde Entregar

- Google Classroom
- Google Drive
- AVA da instituição

###### Prazo Sugerido

Ao final da aula.

##### 11. Encerramento e Reflexão

Promova uma discussão com a turma:

###### Perguntas para reflexão

- Como uma pessoa com deficiência visual utiliza um site?
- Por que o atributo alt é importante?
- O que acontece quando uma página não segue boas práticas de acessibilidade?
- Como a tecnologia pode promover inclusão?
