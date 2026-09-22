---
titulo: "Refinamentos"
tipo: rco-seed
disciplina: analise-e-projeto-de-sistemas
sigla_rco: APS
trimestre: 3
ordem_rco: 73
serie: 3
aula_rco: "Aula 73"
slides: 25
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/APS/3TRI/73-refinamentos/73-refinamentos.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/APS/3TRI/73-refinamentos/AULA 73_ATIVIDADE_ANÁLISE E PROJETO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Refinamentos

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E PROJETO DE SISTEMAS
- 3ª SÉRIE
- Refinamentos
- Aula 73

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Explorar como garantir a qualidade do software por meio de refinamentos nos testes.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Sentry: Uma ferramenta open source de monitoramento de erros que coleta e categoriza bugs automaticamente.
- Bugzilla: Um sistema de rastreamento de defeitos gratuito para ajudar a registrar e gerenciar bugs. Trello: Pode ser usado para organizar o fluxo de bugs e sua correção com base em prioridades.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Abordou a Estratégia de Testes, discutindo como definir a arquitetura, escopo e escolha de ferramentas para garantir um ambiente de testes eficiente e seguro.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Laura é responsável por atualizar uma funcionalidade em um aplicativo e precisa garantir que as mudanças não afetem outras áreas do sistema. Laura inseriu uma nova opção de pagamento no app e teme que isso possa gerar falhas nas integrações anteriores.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta!
- Quem sabe responde!
- Qual solução é a correta?
- Usar testes focados em mudanças e automatizar casos de teste para avaliar o impacto da nova funcionalidade.
- Apenas testar a nova funcionalidade manualmente e não validar outros pontos do sistema.

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- (Correta) Usar testes focados em mudanças e automatizar casos de teste para avaliar o impacto da nova funcionalidade.
- (Incorreta) Apenas testar a nova funcionalidade manualmente e não validar outros pontos do sistema.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Refinamentos
- Refinamentos nos testes visam aprimorar a qualidade e garantir que cada mudança no sistema não cause impactos negativos. Foco em técnicas de teste contínuo e planejado.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Ajustar processos
- Refinamentos são ajustes nos processos de teste e nas práticas de desenvolvimento. São aplicados a cada iteração do ciclo de desenvolvimento para garantir que a qualidade esteja alinhada aos requisitos do projeto.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Encontrar falhas
- Esses ajustes permitem encontrar falhas rapidamente, reduzir retrabalho e facilitar a entrega de um produto mais confiável e seguro. Isso é essencial em ciclos ágeis.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Revisão contínua
- No desenvolvimento ágil, refinamentos envolvem revisão contínua dos testes, ajustando casos existentes e adicionando novos, além de redefinir escopos à medida que o produto evolui.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Aplicação
- Uma maneira prática de aplicar refinamentos é criando um script automatizado para validação de uma mudança específica. Usando Python com a biblioteca Unittest:

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Esse exemplo usa refinamentos para verificar se a função calcular_total se adapta corretamente às mudanças de lógica, como adição de novos tipos de desconto.

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Quais testes focam em avaliar o impacto de mudanças no sistema?
- (A) Testes Unitários
- (B) Testes de Regressão
- (C) Testes Exploratórios
- (D) Testes de Integração
- Realizem a atividade em duplas e socializem no final!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Quais testes focam em avaliar o impacto de mudanças no sistema?
- (A) Testes Unitários
- (B) Testes de Regressão
- (C) Testes Exploratórios
- (D) Testes de Integração
- Resposta: (B)

_3 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/qa-fundamentos

_5 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Testes Relacionados a Mudança
- 4 minutos
- Link para tarefa: https://cursos.alura.com.br/course/qa-fundamentos/task/62487
- Testes relacionados a mudança verificam se uma alteração no sistema impacta negativamente outras funcionalidades. Incluem testes de regressão e de integração para garantir a estabilidade após atualizações.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Mais Técnicas de Execução de Testes
- 4 minutos
- Link para tarefa: https://cursos.alura.com.br/course/qa-fundamentos/task/62488
- Técnicas adicionais de execução de testes incluem testes de desempenho, usabilidade e segurança, focando em diferentes aspectos do produto para identificar falhas e garantir qualidade e eficiência.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Estimativa de Testes
- 3 minutos
- Link para tarefa: https://cursos.alura.com.br/course/qa-fundamentos/task/62489
- Estimativa de testes envolve calcular o tempo, esforço e recursos necessários para testar um produto. Isso ajuda a planejar as atividades, definir prazos realistas e alocar a equipe adequadamente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Discutimos como refinamentos ajudam a melhorar a qualidade de um produto. Vimos como usar testes focados em mudanças, aplicar novas técnicas de teste e estimar esforços para garantir um ciclo contínuo de melhoria.

_4 imagem(ns) no slide._

### Slide 22

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

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 73_ATIVIDADE_ANÁLISE E PROJETO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Análise e Projetos de Sistemas

3ª SÉRIE

ATIVIDADE AULA 73

Questão 1

Qual é a principal vantagem de usar refinamentos contínuos nos testes?

(A) Reduzir o número de colaboradores no projeto.

(B) Identificar falhas rapidamente durante o desenvolvimento.

(C) Diminuir o tempo de criação de novas funcionalidades.

(D) Focar apenas na qualidade visual do produto.

Resposta: (B) Identificar falhas rapidamente durante o desenvolvimento.

Explicação: Refinamentos ajudam a identificar e corrigir erros enquanto o produto ainda está em desenvolvimento, reduzindo retrabalho e melhorando a qualidade.

Questão 2

O que deve ser considerado ao definir o escopo de testes para um novo recurso?

(A) Impacto no ambiente de produção.

(B) Tempo de execução dos testes automatizados.

(C) Probabilidade de falhas em áreas críticas.

(D) Design visual do sistema.

Resposta: (C) Probabilidade de falhas em áreas críticas.

Explicação: Considerar áreas críticas é essencial para garantir que novas mudanças não causem problemas graves no sistema.
