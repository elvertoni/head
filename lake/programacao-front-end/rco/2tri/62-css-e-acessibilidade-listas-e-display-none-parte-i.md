---
titulo: "CSS e Acessibilidade: Listas e display: none – Parte I"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 62
serie: 2
aula_rco: "Aula 62"
slides: 21
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/62-css-e-acessibilidade-listas-e-display-none-parte-i/62-css-e-acessibilidade-listas-e-display-none-parte-i.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/62-css-e-acessibilidade-listas-e-display-none-parte-i/AULA 62_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/62-css-e-acessibilidade-listas-e-display-none-parte-i/AULA 62_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# CSS e Acessibilidade: Listas e display: none – Parte I

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- CSS e Acessibilidade: Listas e display: none – Parte I
- Aula 62

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
- Compreender se o CSS interfere no leitor de tela Parte I.
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
- Projeto aula anterior:
- https://github.com/designernatan/curso-acessibilidade-web-front-end-1/archive/4777a875b8e01a9f14d519e94ce3d282b325a3f9.zip

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Concluímos os estudos sobre os atributos lang e alt e os impactos que ele oferece na utilização de recursos para portadores de deficiência visual.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Carlos é um desenvolvedor web iniciante que está trabalhando em seu primeiro site. Ele quer criar uma lista de produtos oferecidos na página inicial. No entanto, ele também quer que seu site seja acessível para todos os usuários, incluindo aqueles que utilizam leitores de tela.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Ele decidiu usar listas HTML para organizar os produtos e CSS para estilizá-los. No entanto, ele ouviu dizer que a maneira como ele usa o CSS pode afetar a forma como os leitores de tela interpretam o conteúdo da lista. Preocupado, ele se pergunta: "Como eu posso estilizar minha lista sem prejudicar a acessibilidade do meu site para os usuários de leitores de tela?"
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Carlos deve lembrar que os estilos CSS são utilizados principalmente para a aparência visual e não alteram a semântica do HTML. Portanto, desde que ele use as listas HTML corretamente e não dependa apenas do CSS para a estrutura da lista (por exemplo, usando CSS para criar marcadores de lista em vez de usar a tag <li> do HTML), os leitores de tela ainda poderão interpretar a lista corretamente.

_1 imagem(ns) no slide._

### Slide 10

- Resposta
- O essencial é manter a semântica adequada do HTML, garantindo que a lista seja marcada corretamente, mesmo que a apresentação visual seja estilizada com CSS.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- As listas em HTML e sua formatação com CSS desempenham um papel significativo na acessibilidade das páginas da web, especialmente para usuários de leitores de tela.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Listas em HTML (tanto listas ordenadas <ol> quanto listas não ordenadas <ul>) são estruturas semânticas que permitem organizar as informações de forma clara e acessível. Leitores de tela podem informar o usuário sobre o número de itens na lista e a posição de cada item, proporcionando uma experiência de navegação mais completa. Elas são muito úteis para apresentar itens semelhantes ou etapas sequenciais.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- O CSS, Cascading Style Sheets, é a linguagem utilizada para estilizar e formatar o HTML. Através do CSS, é possível personalizar a aparência das listas, como as cores de fundo, os tipos de marcadores usados, o espaçamento entre itens, entre outros. No entanto, é importante que a estilização não prejudique a semântica do HTML ou a experiência dos usuários de leitores de tela.

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Os leitores de tela dependem do correto uso das estruturas semânticas do HTML para interpretar o conteúdo de forma precisa. Se as listas são usadas de forma inadequada (por exemplo, para criar espaçamento ou layout), isso pode confundir os leitores de tela e tornar o conteúdo menos acessível. O uso adequado de listas HTML juntamente com a formatação CSS cuidadosa pode garantir que seu conteúdo seja apresentado de forma agradável visualmente, sem comprometer a acessibilidade.

### Slide 15

- Ainda sobre HTML e leitores de tela, vamos conhecer praticando?
- Na plataforma Alura, vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/acessibilidade-web-front-end
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 16

- Listas para todos
- 11 minutos
- Sabemos que, normalmente, quando clicamos no logotipo de um site somos conduzidos para sua homepage.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36242
- No caso de um usuário com deficiência visual, precisaremos pensar em um recurso mais descritivo para o logo.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 18

- O que vimos na aula de hoje:
- Aprendemos como o CSS pode impactar nos leitores de tela fazendo uso de listas.

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

_Fonte: AULA 62_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 62

Questão 1

Qual das seguintes práticas é a melhor para garantir que sua lista HTML seja acessível para usuários de leitores de tela, mesmo quando você estiliza a lista com CSS?

a) Use o CSS para criar marcadores de lista em vez de usar a tag <li> do HTML.

b) Use apenas CSS para criar a estrutura da lista.

c) Ignore as tags de lista do HTML e confie apenas no CSS para a estrutura e aparência da lista.

d) Use as tags de lista HTML corretamente e use CSS para estilizar a aparência, mantendo a estrutura semântica da lista intacta.

Comentário: A alternativa correta é a D. Isso porque é importante manter a semântica do HTML intacta para que os leitores de tela possam interpretar a lista corretamente. O CSS deve ser usado para estilizar a aparência visual, mas não deve ser usado para criar a estrutura da lista à custa das tags de lista HTML.

Questão 2

Como o uso do CSS pode impactar a forma como os leitores de tela interpretam o conteúdo de uma lista HTML?

a) O CSS pode alterar a semântica do HTML, confundindo os leitores de tela.

b) Os leitores de tela ignoram completamente o CSS, por isso não importa como você estiliza sua lista.

c) O CSS pode adicionar informações adicionais que os leitores de tela podem usar para interpretar o conteúdo da lista.

d) O CSS é usado principalmente para a aparência visual e não altera a semântica do HTML, portanto, desde que a estrutura semântica da lista HTML seja mantida, os leitores de tela ainda podem interpretar a lista corretamente.

Comentário: A alternativa correta é a D. O CSS é usado para alterar a aparência visual do conteúdo HTML, mas não altera a semântica do HTML. Portanto, desde que a estrutura semântica da lista HTML seja mantida, os leitores de tela ainda podem interpretar a lista corretamente.

## Prática

_Fonte: AULA 62_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 62

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Utilizar listas HTML de forma semântica e acessível.
- Diferenciar listas ordenadas e não ordenadas.
- Aplicar estilização CSS em listas sem comprometer a acessibilidade.
- Compreender como leitores de tela interpretam listas.
- Identificar problemas causados pelo uso inadequado do CSS em estruturas semânticas.
- Melhorar a experiência de navegação para usuários que utilizam tecnologias assistivas.

###### Produto Final Esperado

O estudante deverá criar uma página HTML contendo:

- Lista de produtos ou serviços.
- Estrutura semântica correta utilizando <ul>, <ol> e <li>.
- Estilização personalizada com CSS.
- Elementos acessíveis para usuários de leitores de tela.

##### 2. Ferramentas Recomendadas

###### Visual Studio Code (VS Code)

Para que serve: edição dos arquivos HTML e CSS.

Por que é adequado: facilita a criação e organização da estrutura da página.

Como facilita o aprendizado: permite visualizar rapidamente as alterações realizadas.

Site: https://code.visualstudio.com

###### Navegador Web

Para que serve: visualização e testes da página.

Por que é adequado: permite validar o comportamento visual e estrutural.

Como facilita o aprendizado: ajuda a comparar a experiência visual com a experiência semântica.

###### NVDA (NonVisual Desktop Access)

Para que serve: leitor de tela gratuito.

Por que é adequado: demonstra como usuários com deficiência visual navegam pelo conteúdo.

Como facilita o aprendizado: permite testar se as listas estão sendo interpretadas corretamente.

Site: https://www.nvaccess.org

###### WAVE Accessibility Tool

Para que serve: análise de acessibilidade.

Por que é adequado: identifica possíveis problemas estruturais.

Como facilita o aprendizado: fornece feedback rápido sobre boas práticas.

Site: https://wave.webaim.org

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve possuir:

VS Code instalado

Navegador atualizado

Projeto HTML da aula anterior

Conexão com internet

Leitor de tela NVDA (opcional)

Conhecimentos básicos de HTML e CSS

Projeto Apeperia ou projeto disponibilizado pelo professor

###### Materiais de Apoio

Curso Alura:

https://cursos.alura.com.br/course/acessibilidade-web-front-end

Projeto base:

https://github.com/designernatan/curso-acessibilidade-web-front-end-1/archive/4777a875b8e01a9f14d519e94ce3d282b325a3f9.zip

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações Necessárias

- Disponibilizar o projeto utilizado na aula anterior.
- Garantir acesso ao VS Code.
- Demonstrar exemplos de listas acessíveis.
- Preparar uma página com listas e navegação.

###### Contextualização (5 minutos)

Apresente o cenário:

Carlos deseja criar uma lista de produtos em seu site, mas quer garantir que usuários de leitores de tela consigam compreender facilmente as informações.

Pergunta para a turma:

É possível deixar uma lista visualmente bonita sem prejudicar a acessibilidade?

###### Conceituando Listas Semânticas (10 minutos)

Explique:

- Lista ordenada (<ol>)
- Lista não ordenada (<ul>)
- Item de lista (<li>)
Mostrar como leitores de tela interpretam:

- quantidade de itens;
- posição de cada item;
- estrutura da informação.

###### CSS e Acessibilidade (10 minutos)

Explicar:

- CSS altera aparência.
- HTML define significado.
Mostrar exemplos onde:

- a lista continua acessível;
- a lista perde significado por uso inadequado.
Discutir boas práticas.

###### Demonstração Prática (10 minutos)

Demonstrar:

- Criação de lista semântica.
- Personalização com CSS.
- Teste em leitor de tela.
- Navegação utilizando teclado.

###### Prática Guiada (10 minutos)

Orientar os alunos a:

- criar listas;
- estilizar com CSS;
- testar acessibilidade;
- analisar comportamento dos leitores de tela.

###### Encerramento (5 minutos)

Compartilhar resultados e discutir dificuldades encontradas.

###### Pontos de Atenção

- Não utilizar listas apenas para criar layout.
- Manter a estrutura semântica correta.
- Evitar substituir elementos HTML por soluções apenas visuais.
- Garantir que os itens da lista façam sentido quando lidos por um leitor de tela.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá criar uma seção de catálogo para um site institucional contendo uma lista de produtos ou serviços.

A lista deverá:

- Utilizar estrutura HTML correta.
- Possuir estilização CSS personalizada.
- Permanecer acessível para leitores de tela.

###### Problema Real Simulado

Uma empresa deseja exibir seus produtos em uma página web sem comprometer a acessibilidade para usuários com deficiência visual.

###### Habilidade Desenvolvida

Construção de componentes HTML semânticos aliados à estilização acessível com CSS.

##### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Problemas (PBL)

Os estudantes solucionam um problema real de acessibilidade.

###### Aprendizagem por Experimentação

Criam e testam listas utilizando leitores de tela.

###### Ensino por Descoberta

Observam como alterações visuais afetam a experiência do usuário.

###### Elementos de Lemov

- Modelagem
- Prática Guiada
- Verificação de Compreensão
- Feedback Imediato
- Revisão

##### 7. Passo a Passo da Atividade Prática (para os alunos)

###### Etapa 1 – Criar a Estrutura

- Abra o projeto da aula anterior.
- Crie uma nova seção chamada "Produtos".
- Adicione um título para a seção.

###### Etapa 2 – Criar a Lista

- Crie uma lista contendo pelo menos 5 produtos ou serviços.
- Utilize corretamente:
- <ul>
- <li>

###### Etapa 3 – Aplicar Estilização

- No arquivo CSS:
- altere cores;
- ajuste espaçamentos;
- personalize marcadores da lista.
- Mantenha a estrutura HTML original.

###### Etapa 4 – Melhorar Acessibilidade

- Verifique se cada item possui descrição clara.
- Certifique-se de que a ordem das informações faz sentido.

###### Etapa 5 – Testar

- Navegue utilizando apenas o teclado.
- Quando disponível, teste com NVDA.
- Observe como a lista é anunciada.

###### Etapa 6 – Evidências

- Capture prints:
- da estrutura HTML;
- da página estilizada;
- do resultado final.

##### 8. Exemplo ou Demonstração

###### Exemplo de Lista Semântica

<section>

<h2>Nossos Serviços</h2>

<ul>

<li>Desenvolvimento Web</li>

<li>Criação de Aplicativos</li>

<li>Consultoria em TI</li>

<li>Hospedagem de Sites</li>

<li>Suporte Técnico</li>

</ul>

</section>

###### Exemplo de CSS

ul {

list-style-type: square;

padding-left: 20px;

}

li {

margin-bottom: 10px;

}

###### Estrutura Correta

Seção

└── Lista

├── Item 1

├── Item 2

├── Item 3

├── Item 4

└── Item 5

###### Fluxo da Atividade

Criar Lista

↓

Aplicar CSS

↓

Testar Navegação

↓

Validar Acessibilidade

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Lista criada corretamente.
- Estrutura semântica adequada.
- Estilização CSS aplicada.
- Navegação acessível.
- Conteúdo compreensível para leitores de tela.

###### Critérios de Verificação

O professor deverá verificar:

Uso correto de <ul> e <li>

Estrutura semântica adequada

Estilização sem perda de acessibilidade

Organização visual da lista

Participação na atividade

##### 10. Formato de Entrega da Atividade

###### O que deve ser enviado

- Arquivo HTML.
- Arquivo CSS.
- Capturas de tela da página final.
- Relatório simples contendo:
- melhorias realizadas;
- testes executados;
- aprendizados obtidos.

###### Nomeação Sugerida

Aula62_NomeSobrenome

Exemplo:

Aula62_CarlosSilva

###### Onde Entregar

- Google Classroom
- Google Drive
- AVA da instituição

###### Prazo Sugerido

Ao final da aula.

##### 11. Encerramento e Reflexão

Promova uma discussão com a turma:

###### Perguntas para reflexão

- Por que listas HTML são importantes para acessibilidade?
- O CSS altera a semântica de uma página?
- Como leitores de tela interpretam listas?
- Qual a diferença entre organizar visualmente e estruturar semanticamente?
