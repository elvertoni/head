---
titulo: "Comparando Python com C"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 9
serie: 3
aula_rco: "Aula 09"
slides: 30
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/9-comparando-python-com-c/9-comparando-python-com-c.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/9-comparando-python-com-c/AULA 09_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Comparando Python com C

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Comparando Python com C
- Aula 09

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Conhecer as diferenças fundamentais e as aplicações práticas de Python e C, duas linguagens de programação.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Leituras Sugeridas: "A Byte of Python" para uma introdução amigável ao Python e "C Programming Absolute Beginner's Guide" para começar com C.
- IDE Online: Utilize o Repl.it (replit.com) ou o PythonAnywhere para Python e o JDoodle (jdoodle.com/c-online-compiler) para C, que são ambientes de desenvolvimento integrados online e permitem praticar sem necessidade de instalação local.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Aprendemos técnicas de refatoração para melhorar a legibilidade e manutenibilidade do código.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Pedro está preocupado com a transição e como as diferenças entre as linguagens podem afetar sua produtividade e a qualidade do projeto.
- Pedro é um desenvolvedor iniciante que sempre programou em Python devido à sua simplicidade e clareza…
- Enfrenta um desafio em seu novo emprego:
- um projeto de sistema embarcado que requer conhecimento em C, uma linguagem que ele nunca usou!

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Como Pedro pode aproveitar seu conhecimento em Python enquanto aprende C para o projeto de sistema embarcado?
- Quem sabe responde!
- https://i.pinimg.com/originals/ba/ca/88/baca8872f2ca15abdac0e8ca7b999a7c.gif

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Pedro pode começar identificando as semelhanças e diferenças entre Python e C, focando em estruturas de controle, tipos de dados e sintaxe.
- Ele deve praticar pequenos programas em C para se familiarizar com a linguagem.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Além disso, estudar sobre gerenciamento de memória e ponteiros será necessário, pois são conceitos importantes em C que não são tão presentes em Python.
- Integrar gradualmente o conhecimento de ambas as linguagens permitirá a Pedro entender quando e como aplicar cada uma delas efetivamente, aumentando sua versatilidade como desenvolvedor.
- https://dojo.bylearn.com.br/wp-content/uploads/2021/05/01-e1630594244238.png

_4 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: Esta decisão depende muito do contexto do projeto de João. Se a performance for crítica e ele estiver disposto a enfrentar uma curva de aprendizado mais acentuada, C pode ser uma boa escolha. Caso contrário, melhorar o código Python existente ou utilizar extensões escritas em C para operações críticas pode ser uma abordagem mais balanceada.

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Comparando Python com C
- Ao mergulhar no universo da programação, dois gigantes que você inevitavelmente encontrará são Python e C.
- Essas linguagens, embora sirvam a propósitos diferentes, formam a base de muitas tecnologias que usamos diariamente.
- Compreender suas diferenças e aplicações é fundamental para qualquer desenvolvedor, especialmente os iniciantes.

_5 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Python: A Linguagem Interpretada
- Python é uma linguagem de alto nível, interpretada e de script. Isso significa que o código escrito em Python é executado linha por linha por um interpretador, que traduz o código em linguagem de máquina em tempo real.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Python: A Linguagem Interpretada
- Python é famosa por sua sintaxe clara e legibilidade, permitindo aos desenvolvedores expressar conceitos complexos de forma concisa.
- Essa característica torna a Python extremamente flexível e fácil de usar, ideal para desenvolvimento rápido de aplicações, automação, análise de dados, e aprendizado de máquina.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Python: A Linguagem Interpretada
- # Imprime "Olá, mundo!"print("Olá, mundo!")

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- C: A Linguagem Compilada
- C, por outro lado, é uma linguagem de programação de baixo nível e compilada. Isto significa que o código C deve ser transformado (compilado) em linguagem de máquina pelo compilador antes de ser executado pelo computador. Este processo cria um arquivo executável que pode ser rodado diretamente.

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- C: A Linguagem Compilada
- C é conhecida por oferecer controle preciso sobre os recursos do sistema e memória, o que a torna ideal para desenvolvimento de sistemas operacionais, aplicativos de software que exigem alta performance e programação de hardware.

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- C: A Linguagem Compilada
- #include <stdio.h>
- int main() {
- // Imprime "Olá, mundo!"
- printf("Olá, mundo!\n"); return 0;
- }

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Interpretado X Compilado
- A principal diferença entre essas duas linguagens reside na forma como o código é executado. Enquanto Python é interpretado e oferece maior flexibilidade e rapidez no desenvolvimento, C é compilado, proporcionando maior controle e eficiência em termos de execução.

_4 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Finalidade e Utilização
- C é preferido para desenvolvimento de sistemas, aplicações que exigem alta performance, e programação embutida ou de sistemas, devido ao seu acesso direto ao hardware e gestão de memória.
- Python é frequentemente escolhido para desenvolvimento web, ciência de dados, e prototipagem rápida, graças à sua simplicidade e vasta biblioteca de pacotes.

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Escolha
- A escolha entre Python e C depende amplamente do projeto em questão, dos requisitos de desempenho e da familiaridade do desenvolvedor com a linguagem.
- Para aplicações rápidas e de alto nível, Python é geralmente o caminho a seguir. Para aplicações que necessitam de otimização de recursos e performance, C é a escolha certa.

_4 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual das seguintes afirmações melhor descreve a diferença entre Python e C em termos de execução?
- (A) Ambos Python e C são interpretados e executam o código linha por linha.
- (B) Python é compilado para código de máquina antes da execução, enquanto C é interpretado.
- (C) Python é interpretado, o que permite execução direta, enquanto C é compilado, necessitando de um passo adicional antes da execução.
- (D) C é executado diretamente pelo sistema operacional, enquanto Python precisa de uma JVM (Java Virtual Machine).
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual das seguintes afirmações melhor descreve a diferença entre Python e C em termos de execução?
- (A) Ambos Python e C são interpretados e executam o código linha por linha.
- (B) Python é compilado para código de máquina antes da execução, enquanto C é interpretado.
- (C) Python é interpretado, o que permite execução direta, enquanto C é compilado, necessitando de um passo adicional antes da execução.
- (D) C é executado diretamente pelo sistema operacional, enquanto Python precisa de uma JVM (Java Virtual Machine).
- Resposta Correta: (C) Python é interpretado, o que permite execução direta, enquanto C é compilado, necessitando de um passo adicional antes da execução.

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: A alternativa c) é correta porque captura a essência das diferenças de execução entre Python e C. Python, sendo interpretado, permite que o desenvolvedor veja os resultados do código imediatamente após sua escrita, o que é ideal para desenvolvimento rápido e testes. C, sendo compilado, passa por um processo de compilação que transforma o código fonte em código de máquina antes de ser executado, o que pode levar a uma execução mais rápida e eficiente

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- Exploramos as diferenças fundamentais entre Python, uma linguagem interpretada, e C, uma linguagem compilada, destacando como essas características influenciam a escolha para diferentes projetos.

_5 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-introducao-a-linguagem

_5 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- Python vs C
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-introducao-a-linguagem/task/24656
- Python é uma linguagem de alto nível, interpretada, com uma sintaxe clara e concisa, ideal para desenvolvimento rápido e projetos de data science. C é uma linguagem compilada, oferecendo alto desempenho e controle sobre sistemas e hardware, usada em aplicações que demandam eficiência.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Interpretado vs Compilado
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-introducao-a-linguagem/task/24657
- Python é uma linguagem de alto nível, interpretada, com uma sintaxe clara e concisa, ideal para desenvolvimento rápido e projetos de data science. C é uma linguagem compilada, oferecendo alto desempenho e controle sobre sistemas e hardware, usada em aplicações que demandam eficiência.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Na aula de hoje, mergulhamos nas distinções entre Python e C, focando na compilação versus interpretação e como isso afeta a execução e o desenvolvimento de softwares.
- Na próxima aula, desenvolveremos um jogo da forca, desde a montagem da infraestrutura básica até a implementação do loop principal do jogo.

_5 imagem(ns) no slide._

### Slide 27

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

### Slide 28

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 29

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 30

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 09_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 09

Questão 1

Qual das seguintes afirmações melhor descreve Python?

a) É uma linguagem de programação compilada, ideal para sistemas operacionais.

b) É uma linguagem de baixo nível usada principalmente para programação de hardware.

c) É uma linguagem de programação interpretada, conhecida por sua facilidade de uso.

d) É uma linguagem que não suporta programação orientada a objetos.

Resposta correta: c)

Comentário sobre a resposta correta: Python é uma linguagem de alto nível e interpretada, conhecida por sua clara sintaxe e por promover um desenvolvimento rápido, sendo uma escolha popular para análise de dados, aprendizado de máquina e desenvolvimento web.

Questão 2

O que caracteriza uma linguagem de programação compilada, como C?

a) Execução linha por linha pelo interpretador.

b) Geração de um arquivo executável antes da execução.

c) Flexibilidade e rapidez no desenvolvimento de protótipos.

d) Ausência de controle sobre a gestão de memória.

Resposta correta: b)

Comentário sobre a resposta correta: As linguagens compiladas, como C, são transformadas em código de máquina pelo compilador, gerando um arquivo executável. Isso permite uma execução mais eficiente e dá ao desenvolvedor controle preciso sobre recursos do sistema e gestão de memória.
