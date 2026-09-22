# Curadoria de conceitos órfãos — amostra de 20 rascunhos

Data da inspeção: 2026-09-21. Propostas para Toni/Luna; nenhum conceito ou aula foi alterado por esta auditoria.

## Método e limites

A amostra intencional contém dez páginas de full-stack/cloud e dez de inovação/IA/robótica. Todos os caminhos foram conferidos, todos os frontmatters estão como rascunho e os vinte arquivos constavam no diagnóstico orphan de tools.lint_wiki.lint(Path.cwd()). Inclui continuidades da amostra anterior, relações textuais fortes, fontes com incerteza e possíveis raízes; não é estimativa estatística do conjunto.

Foram excluídos git e os nove conceitos com backlinks canônicos recém-corrigidos: arquitetura-cliente-servidor, api-rest, metodos-http, validacao-de-formulario, codigos-de-status-http, acessibilidade, alta-disponibilidade, seguranca-da-informacao e matriz-gut.

As evidências são observações das páginas locais, com linhas válidas nesta inspeção. As sugestões semânticas são hipóteses de curadoria. Dezenove fontes declaradas estão ausentes no caminho indicado neste checkout; isso não prova perda do original. A única fonte disponível da amostra é o PDF de Git, cuja página sobre hooks foi lida. Nenhuma outra afirmação foi validada contra PDF bruto. Cache, quando houver, não substitui fonte.

Candidato a link indica relação contextual plausível; aguardar fonte indica dúvida específica que precede edição; manter raiz preserva entrada geral provisória; possível duplicata exige comparação e decisão humana. Mesmo candidatos e raízes continuam sujeitos à recuperação das fontes ausentes.

Resultado: 12 candidatos a link, 4 aguardando fonte, 2 possíveis duplicatas e 2 raízes provisórias.

## 01. active-record

- Caminho: [conceitos/desenvolvimento-full-stack-e-cloud-computing/active-record.md](../conceitos/desenvolvimento-full-stack-e-cloud-computing/active-record.md).
- Slug: active-record; status observado: rascunho; classificação: **candidato a link**.
- Fonte declarada: `lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/17 - Aula 17 - Uso de MVC como Padrão de Projeto II - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: A definição (14) reúne registro e persistência; o corpo (22) distingue Active Record de ORM. orm:14–22 descreve mapeamento objeto/tabela, mas não nomeia o padrão.
- Página relacionada conferida: [orm](../conceitos/desenvolvimento-full-stack-e-cloud-computing/orm.md).
- Próxima ação: Luna: propor frase em orm explicando Active Record como opção de implementação, após conferir a fonte; não tornar os termos sinônimos.

## 02. ambiente-de-teste

- Caminho: [conceitos/desenvolvimento-full-stack-e-cloud-computing/ambiente-de-teste.md](../conceitos/desenvolvimento-full-stack-e-cloud-computing/ambiente-de-teste.md).
- Slug: ambiente-de-teste; status observado: rascunho; classificação: **candidato a link**.
- Fonte declarada: `lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/09 - Aula 9 - Ferramentas para Testar Back - End - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: O corpo (22) aborda isolamento. testes-de-integracao:22 exige ambiente e dependências controlados; as linhas 27–28 citam estado, limpeza e isolamento.
- Página relacionada conferida: [testes-de-integracao](../conceitos/desenvolvimento-full-stack-e-cloud-computing/testes-de-integracao.md).
- Próxima ação: Luna: converter a menção ao ambiente em link contextual para ambiente-de-teste; revisar ambas as páginas e registrar a relação de uso.

## 03. autenticacao-multifator

- Caminho: [conceitos/desenvolvimento-full-stack-e-cloud-computing/autenticacao-multifator.md](../conceitos/desenvolvimento-full-stack-e-cloud-computing/autenticacao-multifator.md).
- Slug: autenticacao-multifator; status observado: rascunho; classificação: **candidato a link**.
- Fonte declarada: `lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Estratégias de Cloud Computing/14 - Aula 14 - Gerenciamento e Governança em Serviços de Nuvem - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: A definição (14) apresenta fatores independentes. autenticacao:22 menciona proteção e revogação de fatores sem vincular MFA.
- Página relacionada conferida: [autenticacao](../conceitos/desenvolvimento-full-stack-e-cloud-computing/autenticacao.md).
- Próxima ação: Luna: propor contextualização curta em autenticacao com link para MFA, preservando autenticação versus autorização; conferir a fonte antes de ampliar a explicação.

## 04. arquitetura-monolitica

- Caminho: [conceitos/desenvolvimento-full-stack-e-cloud-computing/arquitetura-monolitica.md](../conceitos/desenvolvimento-full-stack-e-cloud-computing/arquitetura-monolitica.md).
- Slug: arquitetura-monolitica; status observado: rascunho; classificação: **aguardar fonte**.
- Fonte declarada: `lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Aplicações em Cloud Computing/14 - Aula 14 - Aplicações - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: A definição (14) delimita unidade de implantação; a frase (18) associa monólito à concentração de evolução e falhas. O corpo (22) admite modularidade. A fonte está ausente.
- Próxima ação: Toni: disponibilizar o PDF de Aplicações, Aula 14. Luna: revisar a generalização sobre falhas nas páginas 2–5 antes de propor ligação ou mudança editorial.

## 05. graphql

- Caminho: [conceitos/desenvolvimento-full-stack-e-cloud-computing/graphql.md](../conceitos/desenvolvimento-full-stack-e-cloud-computing/graphql.md).
- Slug: graphql; status observado: rascunho; classificação: **candidato a link**.
- Fonte declarada: `lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/31 - Aula 31 - Evolução e Gestão do Ciclo de Vida de uma API II - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: A definição (14) apresenta consulta e runtime; o corpo (22) fala de esquema e resolvers. api:22 enumera contratos Web, com REST já ligado.
- Página relacionada conferida: [api](../conceitos/desenvolvimento-full-stack-e-cloud-computing/api.md).
- Próxima ação: Luna: avaliar inclusão contextual de GraphQL em api após conferir o slide; preservar diferenças entre linguagem de consulta, esquema e estilo REST.

## 06. git-hooks

- Caminho: [conceitos/desenvolvimento-full-stack-e-cloud-computing/git-hooks.md](../conceitos/desenvolvimento-full-stack-e-cloud-computing/git-hooks.md).
- Slug: git-hooks; status observado: rascunho; classificação: **candidato a link**.
- Fonte declarada: `lake/programacao-front-end/Git--para--iniciantes.pdf` — presente; página física 61 lida (número impresso 60).
- Evidência: As linhas 14 e 22 descrevem automação e limites dos hooks locais. A fonte foi lida: página física 61, impressa 60, descreve eventos commit/push/merge e verificações automáticas. pipeline-ci-cd:23 lista verificações da entrega.
- Página relacionada conferida: [pipeline-ci-cd](../conceitos/desenvolvimento-full-stack-e-cloud-computing/pipeline-ci-cd.md).
- Próxima ação: Luna: propor referência a verificações locais em pipeline-ci-cd e explicitar que hooks complementam as verificações do pipeline; distinguir paginação física de impressa em Fontes.

## 07. teste-de-aceitacao

- Caminho: [conceitos/desenvolvimento-full-stack-e-cloud-computing/teste-de-aceitacao.md](../conceitos/desenvolvimento-full-stack-e-cloud-computing/teste-de-aceitacao.md).
- Slug: teste-de-aceitacao; status observado: rascunho; classificação: **candidato a link**.
- Fonte declarada: `lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Cultura DevOps e Integração Contínua/27 - Aula 27 - Desenvolvimento Orientado a Testes (TDD) III - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: A definição (14) trata critérios de uso e negócio. tdd:14 já afirma que TDD não substitui testes de integração e aceitação, sem link em aceitação.
- Página relacionada conferida: [tdd](../conceitos/desenvolvimento-full-stack-e-cloud-computing/tdd.md).
- Próxima ação: Luna: converter a expressão existente em tdd para link com rótulo natural; manter distintos ciclo TDD e critério de aceitação.

## 08. zona-de-disponibilidade

- Caminho: [conceitos/desenvolvimento-full-stack-e-cloud-computing/zona-de-disponibilidade.md](../conceitos/desenvolvimento-full-stack-e-cloud-computing/zona-de-disponibilidade.md).
- Slug: zona-de-disponibilidade; status observado: rascunho; classificação: **candidato a link**.
- Fonte declarada: `lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Estratégias de Cloud Computing/10 - Aula 10 - Arquitetura e Serviço de Computação em Nuvem - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: A definição (14) descreve domínio físico de falhas; o corpo (22) separa zona de região. arquitetura-de-nuvem:22 trata limites, falhas e alta disponibilidade projetada.
- Página relacionada conferida: [arquitetura-de-nuvem](../conceitos/desenvolvimento-full-stack-e-cloud-computing/arquitetura-de-nuvem.md).
- Próxima ação: Luna: propor explicação contextual sobre distribuição entre zonas em arquitetura-de-nuvem após conferir a fonte; preservar a exigência de testar falhas e dependências.

## 09. ansi-sql

- Caminho: [conceitos/desenvolvimento-full-stack-e-cloud-computing/ansi-sql.md](../conceitos/desenvolvimento-full-stack-e-cloud-computing/ansi-sql.md).
- Slug: ansi-sql; status observado: rascunho; classificação: **candidato a link**.
- Fonte declarada: `lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/32 - Aula 32 - Modelo Físico de Dados - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: O corpo (22) separa padrão de implementação. sql:22 explicita diferenças de dialeto entre produtos, ponto concreto para desenvolver portabilidade.
- Página relacionada conferida: [sql](../conceitos/desenvolvimento-full-stack-e-cloud-computing/sql.md).
- Próxima ação: Luna: propor ligação de sql para ansi-sql na frase sobre dialetos; conferir no material padrão versus extensão antes de adicionar afirmações.

## 10. versionamento-semantico

- Caminho: [conceitos/desenvolvimento-full-stack-e-cloud-computing/versionamento-semantico.md](../conceitos/desenvolvimento-full-stack-e-cloud-computing/versionamento-semantico.md).
- Slug: versionamento-semantico; status observado: rascunho; classificação: **aguardar fonte**.
- Fonte declarada: `lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Cultura DevOps e Integração Contínua/09 - Aula 9 - Controle de Versão III - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: A definição (14) resume Major.Minor.Patch e contrato público, mas não delimita fase 0.y.z ou versões preliminares; a fonte está ausente. versionamento-de-api:22 aborda outra decisão: URL, cabeçalho e depreciação.
- Página relacionada conferida: [versionamento-de-api](../conceitos/desenvolvimento-full-stack-e-cloud-computing/versionamento-de-api.md).
- Próxima ação: Toni: fornecer Aula 9 de Controle de Versão III. Luna: delimitar o escopo de SemVer com a fonte antes de propor vínculo; não equiparar estratégia de versão de API com SemVer.

## 11. proposicao-conjuntiva

- Caminho: [conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/proposicao-conjuntiva.md](../conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/proposicao-conjuntiva.md).
- Slug: proposicao-conjuntiva; status observado: rascunho; classificação: **possível duplicata**.
- Fonte declarada: `lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo III - Pensamento Computacional e Robótica/Lógica e Pensamento Matemático/15 - Aula 15 - Proposições Lógicas e Tipos de Proposições Lógicas - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: As linhas 14 e 18 descrevem a mesma condição de verdade de conjuncao-logica:14 e 18. As armadilhas sobre momentos incompatíveis (26) se sobrepõem; a fonte é a Aula 15.
- Página relacionada conferida: [conjuncao-logica](../conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/conjuncao-logica.md).
- Próxima ação: Toni/Luna: revisar o par na seção comparativa, ler ambas as fontes quando disponíveis e decidir entre distinguir expressão/operador ou propor fusão para aprovação.

## 12. conjuncao-logica

- Caminho: [conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/conjuncao-logica.md](../conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/conjuncao-logica.md).
- Slug: conjuncao-logica; status observado: rascunho; classificação: **possível duplicata**.
- Fonte declarada: `lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo III - Pensamento Computacional e Robótica/Lógica e Pensamento Matemático/16 - Aula 16 - Conectivos e Operações Lógicas - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: O corpo (22) explicita conectivo binário; proposicao-conjuntiva:22 trata componentes e requisitos. Existe diferença de foco possível, mas definições atuais muito próximas; a fonte é a Aula 16.
- Página relacionada conferida: [proposicao-conjuntiva](../conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/proposicao-conjuntiva.md).
- Próxima ação: Toni/Luna: não escolher destino de fusão apenas pelo nome; conferir páginas citadas e preservar os dois slugs até decisão explícita.

## 13. startup

- Caminho: [conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/startup.md](../conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/startup.md).
- Slug: startup; status observado: rascunho; classificação: **aguardar fonte**.
- Fonte declarada: `lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo I - Cultura Maker e Educação/Tecnologias Emergentes, Habilidades e Carreira/10 - Aula 10 - Aplicações e Futuro - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: A definição (14) aborda repetição, escala e incerteza; aka (6) inclui empresa de base tecnológica. Onde aparece (31) cita o lote Onda 1, e Fontes (36) remete a páginas de relatório sem identificá-lo.
- Página relacionada conferida: [prototipagem](../conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/prototipagem.md).
- Próxima ação: Toni: fornecer PDF e relatório do lote. Luna: verificar o alias amplo e registrar página concreta; depois avaliar exemplo em prototipagem, cujo corpo aborda teste de hipóteses.

## 14. matematica

- Caminho: [conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/matematica.md](../conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/matematica.md).
- Slug: matematica; status observado: rascunho; classificação: **manter raiz**.
- Fonte declarada: `lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo III - Pensamento Computacional e Robótica/Lógica e Pensamento Matemático/01 - Aula 1 - Matemática e a Sociedade - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: A definição (14) é abrangente; o corpo (22) distribui o tema entre conjunto, função matemática, estatística, raciocínio lógico e resolução de problemas. É uma entrada organizadora possível mesmo sem inlinks.
- Próxima ação: Luna: manter raiz provisória em rascunho e registrar função de navegação; Toni deve recuperar a fonte antes da validação semântica ou promoção. Não inserir retornos apenas pela métrica.

## 15. dropout

- Caminho: [conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/dropout.md](../conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/dropout.md).
- Slug: dropout; status observado: rascunho; classificação: **candidato a link**.
- Fonte declarada: `lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Conceitos Avançados em IA e Blockchain/06 - Aula 6 - Aprendizado de Máquina III - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: O corpo (22) liga regularizacao. regularizacao:22 menciona literalmente dropout entre estratégias sem wikilink. Ambas as páginas declaram Aula 6 de Aprendizado de Máquina III.
- Página relacionada conferida: [regularizacao](../conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/regularizacao.md).
- Próxima ação: Luna: converter a menção existente em regularizacao para link dropout e registrar a relação; essa conversão não valida todas as afirmações do rascunho.

## 16. aprendizado-por-transferencia

- Caminho: [conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/aprendizado-por-transferencia.md](../conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/aprendizado-por-transferencia.md).
- Slug: aprendizado-por-transferencia; status observado: rascunho; classificação: **candidato a link**.
- Fonte declarada: `lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Conceitos Avançados em IA e Blockchain/08 - Aula 8 - Aprendizado Supervisionado II - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: A definição (14) trata reutilização de parâmetros; o corpo (22) liga fine-tuning. fine-tuning:14 descreve ajuste posterior ao pré-treino; a linha 22 contrapõe treino e contexto.
- Página relacionada conferida: [fine-tuning](../conceitos/inteligencia-artificial/fine-tuning.md).
- Próxima ação: Luna: avaliar conexão contextual em fine-tuning após revisão das fontes; explicitar que transferência é mais ampla que ajuste fino de LLM.

## 17. moda

- Caminho: [conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/moda.md](../conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/moda.md).
- Slug: moda; status observado: rascunho; classificação: **candidato a link**.
- Fonte declarada: `lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo III - Pensamento Computacional e Robótica/Lógica e Pensamento Matemático/05 - Aula 5 - Estatística III - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: A definição (14) trata maior frequência; o corpo (22) admite múltiplas modas. estatistica:22 discute medidas, e a linha 27 alerta que média não resume toda distribuição.
- Página relacionada conferida: [estatistica](../conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/estatistica.md).
- Próxima ação: Luna: propor exemplo de medida modal na discussão de resumo dos dados em estatistica após conferir a fonte; evitar mera lista de relacionados.

## 18. regressao-linear

- Caminho: [conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/regressao-linear.md](../conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/regressao-linear.md).
- Slug: regressao-linear; status observado: rascunho; classificação: **aguardar fonte**.
- Fonte declarada: `lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Conceitos Avançados em IA e Blockchain/12 - Aula 12 - Aprendizado Não Supervisionado III - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: A definição (14) descreve previsão numérica e o corpo (22) liga classificacao-e-regressao; a fonte se intitula Aprendizado Não Supervisionado III. O título sozinho não prova erro: o slide pode apresentar comparação.
- Página relacionada conferida: [classificacao-e-regressao](../conceitos/inteligencia-artificial/classificacao-e-regressao.md).
- Próxima ação: Toni: recuperar o PDF da Aula 12. Luna: verificar páginas 2–8 antes de relocar fonte ou classificar conteúdo; não corrigir proveniência inferindo pelo título.

## 19. sistemas-multiagentes

- Caminho: [conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/sistemas-multiagentes.md](../conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/sistemas-multiagentes.md).
- Slug: sistemas-multiagentes; status observado: rascunho; classificação: **candidato a link**.
- Fonte declarada: `lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/10 - Aula 10 - Busca Competitiva - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: O corpo (22) distingue agentes e dinâmica coletiva. agente:28 menciona subagentes e orquestrador dividindo tarefas; este rascunho inclui cooperação e competição, escopo mais amplo.
- Página relacionada conferida: [agente](../conceitos/inteligencia-artificial/agente.md).
- Próxima ação: Luna: revisar ligação contextual em agente, apresentando orquestração como um caso possível; não equiparar todo conjunto de processos a sistema multiagente.

## 20. tecnologia

- Caminho: [conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/tecnologia.md](../conceitos/inovacao-inteligencia-artificial-e-robotica-educacional/tecnologia.md).
- Slug: tecnologia; status observado: rascunho; classificação: **manter raiz**.
- Fonte declarada: `lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo III - Pensamento Computacional e Robótica/Desafio_ Caso de Estudo - Pensamento Computacional e Robótica/03 - Aula 3 - Desenvolvimento Etapa II - Apostila (Slides).pdf` — ausente nesse caminho local.
- Evidência: A definição (14) cobre conhecimentos, práticas, processos e artefatos. O corpo (22) aponta robótica, cultura digital, inovação e tecnologia assistiva, função coerente de entrada geral.
- Próxima ação: Luna: manter raiz provisória em rascunho. Toni: recuperar a fonte para validar formulação. Reavaliar ligação quando outra página usar efetivamente esse conceito.

## Comparação: proposição conjuntiva e conjunção lógica

| Aspecto | proposicao-conjuntiva | conjuncao-logica |
|---|---|---|
| Definição, linha 14 | Combina proposições por “e”; todas verdadeiras | Combina duas proposições por “e”; ambas verdadeiras |
| Corpo, linha 22 | Valor dos componentes, tabela-verdade e requisitos | Conectivo binário, regras, filtros e especificações |
| Armadilha, linha 26 | Valores de momentos diferentes | Dados de tempos incompatíveis |
| Fonte declarada | Aula 15, páginas 7–12 | Aula 16, página 3 |
| Aliases, linha 6 | conjunctive proposition | logical conjunction, AND |

A sobreposição é forte no conteúdo atual, mas há distinção pedagógica possível: uma página pode representar a expressão formada (p ∧ q), e a outra o operador que a forma (∧). Esta é hipótese para revisão, não uma diferença já sustentada pelas fontes nesta inspeção. Os dois PDFs estão ausentes nos caminhos declarados.

Sequência: recuperar ambos os PDFs; verificar trechos citados; comparar exemplos que realmente exigem páginas separadas; pesquisar usos e aliases no vault; apresentar a Toni uma escolha fundamentada. Se a separação for útil, propor definições com escopos claros. Caso contrário, propor um destino com preservação de aliases e proveniência das duas fontes, mapear referências e aguardar aprovação de Toni para merge/obsolescência, conforme AGENTS.md. Esta auditoria não autoriza nem executa fusão.

## Regras para não reduzir órfãos artificialmente

1. Medir inlinks semânticos do corpo de conceitos e canônicas; menções no índice, log ou neste relatório não resolvem isolamento pedagógico.
2. Não adicionar link recíproco só porque A aponta para B. A frase de B precisa usar A para explicar algo.
3. Priorizar menções existentes, como dropout em regularizacao e aceitação em tdd, antes de acrescentar conteúdo novo.
4. Não inserir listas de relacionados só para aumentar grau do grafo. Registrar relações comprovadas em Onde aparece e usar links no fluxo explicativo quando couber.
5. Não promover rascunho, apagar página, marcar obsoleto ou fundir conceitos para melhorar contagem. Merge/obsolescência exige decisão de Toni.
6. Manter raízes gerais justificadas. Zero inlinks é sinal para revisão, não prova de inutilidade.
7. Verificar fonte, contexto e direção da relação antes de ampliar afirmações. Fonte ausente e cache derivado não validam conteúdo.
8. Não converter números de aulas dos PDFs em backlinks canônicos: conferir caminho exato e citação do conceito na canônica.
9. Após edição autorizada, registrar relações efetivamente alteradas e atualizar índice/log conforme schema. Editar canônica exige avançar versão/data e regenerar manifesto.
10. Registrar efeito esperado por relação e dúvidas remanescentes. Redução de órfãos deve decorrer de curadoria útil, nunca ser seu único critério de sucesso.

## Validação do artefato

As vinte páginas foram lidas integralmente; os vizinhos citados foram inspecionados nos trechos apontados; todos os links Markdown relativos foram conferidos no filesystem; as fontes foram verificadas por existência no caminho declarado. O arquivo foi relido após geração. A classificação não altera o conteúdo do vault. O contrato do portal na leitura inicial retornou 89 aulas aprovadas e zero divergências.
