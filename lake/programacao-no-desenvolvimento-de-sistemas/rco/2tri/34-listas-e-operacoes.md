---
titulo: "Listas e operações"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 2
ordem_rco: 34
serie: 3
aula_rco: "Aula 34"
slides: 24
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/34-listas-e-operacoes/34-listas-e-operacoes.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/34-listas-e-operacoes/AULA 34_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/34-listas-e-operacoes/AULA 34_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Listas e operações

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Listas e operações
- Aula 34

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Reconhecer as listas e suas operações em Python, focando em técnicas de ordenação utilizando a biblioteca functools.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- PyCharm Community Edition: Um IDE gratuito que oferece suporte abrangente para Python, ideal para experimentar e depurar métodos especiais.
- Jupyter Notebook: Um ambiente interativo que permite escrever e executar código Python em blocos, ótimo para testes e demonstrações.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Na última aula, aprendemos sobre métodos especiais em Python, como __len__(), __str__(), e discutimos igualdade e identidade. Esses conceitos nos ajudam a criar classes personalizadas e a manipular objetos de maneira avançada.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Diego está criando um programa para organizar uma lista de alunos com suas respectivas notas.
- Ele quer garantir que a lista esteja ordenada de forma eficiente, considerando critérios personalizados.
- Como ele pode usar as operações de listas e a biblioteca functools para ordenar essa lista de alunos por notas de forma personalizada?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Diego pode usar a função sorted() com o argumento key combinado com functools.cmp_to_key para definir critérios de ordenação personalizados, ordenando a lista conforme a necessidade.
- Compreender e aplicar técnicas de ordenação permite a Diego organizar dados de maneira eficiente, facilitando a visualização e análise, o que é importante em contextos profissionais.

_5 imagem(ns) no slide._

> **Notas do apresentador:** Compreender e utilizar métodos especiais permite a Mariana criar classes mais intuitivas e integradas com as funcionalidades nativas de Python, resultando em código mais limpo e de fácil manutenção.

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Explorando Listas em Python
- São coleções ordenadas e mutáveis de elementos, usadas para armazenar sequências de itens.
- São fundamentais para manipulação de dados em Python, permitindo adição, remoção e iteração sobre elementos.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Operações com Listas
- Listas suportam diversas operações, como:
- Adição (append())
- Remoção (remove())
- Fatiamento ([start:stop:step])
- Essas operações gerenciam e transformam dados de forma eficiente.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- A Relevância das Listas
- Listas são uma estrutura de dados versátil e amplamente usada em programação.
- Elas são essenciais para tarefas como armazenamento de coleções de itens, ordenação de dados, e execução de algoritmos de busca.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Aplicações Reais de Listas
- Na prática, listas são usadas para organizar e manipular dados, como listas de estudantes, produtos em um inventário ou resultados de uma pesquisa.
- A capacidade de ordenar e manipular listas auxilia na análise de dados e desenvolvimento de software.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Ordenação Completa e Functools
- Para ordenação avançada, Python oferece a função sorted() e o método sort(), que podem ser personalizados usando funções lambda e functools.cmp_to_key para definir critérios de ordenação complexos. Isso permite uma flexibilidade significativa na maneira como os dados são organizados.

_3 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Integração de Ordenação com Functools
- Usar functools para criar critérios de ordenação personalizados enriquece a funcionalidade das listas. A função cmp_to_key transforma uma função de comparação em uma chave utilizável por sorted(), permitindo ordenar listas com base em múltiplos critérios.

_3 imagem(ns) no slide._

### Slide 14 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- DESENVOLVIMENTO DE SISTEMAS
- Exemplos

_7 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual função em Python pode ser usada para ordenar uma lista com base em um critério personalizado?
- (A) sort()
- (B) filter()
- (C) map()
- (D) sorted()
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Qual função em Python pode ser usada para ordenar uma lista com base em um critério personalizado?
- (A) sort()
- (B) filter()
- (C) map()
- (D) sorted()
- Resposta correta: D) sorted()

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta correta: A função sorted() pode ser usada para ordenar uma lista com base em um critério personalizado fornecido pelo parâmetro key.

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Concluindo
- Utilizamos a biblioteca functools, por meio das operações de ordenação em Python para personalizar critérios de ordenação, uma habilidade essencial para manipulação eficiente de dados.

_4 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-collections-listas-e-tuplas

_8 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Ordenação completa e functools
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-collections-listas-e-tuplas/task/52950
- A ordenação completa em Python pode ser aprimorada com a biblioteca `functools`. Usando `functools.cmp_to_key`, podemos transformar uma função de comparação em uma chave de ordenação personalizada, permitindo ordenar listas de objetos complexos com critérios específicos, melhorando a flexibilidade e eficiência do código.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Compreendemos a importância das listas em Python, aprendendo a realizar operações básicas e avançadas de ordenação, integrando o uso de functools para criar soluções flexíveis e eficientes para organização de dados.
- O que vimos na aula de hoje

_4 imagem(ns) no slide._

### Slide 21

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

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 34_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 34

Questão 1

Como você adiciona um item ao final de uma lista em Python?

A) add()

B) append()

C) insert()

D) extend()

Resposta correta: B) append()

Comentários sobre a resposta correta: O método append() adiciona um item ao final da lista, aumentando sua extensão.

Questão 2

Qual método em Python remove o primeiro item de uma lista que corresponde a um valor específico?

A) pop()

B) delete()

C) remove()

D) discard()

Resposta correta: C) remove()

Comentários sobre a resposta correta: O método remove() elimina o primeiro item da lista que corresponde ao valor especificado.

## Outros documentos

_Fonte: AULA 34_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 34

Exemplo prático:

import functools

class Aluno:

def __init__(self, nome, nota):

self.nome = nome

self.nota = nota

def __repr__(self):

return f'{self.nome}: {self.nota}'

def comparar_alunos(a, b):

return (a.nota > b.nota) - (a.nota < b.nota)

alunos = [Aluno('Ana', 88), Aluno('Rafael', 92), Aluno('Paulo', 78)]

alunos_ordenados = sorted(alunos, key=functools.cmp_to_key(comparar_alunos))

print(alunos_ordenados)

Este código demonstra como usar functools.cmp_to_key para ordenar uma lista de objetos Aluno com base nas notas.
