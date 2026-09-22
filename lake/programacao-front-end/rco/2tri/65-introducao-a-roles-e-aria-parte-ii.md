---
titulo: "Introdução a Roles e ARIA - Parte II"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 65
serie: 2
aula_rco: "Aula 65"
slides: 24
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/65-introducao-a-roles-e-aria-parte-ii/65-introducao-a-roles-e-aria-parte-ii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/65-introducao-a-roles-e-aria-parte-ii/AULA 65_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/65-introducao-a-roles-e-aria-parte-ii/AULA 65_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Introdução a Roles e ARIA - Parte II

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Introdução a Roles e ARIA - Parte II
- Aula 65

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
- Compreender sobre navegação em páginas HTML por teclado e o impacto nos leitores de tela Parte II.
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
- http://www.reinaldoferraz.com.br/acessibilidade-seo-e-svg/
- Lang e Alt:
- https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36282
- Projeto aula anterior:
- https://github.com/designernatan/curso-acessibilidade-web-front-end-1/archive/0115ab16629f4f264184beb291ece993b7246f8c.zip

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Iniciamos os estudos sobre navegação em páginas HTML via teclado, sua importância para a acessibilidade.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Maria, uma desenvolvedora web iniciante, recebeu o desafio de tornar um site já existente mais acessível para usuários de leitores de tela. Enquanto estudava o código do site, ela notou que muitas imagens não tinham o atributo "alt", algumas seções do site não estavam claramente delimitadas e alguns links eram pouco claros, apenas dizendo "clique aqui".

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Dúvida de Maria: "Como posso melhorar a acessibilidade deste site para os usuários de leitores de tela?"
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Maria pode começar adicionando o atributo "alt" em todas as imagens, com descrições breves e precisas que indiquem o propósito ou o conteúdo da imagem. Para melhorar a estrutura do site, ela deve usar corretamente os elementos semânticos do HTML, como cabeçalhos e seções, e garantir que cada parte do site esteja claramente delimitada.

_1 imagem(ns) no slide._

### Slide 10

- Resposta
- Quanto aos links, Maria deve evitar o uso de textos genéricos como "clique aqui", e em vez disso, usar descrições mais claras e contextualizadas, como "leia mais sobre a nossa empresa". Essas mudanças permitirão que os usuários de leitores de tela tenham uma experiência mais completa e satisfatória ao navegar no site.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- Os leitores de tela são ferramentas indispensáveis para pessoas com deficiências visuais, pois permitem a interpretação e a interação com o conteúdo das páginas da web. No entanto, mesmo sendo eficazes, podem encontrar alguns problemas ou dificuldades ao navegar em páginas HTML.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Ausência de texto alternativo para imagens: Quando as imagens não possuem um texto alternativo adequado (atributo alt), os leitores de tela não conseguem descrever o conteúdo da imagem para o usuário, resultando em uma experiência de navegação incompleta.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Problemas de estrutura e semântica: O HTML fornece elementos semânticos que ajudam a definir a estrutura da página (como cabeçalhos, seções, artigos etc.). Se os desenvolvedores não utilizarem esses elementos corretamente, o leitor de tela pode ter dificuldade para interpretar a estrutura da página.

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Links e botões sem descrição clara: Quando os links e botões não são claramente descritos, os usuários de leitores de tela podem não compreender a finalidade deles. Por exemplo, links com textos como "clique aqui" ou "saiba mais" podem ser confusos se o contexto não for claro.

_1 imagem(ns) no slide._

### Slide 15

- Conceituando
- Falta de foco visível: Os usuários de leitores de tela também podem usar o teclado para navegar em uma página. Se o foco visual não é claramente indicado, pode ser difícil saber qual elemento está sendo selecionado.

_1 imagem(ns) no slide._

### Slide 16

- Conceituando
- Inacessibilidade de conteúdo multimídia: Vídeos e áudios sem transcrições ou legendas adequadas são inacessíveis para usuários de leitores de tela. Além disso, se um vídeo começa a tocar automaticamente e não pode ser pausado facilmente, pode ser difícil para o usuário do leitor de tela entender o conteúdo da página.
- Os desenvolvedores da web devem estar cientes desses problemas potenciais ao projetar e criar sites, para garantir que eles sejam acessíveis a todos os usuários, independentemente de suas habilidades físicas.

_1 imagem(ns) no slide._

### Slide 17

- Ainda sobre HTML e leitores de tela, vamos conhecer praticando?
- Na plataforma Alura, vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/acessibilidade-web-front-end
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 18

- Facilitando para outros leitores
- 4 minutos
- O recurso de "pular conteúdo" é tão comum, que a tecnologia voltada para usuários com deficiência criou recursos importantes.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36246
- Alguns leitores de tela como Jaws e Narrator do Windows possuem uma tecla de atalho específica que leva diretamente ao conteúdo principal da página. Infelizmente, o NVDA não possui esse atalho, mas podemos melhorar nosso projeto pensando no usuário que utiliza outros leitores de tela.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 19

- Uma ponta do WAI ARIA
- 7 minutos
- DESENVOLVIMENTO DE SISTEMAS
- No site da Apeperia, temos uma área denominada "Destaques" que contém dois links que são acompanhados por imagens ilustrativas.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36247
- Quando navegamos por um dos links utilizando o "Tab", é exibida a informação "Conheça as primeiras etapas na criação de um logotipo linque" no NVDA. Ou seja, há uma marcação textual dos links.
- Atividade no portal Alura

_5 imagem(ns) no slide._

### Slide 20

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 21

- O que vimos na aula de hoje:
- Aprendemos situações impedem a acessibilidade a navegação em páginas HTML fazendo uso de leitores de tela.

_1 imagem(ns) no slide._

### Slide 22

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 23

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

### Slide 24

_(sem texto)_

## Atividade

_Fonte: AULA 65_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 65

Questão 1

O que o atributo "alt" em uma imagem faz em relação aos leitores de tela?

A) Adiciona uma borda colorida à imagem.

B) Descreve a imagem para os usuários de leitores de tela.

C) Aumenta o tamanho da imagem.

D) Nenhuma das opções.

Resposta: A resposta correta é a opção B. O atributo "alt" é usado para fornecer uma descrição textual da imagem, que pode ser lida por leitores de tela, ajudando a tornar o conteúdo mais acessível.

Questão 2

Por que é importante evitar o uso de textos genéricos como "clique aqui" para links quando se considera a acessibilidade dos leitores de tela?

A) Porque aumenta o tempo de carregamento da página.

B) Porque dificulta a compreensão do propósito do link para os usuários de leitores de tela.

C) Porque torna a página menos atraente.

D) Porque interfere no layout da página.

Resposta: A resposta correta é a opção B. Textos de links genéricos como "clique aqui" são menos úteis para os usuários de leitores de tela, pois não fornecem contexto ou informações sobre o destino do link. É melhor usar textos de links que descrevam com precisão o propósito ou destino do link.

## Prática

_Fonte: AULA 65_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 65

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Identificar problemas que dificultam a navegação por leitores de tela.
- Melhorar a acessibilidade de links, imagens e seções da página.
- Aplicar boas práticas de HTML semântico.
- Compreender o papel dos atributos ARIA na acessibilidade.
- Melhorar a navegação por teclado.
- Criar uma página mais inclusiva para diferentes perfis de usuários.

###### Produto Final Esperado

O estudante deverá revisar e melhorar uma página HTML contendo:

- Imagens com descrições adequadas.
- Links com textos claros e contextualizados.
- Estrutura semântica organizada.
- Elementos preparados para leitores de tela.
- Melhor experiência de navegação por teclado.

##### 2. Ferramentas Recomendadas

###### Visual Studio Code (VS Code)

Para que serve: edição dos arquivos HTML e CSS.

Por que é adequado: permite modificar rapidamente a estrutura da página.

Como facilita o aprendizado: possibilita testar imediatamente as melhorias realizadas.

Site: https://code.visualstudio.com

###### Navegador Web

Para que serve: testar a navegação e a interface.

Por que é adequado: permite validar o comportamento dos elementos acessíveis.

Como facilita o aprendizado: mostra a experiência real do usuário.

###### NVDA (NonVisual Desktop Access)

Para que serve: leitor de tela gratuito.

Por que é adequado: possibilita testar a acessibilidade da página.

Como facilita o aprendizado: demonstra como usuários com deficiência visual utilizam o site.

Site: https://www.nvaccess.org

###### WAVE Accessibility Tool

Para que serve: análise automática de acessibilidade.

Por que é adequado: ajuda a identificar problemas comuns.

Como facilita o aprendizado: fornece feedback rápido sobre melhorias necessárias.

Site: https://wave.webaim.org

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve possuir:

VS Code instalado

Navegador atualizado

Projeto da aula anterior

Conexão com internet

Conhecimentos básicos de HTML e CSS

Projeto Apeperia ou projeto disponibilizado pelo professor

NVDA instalado (opcional)

###### Materiais de Apoio

Curso Alura:

https://cursos.alura.com.br/course/acessibilidade-web-front-end

Projeto Base:

https://github.com/designernatan/curso-acessibilidade-web-front-end-1/archive/0115ab16629f4f264184beb291ece993b7246f8c.zip

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações Necessárias

- Disponibilizar o projeto da aula anterior.
- Garantir acesso ao VS Code.
- Demonstrar navegação por teclado.
- Preparar exemplos de páginas com problemas de acessibilidade.

###### Contextualização (5 minutos)

Apresente o cenário:

Maria recebeu a tarefa de tornar um site mais acessível para usuários de leitores de tela. Durante a análise, percebeu imagens sem descrição, links genéricos e falta de organização estrutural.

Pergunta para a turma:

Como garantir que um usuário consiga compreender uma página sem enxergá-la?

###### Revisão de Conceitos (10 minutos)

Revisar:

- atributo alt;
- HTML semântico;
- navegação por teclado;
- foco visual;
- acessibilidade web.
Explicar como esses elementos trabalham em conjunto.

###### Introdução aos Recursos ARIA (10 minutos)

Apresentar:

- função dos atributos ARIA;
- comunicação com leitores de tela;
- identificação de elementos interativos;
- melhoria da experiência do usuário.
Explicar que ARIA complementa a semântica do HTML.

###### Demonstração Prática (10 minutos)

Demonstrar:

- correção de imagens sem alt;
- melhoria de links genéricos;
- organização das seções;
- navegação utilizando TAB;
- teste com leitor de tela.

###### Prática Guiada (10 minutos)

Orientar os alunos a:

- identificar problemas;
- corrigir os elementos;
- testar navegação;
- validar acessibilidade.

###### Encerramento (5 minutos)

Compartilhar resultados e discutir as melhorias implementadas.

###### Pontos de Atenção

- Evitar textos genéricos em links.
- Garantir descrições relevantes em imagens.
- Utilizar estrutura HTML organizada.
- Testar sempre a navegação por teclado.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá atuar como analista de acessibilidade responsável por revisar um site institucional.

Sua missão será:

- localizar problemas de acessibilidade;
- melhorar a experiência para leitores de tela;
- tornar a navegação mais intuitiva.

###### Problema Real Simulado

Uma empresa identificou dificuldades de navegação em seu portal por usuários com deficiência visual e precisa adequar a plataforma.

###### Habilidade Desenvolvida

Análise e implementação de melhorias de acessibilidade utilizando HTML semântico e conceitos básicos de ARIA.

##### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Problemas (PBL)

Os estudantes resolvem problemas reais de acessibilidade.

###### Aprendizagem por Experimentação

Testam a página utilizando teclado e leitores de tela.

###### Ensino por Descoberta

Identificam falhas e propõem melhorias.

###### Elementos de Lemov

- Modelagem
- Prática Guiada
- Verificação de Compreensão
- Feedback Imediato
- Revisão

##### 7. Passo a Passo da Atividade Prática (para os alunos)

###### Etapa 1 – Análise da Página

- Abra o projeto disponibilizado pelo professor.
- Navegue pela página utilizando apenas TAB.
- Observe:
- links;
- botões;
- imagens;
- seções.
- Liste possíveis problemas encontrados.

###### Etapa 2 – Melhorar as Imagens

- Localize imagens sem descrição adequada.
- Adicione descrições claras e objetivas.

###### Etapa 3 – Melhorar os Links

- Identifique links genéricos.
Exemplos:

Clique aqui

Saiba mais

Substitua por descrições claras e contextuais.

###### Etapa 4 – Organizar a Estrutura

- Verifique:
- títulos;
- seções;
- cabeçalhos.
- Organize a página utilizando HTML semântico.

###### Etapa 5 – Testar Navegação

- Utilize TAB para percorrer a página.
- Verifique se a ordem é lógica.
- Quando disponível, teste utilizando NVDA.

###### Etapa 6 – Relatório

- Documente:
- problemas encontrados;
- melhorias realizadas;
- resultados obtidos.

##### 8. Exemplo ou Demonstração

###### Link Pouco Acessível

- <a href="#">Clique aqui</a>

###### Link Melhorado

- <a href="#">Conheça nossos cursos de programação</a>

###### Estrutura Recomendada

- Página
- │
- ├── Cabeçalho
- ├── Navegação
- ├── Conteúdo Principal
- │ ├── Seção 1
- │ └── Seção 2
- └── Rodapé

###### Fluxo da Atividade

- Analisar Página
- ↓
- Identificar Problemas
- ↓
- Corrigir Elementos
- ↓
- Testar Navegação
- ↓
- Validar Acessibilidade

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Página revisada.
- Imagens acessíveis.
- Links descritivos.
- Estrutura semântica organizada.
- Melhor navegação para leitores de tela.

###### Critérios de Verificação

O professor deverá verificar:

Uso adequado do atributo alt

Links claros e contextualizados

Organização semântica correta

Navegação por teclado funcional

Participação na atividade

##### 10. Formato de Entrega da Atividade

###### O que deve ser enviado

- Arquivo HTML atualizado.
- Arquivo CSS atualizado.
- Capturas de tela das melhorias.
- Relatório simples contendo:
- problemas encontrados;
- melhorias implementadas;
- aprendizados obtidos.

###### Nomeação Sugerida

- Aula65_NomeSobrenome
Exemplo:

- Aula65_MariaSilva

###### Onde Entregar

- Google Classroom
- Google Drive
- AVA da instituição

###### Prazo Sugerido

Ao final da aula.

##### 11. Encerramento e Reflexão

Promova uma discussão com a turma:

###### Perguntas para reflexão

- Como um leitor de tela interpreta uma página web?
- Por que links genéricos dificultam a navegação?
- Qual a importância do HTML semântico para acessibilidade?
- Como pequenas melhorias podem tornar a web mais inclusiva?
