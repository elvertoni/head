---
titulo: "de Strings em C"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 2
ordem_rco: 52
serie: 3
aula_rco: "Aula 52"
slides: 24
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/52-arrays-e-manipulacao-de-strings-em-c/52-arrays-e-manipulacao-de-strings-em-c.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/52-arrays-e-manipulacao-de-strings-em-c/AULA 52_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/52-arrays-e-manipulacao-de-strings-em-c/AULA 52_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# de Strings em C

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Arrays e Manipulação
- de Strings em C
- Aula 52

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Explorar como trabalhar com arrays e manipulação de strings em C. Veremos como declarar, inicializar e manipular arrays, além de entender as operações básicas com strings.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Dev-C++: Um IDE gratuito e leve para programação em C e C++, ótimo para iniciantes.
- OnlineGDB: Um compilador e depurador online para C, fácil de usar e permite compartilhar código.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Aprendemos sobre Entrada e Saída de Dados e Controle de Fluxo em C. Discutimos como obter dados do usuário, exibir informações e controlar o fluxo do programa usando estruturas condicionais e loops.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Ana está desenvolvendo um programa em C que precisa armazenar e manipular uma lista de nomes de estudantes. Ela quer saber como usar arrays para isso e como pode manipular as strings para realizar operações, como concatenação e comparação.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Como Ana pode declarar um array de strings em C e manipular essas strings para, por exemplo, comparar dois nomes?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Ana pode declarar um array de strings usando um array bidimensional de caracteres. Ela pode usar funções da biblioteca <string.h> para manipular essas strings, como strcmp para comparação e strcat para concatenação.

_4 imagem(ns) no slide._

> **Notas do apresentador:** Entender arrays e manipulação de strings permite que Ana crie programas mais complexos e eficientes. Saber comparar e concatenar strings é essencial para muitas aplicações, como ordenação de listas de nomes ou verificação de credenciais.

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Visão Geral dos Arrays e Strings
- Arrays são estruturas de dados que armazenam múltiplos valores do mesmo tipo. Strings em C são arrays de caracteres terminados por um caractere nulo ('\0').

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Um array é uma coleção de variáveis do mesmo tipo, acessadas por um índice. Strings são usadas para armazenar e manipular texto. Arrays e strings são fundamentais para organizar e processar dados sequenciais.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- Eles permitem o armazenamento e a manipulação de grandes volumes de dados de forma eficiente. Strings são cruciais para qualquer operação que envolva texto, desde a entrada de usuário até a formatação de dados.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Arrays são usados para armazenar listas de itens, como números ou nomes. Strings são usadas em praticamente todas as aplicações que interagem com texto, como interfaces de usuário, processamento de arquivos e comunicação em rede.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Utilize a plataforma https://www.onlinegdb.com/
- Vamos criar um programa que armazena uma lista de nomes e permite a comparação entre eles.

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Resultado da compilação
- Utilize a plataforma https://www.onlinegdb.com/

_5 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual a função da biblioteca <string.h> que é usada para comparar duas strings?
- A) strcat
- B) strcmp
- C) strlen
- D) strcpy
- Faça e apresente depois!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Qual a função da biblioteca <string.h> que é usada para comparar duas strings?
- A) strcat
- B) strcmp
- C) strlen
- D) Strcpy
- Resposta Correta: B) strcmp

_3 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Utilize a plataforma https://www.onlinegdb.com/

_6 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Utilize a plataforma https://www.onlinegdb.com/
- Modifique o código para permitir que o usuário insira um nome e verifique se ele está presente no array de nomes.

_5 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Utilize a plataforma https://www.onlinegdb.com/

_6 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Exploramos os conceitos de arrays e manipulação de strings em C. Aprendemos como declarar, inicializar e manipular arrays, e como utilizar funções da biblioteca <string.h> para trabalhar com strings.

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

_Fonte: AULA 52_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 52

Questão 1

Qual é a função usada para concatenar duas strings em C?

A) strcpy

B) strcat

C) strlen

D) strcmp

Resposta Correta: B) strcat

Comentário: A função strcat é usada para concatenar (juntar) duas strings.

Questão 2

Como você declara um array de 10 inteiros em C?

A) int array[10];

B) int array{10};

C) int array;

D) array int[10];

Resposta Correta: A) int array[10];

Comentário: A sintaxe correta para declarar um array de 10 inteiros em C é int array[10];.

## Outros documentos

_Fonte: AULA 52_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 52

Resumo Explicativo:

Arrays e manipulação de strings são conceitos fundamentais na programação em C. Arrays permitem armazenar múltiplos valores do mesmo tipo em uma única variável, enquanto strings são arrays de caracteres terminados por um caractere nulo. Esses conceitos são essenciais para gerenciar e manipular grandes quantidades de dados de maneira eficiente.

Estudo de Caso:

Imagine que você está desenvolvendo um sistema de gerenciamento de alunos para uma escola. Esse sistema precisa armazenar e manipular informações dos alunos, como nomes, idades e notas. Usaremos arrays para armazenar as informações e strings para os nomes dos alunos.

Vamos construir um programa que:

Armazene nomes de alunos em um array.

Permita a entrada e exibição de nomes.

Realize operações básicas de manipulação de strings, como comparação e busca.

Questões:

1- Liste e descreva os aspectos básicos dos arrays e strings em C.

Resposta Esperada: Arrays são coleções de elementos do mesmo tipo armazenados contiguamente na memória. Strings são arrays de caracteres terminados por um caractere nulo (\0).

2- Explique com suas próprias palavras como strings são manipuladas em C.

Resposta Esperada: Strings em C são manipuladas usando funções da biblioteca padrão, como strcpy para copiar strings, strlen para obter o comprimento, e strcmp para comparar strings. Essas funções permitem realizar operações básicas e avançadas em strings.

3- Resolva o seguinte problema: crie um programa que armazene cinco nomes de alunos e permita ao usuário buscar um nome específico, informando se ele foi encontrado.

#include <stdio.h>

#include <string.h>

int main() {

char nomes[5][50]; // Array de 5 strings

char nomeBusca[50];

int encontrado = 0;

// Inserindo nomes no array

for(int i = 0; i < 5; i++) {

printf("Digite o nome %d: ", i + 1);

scanf("%s", nomes[i]);

}

// Buscando um nome no array

printf("Digite o nome para buscar: ");

scanf("%s", nomeBusca);

for(int i = 0; i < 5; i++) {

if(strcmp(nomes[i], nomeBusca) == 0) {

encontrado = 1;

break;

}

}

if(encontrado) {

printf("Nome %s encontrado.\n", nomeBusca);

} else {

printf("Nome %s não encontrado.\n", nomeBusca);

}

return 0;

}

4- Identifique e explique as partes componentes do programa acima e como elas se relacionam.

Resposta Esperada: O programa possui:

Declaração de arrays para armazenar strings.

Entrada de dados do usuário para inserir nomes.

Loop para percorrer os nomes armazenados e comparar com o nome buscado.

Condicional para informar se o nome foi encontrado ou não.

5- Avalie a eficiência do programa acima. Como ele poderia ser melhorado para lidar com um número maior de alunos?

Resposta Esperada: O programa é eficiente para um pequeno número de alunos, mas para um número maior, pode ser necessário usar estruturas de dados dinâmicas ou otimizar a busca usando algoritmos como busca binária em um array ordenado.

6- Desenvolva um projeto que permita adicionar, buscar e remover alunos de um array, garantindo que o array esteja sempre ordenado alfabeticamente.

#include <stdio.h>

#include <string.h>

#define MAX_ALUNOS 5

void inserirAluno(char alunos[][50], int *numAlunos, char novoAluno[]) {

int i;

if (*numAlunos >= MAX_ALUNOS) {

printf("Número máximo de alunos atingido.\n");

return;

}

for (i = *numAlunos - 1; (i >= 0 && strcmp(alunos[i], novoAluno) > 0); i--) {

strcpy(alunos[i + 1], alunos[i]);

}

strcpy(alunos[i + 1], novoAluno);

(*numAlunos)++;

}

void exibirAlunos(char alunos[][50], int numAlunos) {

printf("Lista de alunos:\n");

for (int i = 0; i < numAlunos; i++) {

printf("%s\n", alunos[i]);

}

}

int buscarAluno(char alunos[][50], int numAlunos, char nome[]) {

for (int i = 0; i < numAlunos; i++) {

if (strcmp(alunos[i], nome) == 0) {

return i;

}

}

return -1;

}

void removerAluno(char alunos[][50], int *numAlunos, char nome[]) {

int index = buscarAluno(alunos, *numAlunos, nome);

if (index == -1) {

printf("Aluno não encontrado.\n");

return;

}

for (int i = index; i < *numAlunos - 1; i++) {

strcpy(alunos[i], alunos[i + 1]);

}

(*numAlunos)--;

}

int main() {

char alunos[MAX_ALUNOS][50];

int numAlunos = 0;

char nome[50];

int opcao;

while (1) {

printf("\n1. Adicionar Aluno\n2. Exibir Alunos\n3. Buscar Aluno\n4. Remover Aluno\n5. Sair\nEscolha uma opção: ");

scanf("%d", &opcao);

switch (opcao) {

case 1:

printf("Digite o nome do aluno: ");

scanf("%s", nome);

inserirAluno(alunos, &numAlunos, nome);

break;

case 2:

exibirAlunos(alunos, numAlunos);

break;

case 3:

printf("Digite o nome do aluno para buscar: ");

scanf("%s", nome);

if (buscarAluno(alunos, numAlunos, nome) != -1) {

printf("Aluno %s encontrado.\n", nome);

} else {

printf("Aluno %s não encontrado.\n", nome);

}

break;

case 4:

printf("Digite o nome do aluno para remover: ");

scanf("%s", nome);

removerAluno(alunos, &numAlunos, nome);

break;

case 5:

return 0;

default:

printf("Opção inválida.\n");

}

}

}
