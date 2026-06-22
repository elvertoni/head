# Brief de imagens — Aula 31: A Memória do Computador - Parte 1 - a Cache

## 1. Cache, RAM e disco por distância da CPU
- **secao:** Desenvolvimento › "Por que ser rápida e pequena ao mesmo tempo"
- **arquivo:** img/cache-distancia-cpu.png
- **objetivo:** Mostrar a cache como o cantinho ao alcance da mão (mais perto e mais rápido), a RAM como a mesa e o disco como a gaveta — ligando proximidade à velocidade.
- **alt:** A CPU no centro, com a cache colada nela, a RAM um pouco mais distante e o disco mais longe ainda, indicando que mais perto significa mais rápido.
- **prompt:** Ilustração educacional vetorial flat, proporção 16:9, fundo claro. No centro, um chip de CPU. Coladinho a ele, uma caixinha pequena rotulada "cache" com um ícone de raio. Um pouco mais afastada, uma caixa média "RAM". Bem mais distante, uma caixa grande "disco". Anéis concêntricos sutis indicam a distância crescente; uma legenda visual mostra "mais perto = mais rápido, menor e mais caro". Paleta índigo e azul-petróleo com acento laranja, estilo limpo de apostila, rótulos curtos.

## 2. Cache hit × cache miss
- **secao:** Desenvolvimento › diagrama "O caminho de uma busca de dado"
- **arquivo:** img/cache-hit-miss.png
- **objetivo:** Representar os dois desfechos de uma busca: dado na cache (hit, rápido) ou ausente (miss, vai à RAM e copia de volta). Visual de fluxo deixa o conceito tangível.
- **alt:** Fluxo da CPU procurando um dado: se está na cache, acesso imediato (acerto); se não está, busca na RAM e copia para a cache (falta).
- **prompt:** Ilustração educacional vetorial flat, proporção 16:9, fundo claro. À esquerda, uma CPU faz uma pergunta a uma caixa "cache". Dois caminhos saem dela: caminho de cima "hit" com um sinal de certo verde e uma seta curta e rápida (dado encontrado). Caminho de baixo "miss" com um X, seguindo até uma caixa "RAM" e voltando uma cópia do dado para a cache. Paleta índigo e azul com acento laranja e um toque de verde para o acerto, estilo didático minimalista, rótulos curtos.
