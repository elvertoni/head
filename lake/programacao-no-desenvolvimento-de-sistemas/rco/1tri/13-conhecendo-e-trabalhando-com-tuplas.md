---
titulo: "com tuplas"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 13
serie: 3
aula_rco: "Aula 13"
slides: 29
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/13-conhecendo-e-trabalhando-com-tuplas/13-conhecendo-e-trabalhando-com-tuplas.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/13-conhecendo-e-trabalhando-com-tuplas/AULA 13_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# com tuplas

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Conhecendo e trabalhando
- com tuplas
- Aula 13

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Vamos explorar o conceito de tuplas em Python, entender como elas se diferenciam das listas e como podemos usá-las em conjunto para organizar dados de forma eficiente.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Leitura Sugerida: "Python Crash Course" por Eric Matthes, um capítulo dedicado a listas e estruturas de dados.
- IDE Online: Repl.it (https://repl.it) ou o Python Tutor (http://pythontutor.com), que permitem a execução de código Python online sem necessidade de instalação local.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Exploramos as listas em Python, aprendendo a criar, acessar e modificar seus elementos. Também discutimos sobre métodos úteis como append, remove e sort para manipulação de listas.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Imagine que João, um desenvolvedor iniciante, está trabalhando em um projeto que requer armazenamento de dados imutáveis para configurações do sistema.
- Ele precisa escolher entre usar listas ou tuplas.
- Qual seria a melhor escolha para garantir que os dados não sejam alterados acidentalmente?

_5 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Por que usar tuplas ao invés de listas para armazenar dados de configuração?
- Quem sabe responde!

_6 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Ao usá-las, João garante que as configurações do sistema não sejam alteradas acidentalmente, pois tuplas não podem ser modificadas após sua criação. Isso traz segurança e estabilidade ao projeto, evitando bugs relacionados a mudanças indesejadas de dados.
- Tuplas
- são ideais para armazenar dados imutáveis.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- O que são Tuplas?
- Tuplas são uma estrutura de dados imutável em Python. Isso significa que, uma vez definida, não é possível alterar seus elementos. Tuplas são declaradas usando parênteses () e podem armazenar diferentes tipos de dados, como números, strings e até outras tuplas.
- https://news.mit.edu/sites/default/files/images/202303/MIT-Python.png

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- A imutabilidade das tuplas as torna ideais para armazenar dados que não devem ser alterados, como dias da semana ou configurações de um sistema.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Listas e Tuplas Juntas
- Listas, que são mutáveis e definidas por colchetes [], são ideais para coleções de dados que precisam ser alteradas, como adicionar, remover ou alterar itens.
- Embora listas e tuplas possam parecer similares, elas são usadas em situações diferentes.

_5 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Listas e Tuplas Juntas
- No entanto, quando trabalhamos com dados fixos que devem permanecer constantes ao longo do programa…
- As tuplas são a escolha certa!

_8 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- # Definindo uma tupla
- dias_da_semana = ("segunda", "terça", "quarta", "quinta", "sexta")
- # Definindo uma lista
- tarefas = ["lavar a louça", "comprar pão"]
- # Adicionando uma tarefa à lista
- tarefas.append("estudar Python")

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- # Tentar alterar um elemento
- da tupla resultaria em erro
- # dias_da_semana[0] = "domingo"
- # Isso causaria um TypeError
- print(dias_da_semana)
- print(tarefas)

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Finalidade e Utilização
- A escolha entre listas e tuplas depende da natureza dos dados com que você está trabalhando. Se os dados não requerem modificações após sua definição, usar tuplas pode não apenas prevenir erros acidentais de modificação, mas também otimizar a memória do programa.

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Finalidade e Utilização
- Por outro lado, para dados que são dinâmicos, onde itens serão adicionados, removidos ou alterados, listas são mais apropriadas.

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Finalidade e Utilização
- Em resumo, entender a diferença entre listas e tuplas e saber quando usar cada uma permite que desenvolvedores Python criem programas mais eficientes e seguros.
- https://img.freepik.com/vetores-premium/a-chave-dourada-abre-o-cadeado-ilustracao-em-vetor-plana-isolada-no-fundo-branco_124715-1135.jpg

_4 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Este conhecimento é fundamental para qualquer um que deseje explorar a programação Python, desde a manipulação de dados até a configuração de sistemas complexos.

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual das seguintes afirmações melhor descreve a diferença entre listas e tuplas em Python?
- (A) Ambas são imutáveis, mas tuplas podem armazenar mais tipos de dados.
- (B) Listas são imutáveis, enquanto tuplas são mutáveis.
- (C) Tuplas são usadas exclusivamente para dados numéricos, enquanto listas são para strings.
- (D) Listas são mutáveis e tuplas são imutáveis.
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Resposta correta
- Qual das seguintes afirmações melhor descreve a diferença entre listas e tuplas em Python?
- (A) Ambas são imutáveis, mas tuplas podem armazenar mais tipos de dados.
- (B) Listas são imutáveis, enquanto tuplas são mutáveis.
- (C) Tuplas são usadas exclusivamente para dados numéricos, enquanto listas são para strings.
- (D) Listas são mutáveis e tuplas são imutáveis.
- Resposta Correta: (D) Listas são mutáveis e tuplas são imutáveis.

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: A alternativa d é correta porque captura a essência das diferenças entre listas e tuplas. A mutabilidade das listas permite alterar, adicionar ou remover itens após a criação, tornando-as ideais para coleções de dados que podem mudar ao longo do tempo. As tuplas, por serem imutáveis, são perfeitas para armazenar dados que não devem ser alterados, oferecendo segurança adicional no manuseio de dados fixos e configurações dentro de um programa.

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- As tuplas, sendo imutáveis, são ideais para dados constantes, enquanto listas mutáveis se adaptam a dados dinâmicos. Combiná-las permite flexibilidade e segurança no manuseio de dados em Python.

_4 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem

_5 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- O que são tuplas?
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem/task/25150
- Tuplas são estruturas de dados imutáveis em Python, utilizadas para armazenar coleções ordenadas de itens. Uma vez criada, uma tupla não permite alterações em seus elementos, tornando-a ideal para armazenar dados constantes.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- O que são tuplas?
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem/task/25155
- Combinar listas e tuplas em Python permite criar estruturas de dados complexas, utilizando a flexibilidade das listas para elementos mutáveis e a constância das tuplas para dados fixos, otimizando a organização e segurança dos dados no código.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Investigamos as tuplas e listas no contexto de Python, enfatizando suas distinções fundamentais, como imutabilidade em comparação com mutabilidade, e exploramos como essas estruturas de dados podem ser empregadas em conjunto.

_4 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- Bibliografia
- PUREWAL, Semmy. Aprendendo a Desenvolver Aplicações Web. Desenvolva rapidamente com as tecnologias JavaScript mais modernas. São Paulo: Novatec, 2014.
- SILVA, L. F.; OLIVEIRA, A. D. de. Desenvolvimento de Software II C#: programação em camadas. [S. l.]: CBL Edição do Autor, 2017. E-book.
- MARTIN, R. C. Arquitetura limpa: o guia do artesão para estrutura e design de software. Rio de Janeiro: Alta Books, 2019. E-book.
- GALOTTI, G. M. A. Qualidade de software. São Paulo: Pearson Education do Brasil, 2016. E-book.
- VAZQUEZ, C. E.; SIMÕES, G. S. Engenharia de requisitos: software orientado ao negócio. São Paulo: Brasport, 2016. E-book.
- Softwares
- Java Netbeans; WebStorm; Sublime Text; Intellij IDEA; Astah Software; Netbeans; Python; Ccharp; Colab; PyCharm; Jupyter Notebook.
- Referências

_3 imagem(ns) no slide._

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 28

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 29

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 13_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 13

Questão 1

O que torna as tuplas diferentes das listas em Python?

a) Tuplas são mutáveis, enquanto listas são imutáveis.

b) Tuplas permitem a adição de novos elementos após sua criação.

c) Tuplas e listas não têm diferenças significativas em Python.

d) Tuplas são imutáveis, enquanto listas são mutáveis.

Resposta Correta: d) Tuplas são imutáveis, enquanto listas são mutáveis.

Comentário: A alternativa d é correta porque captura a principal diferença entre listas e tuplas. As tuplas, sendo imutáveis, oferecem uma maneira segura de armazenar dados que não devem ser alterados ao longo do programa, enquanto as listas, devido à sua mutabilidade, são ideais para coleções de dados que podem mudar, como adicionar ou remover itens.

Questão 2

Como você pode combinar listas e tuplas em um programa Python?

a) Convertendo todas as listas em tuplas para uniformidade.

b) Usando listas dentro de tuplas para criar uma estrutura de dados complexa.

c) Transformando tuplas em listas para permitir modificações.

d) Tuplas e listas não podem ser combinadas em Python.

Resposta Correta: b) Usando listas dentro de tuplas para criar uma estrutura de dados complexa.

Comentário: A opção b é correta e destaca uma prática comum em Python, onde listas e tuplas são usadas juntas para formar estruturas de dados complexas. Isso permite aproveitar a mutabilidade das listas e a imutabilidade das tuplas, conforme necessário, para armazenar e manipular dados de forma eficaz.
