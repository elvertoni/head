---
titulo: "CSS e Acessibilidade: Listas e display: none – Parte II"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 63
serie: 2
aula_rco: "Aula 63"
slides: 22
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/63-css-e-acessibilidade-listas-e-display-none-parte-ii/63-css-e-acessibilidade-listas-e-display-none-parte-ii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/63-css-e-acessibilidade-listas-e-display-none-parte-ii/AULA 63_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/63-css-e-acessibilidade-listas-e-display-none-parte-ii/AULA 63_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# CSS e Acessibilidade: Listas e display: none – Parte II

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- CSS e Acessibilidade: Listas e display: none – Parte II
- Aula 63

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
- Compreender se o CSS interfere no leitor de tela Parte II.
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
- Concluímos os estudos sobre os atributos lang e alt e os impactos que ele oferecem na utilização de recursos para portadores de deficiência visual.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Joana é uma desenvolvedora web em início de carreira que está trabalhando em seu primeiro projeto grande, um site para uma ONG. Ela tem se esforçado para tornar o site o mais acessível possível e tem utilizado leitores de tela para testar a acessibilidade.
- No entanto, Joana percebe que o leitor de tela está lendo informações que não estão sendo exibidas visualmente na página. Depois de inspecionar o código, ela percebe que está usando CSS para ocultar alguns elementos visuais, mas não os ocultou dos leitores de tela.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Joana está confusa sobre como resolver essa situação. Ela não tem certeza se deve remover o código CSS que está ocultando os elementos, ou se há outra maneira de fazer com que os leitores de tela ignorem os elementos ocultos.
- O que Joana deve fazer para resolver essa situação?
- Conversem e apresentem suas visões
- https://cryptoid.com.br/wp-content/uploads/2018/01/iStock-838172306.jpg

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Joana deveria usar técnicas apropriadas de CSS e ARIA (Accessible Rich Internet Applications) para ocultar corretamente o conteúdo dos leitores de tela. A propriedade "display: none" ou "visibility: hidden" no CSS, ou o atributo "hidden" no HTML, irá ocultar os elementos tanto visualmente quanto dos leitores de tela.

_1 imagem(ns) no slide._

### Slide 10

- Resposta
- Se Joana quiser ocultar o elemento visualmente, mas ainda quer que seja lido pelos leitores de tela, ela pode usar técnicas de CSS off-screen. Para controlar a exposição do conteúdo aos leitores de tela de uma forma mais granular, ela pode usar os atributos ARIA "aria-hidden" e "aria-labelledby". Pesquise sobre eles.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- Os leitores de tela são ferramentas assistivas importantes que permitem aos usuários com deficiência visual navegar na internet. No entanto, eles podem encontrar dificuldades para interpretar o conteúdo da página da web se o CSS (Cascading Style Sheets) for usado de forma inadequada.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Um exemplo comum de problema surge quando os desenvolvedores usam CSS para alterar a ordem visual dos elementos na página. Os leitores de tela leem os elementos na ordem em que aparecem no código HTML, e não na ordem que aparecem visualmente na página. Se o CSS for usado para alterar drasticamente a ordem visual, o usuário do leitor de tela pode se confundir ou perder informações importantes.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Outro problema ocorre quando os desenvolvedores usam CSS para esconder o conteúdo visualmente, mas não o escondem dos leitores de tela. Isso pode levar a uma situação onde o leitor de tela está lendo o conteúdo que não é visível na página, causando confusão.

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Os leitores de tela também têm problemas para interpretar o texto que é inserido usando CSS. Este texto, muitas vezes usado para ícones ou elementos de design, não será lido pelos leitores de tela, pois eles só leem o conteúdo inserido no HTML. Isso pode deixar os usuários de leitores de tela sem acesso a informações importantes.

_1 imagem(ns) no slide._

### Slide 15

- Conceituando
- Por último, embora o CSS seja uma ferramenta poderosa para aprimorar a aparência visual de um site, ele não deve ser usado para transmitir informações importantes ou para implementar funcionalidades do site. Informações importantes devem sempre ser codificadas em HTML, que é muito mais acessível para os leitores de tela, e a funcionalidade interativa deve ser implementada com HTML e JavaScript, não CSS.

_1 imagem(ns) no slide._

### Slide 16

- Ainda sobre HTML e leitores de tela, vamos conhecer praticando?
- Na plataforma Alura, vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/acessibilidade-web-front-end
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 17

- Escondido demais
- 10 minutos
- Alguns elementos ficam escondidos demais para os leitores de tela.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36243
- Perceberemos que o leitor de tela ignora totalmente o check box. Vamos verificar como podemos realizar melhorias no código.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 19

- O que vimos na aula de hoje:
- Aprendemos como o CSS pode impactar nos leitores com itens que podem ficar ocultos.

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

_Fonte: AULA 63_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 63

Questão 1

Como garantir que uma checkbox seja lida corretamente por leitores de tela?

A) Utilizando apenas imagens para representar o estado da checkbox.

B) Criando uma label associada à checkbox usando o atributo "for" com o mesmo valor do atributo "id" da checkbox.

C) Colocando a checkbox em um elemento "div" sem atributos adicionais.

D) Deixando a checkbox sem uma label e apenas utilizando um título visualmente perceptível.

Resposta correta: B) Criando uma label associada à checkbox usando o atributo "for" com o mesmo valor do atributo "id" da checkbox.

Comentário: A opção B é a correta pois as labels associadas fornecem uma descrição textual para as checkbox, tornando-as acessíveis para os leitores de tela. Sem uma label associada, a checkbox pode não fazer sentido para os usuários do leitor de tela.

Questão 2

Como você pode facilitar a navegação do usuário do leitor de tela em um formulário com várias checkboxes?

A) Agrupando as checkboxes em um elemento fieldset com uma legenda apropriada.

B) Utilizando apenas cores para diferenciar as checkboxes.

C) Colocando todas as checkboxes em uma única linha.

D) Fazendo com que todas as checkboxes tenham o mesmo rótulo.

Resposta correta: A) Agrupando as checkboxes em um elemento fieldset com uma legenda apropriada.

Comentário: Agrupar checkboxes relacionadas com o elemento "fieldset" e fornecer uma legenda apropriada com o elemento "legend" melhora a acessibilidade, facilitando a compreensão dos usuários de leitores de tela. As outras opções não melhoram a acessibilidade e podem, de fato, tornar a navegação mais difícil para os usuários de leitores de tela.

## Prática

_Fonte: AULA 63_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 63

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender como leitores de tela interpretam conteúdos ocultos.
- Identificar problemas de acessibilidade causados pelo uso inadequado do CSS.
- Diferenciar conteúdos ocultos visualmente e conteúdos ocultos para leitores de tela.
- Aplicar corretamente propriedades como display: none, visibility: hidden e atributo hidden.
- Analisar situações em que conteúdos devem ou não ser lidos por tecnologias assistivas.
- Melhorar a acessibilidade de componentes web.

###### Produto Final Esperado

O estudante deverá criar uma página HTML contendo elementos visíveis e ocultos, demonstrando diferentes formas de ocultação de conteúdo e explicando seus impactos na acessibilidade.

##### 2. Ferramentas Recomendadas

###### Visual Studio Code (VS Code)

Para que serve: edição dos arquivos HTML e CSS.

Por que é adequado: facilita a construção e testes dos exemplos de acessibilidade.

Como facilita o aprendizado: permite alterar rapidamente o comportamento dos elementos e visualizar os resultados.

Site: https://code.visualstudio.com

###### Navegador Web

Para que serve: visualização da página.

Por que é adequado: permite validar o comportamento visual dos elementos ocultos.

Como facilita o aprendizado: possibilita comparar a exibição visual com a estrutura do HTML.

###### NVDA (NonVisual Desktop Access)

Para que serve: leitor de tela gratuito.

Por que é adequado: permite verificar quais elementos são lidos ou ignorados.

Como facilita o aprendizado: demonstra o impacto das decisões de desenvolvimento na experiência do usuário.

Site: https://www.nvaccess.org

###### WAVE Accessibility Tool

Para que serve: análise de acessibilidade.

Por que é adequado: ajuda a identificar problemas relacionados à ocultação inadequada de conteúdo.

Como facilita o aprendizado: fornece feedback imediato sobre possíveis falhas.

Site: https://wave.webaim.org

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve possuir:

VS Code instalado

Navegador atualizado

Projeto da aula anterior

Conexão com internet

NVDA instalado (opcional)

Conhecimentos básicos de HTML e CSS

Projeto Apeperia ou projeto disponibilizado pelo professor

###### Materiais de Apoio

Curso Alura:

https://cursos.alura.com.br/course/acessibilidade-web-front-end

Projeto base:

https://github.com/designernatan/curso-acessibilidade-web-front-end-1/archive/4777a875b8e01a9f14d519e94ce3d282b325a3f9.zip

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações Necessárias

- Disponibilizar projeto utilizado nas aulas anteriores.
- Garantir acesso ao VS Code e navegador.
- Demonstrar o funcionamento de um leitor de tela.
- Preparar exemplos com diferentes técnicas de ocultação.

###### Contextualização (5 minutos)

Apresente o cenário:

Joana percebeu que alguns conteúdos ocultos visualmente continuam sendo lidos pelo leitor de tela, causando confusão para os usuários.

Pergunta para a turma:

Quando escondemos algo na tela, ele deve sempre desaparecer também para os leitores de tela?

###### Conceituando Conteúdo Oculto (10 minutos)

Explique:

- Conteúdo visual.
- Conteúdo acessível.
- Leitura por tecnologias assistivas.
Apresente exemplos de situações onde o conteúdo deve:

- ser ocultado para todos;
- permanecer acessível apenas para leitores de tela.

###### Conceituando Técnicas de Ocultação (10 minutos)

Explique:

- display: none
- visibility: hidden
- atributo hidden
- ocultação visual para acessibilidade
Discutir quando utilizar cada abordagem.

###### Demonstração Prática (10 minutos)

Demonstrar:

- Elementos visíveis.
- Elementos ocultos.
- Comportamento no navegador.
- Comportamento em leitores de tela.
Comparar resultados.

###### Prática Guiada (10 minutos)

Orientar os alunos a:

- criar exemplos;
- aplicar estilos;
- testar acessibilidade;
- registrar observações.

###### Encerramento (5 minutos)

Promover compartilhamento das conclusões obtidas durante os testes.

###### Pontos de Atenção

- Não ocultar informações importantes sem justificativa.
- Evitar utilizar CSS como única forma de transmitir informação.
- Garantir que elementos interativos permaneçam acessíveis.
- Avaliar sempre a experiência do usuário final.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá construir uma página de demonstração sobre acessibilidade contendo diferentes exemplos de conteúdos ocultos.

A atividade deverá demonstrar:

- Conteúdo visível.
- Conteúdo oculto com CSS.
- Conteúdo oculto utilizando atributo HTML.
- Explicações sobre o comportamento de cada caso.

###### Problema Real Simulado

Uma ONG deseja revisar seu portal para garantir que conteúdos ocultos não prejudiquem usuários de leitores de tela.

###### Habilidade Desenvolvida

Análise e implementação de técnicas de acessibilidade relacionadas à exibição e ocultação de conteúdo.

##### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Problemas (PBL)

Os alunos resolvem problemas reais de acessibilidade.

###### Aprendizagem por Experimentação

Testam diferentes técnicas de ocultação.

###### Ensino por Descoberta

Observam como tecnologias assistivas interpretam cada cenário.

###### Elementos de Lemov

- Modelagem
- Prática Guiada
- Verificação de Compreensão
- Feedback Imediato
- Revisão

##### 7. Passo a Passo da Atividade Prática (para os alunos)

###### Etapa 1 – Criar Estrutura da Página

- Crie uma página chamada:
- acessibilidade.html
- Adicione um título principal.
- Crie três seções de demonstração.

###### Etapa 2 – Criar Exemplos

- Crie:
- um conteúdo totalmente visível;
- um conteúdo ocultado visualmente;
- um conteúdo ocultado para todos os usuários.
- Identifique cada exemplo com títulos explicativos.

###### Etapa 3 – Aplicar CSS

- Crie classes para controlar a exibição.
- Organize visualmente a página.
- Destaque as diferenças entre os exemplos.

###### Etapa 4 – Análise

- Observe o comportamento dos elementos no navegador.
- Compare os resultados obtidos.
- Quando disponível, teste utilizando NVDA.

###### Etapa 5 – Documentação

- Crie uma tabela explicando:
- técnica utilizada;
- efeito visual;
- impacto na acessibilidade.

###### Etapa 6 – Evidências

- Capture prints:
- da página pronta;
- dos exemplos criados;
- da tabela explicativa.

##### 8. Exemplo ou Demonstração

###### Estrutura da Página

- Página de Testes
- │
- ├── Exemplo Visível
- ├── Exemplo Oculto Visualmente
- └── Exemplo Oculto Totalmente

###### Tabela de Análise

| Técnica | Visível na Tela | Leitor de Tela |
| --- | --- | --- |
| Conteúdo normal | Sim | Sim |
| display: none | Não | Não |
| hidden | Não | Não |

###### Fluxo da Atividade

- Criar Conteúdo
- ↓
- Aplicar CSS
- ↓
- Testar Navegação
- ↓
- Comparar Resultados
- ↓
- Documentar Conclusões

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Página funcional.
- Exemplos de ocultação corretamente implementados.
- Tabela explicativa.
- Relatório com observações dos testes realizados.

###### Critérios de Verificação

O professor deverá verificar:

Estrutura HTML organizada

Aplicação correta das técnicas estudadas

Entendimento da relação entre CSS e acessibilidade

Registro das observações

Participação na atividade

##### 10. Formato de Entrega da Atividade

###### O que deve ser enviado

- Arquivo HTML.
- Arquivo CSS.
- Capturas de tela da atividade.
- Relatório simples contendo:
- exemplos criados;
- comportamento observado;
- conclusões obtidas.

###### Nomeação Sugerida

- Aula63_NomeSobrenome
Exemplo:

- Aula63_MariaOliveira

###### Onde Entregar

- Google Classroom
- Google Drive
- AVA da instituição

###### Prazo Sugerido

Ao final da aula.

##### 11. Encerramento e Reflexão

Promova uma discussão com a turma:

###### Perguntas para reflexão

- Todo conteúdo oculto deve ser ignorado pelos leitores de tela?
- Qual a diferença entre ocultar visualmente e ocultar semanticamente?
- Como o CSS pode impactar negativamente a acessibilidade?
- Quais cuidados um desenvolvedor deve ter ao esconder informações?
