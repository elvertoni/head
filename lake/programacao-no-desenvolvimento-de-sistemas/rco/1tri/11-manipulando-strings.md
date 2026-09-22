---
titulo: "Manipulando strings"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 11
serie: 3
aula_rco: "Aula 11"
slides: 27
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/11-manipulando-strings/11-manipulando-strings.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/11-manipulando-strings/AULA 11_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Manipulando strings

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Manipulando strings
- Aula 11

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Manipular strings em Python e aprender a localização das letras específicas da string para análise e manipulação de texto.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Leitura Sugerida: "Aprenda Python jogando" para entender como utilizar Python em jogos simples.
- IDE Online: Replit.com, uma plataforma excelente para desenvolvimento e teste de jogos em Python sem necessidade de instalação local.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Iniciamos a estrutura do jogo da forca em Pyhton.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Seu desafio é identificar e extrair palavras-chave, contabilizar ocorrências de certas letras e palavras, e analisar a estrutura do texto.
- Carlos é um desenvolvedor iniciante trabalhando em um projeto de análise de texto.
- Ele precisa extrair informações específicas de grandes volumes de texto, mas está incerto sobre como iniciar...

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Como Carlos pode eficientemente encontrar uma letra específica em uma string e analisar a frequência de palavras em Python?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Carlos pode usar a função count() para encontrar a frequência de uma letra específica dentro de uma string e o método find() ou index() para localizar a posição de uma letra.
- Para analisar a frequência de palavras, pode-se utilizar o método split() para dividir o texto em palavras e um dicionário para contabilizar as ocorrências.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Essas ferramentas básicas de manipulação de strings são poderosas para análise de texto, permitindo que Carlos execute suas tarefas de forma eficiente e eficaz.
- Com a prática, ele desenvolverá a habilidade de manipular e extrair dados de strings complexas, uma competência essencial para muitos projetos de programação.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Introdução
- Strings são sequências de caracteres, como palavras ou frases, que podem ser manipuladas de diversas maneiras para atender a necessidades específicas, como análise de dados, processamento de texto ou simplesmente para modificar o conteúdo de uma mensagem exibida ao usuário.
- Manipular strings é uma habilidade fundamental na programação, especialmente útil quando lidamos com texto em nossos programas.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Find & Count
- Encontrar letras ou sequências específicas dentro de uma string é uma operação comum. Isso pode ser necessário para validar entradas do usuário, para pesquisar por dados em um texto ou para processar informações.
- Python, como muitas outras linguagens de programação, fornece uma gama de funções que facilitam essas operações.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Find & Count
- Por exemplo, o método .find() retorna a primeira posição de uma sub-string dentro de uma string, enquanto o método .count() pode ser usado para contar quantas vezes uma letra ou uma sequência de letras aparece.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Upper & Lower
- Além dessas, existem várias outras funções importantes para trabalhar com strings. O método .upper() e .lower() são usados para converter uma string inteira para maiúscula ou minúscula, respectivamente. Isso pode ser útil para normalizar dados para comparação.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Replace
- O método .replace() permite substituir uma parte da string por outra, o que é especialmente útil para corrigir erros de digitação ou para substituir termos.

_4 imagem(ns) no slide._

### Slide 15 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- texto = "Olá, mundo!“
- print(texto.find("mundo")) # Resultado: 5
- print(texto.count("o")) # Resultado: 2
- print(texto.upper()) # Resultado: OLÁ, MUNDO!
- print(texto.replace("Olá", "Adeus")) # Resultado: Adeus, mundo!

_3 imagem(ns) no slide._

> **Notas do apresentador:** Para iniciantes, entender e praticar essas funções básicas de manipulação de strings abre portas para tarefas mais complexas, como análise de texto e processamento de linguagem natural. A manipulação eficaz de strings é uma ferramenta poderosa no arsenal de qualquer programador, permitindo a criação de programas mais dinâmicos, interativos e úteis.

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- A Manipulação
- Portanto, a manipulação de strings e o conhecimento de suas funções importantes são essenciais não apenas para a realização de tarefas específicas de processamento de texto, mas também para a preparação de dados para análise, validação de entradas do usuário e muitas outras operações fundamentais na programação. Com prática, essas habilidades se tornam intuitivas, permitindo que desenvolvedores criem soluções mais eficientes e inovadoras.

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual das seguintes funções da string em Python você usaria para substituir todas as ocorrências da palavra "Python" por "JavaScript" em uma string?
- (A) replace("Python", "JavaScript")
- (B) find("JavaScript")
- (C) upper()
- (D) count("Python")
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual das seguintes funções da string em Python você usaria para substituir todas as ocorrências da palavra "Python" por "JavaScript" em uma string?
- (A) replace("Python", "JavaScript")
- (B) find("JavaScript")
- (C) upper()
- (D) count("Python")
- Resposta Correta: (A) replace("Python", "JavaScript")

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: A alternativa a é correta porque o método .replace() é usado para substituir partes de uma string por outra. Neste caso, substituir todas as ocorrências de "Python" por "JavaScript" muda efetivamente o texto da string original para refletir a nova linguagem mencionada, demonstrando uma manipulação direta e eficaz do conteúdo da string.

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- Manipulação de strings é crucial para o processamento de texto, permitindo análises, edições e buscas eficientes dentro de textos.

_4 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem

_5 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Encontrando letras
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem/task/25112
- Encontrar letras em uma string envolve buscar uma letra ou sequência específica dentro do texto. Utilizando métodos como .find() ou .index() em Python, é possível determinar a posição de uma letra, facilitando tarefas como análise de texto ou validações de entrada de dados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Funções importantes da String
- 12 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem/task/25130
- Funções importantes de string em Python, como .upper(), .lower(), .replace(), e .split(), permitem manipular e transformar textos, adaptando-os para diversas necessidades de programação, desde a normalização de dados até a extração e substituição de informações específicas.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Exploramos como manipular strings em Python, focando em funções como .count(), .replace(), .find() e .index(), essenciais para encontrar letras, substituir textos e analisar dados.
- Na próxima aula, vamos compreender como as listas em Python podem ser usadas para armazenar e manipular dados.

_4 imagem(ns) no slide._

### Slide 24

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

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

## Atividade

_Fonte: AULA 11_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 11

Questão 1

Qual método em Python é usado para substituir partes de uma string?

a) .replace()

b) .substring()

c) .concat()

d) .split()

Resposta Correta: a) .replace()

Comentário: A opção a) é correta porque o método .replace() é usado para criar uma nova string, substituindo todas as ocorrências de uma sub-string especificada por outra. É uma função importante para editar e limpar dados de texto.

Questão 2

Como você pode encontrar a posição da primeira ocorrência de 'c' na string "ciência da computação"?

a) .find('c')

b) .index('c')

c) .search('c')

d) .locate('c')

Resposta Correta: b) .index('c')

Comentário: Embora ambas as opções a) e b) estejam tecnicamente corretas para encontrar a posição de uma letra, a .index('c') é especificamente reconhecida por retornar a primeira ocorrência de um caractere numa string. Se o caractere não for encontrado, .find() retorna -1, enquanto .index() gera um erro.
