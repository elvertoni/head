# Caminho alternativo: Projeto do ChatGPT no navegador

Usar quando o Toni pedir explicitamente o navegador, quando o Codex estiver
indisponível, ou quando ele quiser comparar dois geradores na mesma aula.

## Arquivos do Projeto

Anexar **apenas** `tools/imagen-generator/prompt.xml`. É a fonte de verdade
visual que o modelo lê.

Não anexar:

- `LEIA-ME_PROMPT_INFOGRAFICOS_v6.txt` — é manual para o Toni, não para o
  modelo; nos arquivos do Projeto ele compete com o XML;
- `logo-prof-toni-coimbra-horizontal.png` — dar a marca ao modelo generativo é
  convite para ele redesenhá-la. A logo entra só no Photoshop.

## Instrução de configuração do Projeto

Este texto vive no campo de instruções do Projeto, não numa mensagem. Ele
repete de propósito o que já está no XML: em 29/07/2026 duas artes saíram com
fundo branco e cantos ocupados, sinal de que o modelo não abriu o XML anexado.
Fixar paleta e zonas reservadas na instrução é o seguro barato contra isso.

```
# INSTRUÇÕES OBRIGATÓRIAS PARA GERAÇÃO DAS ARTES

Siga integralmente o arquivo XML anexado a este projeto: prompt.xml,
versão 6.0, modo arte_base_para_branding_externo.

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

## FUNDO E PALETA (não negociável)
O fundo é SEMPRE escuro azulado: preto-azulado #050810 e navy profundo #0A1220.
Superfícies de cartão #111A2B e #1A2438. Texto principal #ECE8E7.
Ciano/azul #06B6D4 e #3B82F6 é a cor âncora e aparece sempre.
Fundo branco, claro, cinza neutro ou pastel é o defeito D4 e reprova a peça
inteira — nem uma faixa, nem um painel, nem metade do quadro.
Cor nunca é decorativa: verde #10B981 = certo/entrada, âmbar #F59E0B =
atenção/saída, violeta #8B5CF6 = camada avançada, vermelho #EF4444 =
erro/antipadrão, com parcimônia.

## CANTOS SUPERIORES RESERVADOS
Mantenha os dois cantos superiores escuros, calmos e completamente vazios: sem
texto, ícone, ornamento, moldura, trilha de circuito ou qualquer elemento. A
zona reservada é a AUSÊNCIA de conteúdo. Nunca desenhe caixa tracejada,
contorno, marcação, nem escreva "reservado" ou qualquer indicação de onde o
branding será aplicado. O título não pode invadir esses cantos.

## ARTE-BASE PARA BRANDING EXTERNO
Gere APENAS a arte-base. Não desenhe logotipo, wordmark, monograma, o nome
"Prof. Toni Coimbra", identificação de curso, assinatura ou faixa etária.
Esses elementos são aplicados depois no Photoshop.

## VERIFICAÇÃO FINAL OBRIGATÓRIA
Antes de entregar: percorra o checklist_final inteiro, verifique a regra R3
item por item nos 12 defeitos, confirme o perfil sem mistura, confirme os dois
cantos vazios, confirme ausência de branding e leia cada palavra renderizada
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

Execute integralmente o XML v6 no perfil acima e gere a arte-base final.
Não pare no prompt. Mantenha os dois cantos superiores escuros, vazios e
reservados.
```

Anexar `canonica.md` e `imagens.md` junto.

## Ao receber o PNG

O arquivo cai em Downloads com nome do tipo
`ChatGPT Image 29 de jul. de 2026, 17_55_15 (1).png`. Auditar antes de renomear
— renomear primeiro cria a ilusão de que a peça já foi aceita. Depois de
aprovada, mover para `capa.png` ou `img/{slug}.png`.
