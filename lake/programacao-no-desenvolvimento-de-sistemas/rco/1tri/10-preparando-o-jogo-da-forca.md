---
titulo: "Preparando o jogo da forca"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 10
serie: 3
aula_rco: "Aula 10"
slides: 26
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/10-preparando-o-jogo-da-forca/10-preparando-o-jogo-da-forca.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/10-preparando-o-jogo-da-forca/AULA 10_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/10-preparando-o-jogo-da-forca/AULA 10_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Preparando o jogo da forca

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Preparando o jogo da forca
- Aula 10

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Vamos começar a desenvolver o jogo da forca, começando pela criação da estrutura básica e avançando até a implementação do ciclo principal do jogo.

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
- Anteriormente, exploramos os conceitos básicos de Python, focando em variáveis, estruturas de controle e funções.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Ele está empolgado, mas também um pouco perdido sobre como estruturar o código de forma eficiente e como criar um loop de jogo que seja tanto funcional quanto divertido…
- E se pergunta: "Como posso organizar meu código para que o jogo da forca funcione bem e seja fácil de entender e modificar?"
- João, um desenvolvedor iniciante, decidiu criar seu primeiro jogo, o jogo da forca, usando Python.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Qual a melhor forma de João começar a estruturar o loop principal do seu jogo da forca?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- João deve começar definindo a lógica principal do jogo em um loop while, mantendo-o rodando enquanto o jogador ainda tem tentativas restantes e a palavra não foi completamente adivinhada. Dentro desse loop, ele pode gerenciar a entrada do jogador, atualizar o estado do jogo e fornecer feedback.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Ao manter o código organizado em funções específicas para cada tarefa, João tornará seu jogo mais modular e fácil de entender.
- Esta abordagem não só facilita o desenvolvimento inicial, mas também simplifica a manutenção e a introdução de novas funcionalidades no futuro.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Introdução
- Preparar um jogo da forca, ajustar sua infraestrutura e implementar o game loop são passos essenciais no desenvolvimento de jogos, especialmente para iniciantes. Vamos entender cada uma dessas etapas de forma simplificada, ideal para quem está começando no mundo da programação.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Jogo da forca
- A cada letra incorreta, uma parte do desenho da forca é adicionada. O objetivo é acertar a palavra antes que o desenho da forca se complete.
- O jogo da forca é um clássico jogo de adivinhação de palavras, onde o jogador tenta descobrir uma palavra oculta, adivinhando as letras que ela contém.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Preparando o Jogo da Forca
- A infraestrutura de um jogo da forca pode ser tão simples quanto uma lista de palavras em código e um meio de capturar entradas do usuário.
- Esta etapa envolve definir as regras do jogo, escolher as palavras ou temas e decidir como o jogador interage com o jogo.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Ajustando a Infraestrutura
- Organização do código
- Configuração do ambiente de desenvolvimento
- Definição da estrutura de pastas do projeto
- A escolha de um IDE (Ambiente de Desenvolvimento Integrado)
- e a preparação de qualquer biblioteca de código necessária!
- A infraestrutura é a base onde o jogo será construído!
- Isso inclui:

_7 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Implementando o Game Loop
- O game loop é o coração de qualquer jogo, o ciclo contínuo que mantém o jogo em execução. Ele verifica as entradas do usuário, atualiza o estado do jogo e renderiza o jogo na tela. Para o jogo da forca, isso significa verificar se a letra inserida pelo jogador faz parte da palavra, atualizar o desenho da forca conforme necessário e determinar se o jogo terminou.

_4 imagem(ns) no slide._

### Slide 15 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Implementando o Game Loop
- Quer um exemplo simples de como isso pode ser implementado em Python? Clique em “SAIBA MAIS!”

_4 imagem(ns) no slide._

> **Notas do apresentador:** Ao desenvolver um jogo como o da forca, entender esses conceitos e saber como aplicá-los é fundamental. Isso não apenas facilita o processo de desenvolvimento, mas também ajuda a criar uma base sólida de conhecimento para projetos mais complexos no futuro.

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual é a função do game loop no desenvolvimento do jogo da forca?
- (A) Gerar palavras secretas aleatoriamente.
- (B) Atualizar a interface gráfica do jogo.
- (C) Checar entradas do usuário e atualizar o estado do jogo.
- (D) Compilar o código do jogo para diferentes plataformas.
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual é a função do game loop no desenvolvimento do jogo da forca?
- (A) Gerar palavras secretas aleatoriamente.
- (B) Atualizar a interface gráfica do jogo.
- (C) Checar entradas do usuário e atualizar o estado do jogo.
- (D) Compilar o código do jogo para diferentes plataformas.
- Resposta Correta: (C) Checar entradas do usuário e atualizar o estado do jogo.

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: A alternativa c é correta porque encapsula a essência de um game loop no contexto do jogo da forca. O loop do jogo é responsável por manter o jogo rodando, processando entradas do usuário (como palpites de letras), atualizando o estado do jogo (letras acertadas, número de tentativas restantes), e determinando quando o jogo termina, seja por vitória ou derrota. Este conceito é fundamental para a estruturação lógica de qualquer jogo interativo.

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- Este conteúdo demonstrou como estruturar um jogo da forca, desde preparar a base até implementar um loop que mantém o jogo ativo.

_5 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem

_5 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Ajustando a infraestrutura
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem/task/25097
- Ajustar a infraestrutura envolve configurar o ambiente de desenvolvimento, definir a estrutura do código, e preparar as ferramentas necessárias para construir o jogo da forca, garantindo uma base sólida para o desenvolvimento eficaz e organizado do projeto.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Game Loop
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem/task/25098
- O game loop é o ciclo contínuo que mantém o jogo rodando, processando entradas do usuário, atualizando o estado do jogo e renderizando a saída na tela, essencial para a interatividade e dinamismo de jogos como o da forca.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Nesta aula, aprendemos a desenvolver a infraestrutura para um jogo da forca em Python, desde a preparação inicial até a implementação do game loop.
- Na próxima aula, iremos
- manipular strings em Python.

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

_Fonte: AULA 10_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 10

Questão 1

Qual etapa é essencial antes de iniciar o desenvolvimento do game loop no jogo da forca?

a) Selecionar um banco de dados para armazenar as palavras.

b) Ajustar a infraestrutura, incluindo a definição de variáveis e estruturas de controle.

c) Publicar a primeira versão do jogo.

d) Desenhar os gráficos do jogo.

Resposta Correta: b) Ajustar a infraestrutura, incluindo a definição de variáveis e estruturas de controle.

Comentário: A opção b é correta porque, antes de entrar no game loop, é crucial ter uma base sólida, o que inclui a preparação da infraestrutura do código. Isso envolve definir as variáveis principais, estruturas de controle e entender como o jogo funcionará, elementos essenciais para o desenvolvimento organizado e eficiente.

Questão 2

O que o game loop permite em um jogo da forca?

a) Alterar automaticamente as palavras secretas após cada jogo.

b) Conectar o jogo a uma base de dados online.

c) Manter o jogo em execução, processando entradas e atualizando o estado do jogo.

d) Aumentar a dificuldade do jogo progressivamente.

Resposta Correta: c) Manter o jogo em execução, processando entradas e atualizando o estado do jogo.

Comentário: A alternativa c é a correta porque captura a função principal do game loop: manter o jogo funcionando continuamente. Ele é o ciclo que repete a verificação de entradas (como letras digitadas pelo usuário), atualiza o estado do jogo (verifica se a letra está correta ou não) e decide se o jogo continua ou termina.

## Outros documentos

_Fonte: AULA 10_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 10

Exemplo 1: exemplo de game loop implementado no Python.

palavra_secreta = "girafa"

letras_acertadas = ["_", "_", "_", "_", "_", "_"]

tentativas = 6

while tentativas > 0 and "_" in letras_acertadas:

palpite = input("Digite uma letra: ").lower()

if palpite in palavra_secreta:

index = 0

for letra in palavra_secreta:

if palpite == letra:

letras_acertadas[index] = letra

index += 1

else:

tentativas -= 1

print(f"Você tem {tentativas} tentativas restantes.")

print(" ".join(letras_acertadas))

if "_" not in letras_acertadas:

print("Parabéns, você ganhou!")

else:

print("Que pena, você perdeu. A palavra era:", palavra_secreta)

Este código ilustra um game loop básico para o jogo da forca, onde o jogador tem um número limitado de tentativas para adivinhar a palavra secreta. O loop continua até que o jogador acerte a palavra ou esgote suas tentativas.
