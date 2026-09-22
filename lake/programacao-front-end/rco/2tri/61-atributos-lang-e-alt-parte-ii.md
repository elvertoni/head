---
titulo: "Atributos lang e alt – Parte II"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 61
serie: 2
aula_rco: "Aula 61"
slides: 23
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/61-atributos-lang-e-alt-parte-ii/61-atributos-lang-e-alt-parte-ii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/61-atributos-lang-e-alt-parte-ii/AULA 61_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/61-atributos-lang-e-alt-parte-ii/AULA 61_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Atributos lang e alt – Parte II

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Atributos lang e alt – Parte II
- Aula 61

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
- Entender como funcionam Atributos lang e alt Parte II.
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
- Iniciamos os estudos sobre a utilização do atributo “alt” em imagens em páginas HTML, sua importância e como isso melhora muito a navegação e ranqueamento de sua página com SEO.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- João é um desenvolvedor web iniciante que está construindo um site bilíngue em português e inglês. No entanto, ele percebeu que alguns usuários estão enfrentando dificuldades com os leitores de tela, que estão lendo o conteúdo em inglês com um sotaque português, causando confusão.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Ele perguntou: "Como posso garantir que o leitor de tela interprete corretamente o idioma de cada parte do conteúdo do site?"
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- A resposta para o questionamento de João é que ele pode usar o atributo "lang" para definir o idioma correto para cada parte do conteúdo. Para as seções em inglês, ele pode usar "lang='en'" e para as seções em português, ele pode usar "lang='pt'". Dessa forma, os leitores de tela poderão ler corretamente o conteúdo em cada idioma, melhorando a acessibilidade e a experiência do usuário em seu site.

_2 imagem(ns) no slide._

### Slide 10

- Conceituando
- O atributo "lang" em HTML é um recurso muito importante para a acessibilidade e SEO (Search Engine Optimization) de uma página da web. Ele é usado para indicar a língua principal do conteúdo da página.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- Quando incluímos o atributo "lang" na tag de abertura do documento HTML, estamos informando ao navegador e aos leitores de tela a língua principal do conteúdo da página. Isso é muito útil para usuários com deficiência visual, pois o leitor de tela saberá que língua deve usar para ler o conteúdo.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Além disso, o atributo "lang" também é importante para os motores de busca, como o Google, pois permite que eles entendam melhor o conteúdo do site, melhorando assim a visibilidade do site nas pesquisas. Quando os motores de busca entendem a língua do conteúdo, eles podem indexar a página de forma mais eficiente e exibir o site para usuários que buscam conteúdo naquela língua específica.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Finalmente, o atributo "lang" também pode influenciar a forma como o navegador exibe o texto, já que diferentes línguas têm regras de tipografia diferentes. Por exemplo, em japonês, não há espaço entre as palavras, enquanto em inglês, há.

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Em resumo, o atributo "lang" é uma ferramenta poderosa para melhorar a acessibilidade, o SEO e a experiência do usuário de uma página da web. É uma prática recomendada incluí-lo e garantir que seu valor esteja correto para o conteúdo da página.

_1 imagem(ns) no slide._

### Slide 15

- Ainda sobre HTML e leitores de tela, vamos conhecer praticando?
- Na plataforma Alura, vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/acessibilidade-web-front-end
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 16

- Alt e titles
- 9 minutos
- Daremos prosseguimento na análise da experiência do usuário em um primeiro contato com a página.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36238
- Percebam que pela navegação sem mouse, não conseguimos acessar o logo da Apeperia. Por isso, habilitaremos o mouse em "Preferências> Opções de mouse>" e selecionaremos a opção "Habilitar rastreamento mouse".
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Melhorando o alt
- 7 minutos
- Seguiremos trabalhando na tag <alt> da imagem de dois homens escrevendo em um quadro branco, localizada no site da Apeperia.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36239
- Podemos melhorar a descrição de alt da imagem, tornando-a mais precisa e inteligente de acordo com os objetivos da Apeperia.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Resumo e curiosidades
- 10 minutos
- De maneira resumida, aprendemos até este ponto dois atributos cruciais para o desenvolvimento de uma página acessível.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36240
- Lang e alt, o primeiro faz uma grande diferença no funcionamento do leitor de tela, pois dita o idioma da narração. Se temos um pequeno texto em inglês ou qualquer outro idioma, devemos inserir um idioma específico para este elemento.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 19

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 20

- O que vimos na aula de hoje:
- Aprendemos como utilizar o atributo “lang” em páginas HTML afim de facilitar a leitura de objetos visuais em leitores de tela.

_1 imagem(ns) no slide._

### Slide 21

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 22

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

### Slide 23

_(sem texto)_

## Atividade

_Fonte: AULA 61_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 61

Questão 1

O que o atributo 'lang' faz em uma página HTML?

a) Determina o layout da página

b) Altera a fonte do texto

c) Informa o idioma do conteúdo do elemento ao navegador e aos leitores de tela

d) Muda o idioma do navegador do usuário

Resposta Correta: c) O atributo 'lang' informa o idioma do conteúdo do elemento ao navegador e aos leitores de tela. Ele não altera a aparência da página, a fonte do texto ou o idioma do navegador do usuário.

Questão 2

Como você usaria o atributo 'lang' para informar que o conteúdo de um parágrafo está em inglês?

a) <p lang='eng'>This is a paragraph.</p>

b) <p lang='en'>This is a paragraph.</p>

c) <p language='en'>This is a paragraph.</p>

d) <p> <lang='en'> This is a paragraph. </lang> </p>

Resposta Correta: b) A opção correta é <p lang='en'>This is a paragraph.</p>. O valor 'en' indica que o idioma é inglês. Note que o atributo 'lang' é aplicado diretamente no elemento 'p', e não é um elemento separado.

## Prática

_Fonte: AULA 61_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 61

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Aplicar corretamente o atributo lang em páginas HTML.
- Utilizar o atributo lang em trechos específicos de conteúdo multilíngue.
- Melhorar descrições de imagens utilizando o atributo alt.
- Avaliar como leitores de tela interpretam páginas web.
- Compreender a relação entre acessibilidade e SEO.
- Tornar uma página mais inclusiva para diferentes perfis de usuários.

###### Produto Final Esperado

O estudante deverá entregar uma página HTML acessível contendo:

- Definição correta do idioma principal da página.
- Trechos em idiomas diferentes utilizando lang.
- Imagens com descrições alternativas adequadas.
- Melhorias de acessibilidade voltadas para leitores de tela.

##### 2. Ferramentas Recomendadas

###### Visual Studio Code (VS Code)

Para que serve: edição dos arquivos HTML.

Por que é adequado: permite modificar rapidamente atributos e estruturas da página.

Como facilita o aprendizado: possibilita visualizar imediatamente as melhorias realizadas.

Site: https://code.visualstudio.com

###### NVDA (NonVisual Desktop Access)

Para que serve: leitor de tela gratuito.

Por que é adequado: permite testar a acessibilidade da página.

Como facilita o aprendizado: demonstra como usuários com deficiência visual interagem com o conteúdo.

Site: https://www.nvaccess.org

###### Navegador Web

Para que serve: visualização e testes da página.

Por que é adequado: permite validar as alterações realizadas.

Como facilita o aprendizado: mostra o comportamento real da interface.

###### WAVE Accessibility Tool

Para que serve: avaliação automática de acessibilidade.

Por que é adequado: identifica erros relacionados a acessibilidade.

Como facilita o aprendizado: fornece feedback imediato sobre melhorias necessárias.

Site: https://wave.webaim.org

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve possuir:

VS Code instalado

Navegador atualizado

Projeto HTML da aula anterior

Conexão com internet

Leitor de tela NVDA instalado (opcional)

Conhecimentos básicos de HTML

Arquivos do projeto Apeperia (ou projeto fornecido pelo professor)

###### Materiais de Apoio

Curso Alura:

https://cursos.alura.com.br/course/acessibilidade-web-front-end

Artigo complementar:

http://www.reinaldoferraz.com.br/acessibilidade-seo-e-svg/

Projeto base:

https://github.com/designernatan/curso-acessibilidade-web-front-end-1/archive/9d23967baf7e252a52874a54fe7414e7cf58fd14.zip

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações Necessárias

- Disponibilizar o projeto da aula anterior.
- Garantir acesso ao VS Code.
- Demonstrar rapidamente o funcionamento do NVDA.
- Preparar exemplos de páginas multilíngues.

###### Contextualização (5 minutos)

Apresente o cenário:

João criou um site em português e inglês, mas percebeu que o leitor de tela estava pronunciando palavras em inglês como se fossem português.

Pergunta para a turma:

Como o leitor de tela sabe qual idioma deve utilizar ao ler uma página?

###### Revisão do Atributo Alt (10 minutos)

Revisar:

- O que é o atributo alt.
- Importância para leitores de tela.
- Relação com SEO.
Mostrar exemplos de descrições:

"imagem"

"foto"

"Equipe de desenvolvimento reunida planejando um novo aplicativo"

###### Conceituando o Atributo Lang (10 minutos)

Explicar:

- Definição do idioma principal da página.
- Uso em trechos específicos.
- Impacto nos leitores de tela.
- Benefícios para mecanismos de busca.
Apresentar exemplos de páginas multilíngues.

###### Demonstração Prática (10 minutos)

Demonstrar:

- Aplicação do atributo lang no HTML.
- Aplicação de lang em trechos de texto.
- Melhoria das descrições alt.
Mostrar o comportamento no leitor de tela.

###### Prática Guiada (10 minutos)

Orientar os alunos a:

- revisar imagens;
- melhorar atributos alt;
- aplicar lang corretamente;
- testar a acessibilidade.

###### Encerramento (5 minutos)

Compartilhar os resultados e discutir as melhorias realizadas.

###### Pontos de Atenção

- Evitar descrições genéricas no atributo alt.
- Não utilizar descrições excessivamente longas.
- Verificar se o idioma configurado corresponde ao conteúdo.
- Utilizar lang em trechos estrangeiros quando necessário.

##### 5. Atividade Prática — Descrição Geral

O estudante atuará como desenvolvedor responsável por revisar a acessibilidade de um site institucional multilíngue.

Sua missão será:

- Corrigir descrições de imagens.
- Definir corretamente os idiomas do conteúdo.
- Melhorar a experiência de usuários de leitores de tela.

###### Problema Real Simulado

Uma empresa internacional identificou dificuldades de navegação em seu site por usuários que utilizam tecnologias assistivas.

###### Habilidade Desenvolvida

Implementação de recursos de acessibilidade utilizando atributos HTML voltados para leitores de tela e SEO.

##### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Problemas (PBL)

Os estudantes resolvem problemas reais de acessibilidade.

###### Aprendizagem por Experimentação

Testam páginas utilizando leitores de tela.

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
- Identifique:
- imagens;
- títulos;
- textos em outros idiomas.
- Registre possíveis melhorias.

###### Etapa 2 – Melhorar os Atributos Alt

- Localize todas as imagens da página.
- Analise as descrições existentes.
- Reescreva descrições genéricas tornando-as mais informativas.

###### Etapa 3 – Configurar o Idioma Principal

- Verifique a tag principal do documento.
- Defina corretamente o idioma principal da página.

###### Etapa 4 – Configurar Idiomas Específicos

- Identifique palavras ou trechos em outro idioma.
- Configure o idioma específico desses conteúdos.
Exemplos:

- Inglês
- Espanhol
- Francês

###### Etapa 5 – Teste de Acessibilidade

- Utilize o navegador.
- Teste a página utilizando o teclado.
- Quando disponível, utilize o NVDA.
- Observe a leitura dos conteúdos multilíngues.

###### Etapa 6 – Evidências

- Capture prints:
- antes das correções;
- depois das correções;
- da estrutura final.

##### 8. Exemplo ou Demonstração

###### Exemplo de Idioma Principal

- <html lang="pt-BR">

###### Exemplo de Trecho em Inglês

- <p lang="en">Welcome to our website</p>

###### Exemplo de Alt Pouco Informativo

- <img src="equipe.jpg" alt="foto">

###### Exemplo Melhorado

- <img src="equipe.jpg" alt="Equipe de desenvolvedores reunida em uma sala de planejamento">

###### Fluxo da Atividade

- Análise
- ↓
- Correção de Alt
- ↓
- Configuração de Lang
- ↓
- Teste
- ↓
- Validação

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Página HTML revisada.
- Uso correto do atributo lang.
- Uso adequado do atributo alt.
- Melhor experiência para leitores de tela.
- Estrutura mais amigável para SEO.

###### Critérios de Verificação

O professor deverá verificar:

Configuração correta do idioma principal

Uso adequado de lang em conteúdos multilíngues

Descrições alt relevantes

Melhorias na acessibilidade

Participação na atividade

##### 10. Formato de Entrega da Atividade

###### O que deve ser enviado

- Arquivo HTML corrigido.
- Prints das melhorias realizadas.
- Relatório simples contendo:
- problemas encontrados;
- melhorias aplicadas;
- aprendizados obtidos.

###### Nomeação Sugerida

- Aula61_NomeSobrenome
Exemplo:

- Aula61_JoaoSilva

###### Onde Entregar

- Google Classroom
- Google Drive
- AVA da instituição

###### Prazo Sugerido

Ao final da aula.

##### 11. Encerramento e Reflexão

Promova uma discussão com a turma:

###### Perguntas para reflexão

- Como o atributo lang melhora a experiência de usuários de leitores de tela?
- Por que o atributo alt é importante para acessibilidade e SEO?
- Quais problemas podem ocorrer quando o idioma não é definido corretamente?
- Como pequenas alterações no HTML podem tornar a web mais inclusiva?
