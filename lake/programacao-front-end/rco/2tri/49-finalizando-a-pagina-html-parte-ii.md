---
titulo: "Finalizando nossa página HTML Parte II"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 49
serie: 2
aula_rco: "Aula 49"
slides: 22
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PFE/2TRI/49-finalizando-a-pagina-html-parte-ii/49-finalizando-a-pagina-html-parte-ii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/49-finalizando-a-pagina-html-parte-ii/AULA 49_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/49-finalizando-a-pagina-html-parte-ii/AULA 49_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Finalizando nossa página HTML Parte II

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Finalizando nossa página HTML Parte II
- Aula 49

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Desenvolver interfaces gráficas para aplicações computacionais.
- Finalizar e validar páginas web.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Conclusão da mais um página em HTML, falar sobre footer e pseudo classes Parte II.
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
- Projeto aula anterior:
- https://github.com/alura-cursos/aluraplus/archive/refs/heads/aula03.zip
- VS Code:
- https://code.visualstudio.com/

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Dando continuidade ao projeto, iniciamos a finalização de mais uma página do projeto com uso de flexbox, criação de layouts adaptativos.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Alice é uma desenvolvedora web iniciante e foi contratada para criar um site para um cliente. Ela já concluiu a maior parte do trabalho, mas está enfrentando um desafio: fazer com que o rodapé (footer) fique sempre na parte inferior da página, independentemente do conteúdo da página. Ela pesquisa na internet e encontra algumas sugestões, mas não tem certeza de qual método utilizar.
- https://konia.com.br/wp-content/uploads/2020/02/code-1839406_1920-844x563.jpg

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Como Alice pode garantir que o rodapé permaneça sempre na parte inferior da página, independentemente do conteúdo da página?
- Troque ideias com seus colegas!!

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Alice pode utilizar o Flexbox para resolver esse problema. Ao aplicar display: flex; e flex-direction: column; ao container principal (que envolve todo o conteúdo da página, incluindo o rodapé), ela garante que o conteúdo seja disposto em uma única coluna. Em seguida, ela pode aplicar min-height: 100vh; ao container principal para garantir que ele ocupe pelo menos a altura total da janela de visualização.

_1 imagem(ns) no slide._

### Slide 10

- Resposta
- Por fim, Alice pode aplicar flex: 1; ao conteúdo principal da página (não incluindo o rodapé) para fazer com que esse conteúdo ocupe todo o espaço disponível, empurrando o rodapé para a parte inferior da página. Assim, o rodapé permanecerá na parte inferior da página, independentemente do tamanho do conteúdo.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- O footer é uma parte importante de um site, geralmente localizado na parte inferior de uma página, e é usado para fornecer informações adicionais, como direitos autorais, informações de contato, links úteis e outros dados relevantes. Ele desempenha um papel importante na organização e na hierarquia do conteúdo, ajudando os visitantes a encontrar informações adicionais sobre o site e a empresa. Em HTML, um footer é geralmente representado pelo elemento <footer>, que pode ser estilizado usando CSS.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- As pseudo-classes são um recurso do CSS que permite selecionar e estilizar elementos HTML com base em seu estado ou características específicas, sem a necessidade de adicionar classes ou IDs adicionais aos elementos. Pseudo-classes são escritas com dois pontos seguidos pelo nome da pseudo-classe, por exemplo, :hover. Algumas pseudo-classes comuns incluem :hover, :active, :focus, e :nth-child().

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Um exemplo prático de uso de pseudo-classes no contexto de um footer é adicionar um efeito de destaque aos links contidos nele. Utilizando a pseudo-classe :hover, é possível alterar a cor ou o sublinhado dos links quando o usuário passa o cursor sobre eles, fornecendo um feedback visual útil e melhorando a usabilidade.
- https://www.seobility.net/en/wiki/images/7/72/HTML-Sitemap.png

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Para começar a trabalhar com footers e pseudo-classes, basta criar um elemento <footer> em seu arquivo HTML e adicionar algum conteúdo dentro dele, como links ou informações de contato. Em seguida, no arquivo CSS, você pode usar seletores e pseudo-classes para aplicar estilos específicos ao footer e aos elementos dentro dele, personalizando a aparência do footer e proporcionando uma experiência de usuário aprimorada.
- https://www.seobility.net/en/wiki/images/c/ca/HTML-Special-Characters.png

_1 imagem(ns) no slide._

### Slide 15

- Ainda sobre o HTML e CSS, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/html-css-praticando-html-css
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 16

- O desafio do footer
- 7 minutos
- Vamos analisar quais elementos precisamos nesse HTML.
- Link para tarefa: https://cursos.alura.com.br/course/html-css-praticando-html-css/task/103169
- No footer ele vai ser o próprio elemento dele que é o footer, o HTML nos permite criar isso. E a primeira coisa que tem é a imagem do logo e depois tem uma lista de links e dois textos de copyright dando o endereço do site.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Pseudo-classes
- 7 minutos
- O nosso site está ali preto e branco com algumas imagens, alguns botões coloridos.
- Link para tarefa: https://cursos.alura.com.br/course/html-css-praticando-html-css/task/103170
- Mas vamos colocar um detalhe, um brilho, uma coisa diferente. E o que podemos fazer? Queremos ir além do que tem lá. Olhando assim, encaramos o footer, vamos colocar que mude a cor do link quando passo o mouse em cima dele.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 19

- O que vimos na aula de hoje:
- Aprendemos a utilizar o footer e pseudo classes em páginas HTML e CSS.

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

_Fonte: AULA 49_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 49

Questão 1

Qual elemento HTML é geralmente usado para representar o footer de um site?

a) <div>

b) <section>

c) <footer>

d) <nav>

Resposta correta: c) <footer>

O elemento <footer> é usado para representar a parte inferior de uma página, onde informações adicionais, como direitos autorais, informações de contato e links úteis são geralmente colocados.

Questão 2

Qual das seguintes pseudo-classes CSS é usada para aplicar estilos a um link quando o cursor do mouse está sobre ele?

a) :active

b) :focus

c) :visited

d) :hover

Resposta correta: d) :hover

A pseudo-classe :hover é usada para aplicar estilos a um elemento (como um link) quando o cursor do mouse está sobre ele. Isso ajuda a fornecer feedback visual e a melhorar a usabilidade do site.

## Prática

_Fonte: AULA 49_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 49

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Criar e estruturar corretamente um elemento <footer> em HTML.
- Organizar links e informações institucionais no rodapé da página.
- Aplicar pseudo-classes CSS para melhorar a interação do usuário.
- Utilizar efeitos visuais com :hover.
- Finalizar e validar a página web desenvolvida durante o projeto.

###### Produto Final Esperado

Uma página HTML completa contendo:

- Footer estruturado;
- Logo da página;
- Lista de links;
- Informações de copyright;
- Efeitos visuais utilizando pseudo-classes CSS.

##### 2. Ferramentas Recomendadas

###### VS Code

Para que serve: desenvolvimento e edição do HTML e CSS.

Por que é adequado: facilita a organização do projeto e a edição simultânea dos arquivos.

Como facilita o aprendizado: permite visualizar rapidamente as alterações realizadas.

###### Navegador Web

Para que serve: visualizar e testar a página final.

Por que é adequado: permite verificar o comportamento dos links e do footer.

Como facilita o aprendizado: possibilita validar a experiência do usuário.

###### DevTools do Navegador

Para que serve: inspecionar elementos HTML e CSS.

Por que é adequado: ajuda a identificar problemas de alinhamento e estilos.

Como facilita o aprendizado: permite analisar os efeitos das pseudo-classes em tempo real.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve possuir:

Projeto das aulas anteriores concluído

Arquivos:

- index.html
- style.css
Estrutura principal da página criada

Logo do projeto disponível

Navegador atualizado

VS Code instalado

Conexão com internet

###### Material de Apoio

Curso Alura:

https://cursos.alura.com.br/course/html-css-praticando-html-css

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações Necessárias

- Verificar se todos possuem o projeto aberto.
- Revisar rapidamente:
- Flexbox;
- Classes CSS;
- Estrutura HTML;
- Links.

###### Contextualização (5 minutos)

Apresentar o problema:

Muitos sites possuem um rodapé com informações importantes para os usuários.

Perguntar:

O que normalmente encontramos no rodapé de um site?

###### Conceituando o Footer (10 minutos)

Explicar:

- Função do elemento <footer>;
- Informações normalmente presentes:
- contatos;
- links úteis;
- redes sociais;
- direitos autorais.
Demonstrar exemplos reais de sites conhecidos.

###### Conceituando Pseudo-classes (10 minutos)

Explicar:

Pseudo-classes permitem alterar a aparência de elementos em determinados estados.

Apresentar:

- :hover
- :active
- :focus
Mostrar exemplos práticos.

###### Demonstração Prática (10 minutos)

Criar:

- footer;
- lista de links;
- textos institucionais.
Aplicar:

- efeito de mudança de cor ao passar o mouse.

###### Prática Guiada (10 minutos)

Orientar os alunos a:

- criar o footer;
- adicionar links;
- aplicar pseudo-classes;
- testar comportamento.

###### Revisão e Fechamento (5 minutos)

Verificar:

- footer visível;
- links funcionando;
- efeitos visuais aplicados;
- organização visual.

###### Pontos de Atenção

- Verificar fechamento correto das tags.
- Conferir caminhos das imagens.
- Garantir contraste adequado nos links.
- Evitar excesso de efeitos visuais.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá finalizar a landing page desenvolvida ao longo das aulas criando um rodapé completo e aplicando efeitos interativos nos links.

O footer deverá conter:

- logo do projeto;
- lista de links;
- informações de copyright;
- informações institucionais.
Além disso, os links deverão possuir efeitos utilizando pseudo-classes CSS.

###### Problema Real Simulado

Finalização de uma landing page profissional para uma plataforma de streaming.

###### Habilidade Desenvolvida

Construção de componentes finais de interface e aplicação de interatividade utilizando CSS.

##### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Projeto (PBL)

Os estudantes continuam a evolução do projeto iniciado nas aulas anteriores.

###### Experimentação Prática

Testam diferentes estilos e efeitos nos links.

###### Ensino por Descoberta

Observam como pseudo-classes modificam a experiência do usuário.

###### Elementos de Lemov

- Modelagem
- Prática Guiada
- Verificação de Compreensão
- Feedback Imediato
- Revisão Contínua

##### 7. Passo a Passo da Atividade Prática (para os alunos)

###### Etapa 1 – Criar o Footer

- Abra o arquivo index.html.
- Vá até o final da página.
- Crie o elemento <footer>.

###### Etapa 2 – Inserir Conteúdo

- Adicione a logo do projeto.
- Crie uma lista contendo pelo menos 5 links.
- Adicione dois textos institucionais:
- copyright;
- endereço ou informações da empresa.

###### Etapa 3 – Estilizar o Footer

- Abra o arquivo style.css.
- Estilize:
- fundo;
- alinhamento;
- espaçamentos;
- textos.

###### Etapa 4 – Aplicar Pseudo-classes

- Crie efeito para os links usando:
- :hover
- Altere cor ou destaque do link.

###### Etapa 5 – Testar

- Salve os arquivos.
- Atualize o navegador.
- Passe o mouse sobre os links.
- Verifique o comportamento do footer.

##### 8. Exemplo ou Demonstração

###### Estrutura HTML

- <footer>
- <img src="img/logo.png" alt="Logo">
- <ul>
- <li><a href="#">Início</a></li>
- <li><a href="#">Planos</a></li>
- <li><a href="#">Ajuda</a></li>
- <li><a href="#">Contato</a></li>
- </ul>
- <p>© 2025 Plataforma Streaming</p>
- </footer>

###### Exemplo CSS

- footer {
- text-align: center;
- padding: 20px;
- }

###### Exemplo de Pseudo-classe

- footer a:hover {
- color: #167BF7;
- }

###### Conceitos Aplicados

| Conceito | Aplicação |
| --- | --- |
| Footer | Rodapé do site |
| Pseudo-classe | Interação visual |
| Hover | Destaque ao passar o mouse |
| CSS | Estilização do componente |

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Footer completo.
- Logo inserida corretamente.
- Lista de links organizada.
- Informações institucionais.
- Efeito visual utilizando pseudo-classes.

###### Critérios de Verificação

O professor deverá verificar:

Estrutura correta do footer

Links funcionando

Aplicação correta do hover

Organização visual

Código limpo e organizado

##### 10. Formato de Entrega da Atividade

###### Arquivos

- index.html
- style.css
- pasta de imagens

###### Nome da Pasta

- Aula49_NomeSobrenome
Exemplo:

- Aula49_MariaSilva

###### Local de Entrega

- Google Classroom
- Google Drive
- AVA da instituição

###### Prazo

Entrega ao final da aula.

##### 11. Encerramento e Reflexão

Promova uma conversa final com a turma:

###### Perguntas para reflexão

- Qual a função do footer em um site?
- Como as pseudo-classes melhoram a experiência do usuário?
- O que torna um site mais profissional?
- Como pequenos detalhes visuais influenciam a navegação?
