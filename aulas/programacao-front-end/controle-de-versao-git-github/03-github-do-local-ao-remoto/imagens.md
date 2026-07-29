# Imagens — GitHub: tirando seu repositório do notebook e colocando na nuvem

Brief neutro de plataforma. Nenhuma imagem existe ainda — prompts prontos para colar num gerador (Gemini Nano Banana / GPT). O `alt` já carrega a informação de verdade (nenhum renderer hoje serve `img/` de conteúdo).

---

## 1. Duas portas de entrada: repositório local → GitHub e GitHub → local

- **secao:** Desenvolvimento › Duas portas de entrada pro GitHub (diagrama-progressivo)
- **objetivo:** Consolidar num único visual as duas direções que o texto explica em separado — repositório que nasce local subindo com push, e repositório que já existe no GitHub descendo com clone — pra fixar que são dois pontos de partida diferentes que convergem no mesmo lugar.
- **alt:** Diagrama com um ícone de computador à esquerda e um ícone de nuvem com o logo do GitHub à direita. Uma seta grossa saindo do computador em direção à nuvem está rotulada "git push (repositório nasceu aqui)". Uma segunda seta grossa saindo da nuvem em direção ao computador está rotulada "git clone (repositório já existia lá)". No meio, abaixo das duas setas, uma legenda menor diz "depois da primeira conexão: git push envia, git pull traz".
- **prompt:** "Diagrama técnico plano sobre fundo escuro (#0a0a0a), dois ícones grandes: à esquerda um ícone simples de notebook/computador em cinza-claro, à direita um ícone de nuvem com o contorno do logo do GitHub (Octocat estilizado ou apenas silhueta de nuvem) em branco. Duas setas curvas grossas conectando os dois ícones: uma seta verde saindo do computador em direção à nuvem, rotulada 'git push — nasceu aqui'; uma seta azul saindo da nuvem em direção ao computador, rotulada 'git clone — já existia lá'. Abaixo, uma legenda pequena centralizada: 'depois: push envia, pull traz'. Tipografia sans-serif técnica, estilo editorial minimalista, poucas cores saturadas sobre fundo escuro, sem sombras pesadas."

## 2. Onde mora cada forma de autenticação

- **secao:** Desenvolvimento › Autenticação: como o GitHub sabe que é você
- **objetivo:** Tornar concreta a diferença entre os três métodos citados (senha — bloqueada, SSH, GitHub CLI), mostrando visualmente onde cada credencial fica guardada e por que a senha não participa mais desse fluxo.
- **alt:** Três colunas comparativas. Primeira coluna, "Senha", com um X vermelho grande sobre um ícone de cadeado, indicando que essa via está bloqueada para operações de linha de comando. Segunda coluna, "SSH", com um ícone de duas chaves — uma marcada "privada, fica no seu computador" e outra marcada "pública, vai pro GitHub". Terceira coluna, "GitHub CLI", com um ícone de navegador conectado a um ícone de cofre, rotulado "login pelo navegador, credencial guardada com segurança pelo gh".
- **prompt:** "Infográfico comparativo de três colunas verticais sobre fundo escuro (#0a0a0a). Coluna 1, título 'Senha': um ícone de cadeado cinza com um X vermelho grande sobreposto, e o texto pequeno 'bloqueada desde 2021'. Coluna 2, título 'SSH': dois ícones de chave — uma dourada rotulada 'privada (fica no seu computador)' e uma prateada rotulada 'pública (vai pro GitHub)', conectadas por uma linha pontilhada. Coluna 3, título 'GitHub CLI (gh)': um ícone de janela de navegador conectado por uma seta a um ícone de cofre fechado, com o texto pequeno 'login pelo navegador, credencial guardada com segurança'. Tipografia sans-serif técnica, estilo editorial minimalista, cores distintas por coluna (vermelho para bloqueado, dourado/prateado para SSH, azul para GitHub CLI), fundo escuro uniforme."
