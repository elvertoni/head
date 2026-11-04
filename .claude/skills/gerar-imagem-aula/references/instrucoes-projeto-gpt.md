# Caminho alternativo: Projeto do ChatGPT no navegador

Usar quando o Toni pedir explicitamente o navegador, quando o Codex estiver
indisponível, ou quando ele quiser comparar dois geradores na mesma aula.

## Arquivos do Projeto

Anexar **apenas** `tools/imagen-generator/prompt.xml`. É a fonte de verdade
visual que o modelo lê.

Não anexar:

- `LEIA-ME_PROMPT_INFOGRAFICOS_v8.txt` — é manual para o Toni, não para o
  modelo; nos arquivos do Projeto ele compete com o XML;
- `logo-prof-toni-coimbra-horizontal.png` — dar a marca ao modelo generativo é
  convite para ele redesenhá-la. A peça é final e não leva marca (v8).

## Instrução de configuração do Projeto

Este texto vive no campo de instruções do Projeto, não numa mensagem. Ele
repete de propósito o que já está no XML: em 29/07/2026 duas artes saíram com
fundo branco, sinal de que o modelo não abriu o XML anexado. Fixar paleta,
margem e ausência de marca na instrução é o seguro barato contra isso.

```
# INSTRUÇÕES OBRIGATÓRIAS PARA GERAÇÃO DAS ARTES

Siga integralmente o arquivo XML anexado a este projeto: prompt.xml,
versão 8.0, modo arte_final_sem_branding.

A cada solicitação serão enviados: canonica.md, imagens.md, o PERFIL desejado
e o título exato da aula-alvo.

## PASSO 0 — DECLARAÇÃO OBRIGATÓRIA
1. Declare o perfil: CAPA ou INFOGRAFICO.
2. Reafirme o título exato da aula-alvo.
3. Só então gere.

Uma solicitação = UMA peça, de UM perfil só. É proibido empilhar uma capa e um
infográfico no mesmo quadro, ou pendurar um painel de comparação abaixo de uma
capa. Se o perfil é CAPA, a peça termina na faixa de síntese do rodapé — nada
vem depois dela. Perfil trocado ou fundido é o defeito D12.

## PERFIL CAPA
Proporção 3:2, alvo 1536x1024. De 4 a 10 blocos. Cada bloco: rótulo em
CAIXA-ALTA + microparágrafo de 1 a 3 linhas + ícone linear. Subtítulo
obrigatório sob o título. Faixa de síntese full-width no rodapé, obrigatória.
Miolo ocupando 70% a 90% da altura útil.

## PERFIL INFOGRAFICO
Proporção 16:9. De 2 a 5 blocos. Somente rótulos curtos: no máximo 8 na arte
inteira, cada um com até 4 palavras. Proibido: subtítulo, faixa de rodapé,
parágrafo, microparágrafo, texto explicativo. Miolo ocupando 60% a 80% da
altura útil.

## FUNDO E PALETA — VOLTA ATELIER (não negociável)
O fundo é SEMPRE grafite neutro quase preto: #141414, com faixas #0D0D0D.
Painéis #1C1C1E e #232326, filetes de 1 px #2E2E31. Texto principal osso
#F4F3F0, secundário #8E8E95.
O vermelho signal #FB3732 é a cor âncora: palavra-chave do título, seta
principal, badges numerados. Aparece sempre, com parcimônia.
Fundo branco, claro, navy, azulado ou colorido é o defeito D4 e reprova a peça.
Degradê, brilho (glow), vidro, neon e sombra colorida são o defeito D13.
Cor nunca é decorativa: esmeralda #10B981 = certo/entrada/conclusão, âmbar
#FFA31A = atenção/saída, azul volt #3B49E4 = camada de apoio/processamento,
azul-céu #38BDF8 = definição (pontual). Erro/antipadrão = painel acinzentado
com ✗ vermelho e rótulo (ERRADO, EVITE).
Estilo: brutalismo editorial refinado — cor chapada, grade, filetes finos,
título em grotesca pesada (tipo Archivo Black), rótulos em mono caixa-alta.

## MARGEM E TOPO
Margem segura de 8% em todas as bordas. O título fica no topo, usando a
largura útil, sem faixa vazia acima e sem deixar os cantos superiores vazios
como se fossem reservados. Nunca desenhe caixa tracejada ou vazia nem escreva
"reservado", "logo aqui" ou qualquer placeholder.

## PEÇA FINAL, SEM MARCA
A imagem é publicada exatamente como sair, sem edição posterior. Não desenhe
logotipo, wordmark, monograma, as letras TC, o nome "Prof. Toni Coimbra",
identificação de curso, assinatura ou faixa etária.

## VERIFICAÇÃO FINAL OBRIGATÓRIA
Antes de entregar: percorra o checklist_final inteiro, verifique a regra R3
item por item nos 13 defeitos, confirme o perfil sem mistura, confirme os dois
margem segura e o título no topo, confirme ausência de marca e leia cada palavra renderizada
conferindo se existe em português e está escrita certo.
Qualquer ocorrência: REGENERE. Não entregue imagem com ressalva ou aviso.

## ENTREGA
Entregue a IMAGEM FINAL EM PNG, já renderizada, na maior resolução possível.
Não entregue apenas o prompt em inglês, uma descrição, um roteiro ou uma
confirmação sem a imagem. A tarefa só termina quando o PNG for entregue.
```

## Mensagem de cada rodada

```
PERFIL: {CAPA|INFOGRAFICO}
AULA: {título exato da aula-alvo}

Execute integralmente o XML v8 no perfil acima e gere a peça final.
Não pare no prompt. Sem marca, sem placeholder e com o título no topo.
```

Anexar `canonica.md` e `imagens.md` junto.

## Ao receber o PNG

O arquivo cai em Downloads com nome do tipo
`ChatGPT Image 29 de jul. de 2026, 17_55_15 (1).png`. Auditar antes de renomear
— renomear primeiro cria a ilusão de que a peça já foi aceita. Depois de
aprovada, mover para `capa.png` ou `img/{slug}.png`.
