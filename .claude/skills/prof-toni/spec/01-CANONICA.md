# 01-CANONICA — Formato da Aula Canônica

> **Versão:** 1.0 · **Herda de:** METODO.md v1.1 §5 (validado em uso real)
> Leia este arquivo antes de gerar ou editar qualquer `canonica.md`. A calibração de qualidade vem de `spec/EXEMPLO-canonica.md` — leitura obrigatória antes da primeira geração de cada sessão.

---

## 1. O que é

Um arquivo Markdown estendido, **neutro de plataforma**, que captura toda a inteligência pedagógica de uma aula de 50 min. Qualquer LLM que leia esta spec produz a mesma estrutura. Nenhum elemento aqui assume ProfessorDash, HTML ou qualquer renderer.

A Canônica é *mais rica* que qualquer saída. As ferramentas de renderização (skill `aula-estatica`, ProfessorDash, futuras) só sabem traduzir o que está aqui — nunca inventam, nunca enriquecem além disto.

## 2. Frontmatter (schema do acervo)

```yaml
---
# — identidade pedagógica —
titulo: Manifesto Ágil e os 4 valores
tema: Metodologias Ágeis
disciplina: engenharia-de-software      # slug, igual ao da pasta
serie: 2ª
prerequisitos: [Ciclo de vida de software]   # ou []
objetivos:
  - Explicar os 4 valores do Manifesto Ágil
  - Diferenciar abordagem ágil de cascata

# — posição no acervo —
trilha: fundamentos-ageis               # slug da sequência didática
ordem: 1                                # posição na trilha (= NN da pasta)
slug: manifesto-agil-e-os-4-valores     # = slug da pasta {NN-slug} e do manifesto

# — proveniência e ciclo de vida —
modo_origem: tema                       # seed | material | tema
fontes: []                              # caminhos em fontes/ ou URLs; [] no Modo Tema
revisao: false                          # true quando nasceu de origem COM correções aplicadas
status: rascunho                        # rascunho | aprovada | publicada
versao: 1
atualizado_em: 2026-06-11
---
```

Regras do frontmatter:
- **Obrigatório e completo** — aula sem frontmatter íntegro reprova no checklist.
- `disciplina` e `trilha` são slugs minúsculos idênticos aos das pastas (`aulas/{disciplina}/{trilha}/`).
- `slug` é idêntico ao `{slug}` da pasta `{NN-slug}` e ao `slug` do manifesto. `ordem` = `NN` da pasta.
- `status` só vira `aprovada` por ação explícita do Toni; `publicada` quando alguma saída foi gerada e distribuída.
- Toda edição de conteúdo incrementa `versao` e atualiza `atualizado_em`. Saídas em `saidas/` geradas com `versao` anterior são consideradas vencidas.

### Contrato de import do portal (INVIOLÁVEL)

O ProfessorDash importa lendo `manifesto.json` + `aulas/**/canonica.md`. A geração
SEMPRE produz saída compatível com este contrato (detalhe completo em `AGENTS.md`
§5.1):

- **Mínimo obrigatório no frontmatter:** `titulo`, `disciplina`, `trilha`, `ordem`,
  `slug`, `status: aprovada`, `versao`, `atualizado_em` (data ISO `YYYY-MM-DD`).
- **Só importa `status: aprovada`.** Aula sem entrada em `lessons[]` do manifesto não importa.
- **Caminho:** `aulas/{disciplina}/{trilha}/{NN}-{slug}/canonica.md`, com `NN` = `ordem`
  em 2 dígitos e `{slug}` casando disciplina/trilha/ordem/slug do manifesto.
- **Bump obrigatório:** o portal só re-importa uma aula existente se `versao` OU
  `atualizado_em` mudou. Editou conteúdo de aula publicada → incremente `versao`
  (ou avance `atualizado_em`), senão a edição não aparece no portal.
- **Regerar o manifesto sempre** que adicionar/aprovar/editar aula:
  `python tools/gerar_manifesto.py` (valide com `--check`). Nunca editar
  `manifesto.json` à mão.

## 3. Anatomia (ordem fixa)

1. **Frontmatter YAML** — acima.
2. **Gancho** — 1 parágrafo de abertura que conecta o tema à realidade do aluno (14–18). Texto puro, sem bloco, sem heading.
3. **`## Objetivos`** — o que o aluno saberá/fará ao final. Verbos observáveis.
4. **`## Pré-requisitos`** — o que precisa saber antes. Pode ser "nenhum".
5. **`## Desenvolvimento`** — o corpo. Subdividido em `###` por ideia. Aqui moram conceitos, comparações, exemplos, callouts e os blocos do catálogo.
6. **`## Prática`** — atividade executável (≤15 min). Tipicamente codificada **no VSCode da máquina** (enunciado + fence de código de referência, não bloco interativo). **Quando a turma ainda não tem base de código** (ex.: 1ª série iniciante, tema de fundamentos), a prática principal vira **desplugada** (atividade concreta sem computador) e o trecho no VSCode entra como *extensão opcional* — nunca pré-requisito.
7. **`## Avaliação`** — verificação formativa. Tipicamente um `quiz`.
8. **`## Fechamento`** — resumo (3–4 pontos) + gancho da próxima aula.
9. **`:::roteiro`** — fala do professor. **Nunca vai para material compartilhado.**

Tempo é **implícito** na sequência — não há campo de cronometragem. A regra dos 50 min é honrada pelo volume, auditado pela rubrica (`spec/02-RUBRICA.md`).

## 4. Conteúdo rico — o que a Canônica PODE usar livremente

Dentro de **qualquer bloco** vale Markdown pleno:

- `**negrito**`, `*itálico*`, `` `código inline` ``
- Listas, tabelas, links
- Blocos de código com destaque de linguagem
- Callouts semânticos aninhando tudo acima

Achatamento, se necessário, é problema do **adaptador** — nunca de quem escreve a Canônica.

## 5. Callouts semânticos (catálogo FECHADO — 6 tipos)

Sintaxe `:::tipo` (legível e portável). Conteúdo interno é Markdown rico.

| Tipo | Uso pedagógico |
|---|---|
| `:::conceito` | definição-chave |
| `:::exemplo` | caso concreto, analogia memorável |
| `:::importante` | comparação crítica, ponto que cai |
| `:::atencao` | erro comum real e diagnosticável |
| `:::dica` | ponte teoria↔prática profissional |
| `:::curiosidade` | contexto histórico, gancho de interesse |

```
:::conceito Acoplamento
Mede o quanto um módulo **depende** de outro. Quanto menor, mais fácil mudar
uma parte sem quebrar o resto.
:::
```

## 6. Catálogo de interativos (FECHADO — 2 blocos)

> Regra de ouro: um interativo só existe se faz um trabalho que o texto estático faria *pior*. Decoração é proibida (teste anti-decoração na rubrica).
>
> **Código não é interativo da Canônica.** Trechos de código são fence Markdown normal (com destaque de linguagem). O aluno escreve e roda **no VSCode da máquina** — ferramenta profissional real, não sandbox de browser.

### 6.1 `quiz` — feedback imediato é o ato de aprender

````markdown
```quiz
- pergunta: O que o Manifesto Ágil prioriza sobre processos e ferramentas?
  alternativas:
    - texto: Documentação extensa
    - texto: Indivíduos e interações
      correta: true
    - texto: Contratos rígidos
    - texto: Seguir o plano inicial
  feedback: >
    Os 4 valores sempre colocam o lado humano e adaptável à esquerda.
    "Processos e ferramentas" é o lado que se cede quando há conflito.
```
````

Regras: exatamente 1 alternativa com `correta: true`; `feedback` explica o porquê (aparece após a resposta).

### 6.2 `diagrama-progressivo` — controla carga cognitiva por camadas

````markdown
```diagrama-progressivo
titulo: Como uma requisição HTTP viaja
camadas:
  - rotulo: 1. Navegador
    conteudo: O usuário digita a URL e o navegador monta a requisição.
  - rotulo: 2. DNS
    conteudo: O domínio é traduzido para um endereço IP.
  - rotulo: 3. Servidor
    conteudo: O servidor processa e devolve a resposta.
```
````

Cada camada revela-se sob comando do aluno — evita despejar a complexidade toda de uma vez.

## 7. Roteiro do professor

```
:::roteiro
Abrir perguntando quem já refez um trabalho inteiro por mudança de última hora.
Conectar essa dor ao "responder a mudanças". Não ler os valores — fazer eles deduzirem.
:::
```

Visibilidade: ProfessorDash renderiza em modo professor; **apostila/standalone omite sempre** — é a cola do professor, não vai para material compartilhado. `:::roteiro` nunca contém conteúdo essencial ao aluno.

## 8. Restrições da Canônica

- Frontmatter obrigatório e completo (seção 2).
- **Sem `#` no corpo** — o título vem do frontmatter `titulo`; o corpo começa direto no Gancho.
- Só os 6 callouts e 2 interativos oficiais. Catálogo cresce apenas por decisão explícita do Toni, nunca por iniciativa do agente.
- Interativo sem justificativa pedagógica = remover (auditado na rubrica).
- Nunca reproduzir trechos longos da fonte: reescrever com voz própria.

## 9. Calibração de qualidade

Antes da primeira Canônica de cada sessão, leia o exemplo-ouro em `spec/EXEMPLO-canonica.md`. Ele é o padrão calibrador de:

- **Voz** — segunda pessoa ("você"), tom de professor experiente conversando.
- **Profundidade** — parágrafos densos de verdade, não tópicos esticados.
- **Analogias** — concretas e memoráveis, do mundo do aluno de 14–18.
- **Exemplos** — diagnosticáveis, com erro comum real.

Sintomas de saída abaixo do padrão (detectou → refaça antes de auditar): parágrafos rasos; voz neutra de manual ("é importante notar que…", "vamos explorar…"); ausência de analogia memorável; exemplos genéricos sem contexto; quiz que testa trivialidade.
