# Imagens — Pull Request: propor mudança sem sobrescrever o código de alguém

Brief neutro de plataforma. Nenhuma imagem existe ainda — prompts prontos para colar num gerador (Gemini Nano Banana / GPT). O `alt` já carrega a informação de verdade (nenhum renderer hoje serve `img/` de conteúdo).

---

## 1. Merge direto vs. Pull Request — onde entra a revisão

- **secao:** Desenvolvimento › Por que não fazer merge direto na main
- **objetivo:** Contrastar visualmente os dois caminhos — commit indo direto pra main sem parar, versus commit passando por uma "estação de revisão" antes de chegar lá — tornando concreto o motivo processual (não técnico) do PR existir.
- **alt:** Diagrama com dois fluxos horizontais. No fluxo de cima, rotulado "Merge direto", uma seta reta e única vai de um ícone de branch até a main, sem nenhuma parada no caminho. No fluxo de baixo, rotulado "Pull Request", a seta que vai da branch até a main passa por uma caixa intermediária desenhada como uma "estação de revisão", com ícones de balão de comentário e um sinal de aprovação (check) antes de finalmente chegar na main.
- **prompt:** "Diagrama técnico plano sobre fundo escuro (#0a0a0a), duas fileiras horizontais empilhadas. Fileira de cima com título pequeno 'Merge direto': uma seta vermelha reta e contínua ligando um retângulo rotulado 'branch' diretamente a um retângulo rotulado 'main', sem nenhum elemento no meio do caminho. Fileira de baixo com título pequeno 'Pull Request': uma seta verde ligando o retângulo 'branch' a uma caixa intermediária desenhada com bordas tracejadas contendo um ícone de balão de comentário e um ícone de check verde, rotulada 'revisão', e só depois dessa caixa uma segunda seta chega até o retângulo 'main'. Tipografia sans-serif técnica, estilo editorial minimalista, vermelho para o caminho sem revisão e verde para o caminho com revisão, fundo escuro uniforme."

## 2. Anatomia de uma mensagem de commit no padrão Conventional Commits

- **secao:** Desenvolvimento › Commits que contam uma história: Conventional Commits
- **objetivo:** Decompor visualmente as partes de uma mensagem de commit bem formada (prefixo de tipo + descrição específica), ajudando o aluno a identificar de cabeça o padrão ao ler ou escrever um commit.
- **alt:** Uma linha de texto de commit dividida em partes coloridas e anotadas: o trecho "feat:" destacado em uma cor com uma seta apontando para a legenda "tipo — classifica a intenção", e o restante do texto "adiciona validação de e-mail no formulário de contato" destacado em outra cor com uma seta apontando para a legenda "descrição — diz especificamente o que mudou".
- **prompt:** "Ilustração técnica plana sobre fundo escuro (#0a0a0a), fonte monoespaçada grande centralizada mostrando o texto: 'feat: adiciona validação de e-mail no formulário de contato'. A palavra 'feat:' está destacada com um fundo verde translúcido e uma seta curva saindo de baixo dela apontando para uma legenda abaixo: 'tipo — classifica a intenção (feat, fix, docs...)'. O restante da frase está destacado com um fundo azul translúcido e uma seta curva apontando para outra legenda: 'descrição — diz especificamente o que mudou'. Estilo técnico-editorial minimalista, tipografia monoespaçada para o commit e sans-serif para as legendas, poucas cores saturadas sobre fundo escuro."
