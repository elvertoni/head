---
titulo: "Ordenação total"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 2
ordem_rco: 42
serie: 3
aula_rco: "Aula 42"
slides: 23
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/42-ordenacao-total/42-ordenacao-total.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/42-ordenacao-total/AULA 42_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/42-ordenacao-total/AULA 42_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Ordenação total

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Ordenação total
- Aula 42

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Relembrar a ordenação eficiente de dados utilizando Python, com foco na ordenação total e no uso da biblioteca functools para personalizar nossos critérios de ordenação.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Replit: Um IDE online que suporta Python e outras linguagens, permitindo testar código em tempo real sem instalações complicadas.
- PyCharm Community Edition: Um ambiente de desenvolvimento gratuito que oferece suporte excelente para Python, ideal para experimentar scripts de ordenação.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- No trimestre anterior…
- Estudamos sobre a ordenação de dados, que é uma operação fundamental na programação, utilizada em diversos cenários para organizar e processar informações de forma eficiente.
- O Python oferece diversas ferramentas para realizar essa tarefa, desde métodos simples até algoritmos complexos com alta performance.

_4 imagem(ns) no slide._

### Slide 6

- Para pensarmos juntos!
- Carlos está organizando uma lista de contatos para um aplicativo e precisa garantir que os nomes sejam listados em ordem alfabética, mas também que nomes com acentos sejam tratados corretamente.
- DESENVOLVIMENTO DE SISTEMAS

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Como Carlos pode implementar uma ordenação total que considere caracteres especiais em Python?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Carlos pode usar o módulo functools e o método cmp_to_key para criar uma função de comparação personalizada que trate adequadamente os caracteres acentuados.

_4 imagem(ns) no slide._

> **Notas do apresentador:** A ordenação total com critérios personalizados assegura que os dados sejam consistentes e corretamente acessíveis, melhorando a usabilidade do aplicativo de Carlos e evitando confusões com a ordenação de caracteres especiais.

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Entendendo a Ordenação Total
- No Python, isso é frequentemente realizado usando funções embutidas que permitem comparar e ordenar dados de maneira eficiente e consistente.
- É o processo de organizar todos os elementos de uma coleção de dados em uma sequência específica, geralmente ascendente ou descendente.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Por Que Ordenar?
- facilita a busca e recuperação de informações, ajuda na visualização de dados e na geração de relatórios, e é crucial para a eficiência de algoritmos que dependem de dados previamente ordenados, como a busca binária.
- Uma coleção ordenada é mais fácil de gerenciar e analisar.
- Ordenar dados é fundamental por várias razões:

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Métodos de Ordenação em Python
- Python oferece várias maneiras de ordenar coleções, como a função sorted() e o método list.sort().
- Ambos permitem ordenar qualquer iterável ou lista, respectivamente, e podem ser personalizados com parâmetros para definir critérios específicos de ordenação, como a ordem reversa ou ordenação por um atributo específico de objetos complexos.
- https://cdn.awsli.com.br/2500x2500/78/78037/produto/45589392/9996d20280.jpg

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Explorando Funcionalidades Avançadas com functools
- O módulo functools oferece a função cmp_to_key, que permite converter uma função de comparação personalizada em uma chave de ordenação.
- Isso é útil quando precisamos de controles de ordenação que não são diretamente suportados pelos parâmetros padrão de sorted() ou list.sort().

_4 imagem(ns) no slide._

### Slide 13 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- DESENVOLVIMENTO DE SISTEMAS
- Exemplos
- Acesse o arquivo Saiba Mais

_7 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual método pode ser usado para converter uma função de comparação em uma chave de ordenação em Python?
- (A) functools.wrap()
- (B) functools.order_by()
- (C) functools.cmp_to_key()
- (D) functools.sort_key()
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Qual método pode ser usado para converter uma função de comparação em uma chave de ordenação em Python?
- (A) functools.wrap()
- (B) functools.order_by()
- (C) functools.cmp_to_key()
- (D) functools.sort_key()
- Resposta correta: (C) functools.cmp_to_key()

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: functools.cmp_to_key() transforma uma função de comparação em uma chave que pode ser usada para ordenar listas.

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Concluindo
- Realizar as ordenações completas em Python amplia a nossa capacidade de manipular e apresentar dados de maneira eficaz!

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-collections-listas-e-tuplas

_8 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: functools.cmp_to_key() transforma uma função de comparação em uma chave que pode ser usada para ordenar listas.

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Ordenação completa e functools
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-collections-listas-e-tuplas/task/52950
- A ordenação completa em Python pode ser aprimorada com o módulo functools, usando cmp_to_key para converter funções de comparação em chaves de ordenação. Isso permite personalizar a ordenação com critérios complexos, adaptando-a a necessidades específicas de maneira eficiente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Revisitamos a ordenação total utilizando Python e functools, uma técnica vital para qualquer desenvolvedor trabalhar com coleções de dados de forma eficiente.

_4 imagem(ns) no slide._

### Slide 20

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

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

## Atividade

_Fonte: AULA 42_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 42

Questão 1

O que sorted() faz em Python?

A) Inverte uma lista

B) Ordena uma lista permanentemente

C) Retorna uma nova lista ordenada

D) Remove elementos duplicados

Resposta correta: C) Retorna uma nova lista ordenada

Questão 2

Qual é o propósito de usar parâmetros personalizados em funções de ordenação?

A) Aumentar a velocidade de execução

B) Ignorar a ordenação

C) Adaptar a ordenação a critérios específicos

D) Simplificar o código

Resposta correta: C) Adaptar a ordenação a critérios específicos

## Outros documentos

_Fonte: AULA 42_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 42

Exemplo prático:

from functools import cmp_to_key

def compare_items(a, b):

return (a.lower() > b.lower()) - (a.lower() < b.lower())

strings = ['banana', 'Apple', 'cherry']

sorted_strings = sorted(strings, key=cmp_to_key(compare_items))

print(sorted_strings)
