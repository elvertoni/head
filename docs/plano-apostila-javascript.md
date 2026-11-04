# Plano da apostila de JavaScript — Programação Front-end

Sequência didática aprovada pelo Toni em 2026-11-03.

## Público e proposta

Alunos do Curso Técnico em Desenvolvimento de Sistemas, com necessidade de retomadas frequentes de HTML, CSS e lógica. A apostila deve ser extremamente fácil e aplicável, com instruções pequenas, exemplos executáveis e resultados que o aluno consiga conferir.

Previsão: 20 encontros de 50 minutos. Projeto de referência: uma lista de tarefas de estudo, construída gradualmente. A numeração abaixo organiza o plano; não altera a identidade de nenhuma aula existente no acervo.

## Sequência aprovada

| Aula | Foco e aplicação |
|---|---|
| 1 | **Retomada de HTML e CSS:** montar uma página pequena, salvar e abrir para conferir. |
| 2 | **Primeiro JavaScript:** conectar o arquivo à página e usar o console para observar resultados. |
| 3 | **Variáveis:** guardar e consultar informações com `let` e `const`. |
| 4 | **Tipos de dados:** reconhecer texto, número e booleano em exemplos simples. |
| 5 | **Operações e conversões:** calcular valores e perceber a diferença entre somar números e juntar textos. |
| 6 | **Comparações:** testar regras com `>`, `<` e `===`, prevendo o resultado. |
| 7 | **Condicionais:** usar `if` e `else` para escolher entre dois resultados. |
| 8 | **Mais de uma condição:** introduzir `else if`, `&&` e `||` gradualmente. |
| 9 | **Funções:** dar nome a uma ação e executá-la; começar sem parâmetros. |
| 10 | **DOM:** localizar um elemento e alterar seu texto, retomando tags e `id`. |
| 11 | **Eventos:** fazer um botão executar uma função ao receber um clique. |
| 12 | **Campos de entrada:** ler um valor digitado e apresentar uma resposta na página. |
| 13 | **Formulários:** tratar o envio e impedir entradas vazias, retomando funções e condicionais. |
| 14 | **Criação de elementos:** adicionar uma tarefa visível à página. |
| 15 | **Arrays:** guardar várias tarefas e acessar os itens pelo índice. |
| 16 | **Repetição:** percorrer um array com `for`, acompanhando uma execução por vez. |
| 17 | **Dados virando interface:** usar `forEach` para mostrar as tarefas guardadas no array. |
| 18 | **Classes CSS e interação:** marcar uma tarefa como concluída e mudar sua aparência. |
| 19 | **Filtros:** selecionar tarefas com `filter`; apresentar `map` e `reduce` como aprofundamento guiado. |
| 20 | **Consolidação:** testar o projeto, corrigir erros e melhorar nomes e organização. |

## Orientações para a produção

- Retomar em cada encontro um exercício anterior, o HTML/CSS necessário e o código já conhecido.
- Organizar cada capítulo em retomada, prática guiada, conferência do resultado e pequena alteração autônoma.
- Informar o arquivo a editar, onde inserir o código e o resultado esperado; incluir ajuda para os erros mais comuns.
- Apresentar os termos técnicos quando forem necessários e introduzir uma mudança por vez.
- Trabalhar boas práticas desde a aula 2 e reforçá-las ao longo da sequência.
- Reservar mais tempo de prática nas aulas 8, 13 e 17, que integram vários conhecimentos.
- Tratar `map` e `reduce` como extensão guiada, sem exigir domínio dos quatro métodos de arrays em um encontro.
- Usar VSCode local para editar e o navegador para conferir a página.

## Relação com as fontes

Base curricular: 20 apresentações RCO de Programação Front-end, aulas 78–97, e oito documentos de apoio das aulas 78–81, analisados nesta sessão. A localização dos arquivos originais está registrada no handoff local.

A sequência reorganiza os temas por dependências: funções precedem eventos; introdução, variáveis e coleções são reunidas em uma progressão contínua. A contagem regressiva proposta na fonte inicial fica para depois dos fundamentos, sem integrar o núcleo destes 20 encontros.

## Estado

Plano aprovado e sequência de 20 aulas produzida. Aulas 01 a 11 produzidas em 2026-11-03 e aulas 12 a 20 em 2026-11-04, em rascunho para revisão do Toni. A produção conjunta dos lotes 03–04, 05–07, 08–11, 12–15 e 16–20 foi explicitamente solicitada:

- Aula 01: `aulas/programacao-front-end/javascript-na-pratica/01-retomada-html-css-lista-estudos/canonica.md`; apostila em `saidas/aula-01-meus-estudos-html-css.html`, na mesma pasta de aula.
- Aula 02: `aulas/programacao-front-end/javascript-na-pratica/02-primeiro-javascript-no-console/canonica.md`; apostila em `saidas/aula-02-primeiro-javascript-no-console.html`, na mesma pasta de aula.
- Aula 03: `aulas/programacao-front-end/javascript-na-pratica/03-variaveis-let-const-nos-estudos/canonica.md`; apostila em `saidas/aula-03-variaveis-let-const-nos-estudos.html`, na mesma pasta de aula.
- Aula 04: `aulas/programacao-front-end/javascript-na-pratica/04-textos-numeros-booleanos-nos-estudos/canonica.md`; apostila em `saidas/aula-04-textos-numeros-booleanos-nos-estudos.html`, na mesma pasta de aula.
- Aula 05: `aulas/programacao-front-end/javascript-na-pratica/05-calculos-conversoes-minutos-estudo/canonica.md`; apostila em `saidas/aula-05-calculos-conversoes-minutos-estudo.html`, na mesma pasta de aula.
- Aula 06: `aulas/programacao-front-end/javascript-na-pratica/06-comparando-minutos-e-meta/canonica.md`; apostila em `saidas/aula-06-comparando-minutos-e-meta.html`, na mesma pasta de aula.
- Aula 07: `aulas/programacao-front-end/javascript-na-pratica/07-decisoes-if-else-meta-estudos/canonica.md`; apostila em `saidas/aula-07-decisoes-if-else-meta-estudos.html`, na mesma pasta de aula.
- Aula 08: `aulas/programacao-front-end/javascript-na-pratica/08-condicoes-else-if-e-ou/canonica.md`; apostila em `saidas/aula-08-condicoes-else-if-e-ou.html`, na mesma pasta de aula.
- Aula 09: `aulas/programacao-front-end/javascript-na-pratica/09-funcoes-organizando-acoes-estudo/canonica.md`; apostila em `saidas/aula-09-funcoes-organizando-acoes-estudo.html`, na mesma pasta de aula.
- Aula 10: `aulas/programacao-front-end/javascript-na-pratica/10-dom-alterando-mensagem-estudos/canonica.md`; apostila em `saidas/aula-10-dom-alterando-mensagem-estudos.html`, na mesma pasta de aula.
- Aula 11: `aulas/programacao-front-end/javascript-na-pratica/11-eventos-clique-botao-lembrete/canonica.md`; apostila em `saidas/aula-11-eventos-clique-botao-lembrete.html`, na mesma pasta de aula.
- Aula 12: `aulas/programacao-front-end/javascript-na-pratica/12-lendo-campo-tarefa/canonica.md`; apostila em `saidas/aula-12-lendo-campo-tarefa.html`, na mesma pasta de aula.
- Aula 13: `aulas/programacao-front-end/javascript-na-pratica/13-formulario-validando-tarefa/canonica.md`; apostila em `saidas/aula-13-formulario-validando-tarefa.html`, na mesma pasta de aula.
- Aula 14: `aulas/programacao-front-end/javascript-na-pratica/14-criando-itens-lista-tarefas/canonica.md`; apostila em `saidas/aula-14-criando-itens-lista-tarefas.html`, na mesma pasta de aula.
- Aula 15: `aulas/programacao-front-end/javascript-na-pratica/15-arrays-guardando-tarefas/canonica.md`; apostila em `saidas/aula-15-arrays-guardando-tarefas.html`, na mesma pasta de aula.
- Aula 16: `aulas/programacao-front-end/javascript-na-pratica/16-for-percorrendo-tarefas/canonica.md`; apostila em `saidas/aula-16-for-percorrendo-tarefas.html`, na mesma pasta de aula.
- Aula 17: `aulas/programacao-front-end/javascript-na-pratica/17-foreach-montando-lista/canonica.md`; apostila em `saidas/aula-17-foreach-montando-lista.html`, na mesma pasta de aula.
- Aula 18: `aulas/programacao-front-end/javascript-na-pratica/18-classes-tarefas-concluidas/canonica.md`; apostila em `saidas/aula-18-classes-tarefas-concluidas.html`, na mesma pasta de aula.
- Aula 19: `aulas/programacao-front-end/javascript-na-pratica/19-filtrando-tarefas-estudo/canonica.md`; apostila em `saidas/aula-19-filtrando-tarefas-estudo.html`, na mesma pasta de aula.
- Aula 20: `aulas/programacao-front-end/javascript-na-pratica/20-revisao-projeto-lista-estudos/canonica.md`; apostila em `saidas/aula-20-revisao-projeto-lista-estudos.html`, na mesma pasta de aula.

Na pasta `saidas/` da aula 20, o projeto de referência derivado da canônica está em `projeto-meus-estudos/` e `projeto-meus-estudos.zip`. O pacote `javascript-20-aulas-e-projeto.zip` reúne as 20 apostilas e os dois arquivos do projeto. O projeto é local e temporário: não inclui persistência, servidor nem publicação.

A produção segue a skill `prof-toni`; a apostila deriva das canônicas pela skill `aula-estatica`. Os adaptadores locais estão em `scratch/javascript-aula-NN/gerar_apostila.py`, com `NN` de `01` a `20` (local-only); qualquer correção de conteúdo começa na canônica e exige regenerar a apostila. O lote final também pode ser gerado por `scratch/javascript-final/gerar_lote.py`, e os pacotes, por `scratch/javascript-final/empacotar.py`.
