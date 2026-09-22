---
titulo: "A dupla HTML e CSS Parte I"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 44
serie: 2
aula_rco: "Aula 44"
slides: 20
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/44-a-dupla-html-e-css-parte-i/44-a-dupla-html-e-css-parte-i.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/44-a-dupla-html-e-css-parte-i/AULA 44_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/44-a-dupla-html-e-css-parte-i/AULA 44_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# A dupla HTML e CSS Parte I

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- A dupla HTML e CSS Parte I
- Aula 44

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Desenvolver interfaces gráficas para aplicações computacionais.
- Criar e estilizar páginas utilizando HTML e CSS.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Colocar em prática HTML e CSS Parte I.
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
- https://github.com/alura-cursos/aluraplus/archive/refs/heads/aula01.zip
- VS Code:
- https://code.visualstudio.com/

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Iniciamos os estudos práticos sobre criação de páginas com uso de HTML e CSS.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- João é um desenvolvedor web iniciante e está trabalhando em seu primeiro projeto de site para um cliente. O cliente solicitou que ele crie um botão personalizado para a seção de inscrição do site. João sabe como criar um botão básico com HTML, mas não tem muita experiência com CSS e não tem certeza de como personalizá-lo para atender às necessidades do cliente.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Como João pode criar e personalizar um botão usando HTML e CSS para atender às especificações do cliente?
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Para criar e personalizar um botão usando HTML e CSS, João deve seguir estas etapas:
- Primeiro, João deve criar o botão HTML. Ele pode usar a tag <button> ou um link <a> com uma classe específica para isso.
- Em seguida, João deve criar um arquivo CSS externo (por exemplo, style.css) e vinculá-lo ao seu documento HTML usando a tag <link> dentro da tag <head>

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- Botões são elementos interativos comuns em páginas da web que permitem aos usuários realizar ações, como enviar formulários, navegar para outra página ou acionar eventos em JavaScript. Eles são cruciais para a criação de experiências de usuário intuitivas e agradáveis, permitindo que os visitantes do site interajam de maneira eficaz com o conteúdo.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- No desenvolvimento web, os botões podem ser criados usando várias tags HTML, como <button>, <input> e <a>. A tag <button> é geralmente usada para criar botões genéricos, enquanto a tag <input> com o atributo type="submit" é utilizada em formulários. A tag <a> pode ser estilizada como um botão para criar links que pareçam botões.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Para personalizar a aparência de botões, os desenvolvedores geralmente aplicam estilos CSS, como cores de fundo, fontes, bordas e efeitos de transição. Além disso, é comum adicionar classes e IDs específicas aos botões para aplicar estilos e comportamentos específicos a diferentes botões no site.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- A acessibilidade é outro aspecto importante na utilização de botões em HTML. Garantir que os botões sejam claramente visíveis, facilmente clicáveis e tenham descrições de texto alternativo (usando o atributo aria-label, por exemplo) pode melhorar a experiência do usuário para pessoas com diferentes habilidades e dispositivos. Assim, ao criar botões em HTML, os desenvolvedores devem considerar tanto a estética quanto a funcionalidade para proporcionar uma experiência agradável e acessível a todos os usuários.

_1 imagem(ns) no slide._

### Slide 14

- Ainda sobre o HTML e CSS, vamos conhecer praticando?
- DESENVOLVIMENTO DE SISTEMAS
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/html-css-praticando-html-css
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_5 imagem(ns) no slide._

### Slide 15

- Criando um botão
- 7 minutos
- Vamos começar a criar elementos para a página, o primeiro será um botão
- Link para tarefa: https://cursos.alura.com.br/course/html-css-praticando-html-css/task/103161
- Na última aula construímos a base do CSS, colocamos a estrutura básica do index e também inserimos as imagens da primeira seção. Então vamos continuar esse projeto incluindo botões.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 16

- O que vimos na aula de hoje:
- Entendemos os conceitos necessários para criação de um botão com HTML e CSS.

_2 imagem(ns) no slide._

### Slide 17

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 18

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 19

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

### Slide 20

_(sem texto)_

## Atividade

_Fonte: AULA 44_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 44

Questão 1

Qual tag HTML é comumente usada para criar botões genéricos em uma página da web?

a) <a>

b) <input>

c) <link>

d) <button>

Resposta correta: d) <button>

Comentário: A tag <button> é comumente usada para criar botões genéricos em páginas da web. Embora outras tags, como <a> e <input>, também possam ser usadas para criar botões, a tag <button> é a opção mais simples e direta para essa finalidade.

Questão 2

Como você pode tornar um botão mais acessível para usuários com deficiências visuais?

a) Aumentar o tamanho da fonte

b) Adicionar uma descrição de texto alternativo usando o atributo aria-label

c) Remover a cor de fundo do botão

d) Usar apenas texto no botão, sem ícones

Resposta correta: b) Adicionar uma descrição de texto alternativo usando o atributo aria-label

Comentário: Adicionar uma descrição de texto alternativo usando o atributo aria-label torna o botão mais acessível para usuários com deficiências visuais, pois permite que tecnologias assistivas, como leitores de tela, forneçam informações adicionais sobre a função do botão. As outras opções podem ajudar a melhorar a aparência do botão, mas não abordam diretamente a acessibilidade para usuários com deficiências visuais.

## Prática

_Fonte: AULA 44_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 44

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Criar botões utilizando HTML.
- Personalizar botões utilizando CSS.
- Aplicar estilos como:
- cores
- bordas
- espaçamentos
- tipografia
- Compreender a relação entre HTML e CSS na construção de interfaces.
- Desenvolver componentes visuais mais modernos e interativos.
Produto final esperado:

- Página HTML contendo botões personalizados e estilizados de forma organizada e funcional.

##### 2. Ferramentas Recomendadas

###### VS Code

- Para que serve: desenvolvimento da página HTML e estilização CSS.
- Por que é adequado: permite organização do projeto e visualização rápida do código.
- Como facilita o aprendizado: ajuda na separação entre estrutura e estilo.

###### Navegador Web

- Para que serve: visualizar os botões criados.
- Por que é adequado: permite testar aparência e interação.
- Como facilita o aprendizado: possibilita validar os estilos aplicados.

###### Editor Online HTML5

- Link: https://html5-editor.net/
- Para que serve: testes rápidos de HTML e CSS.
- Como facilita o aprendizado: fornece feedback visual imediato.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Projeto HTML das aulas anteriores
- Arquivo style.css funcionando
- Navegador atualizado
- VS Code instalado
- Estrutura inicial da página criada
- Conexão com internet
Material de apoio indicado na aula: https://cursos.alura.com.br/course/html-css-praticando-html-css

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações necessárias

- Garantir que todos tenham o projeto aberto.
- Revisar rapidamente:
- Estrutura HTML
- Classes CSS
- Vinculação do CSS externo

###### Condução da aula

###### Contextualização (5 minutos)

Apresentar cenário:

- Botões são elementos fundamentais em sites modernos.
Perguntar:

- O que torna um botão mais atrativo e fácil de usar?

###### Conceituando botões em HTML (10 minutos)

Explicar:

- Botões podem ser criados usando:
- <button>
- <a>
- <input>
Demonstrar:

- <button>Assinar Agora</button>
Explicar:

- diferença entre estrutura e aparência.

###### Trabalhando com CSS nos botões (15 minutos)

Demonstrar:

- Alterar:
- cor de fundo
- cor do texto
- bordas
- espaçamento
- arredondamento
Exemplo conceitual:

- .botao {
- background-color: blue;
- color: white;
- padding: 10px;
- }
Mostrar diferença visual antes e depois.

###### Prática guiada (15 minutos)

Alunos devem:

- Criar botões.
- Aplicar classes CSS.
- Personalizar aparência.
- Testar visual no navegador.

###### Revisão e fechamento (5 minutos)

- Conferir alinhamento.
- Verificar legibilidade.
- Ajustar visual dos botões.

###### Pontos de atenção

- Garantir contraste entre texto e fundo.
- Evitar botões muito pequenos.
- Manter consistência visual.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá:

- Criar botões para a página do projeto.
- Aplicar estilos personalizados utilizando CSS.
- Melhorar visualmente a interface.
Problema real simulado: Criação de botões para uma plataforma de streaming.

Habilidade desenvolvida: Criação de componentes visuais utilizando HTML e CSS.

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
- Localize a área principal da página.
- Crie um botão usando:
- <button> ou
- <a>
- Adicione um texto ao botão.
- Crie uma classe CSS para o botão.
- No style.css, aplique:
- cor de fundo
- cor do texto
- espaçamento interno
- borda
- arredondamento
- Ajuste tamanho da fonte.
- Centralize ou alinhe o botão.
- Salve os arquivos.
- Abra no navegador.
- Teste visual do botão.
- Ajuste detalhes finais.

##### 8. Exemplo ou Demonstração

###### Exemplo HTML

- <button class="botao-principal">
- Assinar Agora
- </button>

###### Exemplo CSS

- .botao-principal {
- background-color: #167BF7;
- color: white;
- padding: 12px 24px;
- border-radius: 8px;
- border: none;
- }

###### Conceitos reforçados

- HTML cria estrutura.
- CSS personaliza aparência.
- Botões melhoram interação do usuário.

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Botão funcional criado em HTML.
- CSS aplicado corretamente.
- Interface mais organizada visualmente.
- Código organizado e legível.
O professor verifica:

- Funcionamento do botão.
- Aplicação correta dos estilos.
- Qualidade visual da interface.

##### 10. Formato de Entrega da Atividade

- Formato: Pasta compactada contendo:
- index.html
- style.css
- imagens do projeto
- Entrega: ao final da aula.
- Prazo sugerido: imediato.

##### 11. Encerramento e Reflexão

Perguntas orientadoras:

- Qual a importância dos botões em um site?
- Como o CSS melhora a experiência visual?
- O que torna um botão mais acessível?
