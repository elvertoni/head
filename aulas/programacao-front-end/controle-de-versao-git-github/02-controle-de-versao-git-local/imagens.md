# Imagens — Controle de versão: por que cópia manual não escala

Brief neutro de plataforma. Nenhuma imagem existe ainda — prompts prontos para colar num gerador (Gemini Nano Banana / GPT). O `alt` já carrega a informação de verdade (nenhum renderer hoje serve `img/` de conteúdo).

---

## 1. As três áreas do Git: working directory → stage → repositório

- **secao:** Desenvolvimento › Por que existe uma etapa "add" antes do "commit"?
- **objetivo:** Visualizar por que `add` e `commit` são passos separados — mostrar o arquivo se movendo por três áreas distintas (pasta de trabalho, área de stage, histórico do repositório), o que o texto sozinho descreve mas não "mostra" de uma vez.
- **alt:** Diagrama com três caixas em sequência ligadas por setas. Primeira caixa "Pasta de trabalho" contém ícones de arquivo em cinza, representando mudanças ainda não marcadas. Uma seta rotulada "git add" leva à segunda caixa, "Área de stage", com os mesmos ícones agora em amarelo, marcados para entrar na próxima fotografia. Uma seta rotulada "git commit" leva à terceira caixa, "Histórico do repositório", mostrando um círculo verde carimbado com data e mensagem, representando o commit já gravado permanentemente.
- **prompt:** "Diagrama técnico plano, três caixas retangulares em sequência horizontal conectadas por setas, sobre fundo escuro (#0a0a0a). Caixa 1 rotulada 'Pasta de trabalho' com pequenos ícones de arquivo em cinza-claro. Seta entre caixa 1 e 2 rotulada 'git add'. Caixa 2 rotulada 'Área de stage' com os mesmos ícones agora em amarelo/dourado. Seta entre caixa 2 e 3 rotulada 'git commit'. Caixa 3 rotulada 'Histórico do repositório' com um círculo verde contendo um ícone de carimbo, ao lado um pequeno cartão mostrando 'data + mensagem'. Tipografia sans-serif técnica, poucas cores saturadas (cinza, amarelo, verde) sobre fundo escuro, sem gradientes nem sombras pesadas, estilo editorial minimalista."

## 2. Cópias manuais vs. linha do tempo de commits

- **secao:** Desenvolvimento › O problema que toda cópia manual esconde
- **objetivo:** Contrastar visualmente a bagunça de arquivos duplicados (v1, v2, final, final-agora-vai) com uma linha do tempo limpa de commits — reforça o gancho de abertura com uma imagem memorável antes de entrar na solução técnica.
- **alt:** Comparação lado a lado. À esquerda, uma pilha desorganizada de ícones de arquivo com nomes sobrepostos e ilegíveis: "projeto.html", "projeto-v2.html", "projeto-final.html", "projeto-final-AGORA-VAI.html", transmitindo confusão. À direita, uma linha do tempo horizontal limpa com três círculos conectados por uma linha reta, cada círculo com um número de ordem e uma mensagem curta abaixo, representando commits organizados em sequência.
- **prompt:** "Ilustração plana dividida em duas metades sobre fundo escuro (#0a0a0a). Metade esquerda com título pequeno 'Cópias manuais': uma pilha desorganizada e levemente inclinada de ícones de documento, com etiquetas de texto sobrepostas e bagunçadas simulando nomes de arquivo como 'v1', 'v2', 'final', 'final-agora-vai', em tons de vermelho e laranja transmitindo caos. Metade direita com título pequeno 'Git': uma linha do tempo horizontal reta e limpa com três círculos verdes numerados 1, 2, 3 conectados por uma linha fina, cada círculo com uma legenda curta abaixo (ex.: 'estrutura inicial', 'ajuste no CSS', 'corrige bug'). Tipografia sans-serif técnica, contraste claro entre o caos (esquerda) e a ordem (direita), sem elementos decorativos supérfluos."
