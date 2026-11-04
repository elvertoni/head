# Plano da apostila de JavaScript — Programação Front-end

Sequência didática aprovada pelo Toni em 2026-11-03.

## Público e proposta

Alunos do Curso Técnico em Desenvolvimento de Sistemas, com necessidade de retomadas frequentes de HTML, CSS e lógica. A apostila deve ser extremamente fácil e aplicável, com instruções pequenas, exemplos executáveis e resultados que o aluno consiga conferir.

Previsão: 20 encontros de 50 minutos, numerados como aulas 19 a 38 da disciplina no portal (as aulas 1–18 são das trilhas de HTML semântico, Git e Landing Page). Projeto de referência: uma lista de tarefas de estudo, construída gradualmente. A numeração abaixo organiza o plano; não altera a identidade de nenhuma aula existente no acervo.

## Sequência aprovada

| Aula | Foco e aplicação |
|---|---|
| 19 | **Retomada de HTML e CSS:** montar uma página pequena, salvar e abrir para conferir. |
| 20 | **Primeiro JavaScript:** conectar o arquivo à página e usar o console para observar resultados. |
| 21 | **Variáveis:** guardar e consultar informações com `let` e `const`. |
| 22 | **Tipos de dados:** reconhecer texto, número e booleano em exemplos simples. |
| 23 | **Operações e conversões:** calcular valores e perceber a diferença entre somar números e juntar textos. |
| 24 | **Comparações:** testar regras com `>`, `<` e `===`, prevendo o resultado. |
| 25 | **Condicionais:** usar `if` e `else` para escolher entre dois resultados. |
| 26 | **Mais de uma condição:** introduzir `else if`, `&&` e `||` gradualmente. |
| 27 | **Funções:** dar nome a uma ação e executá-la; começar sem parâmetros. |
| 28 | **DOM:** localizar um elemento e alterar seu texto, retomando tags e `id`. |
| 29 | **Eventos:** fazer um botão executar uma função ao receber um clique. |
| 30 | **Campos de entrada:** ler um valor digitado e apresentar uma resposta na página. |
| 31 | **Formulários:** tratar o envio e impedir entradas vazias, retomando funções e condicionais. |
| 32 | **Criação de elementos:** adicionar uma tarefa visível à página. |
| 33 | **Arrays:** guardar várias tarefas e acessar os itens pelo índice. |
| 34 | **Repetição:** percorrer um array com `for`, acompanhando uma execução por vez. |
| 35 | **Dados virando interface:** usar `forEach` para mostrar as tarefas guardadas no array. |
| 36 | **Classes CSS e interação:** marcar uma tarefa como concluída e mudar sua aparência. |
| 37 | **Filtros:** selecionar tarefas com `filter`; apresentar `map` e `reduce` como aprofundamento guiado. |
| 38 | **Consolidação:** testar o projeto, corrigir erros e melhorar nomes e organização. |

## Orientações para a produção

- Retomar em cada encontro um exercício anterior, o HTML/CSS necessário e o código já conhecido.
- Organizar cada capítulo em retomada, prática guiada, conferência do resultado e pequena alteração autônoma.
- Informar o arquivo a editar, onde inserir o código e o resultado esperado; incluir ajuda para os erros mais comuns.
- Apresentar os termos técnicos quando forem necessários e introduzir uma mudança por vez.
- Trabalhar boas práticas desde a aula 20 e reforçá-las ao longo da sequência.
- Reservar mais tempo de prática nas aulas 26, 31 e 35, que integram vários conhecimentos.
- Tratar `map` e `reduce` como extensão guiada, sem exigir domínio dos quatro métodos de arrays em um encontro.
- Usar VSCode local para editar e o navegador para conferir a página.

## Relação com as fontes

Base curricular: 20 apresentações RCO de Programação Front-end, aulas 78–97, e oito documentos de apoio das aulas 78–81, analisados nesta sessão. A localização dos arquivos originais está registrada no handoff local.

A sequência reorganiza os temas por dependências: funções precedem eventos; introdução, variáveis e coleções são reunidas em uma progressão contínua. A contagem regressiva proposta na fonte inicial fica para depois dos fundamentos, sem integrar o núcleo destes 20 encontros.

## Estado

Plano aprovado, sequência de 20 aulas produzida e aprovada para publicação em 2026-11-04. Produzidas como 01–20 (2026-11-03/04) e renumeradas para 19–38 no mesmo dia, para seguir as aulas 1–18 das outras trilhas de Programação Front-end (decisão #037). A produção conjunta dos lotes 03–04, 05–07, 08–11, 12–15 e 16–20 foi explicitamente solicitada:

- Aula 19: `aulas/programacao-front-end/javascript-na-pratica/19-retomada-html-css-lista-estudos/canonica.md`; apostila em `saidas/aula-19-meus-estudos-html-css.html`, na mesma pasta de aula.
- Aula 20: `aulas/programacao-front-end/javascript-na-pratica/20-primeiro-javascript-no-console/canonica.md`; apostila em `saidas/aula-20-primeiro-javascript-no-console.html`, na mesma pasta de aula.
- Aula 21: `aulas/programacao-front-end/javascript-na-pratica/21-variaveis-let-const-nos-estudos/canonica.md`; apostila em `saidas/aula-21-variaveis-let-const-nos-estudos.html`, na mesma pasta de aula.
- Aula 22: `aulas/programacao-front-end/javascript-na-pratica/22-textos-numeros-booleanos-nos-estudos/canonica.md`; apostila em `saidas/aula-22-textos-numeros-booleanos-nos-estudos.html`, na mesma pasta de aula.
- Aula 23: `aulas/programacao-front-end/javascript-na-pratica/23-calculos-conversoes-minutos-estudo/canonica.md`; apostila em `saidas/aula-23-calculos-conversoes-minutos-estudo.html`, na mesma pasta de aula.
- Aula 24: `aulas/programacao-front-end/javascript-na-pratica/24-comparando-minutos-e-meta/canonica.md`; apostila em `saidas/aula-24-comparando-minutos-e-meta.html`, na mesma pasta de aula.
- Aula 25: `aulas/programacao-front-end/javascript-na-pratica/25-decisoes-if-else-meta-estudos/canonica.md`; apostila em `saidas/aula-25-decisoes-if-else-meta-estudos.html`, na mesma pasta de aula.
- Aula 26: `aulas/programacao-front-end/javascript-na-pratica/26-condicoes-else-if-e-ou/canonica.md`; apostila em `saidas/aula-26-condicoes-else-if-e-ou.html`, na mesma pasta de aula.
- Aula 27: `aulas/programacao-front-end/javascript-na-pratica/27-funcoes-organizando-acoes-estudo/canonica.md`; apostila em `saidas/aula-27-funcoes-organizando-acoes-estudo.html`, na mesma pasta de aula.
- Aula 28: `aulas/programacao-front-end/javascript-na-pratica/28-dom-alterando-mensagem-estudos/canonica.md`; apostila em `saidas/aula-28-dom-alterando-mensagem-estudos.html`, na mesma pasta de aula.
- Aula 29: `aulas/programacao-front-end/javascript-na-pratica/29-eventos-clique-botao-lembrete/canonica.md`; apostila em `saidas/aula-29-eventos-clique-botao-lembrete.html`, na mesma pasta de aula.
- Aula 30: `aulas/programacao-front-end/javascript-na-pratica/30-lendo-campo-tarefa/canonica.md`; apostila em `saidas/aula-30-lendo-campo-tarefa.html`, na mesma pasta de aula.
- Aula 31: `aulas/programacao-front-end/javascript-na-pratica/31-formulario-validando-tarefa/canonica.md`; apostila em `saidas/aula-31-formulario-validando-tarefa.html`, na mesma pasta de aula.
- Aula 32: `aulas/programacao-front-end/javascript-na-pratica/32-criando-itens-lista-tarefas/canonica.md`; apostila em `saidas/aula-32-criando-itens-lista-tarefas.html`, na mesma pasta de aula.
- Aula 33: `aulas/programacao-front-end/javascript-na-pratica/33-arrays-guardando-tarefas/canonica.md`; apostila em `saidas/aula-33-arrays-guardando-tarefas.html`, na mesma pasta de aula.
- Aula 34: `aulas/programacao-front-end/javascript-na-pratica/34-for-percorrendo-tarefas/canonica.md`; apostila em `saidas/aula-34-for-percorrendo-tarefas.html`, na mesma pasta de aula.
- Aula 35: `aulas/programacao-front-end/javascript-na-pratica/35-foreach-montando-lista/canonica.md`; apostila em `saidas/aula-35-foreach-montando-lista.html`, na mesma pasta de aula.
- Aula 36: `aulas/programacao-front-end/javascript-na-pratica/36-classes-tarefas-concluidas/canonica.md`; apostila em `saidas/aula-36-classes-tarefas-concluidas.html`, na mesma pasta de aula.
- Aula 37: `aulas/programacao-front-end/javascript-na-pratica/37-filtrando-tarefas-estudo/canonica.md`; apostila em `saidas/aula-37-filtrando-tarefas-estudo.html`, na mesma pasta de aula.
- Aula 38: `aulas/programacao-front-end/javascript-na-pratica/38-revisao-projeto-lista-estudos/canonica.md`; apostila em `saidas/aula-38-revisao-projeto-lista-estudos.html`, na mesma pasta de aula.

Na pasta `saidas/` da aula 38, o projeto de referência derivado da canônica está em `projeto-meus-estudos/` e `projeto-meus-estudos.zip`. O pacote `javascript-20-aulas-e-projeto.zip` reúne as 20 apostilas e os dois arquivos do projeto. O projeto é local e temporário: não inclui persistência, servidor nem publicação.

A produção segue a skill `prof-toni`; a apostila deriva das canônicas pela skill `aula-estatica`. Os adaptadores locais estão em `scratch/javascript-aula-NN/gerar_apostila.py`, com `NN` de `01` a `20` — numeração de produção; cada um gera a aula `NN+18` (local-only); qualquer correção de conteúdo começa na canônica e exige regenerar a apostila. O lote final também pode ser gerado por `scratch/javascript-final/gerar_lote.py`, e os pacotes, por `scratch/javascript-final/empacotar.py`.
