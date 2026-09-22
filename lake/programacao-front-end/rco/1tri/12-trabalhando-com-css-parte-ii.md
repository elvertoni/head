---
titulo: "Trabalhando com CSS Parte II"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 1
ordem_rco: 12
serie: 2
aula_rco: "Aula 12"
slides: 19
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PFE/1TRI/12-trabalhando-com-css-parte-ii/12-trabalhando-com-css-parte-ii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/12-trabalhando-com-css-parte-ii/AULA 12_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/12-trabalhando-com-css-parte-ii/AULA 12_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Trabalhando com CSS Parte II

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Trabalhando com CSS Parte II
- Aula 12

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Codificar aplicações e rotinas utilizando linguagens de programação específicas.
- Prototipar as habilidades de design visual.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Aprender a trabalhar com o CSS Parte I
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
- Projeto que já foi criado na aula anterior:
- https://caelum-online-public.s3.amazonaws.com/1179-html5-css3/02/aula-2-completa.zip
- Complemento:
- https://cursos.alura.com.br/course/html5-css3-primeiros-passos/task/99821

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Você teve o primeiro contato com o CSS, com funciona e função dentro de uma página web, a aula de hoje será continuação direta da aula anterior.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Folhas de estilo é como o CSS é comumente chamado. Ele é utilizado para organizar os estilos e definir cores, melhorando a apresentação visual de uma página web.
- Assim como utilizamos estilos nas páginas da internet, você também aplica estilos no seu caderno de aula.
- Realizem a atividade em duplas e socializem no final!
- Pense: como você organiza e utiliza esses estilos no seu caderno? Você usa cores diferentes, títulos destacados ou formas de organização para facilitar a leitura e o estudo?

_2 imagem(ns) no slide._

### Slide 8

- Conceituando
- A organização do CSS é baseada em regras e seletores. Cada regra CSS consiste em um seletor que identifica um ou mais elementos HTML e em uma lista de declarações que especificam como esses elementos devem ser estilizados.

_1 imagem(ns) no slide._

### Slide 9

- As regras CSS podem ser aplicadas a elementos HTML de várias maneiras, incluindo:
- Inline: As regras CSS podem ser aplicadas diretamente a elementos HTML usando o atributo "style".

_1 imagem(ns) no slide._

### Slide 10

- Interna: As regras CSS podem ser incluídas em uma seção "style" dentro da tag "head" do documento HTML.
- Externa: As regras CSS podem ser armazenadas em um arquivo separado com a extensão .css e vinculadas ao documento HTML usando a tag "link".

_1 imagem(ns) no slide._

### Slide 11

- Ainda sobre o HTML, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/html5-css3-primeiros-passos
- Para melhor compreensão do conteúdo, recomenda-se responder aos quizzes que aparecem entre as atividades propostas.

_3 imagem(ns) no slide._

### Slide 12

- Organizando o estilo
- Quais são as características dessa forma de criar o CSS? Uma delas é que não usamos o nome CSS. Usamos uma propriedade chamada style.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-primeiros-passos/task/53609
- Existem três formas de configurarmos o CSS. A que fizemos até agora foi a primeira delas, chamada CSS inline. Ou seja, na linha onde temos nossa tag, adicionamos a propriedade do CSS.
- Atividade no portal Alura

_2 imagem(ns) no slide._

### Slide 13

- Além disso, o CSS permite hierarquias de estilo, onde regras mais específicas têm precedência sobre regras gerais. Por exemplo, se uma regra geral especifica que todos os parágrafos tenham uma cor de fundo azul, uma regra mais específica para um parágrafo específico pode especificar que ele tenha uma cor de fundo verde.

_1 imagem(ns) no slide._

### Slide 14

- Em resumo, a organização do CSS permite aplicar estilos a elementos HTML de várias maneiras, incluindo inline, interna e externa, e permite hierarquias de estilo, onde regras mais específicas têm precedência sobre regras gerais.

_1 imagem(ns) no slide._

### Slide 15

- Vamos praticar?
- Hoje você vai dar mais um passo para se tornar um desenvolvedor web! Nesta atividade prática, o desafio será explorar e comparar diferentes formas de aplicar CSS em uma página HTML e entender como organizar estilos de maneira profissional.

_1 imagem(ns) no slide._

### Slide 16

- O que vimos na aula de hoje:
- O que é CSS e qual é o seu papel na construção de páginas web.
- A importância da organização do CSS para manter o código mais claro e fácil de manter.
- As principais formas de organizar e aplicar o CSS em uma página: inline, interno e externo.

_1 imagem(ns) no slide._

### Slide 17

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 18

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

### Slide 19

_(sem texto)_

## Atividade

_Fonte: AULA 12_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 12

Questão 1

Como é aplicado o CSS em uma página HTML?

A) Adicionando o código CSS diretamente na tag HTML

B) Adicionando o código CSS em um arquivo externo e referenciando-o na tag HTML

C) Adicionando o código CSS diretamente na tag head da página HTML

D) Adicionando o código CSS diretamente na tag body da página HTML

Resposta correta: B) Adicionando o código CSS em um arquivo externo e referenciando-o na tag HTML

Questão 2

Qual é a vantagem de se aplicar o CSS em um arquivo externo?

A) Permite a reutilização do código CSS em várias páginas HTML

B) Permite uma melhor organização do código CSS

C) Permite uma melhor otimização do código CSS

D) Todas as opções são corretas

Resposta correta: D) Todas as opções são corretas

## Prática

_Fonte: AULA 12_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 12

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender as diferentes formas de aplicar CSS (inline, interno e externo).
- Organizar estilos de forma adequada, separando conteúdo e apresentação.
- Aplicar regras CSS com diferentes níveis de especificidade.
- Comparar as vantagens e desvantagens de cada forma de organização do CSS.
Produto final esperado:

- Página HTML utilizando as três formas de aplicação de CSS (inline, interno e externo) com organização correta.

##### 2. Ferramentas Recomendadas

###### Editor HTML Online

- Para que serve: criar páginas HTML e aplicar CSS.
- Por que é adequado: permite testar rapidamente diferentes formas de aplicação.
- Como facilita o aprendizado: visualização imediata das alterações.
Link sugerido: https://html5-editor.net/

###### Navegador Web (Chrome, Edge ou Firefox)

- Para que serve: visualizar o comportamento do CSS aplicado.
- Por que é adequado: ambiente real de execução.
- Como facilita o aprendizado: permite validar organização e precedência.

###### Plataforma Alura

- Para que serve: reforçar conteúdo por meio de exercícios guiados.
- Por que é adequada: alinhada ao tema CSS introdutório.
- Como facilita o aprendizado: complementa com prática estruturada.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Página HTML criada anteriormente
- Editor HTML online ou ambiente local
- Navegador atualizado
- Conexão com internet
Link de apoio: https://cursos.alura.com.br/course/html5-css3-primeiros-passos

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações necessárias

- Disponibilizar a página criada na aula anterior.
- Preparar exemplo com CSS inline, interno e externo.
- Testar funcionamento do arquivo .css (caso use externo).

###### Condução da aula

1. Contextualização inicial (5 min)

- Retomar o conceito de CSS visto na aula anterior.
- Perguntar: “Qual a melhor forma de organizar os estilos?”
2. Demonstração do professor (15 min)

Apresentar as três formas:

- CSS Inline
- Uso do atributo style dentro da própria tag.
- Demonstrar limitação de manutenção.
- CSS Interno
- Uso da tag <style> dentro do <head>.
- CSS Externo
- Arquivo separado .css
- Uso da tag <link>
Explicar também:

- Conceito de hierarquia.
- Regras mais específicas sobrescrevem regras gerais.
3. Prática guiada (20 min)

- Alunos aplicam os três tipos.
- Observam qual regra prevalece quando há conflito.
4. Discussão e fechamento (10 min)

- Comparar vantagens e desvantagens.
- Relacionar com projetos maiores.

###### Pontos de atenção

- Corrigir conflitos de estilo.
- Explicar precedência de regras com exemplos simples.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá organizar o CSS de uma página HTML aplicando as três formas de estilização, comparando os resultados.

Problema real simulado: Organizar estilos de um site profissional de forma eficiente e escalável.

Habilidade desenvolvida: Organização e hierarquia de regras CSS.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada na prática
- Ensino por descoberta
- Experimentação
- Elementos de Lemov:
- Modelagem
- Prática guiada
- Verificação de entendimento
- Feedback imediato

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Abra sua página HTML.
- Aplique um estilo inline em um parágrafo.
- Crie uma regra interna no <head> para alterar a mesma propriedade.
- Observe qual estilo prevalece.
- Crie um arquivo externo .css.
- Vincule o arquivo ao HTML usando <link>.
- Aplique uma regra externa que altere novamente o estilo.
- Analise qual regra tem prioridade.
- Registre suas conclusões.

##### 8. Exemplo ou Demonstração

Exemplo conceitual de conflito:

- Regra geral define:
- Cor azul para todos os parágrafos.
- Regra específica define:
- Cor verde para um parágrafo específico.
Resultado:

- Regra mais específica prevalece.
Explicação: CSS segue hierarquia e especificidade.

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Página HTML contendo:
- CSS inline
- CSS interno
- CSS externo
- Demonstração clara de entendimento da hierarquia.
- Organização adequada do código.
O professor verifica analisando a aplicação correta e as conclusões registradas.

##### 10. Formato de Entrega da Atividade

- Formato: arquivo HTML + arquivo CSS (se externo) ou print do editor.
- Conteúdo: demonstração das três formas de CSS.
- Entrega: ao final da aula.
- Prazo sugerido: imediato.

##### 11. Encerramento e Reflexão

Perguntas orientadoras:

- Qual forma de CSS é mais organizada?
- Quando usar CSS externo?
- Por que a hierarquia é importante?
