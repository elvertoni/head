---
titulo: "Pirâmide de testes"
tipo: rco-seed
disciplina: analise-e-projeto-de-sistemas
sigla_rco: APS
trimestre: 3
ordem_rco: 77
serie: 3
aula_rco: "Aula 77"
slides: 23
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/APS/3TRI/77-piramide-de-testes/77-piramide-de-testes.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/APS/3TRI/77-piramide-de-testes/AULA 77_ATIVIDADE_ANÁLISE E PROJETO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Pirâmide de testes

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E PROJETO DE SISTEMAS
- 3ª SÉRIE
- Pirâmide de testes
- Aula 77

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Exploraremos a estrutura da pirâmide de testes, diferenciando entre testes de Caixa Branca e Caixa Preta.

_6 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Selenium IDE: Ferramenta open source que permite criar testes automatizados para aplicações web. Katalon Studio: IDE gratuita para testes de software que suporta automação de APIs, web e mobile.
- Apache JMeter: Plataforma open source para testar a carga e o desempenho de aplicativos e serviços.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Analisamos tipos de testes, como testes relacionados à mudança e testes não-funcionais. Discutimos também técnicas adicionais que ajudam a refinar a cobertura de testes.

_3 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Maria é uma desenvolvedora iniciante que acabou de finalizar um novo módulo para um sistema. Ela quer garantir que todas as funcionalidades estejam corretas e seguras. No entanto, está em dúvida sobre como organizar seus testes para garantir a cobertura total.

_3 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta!
- Quem sabe responde!
- Qual abordagem de teste Maria deve seguir para garantir que desde a lógica interna até a experiência do usuário estejam devidamente validadas?

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Maria deve adotar a pirâmide de testes, que organiza os testes em três níveis: Unitários, de Integração e de Interface. Ela pode começar pelos testes de unidade, passando para a integração e, por último, para a interface (UI).

_3 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Visão Geral do Tema
- A pirâmide de testes é uma estrutura que orienta o uso correto de diferentes níveis de testes em um sistema, garantindo que cada camada do código seja validada eficientemente.

_3 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação do Tema
- Ela é composta por três principais níveis: testes unitários (base), testes de integração (intermediário) e testes de interface ou UI (topo). A base da pirâmide deve ter a maior quantidade de testes para validar funcionalidades isoladas.

_3 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Por Que o Tema é Importante?
- Essa abordagem reduz custos e tempo de manutenção, pois detectar e corrigir problemas nas camadas inferiores é mais simples do que na interface. Ela também diminui a ocorrência de bugs em produção.

_3 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Como o Tema é Usado na Prática
- Na prática, a pirâmide de testes é aplicada ao definir uma estratégia de automação, priorizando testes unitários e de integração antes de realizar testes manuais ou automatizados na interface.

_3 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Usando o Jest, podemos escrever um simples teste de unidade para validar uma função de cálculo de soma

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual é a principal diferença entre testes de Caixa Branca e Caixa Preta?
- (A) Caixa Branca verifica a lógica interna, enquanto Caixa Preta foca no comportamento externo.
- (B) Caixa Branca testa a interface, enquanto Caixa Preta testa a lógica interna.
- (C) Caixa Branca simula o usuário, e Caixa Preta testa algoritmos.
- (D) Caixa Branca é mais rápido que Caixa Preta.
- Realizem a atividade em duplas e socializem no final!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a principal diferença entre testes de Caixa Branca e Caixa Preta?
- (A) Caixa Branca verifica a lógica interna, enquanto Caixa Preta foca no comportamento externo.
- (B) Caixa Branca testa a interface, enquanto Caixa Preta testa a lógica interna.
- (C) Caixa Branca simula o usuário, e Caixa Preta testa algoritmos.
- (D) Caixa Branca é mais rápido que Caixa Preta.
- Resposta Correta: (A)

_3 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/quality-assurance-plano-testes-gestao-bugs

_5 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Testes de Caixa Branca vs testes de Caixa Preta
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/quality-assurance-plano-testes-gestao-bugs/task/101581
- Testes de Caixa Branca verificam a lógica interna e a estrutura do código, enquanto testes de Caixa Preta avaliam a funcionalidade e comportamento do sistema, sem conhecer o código-fonte.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Evidência de teste
- 6 minutos
- Link para tarefa: https://cursos.alura.com.br/course/quality-assurance-plano-testes-gestao-bugs/task/101582
- Evidência de teste é o registro documentado dos resultados obtidos durante a execução dos testes. Inclui capturas de tela, logs e relatórios que demonstram se o sistema atende aos requisitos definidos.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Exploramos a Pirâmide de Testes e a importância de dividir os testes em níveis para uma validação mais eficaz. Também diferenciamos testes de Caixa Branca e Caixa Preta e discutimos a relevância das evidências de teste para documentar a qualidade.

_3 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Referências
- Bibliografia
- PRESSMAN, Roger S.; MAXIM, Bruce R. Engenharia de software: uma abordagem profissional. 8 ed. Porto Alegre: AMGH, 2016. 940 p.
- SOMMERVILLE, Ian. Engenharia de software. 9 ed. São Paulo: Pearson, 2011
- ROGERS, D. L. Transformação digital: repensando o seu negócio para a era digital. Belo Horizonte: Autêntica Business, 2017.
- SCHWAB, K. A quarta revolução industrial. São Paulo: Edipro, 2016.
- Softwares
- Microsoft Visio; Canva.

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

_Fonte: AULA 77_ATIVIDADE_ANÁLISE E PROJETO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Análise e Projetos de Sistemas

3ª SÉRIE

ATIVIDADE AULA 77

Questão 1

Qual é a principal função dos testes de integração?

(A) Validar componentes isolados.

(B) Verificar como diferentes partes do sistema interagem.

(C) Avaliar a experiência do usuário.

(D) Executar testes de performance.

Resposta Correta: (B)

Explicação: Testes de integração asseguram que módulos e componentes funcionem juntos conforme esperado.

Questão 2

Qual o objetivo das evidências de teste?

(A) Documentar problemas encontrados para o time de desenvolvimento.

(B) Provar que os requisitos foram validados com sucesso.

(C) Melhorar o design do código.

(D) Definir novas funcionalidades para o produto.

Resposta Correta: (B)

Explicação: As evidências de teste garantem que todas as funcionalidades especificadas tenham sido validadas e atendam aos requisitos.
