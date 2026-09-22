---
titulo: "Introdução a Roles e ARIA - Parte I"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 64
serie: 2
aula_rco: "Aula 64"
slides: 21
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/64-introducao-a-roles-e-aria-parte-i/64-introducao-a-roles-e-aria-parte-i.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/64-introducao-a-roles-e-aria-parte-i/AULA 64_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/64-introducao-a-roles-e-aria-parte-i/AULA 64_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Introdução a Roles e ARIA - Parte I

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Introdução a Roles e ARIA - Parte I
- Aula 64

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
- Compreender sobre navegação em páginas HTML por teclado e o impacto nos leitores de tela Parte I.
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
- https://github.com/designernatan/curso-acessibilidade-web-front-end-1/archive/0115ab16629f4f264184beb291ece993b7246f8c.zip

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Concluímos os estudos sobre a parte inicial sobre a interferência do CSS em páginas HTML e os impactos que ele oferecem na utilização de recursos para portadores de deficiência visual.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Pedro está começando sua jornada como desenvolvedor web e se depara com seu primeiro projeto. Pedro precisa criar uma página web acessível para todos os usuários. Ele recebe feedback de um usuário que usa exclusivamente o teclado para navegar na página e tem um leitor de tela. O usuário expressa dificuldade em encontrar e interagir com alguns elementos.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Como Pedro pode garantir que todos os elementos interativos de sua página web sejam acessíveis através da navegação por teclado e sejam identificáveis para um leitor de tela?
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Pedro deve garantir que todos os elementos interativos da página, como links, botões e campos de formulário, possam receber foco através da tecla Tab. Ele também precisa garantir que a ordem da tabulação siga uma sequência lógica que corresponda à ordem visual dos elementos.

_1 imagem(ns) no slide._

### Slide 10

- Resposta
- Além disso, Pedro deve usar devidamente os atributos ARIA para comunicar o propósito e o estado dos elementos interativos para os leitores de tela. Por fim, Pedro deve garantir que todos os elementos interativos tenham um foco visível claro, para ajudar aqueles que dependem tanto da navegação por teclado quanto de alguma visão.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- A navegação pelo teclado é um aspecto crucial da acessibilidade na web. Ela permite que usuários que não conseguem ou optam por não usar um mouse possam interagir com páginas da web. Isso é especialmente importante para pessoas que utilizam leitores de tela, tecnologias assistivas que transformam conteúdo textual e visual em fala ou Braille.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- A navegação pelo teclado ocorre principalmente através da tecla Tab. Normalmente, ao pressionar a tecla Tab, o foco se move para o próximo elemento interativo da página, como links, botões ou campos de formulário. Pressionando Shift + Tab, o foco volta para o elemento interativo anterior. Elementos como cabeçalhos, parágrafos e imagens geralmente não recebem foco através da navegação por tabulação, a menos que sejam explicitamente tornados focáveis.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- No entanto, a experiência da navegação por teclado pode ser muito diferente dependendo de como a página da web foi construída. Por exemplo, se a ordem do código HTML não seguir uma sequência lógica, a navegação por teclado pode ser confusa, pois o foco pode pular de um lado para o outro na página. Além disso, se elementos interativos não forem devidamente marcados ou se estiverem escondidos visualmente mas ainda assim acessíveis via teclado, os usuários de leitores de tela podem ser levados a interagir com elementos que não conseguem perceber.
- https://cnttl.org.br/imagens/noticias/inclusao.jpg

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Portanto, é crucial para a acessibilidade da web garantir que a navegação por teclado seja intuitiva e previsível, e que os elementos interativos estejam devidamente identificados e sejam perceptíveis. Isso inclui o uso adequado de atributos ARIA, que ajudam a comunicar o propósito e o estado dos elementos interativos para leitores de tela, bem como garantir que todos os elementos interativos tenham um foco visível claro, para ajudar aqueles que dependem tanto da navegação por teclado quanto de alguma visão.
- https://classic.exame.com/wp-content/uploads/2022/11/pessoa-deficiencia-acessibilidade.jpg?quality=70&strip=info&w=1024

_1 imagem(ns) no slide._

### Slide 15

- Ainda sobre HTML e leitores de tela, vamos conhecer praticando?
- Na plataforma Alura, vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/acessibilidade-web-front-end
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 16

- Pular navegação
- 10 minutos
- Uma pessoa que utiliza o teclado para navegar em um site pode fazer uso de um leitor de tela.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36245
- Este possui alguns atalhos interessantes, assim como a tecla "Tab", que permite trafegar por todos os elementos focáveis da página.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 18

- O que vimos na aula de hoje:
- Aprendemos como a navegação por teclado se faz importante para a inclusão de acessibilidade a navegação em páginas HTML.

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

_Fonte: AULA 64_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 64

Questão 1

Qual das seguintes afirmações é verdadeira sobre a navegação por teclado em páginas HTML?

A. A tecla Tab pode ser usada para navegar entre elementos interativos.

B. A navegação por teclado é incompatível com leitores de tela.

C. A ordem da tabulação não importa para a acessibilidade.

D. Elementos interativos não precisam de foco visível.

Resposta correta: A. A tecla Tab pode ser usada para navegar entre elementos interativos. A navegação por teclado e a ordem da tabulação são fundamentais para a acessibilidade, e os elementos interativos devem ter um foco visível para usuários de teclado.

Questão 2

Como os desenvolvedores podem garantir que os elementos interativos são identificáveis pelos leitores de tela durante a navegação por teclado?

A. Incluindo imagens em cada elemento interativo.

B. Utilizando os atributos ARIA apropriados.

C. Garantindo que todos os elementos interativos sejam clicáveis.

D. Utilizando apenas elementos div para criar interatividade.

Resposta correta: B. Utilizando os atributos ARIA apropriados. Os atributos ARIA permitem que os desenvolvedores comuniquem o propósito e o estado dos elementos interativos para os leitores de tela.

## Prática

_Fonte: AULA 64_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 64

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender a importância da navegação por teclado em páginas web.
- Identificar elementos focáveis em uma interface HTML.
- Avaliar a ordem de navegação utilizando a tecla TAB.
- Reconhecer problemas de acessibilidade relacionados ao foco.
- Aplicar melhorias básicas em páginas HTML para facilitar a navegação por teclado.
- Entender o papel dos atributos ARIA na comunicação com leitores de tela.

###### Produto Final Esperado

O estudante deverá revisar uma página web e garantir que:

- Todos os elementos interativos possam receber foco.
- A navegação por TAB siga uma ordem lógica.
- Os elementos possuam identificação adequada para tecnologias assistivas.
- O foco visual esteja claramente visível.

##### 2. Ferramentas Recomendadas

###### Visual Studio Code (VS Code)

Para que serve: edição dos arquivos HTML e CSS.

Por que é adequado: permite modificar rapidamente a estrutura da página.

Como facilita o aprendizado: possibilita testar imediatamente as melhorias realizadas.

Site: https://code.visualstudio.com

###### Navegador Web

Para que serve: testar navegação por teclado.

Por que é adequado: permite verificar o comportamento real da interface.

Como facilita o aprendizado: ajuda a identificar problemas de foco e navegação.

###### NVDA (NonVisual Desktop Access)

Para que serve: leitor de tela gratuito.

Por que é adequado: permite compreender como usuários com deficiência visual navegam.

Como facilita o aprendizado: demonstra a importância da correta identificação dos elementos.

Site: https://www.nvaccess.org

###### WAVE Accessibility Tool

Para que serve: avaliação de acessibilidade.

Por que é adequado: auxilia na identificação de problemas comuns.

Como facilita o aprendizado: fornece feedback visual rápido.

Site: https://wave.webaim.org

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve possuir:

VS Code instalado

Navegador atualizado

Projeto da aula anterior

Conexão com internet

Conhecimentos básicos de HTML e CSS

Projeto Apeperia ou projeto disponibilizado pelo professor

Leitor de tela NVDA (opcional)

###### Materiais de Apoio

Curso Alura:

https://cursos.alura.com.br/course/acessibilidade-web-front-end

Projeto Base:

https://github.com/designernatan/curso-acessibilidade-web-front-end-1/archive/0115ab16629f4f264184beb291ece993b7246f8c.zip

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações Necessárias

- Disponibilizar o projeto utilizado na aula.
- Garantir acesso ao VS Code.
- Demonstrar a navegação utilizando TAB.
- Preparar exemplos de páginas com problemas de foco.

###### Contextualização (5 minutos)

Apresente o cenário:

Pedro desenvolveu uma página visualmente bonita, mas usuários que navegam apenas pelo teclado encontram dificuldades para acessar algumas funcionalidades.

Pergunta para a turma:

Uma página pode ser considerada acessível se não puder ser utilizada sem mouse?

###### Conceituando Navegação por Teclado (10 minutos)

Explique:

- O que é foco.
- Como funciona a tecla TAB.
- Como funciona Shift + TAB.
- Elementos focáveis.
- Importância da ordem lógica de navegação.

###### Conceituando ARIA e Roles (10 minutos)

Apresente os conceitos iniciais:

- O que é ARIA.
- O que são Roles.
- Como ajudam leitores de tela.
- Quando utilizar.
Explique que ARIA complementa o HTML semântico.

###### Demonstração Prática (10 minutos)

Demonstrar:

- Navegação por teclado.
- Identificação dos elementos focáveis.
- Problemas de ordem de foco.
- Destaque visual do foco.

###### Prática Guiada (10 minutos)

Orientar os alunos a:

- navegar utilizando TAB;
- identificar falhas;
- corrigir elementos;
- validar a navegação.

###### Encerramento (5 minutos)

Promover compartilhamento dos problemas encontrados e soluções aplicadas.

###### Pontos de Atenção

- Todos os elementos interativos devem ser acessíveis via teclado.
- O foco deve ser visível.
- A ordem da navegação deve ser lógica.
- Evitar criar componentes inacessíveis apenas com CSS.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá revisar uma página HTML simulando a experiência de um usuário que utiliza exclusivamente o teclado para navegação.

A atividade consiste em:

- Testar a navegação por TAB.
- Identificar problemas de foco.
- Corrigir a ordem de navegação.
- Melhorar a acessibilidade dos elementos interativos.

###### Problema Real Simulado

Uma organização recebeu reclamações de usuários que não conseguem utilizar o mouse e dependem da navegação por teclado.

###### Habilidade Desenvolvida

Avaliação e melhoria da acessibilidade relacionada à navegação por teclado.

##### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Problemas (PBL)

Os estudantes resolvem problemas reais de acessibilidade.

###### Aprendizagem por Experimentação

Testam interfaces utilizando apenas o teclado.

###### Ensino por Descoberta

Identificam falhas e propõem melhorias.

###### Elementos de Lemov

- Modelagem
- Prática Guiada
- Verificação de Compreensão
- Feedback Imediato
- Revisão

##### 7. Passo a Passo da Atividade Prática (para os alunos)

###### Etapa 1 – Abrir o Projeto

- Abra o projeto disponibilizado pelo professor.
- Execute a página no navegador.

###### Etapa 2 – Testar Navegação

- Utilize apenas a tecla TAB.
- Percorra toda a página.
- Observe:
- links;
- botões;
- formulários;
- menus.

###### Etapa 3 – Identificar Problemas

- Registre elementos que:
- não recebem foco;
- recebem foco em ordem inadequada;
- possuem foco pouco visível.

###### Etapa 4 – Corrigir a Interface

- Ajuste os elementos necessários.
- Organize a estrutura da página.
- Garanta uma sequência lógica de navegação.

###### Etapa 5 – Validar

- Execute novamente a navegação utilizando TAB.
- Verifique se todos os elementos são acessíveis.
- Teste com leitor de tela quando disponível.

###### Etapa 6 – Documentação

- Crie um relatório contendo:
- problemas encontrados;
- melhorias realizadas;
- resultados obtidos.

##### 8. Exemplo ou Demonstração

###### Fluxo de Navegação Correto

- Logo
- ↓
- Menu Principal
- ↓
- Botão Principal
- ↓
- Formulário
- ↓
- Rodapé

###### Exemplo de Elementos Focáveis

| Elemento | Recebe Foco |
| --- | --- |
| Link | Sim |
| Botão | Sim |
| Campo de Texto | Sim |
| Parágrafo | Não |
| Imagem | Não |

###### Fluxo da Atividade

- Abrir Página
- ↓
- Navegar com TAB
- ↓
- Identificar Problemas
- ↓
- Corrigir
- ↓
- Validar

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Página revisada.
- Navegação funcional por teclado.
- Ordem lógica de foco.
- Melhor experiência para usuários de tecnologias assistivas.

###### Critérios de Verificação

O professor deverá verificar:

Todos os elementos interativos acessíveis por TAB

Ordem lógica de navegação

Foco visual perceptível

Correções realizadas adequadamente

Participação na atividade

##### 10. Formato de Entrega da Atividade

###### O que deve ser enviado

- Arquivo HTML atualizado.
- Arquivo CSS atualizado.
- Prints da navegação.
- Relatório simples contendo:
- problemas identificados;
- melhorias realizadas;
- conclusões obtidas.

###### Nomeação Sugerida

- Aula64_NomeSobrenome
Exemplo:

- Aula64_AnaSilva

###### Onde Entregar

- Google Classroom
- Google Drive
- AVA da instituição

###### Prazo Sugerido

Ao final da aula.

##### 11. Encerramento e Reflexão

Promova uma discussão com a turma:

###### Perguntas para reflexão

- Você conseguiria utilizar um site sem mouse?
- Por que a navegação por teclado é essencial para acessibilidade?
- O que acontece quando a ordem do foco não segue a estrutura visual?
- Como ARIA pode complementar a acessibilidade de uma página?
