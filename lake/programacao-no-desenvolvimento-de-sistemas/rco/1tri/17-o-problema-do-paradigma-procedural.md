---
titulo: "O problema do paradigma procedural"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 17
serie: 3
aula_rco: "Aula 17"
slides: 23
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/17-o-problema-do-paradigma-procedural/17-o-problema-do-paradigma-procedural.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/17-o-problema-do-paradigma-procedural/AULA 17_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/17-o-problema-do-paradigma-procedural/AULA 17_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# O problema do paradigma procedural

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- O problema do paradigma procedural
- Aula 17

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Explorar as limitações do paradigma procedural, identificando seus desafios na manutenção e escalabilidade de projetos.

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
- Discutimos conceitos básicos de programação, enfatizando a importância de compreender diferentes paradigmas para escolher a abordagem mais adequada a cada projeto, melhorando o código.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Carlos, um desenvolvedor recém-contratado, enfrenta dificuldades ao trabalhar em um legado de software estruturado no paradigma procedural.
- Ele nota que as constantes modificações no código geram efeitos colaterais indesejados e percebe a dificuldade em adicionar novas funcionalidades sem afetar o sistema existente.
- Carlos se questiona: "Existe uma maneira mais eficaz de organizar e expandir este código, minimizando os riscos e melhorando a manutenção?"

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Qual seria o primeiro passo para Carlos abordar a refatoração desse sistema?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Carlos deve começar avaliando as partes do sistema que poderiam se beneficiar da encapsulação em funções ou módulos, separando as responsabilidades e facilitando futuras alterações.

_4 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: Ao identificar e isolar as funcionalidades em blocos lógicos, Carlos pode reduzir a complexidade do código. Essa estratégia permite uma manutenção mais ágil e segura, além de preparar o terreno para a possível introdução de paradigmas mais modernos, como a programação orientada a objetos, que oferecem soluções mais robustas para os problemas identificados.

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- O paradigma procedural é uma abordagem de programação que enfatiza a execução de sequências de comandos ou funções para realizar tarefas. É um dos paradigmas mais antigos e fundamentais, baseado na ideia de chamar procedimentos (também conhecidos como funções ou sub-rotinas) para realizar operações específicas.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Finalidade
- A finalidade desse paradigma é estruturar um programa como uma coleção de procedimentos ou rotinas, cada um realizando uma parte específica da tarefa geral. Isso permite decompor problemas complexos em tarefas menores e mais gerenciáveis, facilitando o desenvolvimento e a compreensão do código.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Fragilidades
- No entanto, o paradigma procedural tem suas fragilidades, especialmente em projetos de grande escala. Uma delas é a dificuldade de manutenção do código, pois alterações em uma parte do programa podem exigir mudanças em várias outras partes. Além disso, a reutilização de código pode ser limitada, pois a abordagem procedural não incentiva tanto a encapsulação e abstração quanto outros paradigmas, como a programação orientada a objetos (POO).

_4 imagem(ns) no slide._

### Slide 12 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Exemplos

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual das seguintes opções é considerada uma fragilidade do paradigma procedural?
- (A) Encapsulamento de dados
- (B) Reutilização de código facilitada
- (C) Manutenção difícil em projetos grandes
- (D) Uso eficiente de memória
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Resposta correta
- Qual das seguintes opções é considerada uma fragilidade do paradigma procedural?
- (A) Encapsulamento de dados
- (B) Reutilização de código facilitada
- (C) Manutenção difícil em projetos grandes
- (D) Uso eficiente de memória
- Resposta Correta: (C) Manutenção difícil em projetos grandes.

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: A manutenção difícil em projetos grandes é uma fragilidade do paradigma procedural, pois a interdependência entre partes do código pode levar a uma complexidade crescente. Isso torna o rastreamento de bugs e a implementação de novas funcionalidades mais complicados, destacando a importância de abordagens mais modernas, como a programação orientada a objetos, que promovem melhor organização e reusabilidade do código.

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- Aprofundar no paradigma procedural revela desafios significativos em escalabilidade e manutenção, ressaltando a importância de abordagens mais modernas na engenharia de software.

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos

_5 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Dados da conta
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos/task/128376
- Utilizando Python 3.6.0 e PyCharm, esta aula foca em iniciar um novo projeto "oo" e explorar a orientação a objetos (OO), um avanço sobre o paradigma procedural usado anteriormente. Aprenderemos a organizar dados em dicionários para representar contas bancárias, movendo-nos em direção a encapsular essa lógica em funções.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Dados e comportamento
- 12 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos/task/128377
- Explorando a transição do paradigma procedural para a Orientação a Objetos (OO), discutimos problemas e limitações procedurais, como lembrar nomes de chaves e gerenciar funções de conta bancária (depositar, sacar, extrato). OO propõe unir dados e funcionalidades, mas a abordagem procedural apresenta desafios na organização e ligação entre dados e ações, destacando a fragilidade dessa ligação sem uma estrutura OO forte.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Exploramos as limitações do paradigma procedural, enfocando como a manutenção e a expansão de projetos se tornam complexas com esse modelo, e destacamos a necessidade de paradigmas mais flexíveis como a programação orientada a objetos.

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

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 17_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 17

Questão 1

Qual é uma consequência comum da utilização do paradigma procedural em projetos de grande escala?

a) Aumento da eficiência na execução do código.

b) Facilidade na implementação de novas funcionalidades.

c) Dificuldade na manutenção e no rastreamento de bugs.

d) Melhoria na reutilização de código entre diferentes projetos.

Resposta Correta: c) Dificuldade na manutenção e no rastreamento de bugs.

Comentário: A alternativa c é correta porque o paradigma procedural, ao enfatizar sequências de instruções e uso intensivo de variáveis globais, pode levar a um código interdependente e rígido, dificultando a manutenção e a introdução de mudanças sem efeitos colaterais indesejados.

Questão 2

Por que a reutilização de código pode ser limitada no paradigma procedural?

a) Devido ao encapsulamento eficiente de dados.

b) Por causa da abstração e herança nativas do paradigma.

c) Porque a lógica de programação é baseada em funções globais.

d) Devido à modularidade e ao baixo acoplamento entre funções.

Resposta Correta: c) Porque a lógica de programação é baseada em funções globais.

Comentário: Escolher c é adequado, já que no paradigma procedural, o código tende a ser organizado em torno de funções que operam em dados globais, o que pode reduzir a modularidade e a reutilização do código, pois as funções podem ser altamente dependentes do contexto específico do programa.

## Outros documentos

_Fonte: AULA 17_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 17

Este exemplo ilustra a abordagem procedural: definimos uma função para calcular a média e a chamamos a partir da função main. Embora eficaz para programas simples, essa estrutura pode se tornar difícil de gerenciar conforme o programa cresce.

Exemplo prático:

#include <stdio.h>

float calcular_media(int numeros[], int tamanho) {

int soma = 0;

for(int i = 0; i < tamanho; i++) {

soma += numeros[i];

}

return soma / (float)tamanho;

}

int main() {

int numeros[] = {10, 20, 30, 40, 50};

int tamanho = sizeof(numeros) / sizeof(numeros[0]);

float media = calcular_media(numeros, tamanho);

printf("A média é: %.2f\n", media);

return 0;

}
