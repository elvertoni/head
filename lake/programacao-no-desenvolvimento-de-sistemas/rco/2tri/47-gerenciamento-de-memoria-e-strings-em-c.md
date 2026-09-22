---
titulo: "Gerenciamento de Memória e Strings em C"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 2
ordem_rco: 47
serie: 3
aula_rco: "Aula 47"
slides: 28
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/47-gerenciamento-de-memoria-e-strings-em-c/47-gerenciamento-de-memoria-e-strings-em-c.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/47-gerenciamento-de-memoria-e-strings-em-c/AULA 47_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/47-gerenciamento-de-memoria-e-strings-em-c/AULA 47_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Gerenciamento de Memória e Strings em C

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Gerenciamento de Memória e Strings em C
- Aula 47

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Conhecer como o C gerencia a memória e manipula strings, aprendendo técnicas fundamentais para criar programas.

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
- Aprendemos sobre funções e modularização em C. Dividimos nosso código em funções para melhorar a organização e facilitamos a manutenção ao modularizar o código em diferentes arquivos.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Maria está desenvolvendo um programa em C que manipula grandes volumes de texto. Ela precisa garantir que o uso de memória seja eficiente e que a manipulação de strings seja robusta e segura.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Duas Soluções Possíveis:
- 1- Utilizar funções como malloc, free, strcpy e strcat para gerenciar memória dinamicamente e manipular strings com segurança.
- 2- Declarar todas as strings como arrays de caracteres estáticos grandes, sem gerenciamento dinâmico de memória.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Correta: A alocação dinâmica de memória permite que o programa use apenas a quantidade necessária de memória, prevenindo desperdício e potencializando a eficiência.
- Falsa: O uso de arrays estáticos pode desperdiçar memória e não é escalável para grandes volumes de texto, levando a possíveis erros e limitações de capacidade.

_3 imagem(ns) no slide._

> **Notas do apresentador:** Análise de Consequências: Ao usar funções, João reduz a repetição de código e melhora a clareza do seu programa. A modularização facilita a manutenção e a atualização do sistema, permitindo que ele faça alterações em partes específicas do código sem afetar o programa inteiro.

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Gerenciamento de Memória e Strings
- O gerenciamento de memória em C é crucial para criar programas eficientes. Strings são arrays de caracteres terminados em \0. Compreender como alocar, acessar e liberar memória dinamicamente é essencial para manipular strings de forma eficaz.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Gerenciamento de memória envolve alocar (malloc), realocar (realloc) e liberar (free) memória durante a execução do programa. Manipulação de strings inclui operações como cópia (strcpy), concatenação (strcat) e comparação (strcmp).

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importancia
- Gerenciar memória e strings corretamente previne problemas como vazamentos de memória, falhas de segmentação e corrupção de dados, garantindo a eficiência e robustez do programa.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Em aplicações reais, como editores de texto, servidores web e bancos de dados, a manipulação eficiente de strings e o gerenciamento adequado de memória são fundamentais para o desempenho e a confiabilidade.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Utilize a plataforma https://www.onlinegdb.com/

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Utilize a plataforma https://www.onlinegdb.com/

_5 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resultado da compilação
- Utilize a plataforma https://www.onlinegdb.com/

_5 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Mais Exemplos
- Acesse o arquivo Saiba Mais:

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Liste as funções básicas usadas para gerenciamento de memória em C.
- Escolhendo alguém para responder essa questão!

_5 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Resposta Esperada: malloc, realloc, free.

_4 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: O método sort() é usado para ordenar uma lista no local, modificando a lista original.

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Utilize a plataforma https://www.onlinegdb.com/

_6 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta correta: A imutabilidade das tuplas garante que os dados não sejam alterados acidentalmente, proporcionando segurança.

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Utilize a plataforma https://www.onlinegdb.com/
- Analise o código anterior e explique como a memória está sendo gerenciada.

_5 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta correta: A imutabilidade das tuplas garante que os dados não sejam alterados acidentalmente, proporcionando segurança.

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Utilize a plataforma https://www.onlinegdb.com/
- O código aloca memória para um array de 5 inteiros, preenche o array com valores, e depois libera a memória alocada.

_5 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta correta: A imutabilidade das tuplas garante que os dados não sejam alterados acidentalmente, proporcionando segurança.

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/introducao-a-programacao-com-c-parte-2

_6 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Itens da aula 5 – ponteiros e endereços
- 34 minutos
- Link para tarefa: https://cursos.alura.com.br/course/introducao-a-programacao-com-c-parte-2/task/8955
- Ponteiros são variáveis que armazenam endereços de memória, permitindo acesso e manipulação direta de dados armazenados em outros locais. Eles são fundamentais para a eficiência e flexibilidade na programação em C, especialmente para alocação dinâmica de memória e manipulação de arrays e strings.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Vimos como gerenciar a memória e manipular strings em C, aprendendo a usar funções como malloc, free, strcpy e strcat para criar programas eficientes e seguros.

_4 imagem(ns) no slide._

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

_Fonte: AULA 47_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 47

Questão 1

Qual das seguintes funções é usada para liberar a memória alocada dinamicamente em C?

A) malloc

B) free

C) alloc

D) release

Resposta Correta: B) free

Comentário: A função free é usada para liberar a memória que foi alocada dinamicamente. malloc é usada para alocar memória, enquanto alloc e release não são funções padrão em C.

Questão 2

O que acontece se você tentar acessar uma área de memória após ter chamado free nessa memória?

A) Nada acontece, você pode acessar normalmente.

B) O programa sempre falha imediatamente.

C) Pode causar comportamento indefinido, incluindo possíveis falhas.

D) A memória é automaticamente realocada.

Resposta Correta: C) Pode causar comportamento indefinido, incluindo possíveis falhas.

Comentário: Acessar memória após liberá-la com free pode levar a comportamento indefinido, o que pode incluir falhas de segmentação, corrupção de dados ou outros problemas.

## Outros documentos

_Fonte: AULA 47_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 47

Resumo Explicativo:

O gerenciamento de memória e a manipulação de strings são aspectos essenciais da programação em C. O gerenciamento eficiente da memória é crucial para evitar vazamentos e otimizar o uso dos recursos do sistema. A manipulação de strings, que são arrays de caracteres terminados em \0, é fundamental para muitas aplicações, desde processamento de texto até comunicação de dados.

Estudo de Caso:

João é um estudante de programação que está desenvolvendo um editor de texto básico em C. Ele precisa garantir que seu programa seja eficiente em termos de uso de memória e que possa manipular strings de forma eficaz. João utiliza o OnlineGDB para escrever e testar seu código. Ele enfrenta desafios como alocar e liberar memória dinamicamente e manipular strings de maneira segura.

João está trabalhando em uma função que lê uma linha de texto do usuário e a armazena em memória dinâmica. Ele também precisa implementar funções para concatenar duas strings e liberar a memória alocada após o uso. João sabe que um gerenciamento inadequado da memória pode levar a vazamentos de memória, enquanto uma manipulação inadequada de strings pode causar erros de segmentação.

Questões:

1- Liste três funções usadas para gerenciamento de memória dinâmica em C.

Resposta Esperada: malloc, calloc, free.

2-Explique por que é importante liberar a memória alocada dinamicamente após o uso.

Resposta Esperada: Liberar a memória alocada dinamicamente é importante para evitar vazamentos de memória, que podem esgotar os recursos do sistema e levar a falhas ou degradação de desempenho.

3- Escreva um programa em C que aloque dinamicamente memória para armazenar uma string, copie uma string de origem para esta memória e depois libere a memória.

#include <stdio.h>

#include <stdlib.h>

#include <string.h>

int main() {

char origem[] = "Hello, World!";

char *destino;

destino = (char *)malloc(strlen(origem) + 1);

if (destino == NULL) {

printf("Erro de alocação de memória.\n");

return 1;

}

strcpy(destino, origem);

printf("String copiada: %s\n", destino);

free(destino);

return 0;

}

4- Analise o seguinte código e explique o que está errado com o gerenciamento de memória.

char* str = (char*)malloc(10);

strcpy(str, "Hello");

free(str);

strcpy(str, "World");

Resposta Esperada: Após chamar free(str), a memória apontada por str é liberada. Qualquer tentativa de acessar ou modificar essa memória pode levar a comportamento indefinido, incluindo falhas de segmentação.

5- Avalie as implicações de não liberar a memória alocada dinamicamente em um programa de longo prazo.

Resposta Esperada: Não liberar memória alocada dinamicamente pode causar vazamentos de memória, onde a memória não é devolvida ao sistema, eventualmente esgotando os recursos disponíveis e levando a falhas do sistema ou degradação significativa do desempenho.

6- Desenvolva um programa que leia múltiplas linhas de texto do usuário, armazene-as dinamicamente em um array de strings e depois exiba todas as linhas. Certifique-se de liberar toda a memória alocada no final.

#include <stdio.h>

#include <stdlib.h>

#include <string.h>

int main() {

char *linhas[5];

char buffer[100];

int i;

for (i = 0; i < 5; i++) {

printf("Digite a linha %d: ", i + 1);

fgets(buffer, sizeof(buffer), stdin);

buffer[strcspn(buffer, "\n")] = '\0'; // Remove o newline

linhas[i] = (char *)malloc(strlen(buffer) + 1);

if (linhas[i] == NULL) {

printf("Erro de alocação de memória.\n");

return 1;

}

strcpy(linhas[i], buffer);

}

printf("\nLinhas digitadas:\n");

for (i = 0; i < 5; i++) {

printf("%s\n", linhas[i]);

free(linhas[i]);

}

return 0;

}
