---
titulo: "Atributos lang e alt – Parte I"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 60
serie: 2
aula_rco: "Aula 60"
slides: 22
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/60-atributos-lang-e-alt-parte-i/60-atributos-lang-e-alt-parte-i.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/60-atributos-lang-e-alt-parte-i/AULA 60_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/60-atributos-lang-e-alt-parte-i/AULA 60_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Atributos lang e alt – Parte I

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Atributos lang e alt – Parte I
- Aula 60

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
- Entender como funcionam Atributos lang e alt Parte I.
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
- http://www.reinaldoferraz.com.br/acessibilidade-seo-e-svg/
- Lang e Alt:
- https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36282
- Projeto aula anterior:
- https://github.com/designernatan/curso-acessibilidade-web-front-end-1/archive/9d23967baf7e252a52874a54fe7414e7cf58fd14.zip

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Concluímos os estudos sobre utilização de leitores de tela para páginas HTML, sua importância para inclusão de pessoas portadoras de necessidades especiais a seus projetos.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Rafael está trabalhando em um site para um cliente que vende produtos artesanais. Ele adicionou várias imagens dos produtos na página principal, mas quando ele testou o site com um simulador de leitor de tela, as imagens não eram descritas, tornando a navegação confusa para usuários que dependem dessa tecnologia.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Rafael então se perguntou: "Como posso tornar as imagens acessíveis para os usuários de leitores de tela e garantir que, caso as imagens não sejam carregadas, o usuário ainda saiba o que elas representam?"
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Rafael precisa usar o atributo "alt" em todas as imagens que ele adicionou ao site. Ao fazer isso, ele estará fornecendo uma descrição textual para cada imagem que os leitores de tela podem ler para os usuários, tornando o conteúdo da imagem acessível.
- Além disso, se por algum motivo as imagens não forem carregadas, o texto alternativo será exibido, permitindo que todos os usuários entendam o que a imagem deveria representar.

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- O atributo "alt" é um elemento crucial em páginas HTML, especialmente quando se trata de acessibilidade. O termo "alt" é a abreviação de "alternativo", o que dá uma ideia de seu propósito fundamental. Este atributo é usado com o elemento de imagem "<img>" para fornecer uma descrição textual das imagens.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- Esta descrição alternativa desempenha um papel importante quando a imagem não pode ser carregada na página, seja devido a problemas de rede, problemas com a própria imagem, ou quando o usuário desativou o carregamento de imagens. Nesses casos, a descrição fornecida pelo atributo "alt" é exibida em vez da imagem.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Além disso, e talvez mais importante, o atributo "alt" é essencial para a acessibilidade na web. Os leitores de tela, que são usados por pessoas com deficiência visual para navegar na internet, leem em voz alta a descrição fornecida pelo atributo "alt", permitindo que esses usuários entendam o conteúdo e o contexto da imagem.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Por fim, o atributo "alt" também tem um papel no SEO (Search Engine Optimization) porque os motores de busca o utilizam para entender o conteúdo da imagem, o que pode melhorar a classificação da página nos resultados de pesquisa.

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Portanto, o atributo "alt" é uma pequena adição à sua marcação HTML que pode ter um impacto significativo na acessibilidade, na experiência do usuário e na visibilidade da sua página na web.

_1 imagem(ns) no slide._

### Slide 15

- Ainda sobre HTML e leitores de tela, vamos conhecer praticando?
- Na plataforma Alura, vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/acessibilidade-web-front-end
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 16

- Cuidados com o sotaque
- 5 minutos
- Espero que você tenha se aventurado no código HTML que foi disponibilizado.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36236
- Iremos nos atentar a alguns detalhes importantes. Analisaremos como se dá a navegação do NVDA ao longo da página. Percebam que o leitor de tela lê os primeiros itens "Sobre", "Planos", "Blog", "Institucional" e "Contato" com um forte sotaque norte-americano.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Textos alternativos
- 13 minutos
- O termo "alt" é conhecido entre desenvolvedores e designers, e se refere a "texto alternativo" vinculado a imagens.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36237
- O atributo “alt” é útil não apenas para usuários de leitor de tela, mas também se por algum motivo a imagem não for carregada na página. Com o apoio de texto, criamos uma experiência melhor na interface.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 19

- O que vimos na aula de hoje:
- Aprendemos como utilizar o atributo “alt” em páginas HTML a fim de facilitar a leitura de objetos visuais em leitores de tela.

_1 imagem(ns) no slide._

### Slide 20

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 21

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

### Slide 22

_(sem texto)_

## Atividade

_Fonte: AULA 60_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 60

Questão 1

Qual é a finalidade principal do atributo "alt" em uma tag de imagem HTML?

a) Alterar a cor da imagem.

b) Fornecer um texto alternativo para a imagem.

c) Ajustar o tamanho da imagem.

d) Adicionar um efeito de hover à imagem.

Comentário: A resposta correta é a opção (b). O atributo "alt" é usado para fornecer um texto descritivo para imagens. Isso é especialmente útil para leitores de tela e situações onde a imagem não pode ser carregada.

Questão 2

Quando você deve usar o atributo "alt" em imagens HTML?

a) Somente quando a imagem é um link.

b) Somente quando a imagem é muito grande.

c) Somente quando a imagem é decorativa.

d) Em todas as imagens, independentemente do propósito.

Comentário: A resposta correta é a opção (d). O atributo "alt" deve ser usado em todas as imagens, independentemente do propósito. Isso ajuda a melhorar a acessibilidade e a experiência do usuário, especialmente para pessoas com deficiência visual ou para situações em que a imagem não pode ser carregada.

## Prática

_Fonte: AULA 60_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 60

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender a função do atributo alt em imagens.
- Identificar imagens sem descrição adequada.
- Criar textos alternativos claros e objetivos.
- Compreender a importância do atributo lang para leitores de tela.
- Melhorar a acessibilidade de páginas HTML.
- Reconhecer a relação entre acessibilidade e SEO.

###### Produto Final Esperado

O estudante deverá entregar uma página HTML contendo:

- Imagens com atributos alt adequados.
- Idioma principal da página configurado corretamente.
- Melhor experiência para usuários de leitores de tela.
- Estrutura acessível e organizada.

##### 2. Ferramentas Recomendadas

###### Visual Studio Code (VS Code)

Para que serve: edição de arquivos HTML.

Por que é adequado: permite editar rapidamente atributos e estruturas da página.

Como facilita o aprendizado: possibilita visualizar imediatamente os resultados das alterações.

Site: https://code.visualstudio.com

###### Navegador Web

Para que serve: visualização e testes da página.

Por que é adequado: permite validar o comportamento do conteúdo.

Como facilita o aprendizado: ajuda a compreender a experiência do usuário final.

###### NVDA (NonVisual Desktop Access)

Para que serve: leitor de tela gratuito.

Por que é adequado: possibilita testar a acessibilidade da página.

Como facilita o aprendizado: demonstra como usuários com deficiência visual acessam conteúdos web.

Site: https://www.nvaccess.org

###### WAVE Accessibility Tool

Para que serve: análise automática de acessibilidade.

Por que é adequado: identifica problemas relacionados à acessibilidade.

Como facilita o aprendizado: fornece feedback rápido para correções.

Site: https://wave.webaim.org

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve possuir:

VS Code instalado

Navegador atualizado

Projeto HTML disponível

Conexão com internet

Conhecimentos básicos de HTML

Leitor de tela NVDA (opcional)

###### Materiais de Apoio

Curso Alura:

https://cursos.alura.com.br/course/acessibilidade-web-front-end

Projeto Base:

https://github.com/designernatan/curso-acessibilidade-web-front-end-1/archive/9d23967baf7e252a52874a54fe7414e7cf58fd14.zip

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações Necessárias

- Disponibilizar um projeto HTML para análise.
- Garantir acesso ao VS Code.
- Demonstrar rapidamente o funcionamento do NVDA.
- Preparar exemplos de imagens sem atributo alt.

###### Contextualização (5 minutos)

Apresente o cenário:

Rafael criou um catálogo virtual com várias imagens de produtos artesanais. Porém, usuários que utilizam leitores de tela não conseguem compreender o conteúdo exibido nas imagens.

Pergunta para a turma:

Como podemos descrever imagens para pessoas que não conseguem vê-las?

###### Conceituando o Atributo Alt (10 minutos)

Explique:

- O significado de "texto alternativo".
- Como leitores de tela utilizam o atributo alt.
- O que acontece quando uma imagem não carrega.
- A importância para SEO.
Apresente exemplos de boas e más descrições.

###### Conceituando o Atributo Lang (10 minutos)

Explique:

- Definição do idioma principal da página.
- Como leitores de tela utilizam essa informação.
- Problemas causados pela ausência do atributo.
Mostre exemplos de páginas em português e inglês.

###### Demonstração Prática (10 minutos)

Demonstrar:

- Inserção de atributo alt em imagens.
- Configuração do idioma principal da página.
- Teste da leitura utilizando leitor de tela.

###### Prática Guiada (10 minutos)

Orientar os alunos a:

- localizar imagens;
- adicionar descrições;
- revisar idioma da página;
- testar acessibilidade.

###### Encerramento (5 minutos)

Compartilhar resultados e discutir os benefícios das melhorias realizadas.

###### Pontos de Atenção

- Evitar descrições genéricas.
- Não repetir informações desnecessárias.
- Garantir que o idioma configurado seja compatível com o conteúdo.
- Pensar na experiência de quem utiliza leitores de tela.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá atuar como desenvolvedor responsável por revisar a acessibilidade de uma página institucional.

Sua missão será melhorar a interpretação do conteúdo por leitores de tela utilizando os atributos alt e lang.

###### Problema Real Simulado

Uma empresa deseja tornar seu catálogo digital acessível para todos os usuários, incluindo pessoas com deficiência visual.

###### Habilidade Desenvolvida

Aplicação de atributos HTML voltados à acessibilidade e otimização da experiência do usuário.

##### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Problemas (PBL)

Os estudantes resolvem desafios reais de acessibilidade.

###### Aprendizagem por Experimentação

Testam a página utilizando leitores de tela.

###### Ensino por Descoberta

Identificam falhas e propõem melhorias.

###### Elementos de Lemov

- Modelagem
- Prática Guiada
- Verificação de Compreensão
- Feedback Imediato
- Revisão

##### 7. Passo a Passo da Atividade Prática (para os alunos)

###### Etapa 1 – Analisar o Projeto

- Abra o projeto disponibilizado pelo professor.
- Identifique todas as imagens da página.
- Verifique se possuem descrição alternativa.

###### Etapa 2 – Revisar Imagens

- Para cada imagem:
- identifique sua função;
- escreva uma descrição clara;
- registre as melhorias realizadas.

###### Etapa 3 – Configurar Idioma

- Localize a estrutura principal da página.
- Verifique o idioma definido.
- Ajuste o idioma conforme o conteúdo apresentado.

###### Etapa 4 – Testar a Página

- Execute a página no navegador.
- Teste a navegação utilizando teclado.
- Quando disponível, utilize o NVDA.

###### Etapa 5 – Validar Melhorias

- Verifique:
- leitura das imagens;
- comportamento do idioma;
- clareza das descrições.

###### Etapa 6 – Evidências

- Capture prints:
- do código atualizado;
- da página em execução;
- das melhorias realizadas.

##### 8. Exemplo ou Demonstração

###### Exemplo sem Texto Alternativo

- <img src="produto.jpg">

###### Exemplo Corrigido

- <img src="produto.jpg" alt="Cesto artesanal produzido com fibras naturais">

###### Idioma da Página

- <html lang="pt-BR">

###### Fluxo da Atividade

- Analisar Página
- ↓
- Identificar Imagens
- ↓
- Adicionar Alt
- ↓
- Configurar Lang
- ↓
- Testar Acessibilidade
- ↓
- Validar Melhorias

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Página HTML revisada.
- Imagens com descrições adequadas.
- Idioma configurado corretamente.
- Melhor experiência para leitores de tela.

###### Critérios de Verificação

O professor deverá verificar:

Uso adequado do atributo alt

Descrições claras e objetivas

Configuração correta do atributo lang

Melhorias de acessibilidade implementadas

Participação na atividade

##### 10. Formato de Entrega da Atividade

###### O que deve ser enviado

- Arquivo HTML atualizado.
- Capturas de tela das melhorias.
- Relatório simples contendo:
- problemas encontrados;
- melhorias realizadas;
- aprendizados obtidos.

###### Nomeação Sugerida

- Aula60_NomeSobrenome
Exemplo:

- Aula60_RafaelSilva

###### Onde Entregar

- Google Classroom
- Google Drive
- AVA da instituição

###### Prazo Sugerido

Ao final da aula.

##### 11. Encerramento e Reflexão

Promova uma discussão com a turma:

###### Perguntas para reflexão

- Por que o atributo alt é importante para acessibilidade?
- Como leitores de tela utilizam o texto alternativo?
- O que acontece quando uma imagem não possui descrição?
- Como o atributo lang melhora a experiência dos usuários?
