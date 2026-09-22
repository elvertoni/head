---
titulo: "HTML e Leitores de Tela – Parte II"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 59
serie: 2
aula_rco: "Aula 59"
slides: 23
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/59-html-e-leitores-de-tela-parte-ii/59-html-e-leitores-de-tela-parte-ii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/59-html-e-leitores-de-tela-parte-ii/AULA 59_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/59-html-e-leitores-de-tela-parte-ii/AULA 59_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# HTML e Leitores de Tela – Parte II

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- HTML e Leitores de Tela – Parte II
- Aula 59

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
- Entender como funcionam os interpretadores de tela em páginas HTML Parte II.
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
- Iniciamos os estudos sobre utilização de leitores de tela para páginas HTML.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Letícia é uma desenvolvedora web iniciante e recebeu a tarefa de melhorar a acessibilidade de um site para usuários de leitores de tela. Ao analisar o site, percebeu que, embora todas as imagens tivessem uma descrição textual alternativa, os links não eram facilmente identificáveis pelos leitores de tela.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Por exemplo, havia muitos links com o texto "Clique aqui", o que é confuso fora de contexto. Letícia percebeu que os usuários de leitores de tela teriam dificuldade em entender o propósito desses links apenas pelo texto do link.

_1 imagem(ns) no slide._

### Slide 9

- Para pensarmos juntos...
- A questão que Letícia se perguntou foi: "Como posso tornar esses links mais acessíveis para usuários de leitores de tela?"
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 10

- Resposta
- A resposta a essa questão é melhorar o texto dos links para torná-los descritivos e significativos por si só, sem a necessidade de contexto visual adicional. Por exemplo, em vez de "Clique aqui para ler mais sobre acessibilidade na web", ela poderia simplesmente usar "Leia mais sobre acessibilidade na web". Isso permite que os usuários de leitores de tela entendam o propósito do link apenas pelo seu texto, independentemente de onde o link esteja na página.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- Os leitores de tela são programas ou softwares que leem o conteúdo de uma página da web em voz alta. Eles são uma ferramenta crucial para tornar a web acessível a pessoas com deficiência visual ou outras dificuldades que dificultam a leitura do texto na tela.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- No que diz respeito à aplicação HTML, os leitores de tela interpretam a estrutura semântica do HTML - ou seja, como as tags são usadas para indicar o tipo de conteúdo (como títulos, links, listas, etc.). Por exemplo, os leitores de tela podem anunciar quando o usuário está navegando através de um cabeçalho ou um link. Para aproveitar ao máximo essa funcionalidade, os desenvolvedores devem usar as tags HTML de forma adequada e consistente.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Outro aspecto importante da aplicação HTML é fornecer texto alternativo para imagens, também conhecido como "alt text". Este é um texto curto que descreve a imagem e é lido pelo leitor de tela. Isso permite que usuários que não podem ver a imagem entendam o que ela representa.

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Além disso, é recomendável estruturar a página HTML de uma forma que faça sentido sem a necessidade de ver o layout visual. Isso significa que as informações devem ser apresentadas em uma ordem lógica, independentemente de como são organizadas visualmente na página.

_1 imagem(ns) no slide._

### Slide 15

- Conceituando
- Finalmente, lembre-se de que nem todos os usuários navegam clicando com o mouse. Muitos usuários de leitores de tela navegam pelo teclado, por isso é importante garantir que todos os elementos interativos da página (como links e formulários) possam ser acessados e usados apenas com o teclado.

_1 imagem(ns) no slide._

### Slide 16

- Ainda sobre HTML e leitores de tela, vamos conhecer praticando?
- Na plataforma Alura, vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/acessibilidade-web-front-end
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 17

- Apresentando a Apeperia
- 9 minutos
- É importante destacar que se o seu Windows 10 estiver em inglês, provavelmente, as vozes disponíveis de narrador virão apenas em inglês.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36232
- Mas podemos instalar as vozes no idioma português.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Vários H1s na mesma página
- 12 minutos
- Vamos começar a realizar modificações produtivas em nosso projeto.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36233
- Veremos alguns atalhos interessantes do NVDA. Se pressionamos a tecla "K", iremos navegar entre todos os links disponíveis na página.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 19

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 20

- O que vimos na aula de hoje:
- Conhecemos formas de utilizar inclusão de pessoas com algum tipo de deficiência na utilização de tecnologias e desenvolvimento de produtos para essas pessoas.

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

_Fonte: AULA 59_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 59

Questão 1

Como você pode tornar os links mais acessíveis para usuários de leitores de tela?

A) Fazendo todos os links com o texto "Clique aqui"

B) Tornando o texto dos links descritivos e significativos por si só

C) Colocando todos os links em negrito

D) Utilizando muitas cores diferentes para os links

Comentário: A resposta correta é B. Os usuários de leitores de tela se beneficiam de links que têm texto descritivo e significativo por si só, sem a necessidade de contexto visual adicional.

Questão 2

O que torna uma imagem mais acessível para usuários de leitores de tela em uma página HTML?

A) Fazendo a imagem o mais colorida possível

B) Adicionando uma descrição textual alternativa à imagem

C) Tornando a imagem o mais grande possível

D) Adicionando tantos detalhes quanto possível na imagem

Comentário: A resposta correta é B. Uma descrição textual alternativa (conhecida como texto alternativo ou alt text) ajuda os usuários de leitores de tela a entender o conteúdo e o propósito da imagem.

## Prática

_Fonte: AULA 59_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 59

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Identificar problemas de acessibilidade relacionados a links e navegação.
- Criar textos de links mais descritivos e acessíveis.
- Organizar corretamente a hierarquia de títulos em uma página HTML.
- Compreender como leitores de tela interpretam elementos HTML.
- Avaliar a navegação de uma página utilizando apenas o teclado.
- Aplicar melhorias de acessibilidade em páginas web.

###### Produto Final Esperado

O estudante deverá entregar uma página HTML revisada contendo:

- Links com textos significativos.
- Estrutura correta de títulos (H1, H2, H3).
- Navegação acessível por teclado.
- Melhor experiência para usuários de leitores de tela.

##### 2. Ferramentas Recomendadas

###### Visual Studio Code (VS Code)

Para que serve: edição dos arquivos HTML.

Por que é adequado: permite realizar ajustes rápidos na estrutura da página.

Como facilita o aprendizado: possibilita testar imediatamente as melhorias implementadas.

Site: https://code.visualstudio.com

###### NVDA (NonVisual Desktop Access)

Para que serve: leitor de tela gratuito.

Por que é adequado: permite testar acessibilidade na prática.

Como facilita o aprendizado: demonstra como usuários com deficiência visual navegam pela web.

Site: https://www.nvaccess.org

###### Navegador Web

Para que serve: visualizar e testar a página.

Por que é adequado: permite validar a navegação e os elementos acessíveis.

Como facilita o aprendizado: possibilita testar links, foco e estrutura da página.

###### WAVE Accessibility Tool

Para que serve: avaliação automática de acessibilidade.

Por que é adequado: identifica erros comuns em páginas HTML.

Como facilita o aprendizado: fornece feedback rápido sobre melhorias necessárias.

Site: https://wave.webaim.org

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve possuir:

VS Code instalado

Navegador atualizado

Página HTML para análise

Conexão com internet

NVDA instalado (quando disponível)

Conhecimentos básicos de HTML

Projeto utilizado na aula anterior

###### Materiais de Apoio

Curso Alura:

https://cursos.alura.com.br/course/acessibilidade-web-front-end

NVDA:

https://www.nvaccess.org

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações Necessárias

- Disponibilizar uma página HTML com problemas de acessibilidade.
- Garantir acesso ao NVDA ou demonstração do leitor de tela.
- Testar previamente a navegação por teclado.

###### Contextualização (5 minutos)

Apresente o cenário da aula:

Letícia identificou que diversos links utilizavam textos genéricos como "Clique aqui", dificultando a compreensão para usuários de leitores de tela.

Pergunta para a turma:

Um link continua sendo útil quando é lido isoladamente por um leitor de tela?

###### Conceituando Links Acessíveis (10 minutos)

Explique:

- Como leitores de tela anunciam links.
- Problemas causados por textos genéricos.
- Importância de textos descritivos.
Exemplos:

Clique aqui

Saiba mais

Leia mais sobre acessibilidade web

Conheça nossos cursos de programação

###### Estrutura Semântica e Hierarquia (10 minutos)

Revisar:

- H1
- H2
- H3
- listas
- links
Explicar como leitores de tela utilizam essas informações para navegação.

###### Demonstração Prática (10 minutos)

Demonstrar:

- Página com problemas.
- Correção dos links.
- Organização dos títulos.
- Teste utilizando teclado.

###### Prática Guiada (10 minutos)

Orientar os alunos a:

- revisar uma página;
- corrigir links;
- ajustar títulos;
- testar acessibilidade.

###### Encerramento (5 minutos)

Compartilhar resultados e discutir melhorias realizadas.

###### Pontos de Atenção

- Evitar textos vagos em links.
- Não utilizar vários H1 sem necessidade.
- Garantir ordem lógica de navegação.
- Verificar se todos os links possuem significado próprio.

##### 5. Atividade Prática — Descrição Geral

O estudante atuará como desenvolvedor responsável por revisar a acessibilidade de um portal institucional.

Sua missão será corrigir problemas relacionados à navegação por leitores de tela.

###### Problema Real Simulado

Uma organização recebeu reclamações de usuários com deficiência visual devido à dificuldade de navegação em seu site.

###### Habilidade Desenvolvida

Aplicação de boas práticas de acessibilidade em links, títulos e navegação HTML.

##### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Problemas (PBL)

Os estudantes resolvem problemas reais de acessibilidade.

###### Aprendizagem por Experimentação

Testam a navegação utilizando leitores de tela e teclado.

###### Ensino por Descoberta

Identificam falhas e propõem soluções.

###### Elementos de Lemov

- Modelagem
- Prática Guiada
- Verificação de Compreensão
- Feedback Imediato
- Revisão

##### 7. Passo a Passo da Atividade Prática (para os alunos)

###### Etapa 1 – Análise da Página

- Abra o projeto fornecido pelo professor.
- Identifique:
- links;
- títulos;
- menus;
- elementos interativos.
- Registre possíveis problemas encontrados.

###### Etapa 2 – Revisão dos Links

- Localize todos os links da página.
- Verifique se o texto explica claramente o destino do link.
- Substitua textos genéricos por descrições mais claras.

###### Etapa 3 – Revisão da Estrutura

- Analise os títulos.
- Verifique a existência de múltiplos H1.
- Organize a hierarquia corretamente.

###### Etapa 4 – Navegação por Teclado

- Utilize a tecla TAB para navegar.
- Verifique se todos os elementos podem receber foco.
- Observe a ordem da navegação.

###### Etapa 5 – Teste de Acessibilidade

- Utilize o NVDA (ou observação guiada pelo professor).
- Teste a leitura:
- dos links;
- dos títulos;
- das imagens.

###### Etapa 6 – Evidências

- Capture prints:
- antes das correções;
- depois das correções;
- da estrutura final da página.

##### 8. Exemplo ou Demonstração

###### Exemplo de Link Pouco Acessível

- <a href="curso.html">Clique aqui</a>

###### Exemplo Corrigido

- <a href="curso.html">Conheça nosso curso de acessibilidade web</a>

###### Estrutura Incorreta

- H1
- H1
- H1
- H2

###### Estrutura Recomendada

- H1
- ├─ H2
- │ ├─ H3
- │ └─ H3
- └─ H2

###### Fluxo da Atividade

- Análise
- ↓
- Correção
- ↓
- Teste
- ↓
- Validação
- ↓
- Página Acessível

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Página revisada.
- Links descritivos.
- Hierarquia correta de títulos.
- Navegação acessível por teclado.
- Melhor experiência para leitores de tela.

###### Critérios de Verificação

O professor deverá verificar:

Links com textos significativos

Estrutura correta de títulos

Navegação por teclado funcional

Organização semântica adequada

Participação na atividade

##### 10. Formato de Entrega da Atividade

###### O que deve ser enviado

- Arquivo HTML corrigido.
- Capturas de tela das melhorias realizadas.
- Relatório simples contendo:
- problemas identificados;
- melhorias implementadas;
- aprendizados obtidos.

###### Nomeação Sugerida

- Aula59_NomeSobrenome
Exemplo:

- Aula59_AnaSouza

###### Onde Entregar

- Google Classroom
- Google Drive
- AVA da instituição

###### Prazo Sugerido

Ao final da aula.

##### 11. Encerramento e Reflexão

Promova uma discussão com a turma:

###### Perguntas para reflexão

- Por que "Clique aqui" não é um bom texto para links?
- Como os leitores de tela interpretam os links de uma página?
- Qual a importância da navegação por teclado?
- Como a acessibilidade contribui para uma internet mais inclusiva?
