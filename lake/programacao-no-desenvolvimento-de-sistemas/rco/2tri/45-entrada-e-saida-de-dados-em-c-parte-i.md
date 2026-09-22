---
titulo: "Entrada e Saída de Dados em C"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 2
ordem_rco: 45
serie: 3
aula_rco: "Aula 45"
slides: 28
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/45-entrada-e-saida-de-dados-em-c-parte-i/45-entrada-e-saida-de-dados-em-c-parte-i.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/45-entrada-e-saida-de-dados-em-c-parte-i/AULA 45_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/45-entrada-e-saida-de-dados-em-c-parte-i/AULA 45_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Entrada e Saída de Dados em C

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Entrada e Saída de Dados em C
- Aula 45

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Conhecer como os programas em C manipulam dados através de entrada e saída, e como as variáveis armazenam essas informações na memória.

_6 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Code::Blocks: Um IDE gratuito e open source que suporta a linguagem C. Ele é ideal para iniciantes devido à sua simplicidade e ao conjunto de ferramentas de depuração integradas.
- GCC Compiler: O compilador GNU C é amplamente usado na programação em C, essencial para transformar o código escrito em programas executáveis.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Exploramos arrays e controle de fluxo em C, fundamentais para estruturar lógicas complexas em programas. Esses conceitos são a base para hoje, onde expandimos para entrada/saída e manipulação de memória.

_3 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Mateus está tentando coletar dados do usuário em seu programa C para calcular médias, mas encontra problemas em armazenar e recuperar esses dados corretamente.

_3 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Como Mateus pode eficientemente coletar e armazenar dados de entrada em variáveis para posterior cálculo e saída?
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Mateus deve utilizar funções de entrada como scanf() para coletar dados e armazená-los em variáveis previamente definidas, garantindo que os tipos de dados correspondam aos esperados pelas variáveis.

_3 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- A correta manipulação de entrada e saída em C permite que programas interajam de forma eficaz com o usuário, enquanto a gestão adequada da memória assegura que os dados sejam armazenados e acessados sem erros.

_3 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Dominando as Funções Básicas de I/O em C
- Em C, as funções de entrada e saída são essenciais para qualquer interação do programa com o usuário. A função scanf() é usada para capturar dados digitados no teclado, enquanto printf() é usada para exibir informações na tela.

_3 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Dominando as Funções Básicas de I/O em C
- Essas funções permitem que os programas recebam e processem dados do usuário, e então apresentem os resultados das operações realizadas. Entender essas funções é o primeiro passo para criar programas interativos.

_3 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Variáveis: Armazenando Dados Eficientemente
- Variáveis são fundamentais em qualquer linguagem de programação, atuando como contêineres para armazenar dados que podem ser usados e modificados pelo programa.

_3 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Variáveis: Armazenando Dados Eficientemente
- Em C, cada variável possui um tipo que define o tamanho da memória que ela ocupa e o tipo de dados que pode armazenar, como int para números inteiros, float para números decimais, e char para caracteres. A correta declaração e inicialização de variáveis são importante para a manipulação eficaz dos dados.

_3 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Gerenciamento de Memória em C
- C oferece controle detalhado sobre o gerenciamento de memória, o que é uma poderosa vantagem e também uma complexidade adicional. Entender como as variáveis são armazenadas na memória e como essa memória é gerenciada é vital, especialmente quando se trabalha com arrays e strings, que são coleções de variáveis. A alocação dinâmica de memória usando funções como malloc() e free() permite criar aplicações mais flexíveis e eficientes.

_3 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- I/O em Ação: Aplicações Práticas
- Para ilustrar a aplicação prática de entrada e saída, consideramos um exemplo onde um programa em C solicita ao usuário que insira suas idades e então calcula e exibe a média. Este exemplo não só reforça o uso de scanf() e printf(), mas também mostra como processar e manipular dados de entrada para produzir uma saída útil.

_3 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Sincronizando Variáveis com Entrada/Saída
- A eficácia com que um programa lida com variáveis determina como os dados de entrada são coletados e os resultados exibidos. Neste contexto, discutimos como as variáveis interagem com funções de entrada e saída para armazenar temporariamente os dados do usuário, processá-los e, em seguida, exibir os resultados. Este processo é importante para o desenvolvimento de programas que não apenas executam cálculos, mas também interagem de forma significativa com o usuário.

_3 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Exemplos
- Arquivo Saiba mais com exemplo

_3 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual função em C é utilizada para ler dados do teclado?
- A) printf()
- B) scanf()
- C) print()
- D) scan()
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Qual função em C é utilizada para ler dados do teclado?
- A) printf()
- B) scanf()
- C) print()
- D) scan()
- Resposta correta: B) scanf()

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta correta: A função scanf() é usada para ler dados formatados do teclado, permitindo que o programa colete entradas diretamente dos usuários.

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Concluindo
- Hoje, abordamos como os programas em C processam entrada e saída e como as variáveis são essenciais para armazenar e manipular dados, preparando-os para desafios mais avançados em programação.

_3 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/introducao-a-programacao-com-c-parte-1

_5 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Variáveis e memória
- 3 minutos
- Link para tarefa: https://cursos.alura.com.br/course/introducao-a-programacao-com-c-parte-1/task/8868
- Variáveis em C são usadas para armazenar informações que podem ser manipuladas durante a execução de um programa. Elas ocupam espaço na memória, com cada tipo de dado (como int, float, char) usando uma quantidade específica de memória. Entender isso é crucial para gerenciar eficientemente os recursos do sistema.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Trabalhando com casas decimais
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/introducao-a-programacao-com-c-parte-1/task/8869
- Trabalhar com casas decimais em C geralmente envolve o uso de tipos de dados como `float` ou `double` para representar números com frações. Ao imprimir esses valores, funções como `printf()` permitem especificar a quantidade de casas decimais usando formatadores, como `%.2f` para duas casas decimais, garantindo precisão na apresentação dos dados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprofundamos nosso conhecimento em entrada e saída em C, essencial para desenvolver interações dinâmicas em programas e entender como os dados são gerenciados dentro de um computador.

_3 imagem(ns) no slide._

### Slide 25

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

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 28

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

## Atividade

_Fonte: AULA 45_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 45

Questão 1

Qual função é usada em C para imprimir dados na tela?

A) output()

B) print()

C) printf()

D) put()

Resposta correta: C) printf()

Comentários sobre a resposta correta: A função printf() é amplamente usada em C para imprimir dados na tela, permitindo a formatação de string, números e outros tipos de dados.

Questão 2

Como você pode declarar uma variável para armazenar um número inteiro em C?

A) int num;

B) integer num;

C) num int;

D) dec num;

Resposta correta: A) int num;

Comentários sobre a resposta correta: Em C, a declaração de uma variável inteira é feita com o especificador de tipo int seguido pelo nome da variável, neste caso, num.

## Outros documentos

_Fonte: AULA 45_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 45

Exemplo prático:

#include <stdio.h>

int main() {

int idade;

printf("Digite sua idade: ");

scanf("%d", &idade);

printf("Você tem %d anos.\n", idade);

return 0;

}

Este exemplo simples ilustra como coletar um dado de entrada do usuário e imediatamente fornecer uma saída, aplicando conceitos de variáveis e manipulação de memória.
