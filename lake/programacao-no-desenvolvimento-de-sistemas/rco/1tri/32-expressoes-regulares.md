---
titulo: "Expressões regulares"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 32
serie: 3
aula_rco: "Aula 32"
slides: 26
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/32-expressoes-regulares/32-expressoes-regulares.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/32-expressoes-regulares/AULA 32_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/32-expressoes-regulares/AULA 32_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Expressões regulares

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Expressões regulares
- Aula 32

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Identificar o poder das expressões regulares (RegEx), uma ferramenta importante para buscar e validar informações em textos.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Regex101: Um ambiente online interativo para testar e depurar expressões regulares com suporte para várias linguagens de programação.
- Pythex: Um editor de expressões regulares especificamente para Python, ótimo para visualizar correspondências em tempo real.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Aplicamos o Paradigma de Orientação a Objetos para estruturar e gerenciar projetos de software, enfatizando a criação de classes e a implementação de métodos para melhorar a modularidade e a reusabilidade do código.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Ana está desenvolvendo um formulário de cadastro online e precisa garantir que os e-mails inseridos pelos usuários estão no formato correto.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Como Ana pode usar expressões regulares para validar os endereços de e-mail?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Ana pode utilizar uma expressão regular como:
- ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
- Para garantir que cada e-mail inserido corresponda ao formato desejado.

_4 imagem(ns) no slide._

> **Notas do apresentador:** Comentários sobre a resposta: Utilizar expressões regulares para validar e-mails é eficaz porque permite definir padrões específicos que o texto deve seguir, reduzindo a chance de dados incorretos serem aceitos e melhorando a qualidade dos dados coletados.

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Introdução às Expressões Regulares
- Expressões regulares (RegEx) são ferramentas poderosas para processar e manipular textos, permitindo identificar e extrair dados com base em padrões definidos. Elas são essenciais em validação de dados, segurança e processamento de texto.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Uso de RegEx em Programação
- RegEx é amplamente usada para validar formatos de dados como e-mails e URLs em várias linguagens de programação, facilitando tarefas como validação de formulários e limpeza de dados, essencial para desenvolvedores e analistas.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Finalidades das Expressões Regulares
- RegEx automatiza a verificação de formatos de dados e a extração de informações, sendo crucial em áreas como análise de dados e desenvolvimento web para garantir a integridade e precisão dos dados manipulados.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Explorando Quantificadores e Intervalos
- Dentro das RegEx, quantificadores como *, +, e ? controlam as repetições de padrões, enquanto intervalos especificam conjuntos de caracteres, permitindo expressões precisas para tarefas complexas de manipulação de textos.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Validação de URLs
- com Expressões Regulares
- As RegEx aprimoram a validação de URLs ao permitir a definição de padrões rigorosos para verificar e extrair componentes de URLs, garantindo que apenas dados formatados corretamente sejam aceitos e processados.

_4 imagem(ns) no slide._

### Slide 14 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Exemplos
- Arquivo Saiba Mais com exemplo!

_3 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual quantificador em RegEx é usado para indicar 'um ou mais' da expressão anterior?
- (A) +
- (B) *
- (C) ?
- (D) {1,}
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Qual quantificador em RegEx é usado para indicar 'um ou mais' da expressão anterior?
- (A) +
- (B) *
- (C) ?
- (D) {1,}
- Resposta correta: (A) +

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: O símbolo '+' é usado para representar que o elemento anterior na expressão regular deve aparecer pelo menos uma vez.

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Concluindo
- Exploramos como as expressões regulares podem potencializar a validação e manipulação de dados, uma habilidade crucial para qualquer desenvolvedor.

_3 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/string-python-extraindo-informacoes-url

_5 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- O que são expressões regulares
- 10 minutos
- Link para tarefa: https://cursos.alura.com.br/course/string-python-extraindo-informacoes-url/task/91889
- Expressões regulares (RegEx) são padrões usados para encontrar correspondências específicas em textos, permitindo identificar, extrair, substituir ou dividir dados baseados em regras definidas. São essenciais para validação e análise de texto em programação.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Quantificadores e intervalos
- 4 minutos
- Link para tarefa: https://cursos.alura.com.br/course/string-python-extraindo-informacoes-url/task/91890
- Quantificadores e intervalos em expressões regulares definem quantas vezes um elemento deve aparecer em uma correspondência. Quantificadores comuns incluem `+` (uma ou mais vezes), `*` (zero ou mais vezes) e `?` (zero ou uma vez). Intervalos, como `{1,3}`, especificam um número exato ou um intervalo de ocorrências permitidas.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Validando nossa URL com RegEx
- 12 minutos
- Link para tarefa: https://cursos.alura.com.br/course/string-python-extraindo-informacoes-url/task/91892
- Validar uma URL com RegEx envolve criar um padrão que corresponda à estrutura desejada de uma URL, verificando esquemas, domínios e caminhos. Isso assegura que a URL atenda a critérios específicos, como começar com "http://" ou "https://", e incluir caracteres válidos, aumentando a segurança e a confiabilidade das interações online.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Dominamos o uso de expressões regulares para validação de dados, uma ferramenta poderosa que aumenta a eficiência e precisão no desenvolvimento de software.
- https://miro.medium.com/v2/resize:fit:2000/1*auFmcTb8TH0kvxHFnDbMGw.png

_4 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Referências
- Bibliografia
- PUREWAL, Semmy. Aprendendo a Desenvolver Aplicações Web. Desenvolva rapidamente com as tecnologias JavaScript mais modernas. São Paulo: Novatec, 2014.
- SILVA, L. F.; OLIVEIRA, A. D. de. Desenvolvimento de Software II C#: programação em camadas. [S. l.]: CBL Edição do Autor, 2017. E-book.
- MARTIN, R. C. Arquitetura limpa: o guia do artesão para estrutura e design de software. Rio de Janeiro: Alta Books, 2019. E-book.
- GALOTTI, G. M. A. Qualidade de software. São Paulo: Pearson Education do Brasil, 2016. E-book.
- VAZQUEZ, C. E.; SIMÕES, G. S. Engenharia de requisitos: software orientado ao negócio. São Paulo: Brasport, 2016. E-book.
- Softwares
- Java Netbeans; WebStorm; Sublime Text; Intellij IDEA; Astah Software; Netbeans; Python; Ccharp; Colab; PyCharm; Jupyter Notebook.

_3 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 32_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 32

Questão 1

Qual dos seguintes quantificadores em expressões regulares é usado para especificar que a expressão precedente pode ocorrer zero ou mais vezes?

A) +

B) *

C) ?

D) {1,}

Resposta correta: B) *

Comentário sobre a resposta correta: O quantificador * é usado em expressões regulares para indicar que a expressão pode aparecer zero ou mais vezes, tornando-o útil para encontrar correspondências que podem não existir ou que se repetem várias vezes.

Questão 2

Como uma expressão regular pode ser utilizada para validar URLs que começam especificamente com "https"?

A) ^https?://

B) ^https://

C) https?://$

D) ^https$

Resposta correta: B) ^https://

Comentário sobre a resposta correta: A expressão ^https:// assegura que a URL comece exatamente com "https", onde ^ denota o início da string, garantindo que a correspondência comece com esse esquema específico.

## Outros documentos

_Fonte: AULA 32_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 32

Exemplo prático:

import re

# Validando uma URL com RegEx

pattern = re.compile(r'https?://(www\.)?([a-zA-Z0-9]+)\.([a-zA-Z]{2,})')

url = "http://www.example.com"

match = pattern.match(url)

if match:

print("URL válida")

else:

print("URL inválida")
