---
titulo: "Posicionando Elementos na Página – Parte II"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 47
serie: 2
aula_rco: "Aula 47"
slides: 22
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/47-posicionando-elementos-na-pagina-parte-ii/47-posicionando-elementos-na-pagina-parte-ii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/47-posicionando-elementos-na-pagina-parte-ii/AULA 47_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/47-posicionando-elementos-na-pagina-parte-ii/AULA 47_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Posicionando Elementos na Página – Parte II

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Posicionando Elementos na Página – Parte II
- Aula 47

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Desenvolver interfaces gráficas para aplicações computacionais.
- Organizar layout de páginas web.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Colocar em prática posicionamento de elementos em HTML Parte II.
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
- https://github.com/alura-cursos/aluraplus/archive/refs/heads/aula02.zip
- VS Code:
- https://code.visualstudio.com/

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Iniciamos os estudos sobre o posicionamento dos elementos em páginas HTML, no caso margin pads e alinhamento.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- André é um desenvolvedor web iniciante e está trabalhando em um projeto HTML para criar um blog. Ele percebe que seu site tem várias seções de conteúdo semelhantes, como cabeçalho, rodapé e área de postagens, e deseja organizar melhor o código para facilitar a manutenção. Além disso, ele também quer aplicar estilos consistentes a diferentes elementos do site sem repetir o código CSS.

_2 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- André se pergunta: "Como posso organizar melhor as seções do meu site e reutilizar estilos CSS sem repetir o código?"
- Discutam em duplas e socializem as ideias com a turma no final!

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- André pode usar o elemento HTML <section> para dividir o conteúdo do seu site em seções independentes e semânticas, facilitando a organização e a manutenção do código. Além disso, para reutilizar estilos em diferentes elementos, ele pode criar classes CSS comuns e aplicá-las aos elementos desejados. Isso permite que ele defina um conjunto de estilos uma vez e o aplique a vários elementos, tornando a manutenção e a organização do código mais eficientes.

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- Ao construir páginas HTML, é importante organizar o conteúdo em seções lógicas e semânticas para facilitar a manutenção e melhorar a acessibilidade. O elemento HTML <section> é uma ferramenta útil para criar essas seções. Ele permite agrupar blocos de conteúdo relacionado, como cabeçalhos, rodapés, artigos e áreas de navegação, de uma forma clara e estruturada. Isso torna o código mais fácil de entender e gerenciar, tanto para desenvolvedores quanto para tecnologias assistivas.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- Outro aspecto importante do desenvolvimento de páginas HTML é a capacidade de reutilizar estilos CSS. Isso pode ser alcançado através da criação de classes CSS comuns que podem ser aplicadas a vários elementos. Criar uma classe CSS comum significa definir um conjunto de estilos que pode ser usado em diferentes partes do site, garantindo uma aparência consistente e reduzindo a quantidade de código repetido.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Por exemplo, se você deseja que todos os títulos do seu site tenham a mesma aparência, pode criar uma classe CSS chamada "título" com os estilos desejados e aplicá-la a todos os elementos de título. Isso permite que você faça alterações no estilo de todos os títulos de uma só vez, modificando apenas a classe CSS em vez de atualizar cada elemento individualmente.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Por exemplo, se você deseja que todos os títulos do seu site tenham a mesma aparência, pode criar uma classe CSS chamada "título" com os estilos desejados e aplicá-la a todos os elementos de título. Isso permite que você faça alterações no estilo de todos os títulos de uma só vez, modificando apenas a classe CSS em vez de atualizar cada elemento individualmente.

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Em resumo, a organização do conteúdo em seções semânticas usando o elemento <section> e a reutilização de estilos CSS por meio de classes comuns são práticas fundamentais no desenvolvimento de páginas HTML. Essas técnicas facilitam a manutenção do código, melhoram a acessibilidade e garantem uma aparência consistente em todo o site.

_1 imagem(ns) no slide._

### Slide 15

- Ainda sobre o HTML e CSS, vamos conhecer praticando?
- DESENVOLVIMENTO DE SISTEMAS
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/html-css-praticando-html-css
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_5 imagem(ns) no slide._

### Slide 16

- Construindo nova section
- 9 minutos
- Construímos toda a primeira seção do nosso projeto.
- Link para tarefa: https://cursos.alura.com.br/course/html-css-praticando-html-css/task/103166
- Mas o serviço não acabou, infelizmente. Tem ainda muita coisa naquele layout para construirmos.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Reutilizando estilos
- 9 minutos
- Reutilizar os estilos é algo importante
- Link para tarefa: https://cursos.alura.com.br/course/html-css-praticando-html-css/task/103167
- Na vida real, no ambiente e você vai ser desenvolvedor front-end, é super comum isso. Ou seja, você precisa entender como funciona cada um dos atributos e propriedades do CSS, mas depois você vai reutilizar esse entendimento.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- O que vimos na aula de hoje:
- Aprendemos reutilizar estilos e construções de novas seções em páginas HTML e CSS.

_1 imagem(ns) no slide._

### Slide 19

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

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

_Fonte: AULA 47_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 47

Questão 1

Qual elemento HTML é usado para criar seções independentes e semânticas em uma página?

a) <section>

b) <div>

c) <article>

d) <span>

Resposta correta: a) <section>

Comentário: O elemento HTML <section> é usado para criar seções independentes e semânticas em uma página. Ele ajuda a organizar o conteúdo em blocos lógicos, facilitando a manutenção e a compreensão do código.

Questão 2

Qual técnica é usada para reutilizar estilos em diferentes elementos de uma página HTML?

a) Repetir o estilo inline para cada elemento

b) Aplicar uma classe CSS comum aos elementos

c) Usar um atributo HTML específico para estilos

d) Criar múltiplos arquivos CSS para cada elemento

Resposta correta: b) Aplicar uma classe CSS comum aos elementos

Comentário: Para reutilizar estilos em diferentes elementos de uma página HTML, você pode aplicar uma classe CSS comum aos elementos desejados. Isso permite que você defina um conjunto de estilos uma vez e o aplique a vários elementos, tornando a manutenção e a organização do código mais eficientes.

## Prática

_Fonte: AULA 47_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 47

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Organizar conteúdos em seções utilizando a tag <section>.
- Reutilizar estilos CSS através de classes.
- Criar layouts mais organizados e padronizados.
- Melhorar a manutenção e legibilidade do código.
- Aplicar estilos reutilizáveis em diferentes elementos da página.
Produto final esperado:

- Página HTML organizada em seções semânticas e estilizada utilizando classes CSS reutilizáveis.

##### 2. Ferramentas Recomendadas

###### VS Code

- Para que serve: edição dos arquivos HTML e CSS.
- Por que é adequado: facilita organização e reutilização do código.
- Como facilita o aprendizado: permite visualizar a estrutura do projeto e editar rapidamente os estilos.

###### Navegador Web

- Para que serve: visualizar a página desenvolvida.
- Por que é adequado: mostra o comportamento real do layout.
- Como facilita o aprendizado: possibilita validar a organização visual.

###### DevTools do Navegador

- Para que serve: inspecionar elementos e classes CSS.
- Por que é adequado: ajuda a visualizar estilos aplicados.
- Como facilita o aprendizado: permite identificar reutilização de classes.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Projeto das aulas anteriores funcionando
- Arquivos:
- index.html
- style.css
- Estrutura HTML básica criada
- Navegador atualizado
- VS Code instalado
- Conexão com internet
Material de apoio indicado na aula: https://cursos.alura.com.br/course/html-css-praticando-html-css

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações necessárias

- Garantir que todos tenham o projeto aberto.
- Revisar rapidamente:
- classes CSS
- margin e padding
- organização estrutural HTML

###### Condução da aula

###### Contextualização (5 minutos)

Apresentar cenário:

- Sites grandes possuem muitas áreas semelhantes.
Perguntar:

- Como evitar repetir o mesmo código várias vezes?

###### Conceituando Sections (10 minutos)

Explicar:

###### <section>

- Organiza conteúdos relacionados.
- Melhora:
- manutenção
- acessibilidade
- organização
Demonstrar exemplo simples.

###### Reutilizando estilos CSS (10 minutos)

Explicar:

- Classes permitem reutilização de estilos.
Demonstrar:

- .botao {
- background-color: blue;
- color: white;
- }
Mostrar:

- mesma classe aplicada em vários elementos.

###### Demonstração prática (10 minutos)

Demonstrar:

- Criar nova <section>.
- Aplicar classes reutilizáveis.
- Organizar elementos visualmente.
Mostrar:

- redução de repetição no CSS.

###### Prática guiada (10 minutos)

Alunos devem:

- Criar nova seção.
- Aplicar classes reutilizadas.
- Ajustar alinhamento e organização.

###### Revisão e fechamento (5 minutos)

- Conferir reutilização correta.
- Verificar organização do HTML.
- Ajustar detalhes visuais.

###### Pontos de atenção

- Evitar criar muitas classes desnecessárias.
- Manter nomes claros para classes.
- Organizar indentação do HTML.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá:

- Criar uma nova seção no projeto.
- Organizar o conteúdo utilizando HTML semântico.
- Criar classes CSS reutilizáveis.
- Aplicar os mesmos estilos em diferentes elementos.
Problema real simulado: Organização estrutural e padronização visual de uma landing page profissional.

Habilidade desenvolvida: Estruturação semântica e reutilização de estilos CSS.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em projeto
- Experimentação prática
- Ensino por descoberta
- Elementos de Lemov:
- Modelagem
- Prática guiada
- Verificação de entendimento
- Feedback imediato

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Abra o projeto desenvolvido anteriormente.
- Localize o arquivo index.html.
- Crie uma nova <section>.
- Adicione:
- título
- texto
- botão
- imagem (opcional)
- No CSS, crie uma classe reutilizável.
- Aplique a mesma classe em:
- botões
- títulos
- caixas
- Ajuste:
- cores
- espaçamentos
- alinhamentos
- Verifique se os estilos estão padronizados.
- Salve os arquivos.
- Abra no navegador.
- Analise:
- organização visual
- reutilização dos estilos
- Ajuste detalhes finais.

##### 8. Exemplo ou Demonstração

###### Exemplo de section

- <section class="conteudo">
- <h2>Título da seção</h2>
- <p>Texto da seção.</p>
- </section>

###### Exemplo de classe reutilizável

- .titulo {
- color: white;
- font-size: 32px;
- }

###### Aplicação da classe

- <h1 class="titulo">Título principal</h1>
- <h2 class="titulo">Título secundário</h2>

###### Conceitos reforçados

- Sections organizam conteúdo.
- Classes evitam repetição.
- CSS reutilizável melhora manutenção.

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Página organizada em seções.
- Uso correto da tag <section>.
- Classes CSS reutilizadas corretamente.
- Layout visual padronizado.
- Código organizado e funcional.
O professor verifica:

- Organização semântica do HTML.
- Reutilização correta das classes.
- Qualidade visual da página.

##### 10. Formato de Entrega da Atividade

- Formato: Pasta compactada contendo:
- index.html
- style.css
- imagens utilizadas
- Entrega: ao final da aula.
- Prazo sugerido: imediato.

##### 11. Encerramento e Reflexão

Perguntas orientadoras:

- Como as sections ajudam na organização do site?
- Qual a vantagem de reutilizar classes CSS?
- O que acontece quando repetimos muito código?
