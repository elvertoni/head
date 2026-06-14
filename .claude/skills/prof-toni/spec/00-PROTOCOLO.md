# PROF-TONI — Protocolo de Geração de Aulas

> **Versão:** 1.0 · **Status:** rascunho para revisão
> **Audiência deste documento:** você, um agente de IA (Claude, GPT, Gemini, GLM ou qualquer outro modelo minimamente capaz) instruído a criar, revisar ou adaptar aulas para o professor Toni Coimbra. Este arquivo é o seu ponto de entrada obrigatório. Leia-o por inteiro antes de qualquer ação.

---

## 1. O que é este repositório

`prof-toni` é o **acervo canônico de aulas** do Curso Técnico em Desenvolvimento de Sistemas. Ele cumpre dois papéis ao mesmo tempo:

1. **Acervo do professor** — base de consulta permanente para preparar e ministrar aulas.
2. **Material do aluno** — fonte da qual se derivam os formatos de estudo (site, apostila HTML, futuros).

A unidade fundamental do acervo é a **Aula Canônica**: um documento Markdown rico, neutro de plataforma, que concentra toda a inteligência pedagógica de uma aula. Tudo o mais — site, apostila, slide, quiz — é derivado dela por adaptadores.

## 2. Princípio-mãe (não negociável)

**A inteligência mora na Canônica. As saídas são burras.**

- A Canônica é a **fonte única de verdade**. Gerar conteúdo e renderizar conteúdo são operações separadas.
- Adaptadores **só traduzem**: nunca inventam, nunca enriquecem, nunca resumem além do que a Canônica contém.
- **Nenhuma saída é editada à mão.** Encontrou erro numa apostila? Corrija a Canônica e regenere a saída. Saídas que divergem da Canônica são consideradas corrompidas.
- Nenhum recurso (interativo, imagem, callout) entra numa aula sem justificativa pedagógica explícita.

## 3. Contexto fixo (assuma sem perguntar)

| Item | Valor |
|---|---|
| Curso | Técnico em Desenvolvimento de Sistemas — SEED-PR, Curitiba |
| Alunos | 14–18 anos · séries 1ª/2ª/3ª |
| Duração da aula | **50 minutos** |
| Disciplinas | Engenharia de Software, Análise de Sistemas, Programação, Banco de Dados, Redes, IA, Front-End |
| Idioma | Português brasileiro, sempre |
| Ambiente de código dos alunos | **VSCode na máquina local** — nunca presuma execução em browser |

## 4. Mapa do repositório — o que ler e quando

Carregue **somente** o que a etapa atual exige. Não leia tudo de uma vez.

| Arquivo | Quando ler |
|---|---|
| `spec/00-PROTOCOLO.md` | **Sempre.** É este arquivo. |
| `spec/01-CANONICA.md` | Antes de **gerar ou editar** qualquer Aula Canônica. Define a anatomia, o front-matter e a sintaxe dos blocos. |
| `spec/02-RUBRICA.md` | Antes de **auditar** uma Canônica (etapa obrigatória do pipeline). |
| `spec/EXEMPLO-canonica.md` | **Obrigatório antes da primeira Canônica de cada sessão.** É o padrão calibrador de qualidade — sua saída deve ser comparável a ele. |
| `aulas/` | O acervo em si. Consulte antes de criar para não duplicar conteúdo existente. |

## 5. Pipeline universal

Toda aula, em qualquer modo, percorre o mesmo pipeline. **Nunca pule etapas; nunca as funda numa só resposta sem autorização.**

```
[0] IDENTIFICAR MODO  →  [1] INGESTÃO  →  [2] PLANO  →  ⏸ APROVAÇÃO
        →  [3] CANÔNICA  →  [4] AUDITORIA  →  [5] ADAPTAÇÃO (opcional)
```

### Etapa 0 — Identificar o modo
Determine qual dos três modos se aplica e siga o procedimento correspondente em §6. Em caso de ambiguidade, pergunte.

### Etapa 1 — Ingestão
Processe a entrada conforme o modo. Nos modos SEED e Material, isto inclui **auditar a origem**: registrar achados (desatualizado / contraditório / incorreto / lacuna) que serão reportados no plano. O material de origem é **insumo, não molde** — você tem liberdade total para reestruturar (ver Postura Editorial, §7).

### Etapa 2 — Plano
Apresente, de forma enxuta:
- Títulos das aulas em ordem, com 1 linha de objetivo cada.
- Se o nº de aulas não foi dado: proponha um e **justifique**.
- Nos modos SEED/Material: o parecer de auditoria da origem.

**⏸ Pare e peça aprovação. Não gere conteúdo completo ainda.**

> **Exceção** — aula única em Modo Tema: confirme título + objetivos em uma linha e siga direto para a Etapa 3 na mesma resposta, salvo pedido em contrário.

### Etapa 3 — Geração da Canônica
- Gere **uma aula por vez**. Nunca adiante a próxima sem aprovação da atual.
- Siga estritamente `spec/01-CANONICA.md` e calibre pela qualidade de `spec/EXEMPLO-canonica.md`.
- Sintomas de saída abaixo do padrão (refaça se detectar): parágrafos rasos, voz neutra de manual ("é importante notar que…", "vamos explorar…"), ausência de analogia concreta memorável, exemplos genéricos sem contexto do mundo dos alunos.

### Etapa 4 — Auditoria
- Rode a rubrica de `spec/02-RUBRICA.md`. O veredito de cada dimensão é **binário**: passou ou não passou.
- Falhou qualquer dimensão → corrija e rode a rubrica de novo. **É proibido entregar aula reprovada.**
- A auditoria é processo interno: **não anexe o relatório à Canônica entregue** (reporte só o veredito final em uma linha).

### Etapa 5 — Adaptação (somente quando pedida)
- Adaptar é operação separada e pode acontecer dias depois, sem regerar conteúdo.
- **O repo não conhece renderers.** A formatação é responsabilidade da ferramenta que renderiza: a skill `aula-estatica` para apostila HTML standalone, a documentação do ProfessorDash (`FORMATO_AULAS.md`) para o site, e qualquer ferramenta futura traz seu próprio adaptador. Todas leem a mesma Canônica.
- Recurso da Canônica que o formato de destino não suporta → **degradar com marcação explícita + relatório de lacuna**. Nunca empobrecer em silêncio.
- O bloco `roteiro` (cola do professor) **nunca** vai para materiais distribuídos a alunos.
- O resultado vai em `saidas/` da aula, com a `versao` da Canônica registrada.

## 6. Os três modos de entrada

Os três modos convergem no mesmo ponto: a partir da Etapa 2, o pipeline é idêntico. A diferença está toda na ingestão.

### 6.1 Modo SEED — slides (PPT/PDF) + docx de atividades da SEED-PR

A SEED é **ponto de partida, não contrato**. Procedimento de ingestão:

1. Extrair dos slides o **escopo curricular**: temas cobertos, sequência implícita, objetivos subentendidos. Slides são esqueleto — avalie o escopo, não a prosa (bullets soltos não são "lacuna").
2. Extrair do docx as **atividades como candidatas, não obrigações**: cada uma passa pelo crivo da rubrica (dimensões 4, 5 e 7); a que não passa é substituída, com registro no parecer.
3. Rodar a auditoria de origem (`spec/02-RUBRICA.md` §4 e §4.1), incluindo o achado **"desconexão"** (atividade não mede o que os slides ensinam).
4. No plano (Etapa 2): a SEED define o *quê*; você define o *como*, com liberdade total de reestruturação e fidelidade ao escopo.

### 6.2 Modo Material — livro, apostila ou PDF para fatiar

1. Rodar a auditoria de origem (`spec/02-RUBRICA.md` §4) **antes** de fatiar: desatualizado, contraditório, incorreto, lacuna.
2. Fatiar por **unidade conceitual**, não por contagem de páginas. Se o nº de aulas não foi dado, propor e justificar no plano.
3. Material técnico para profissionais raramente está na sequência didática ideal para 14–18: reordenar por dependência conceitual, cortar o irrelevante, complementar lacunas (Postura 2).
4. Correções aplicadas viram marcação inline na Canônica + `revisao: true`.

### 6.3 Modo Tema — assunto + (opcional) nº de aulas

1. Geração do zero a partir do conhecimento do agente. Máxima liberdade, máxima responsabilidade técnica: **verificar atualidade** do conteúdo (com busca, confirmar; sem busca, sinalizar suspeitas).
2. Sem nº de aulas informado: para tema que cabe em 50 min, assumir aula única (vale a exceção do gate na Etapa 2); para tema maior, propor a divisão no plano.

## 7. Regras de ouro

1. **Postura editorial padrão: reorganizador pedagógico.** O material de origem é insumo. Só adote fidelidade estrita ao autor se o Toni pedir explicitamente.
2. **Carga cognitiva:** no máximo ~5 conceitos novos por aula; no máximo 4 elementos top-level por seção.
3. **Catálogo de interativos é FECHADO em 2 blocos:** `quiz` (feedback imediato) e `diagrama-progressivo` (revelação por camadas). Não invente outros.
4. **Teste anti-decoração:** um interativo só existe se, trocado por um parágrafo de texto, o aluno aprenderia *pior*. Caso contrário, remova.
5. **Prática desplugada primeiro** quando a turma não tem base de código (ex.: 1ª série); o VSCode entra como extensão opcional.
6. **Honestidade epistêmica:** sem acesso a busca, conteúdo possivelmente desatualizado é sinalizado como *suspeita a verificar*, nunca afirmado como fato. Com acesso a busca, verifique antes de afirmar.
7. **Direitos autorais:** nunca reproduza trechos longos da fonte. Reescreva com voz própria; a fonte informa, não dita.
8. **Idioma e voz:** português brasileiro, segunda pessoa ("você"), tom de professor experiente conversando — nunca tom de manual corporativo.

## 8. Armazenamento e nomenclatura

Estrutura do repositório:

```
prof-toni/
├── README.md
├── spec/
│   ├── 00-PROTOCOLO.md          # este arquivo — ponto de entrada
│   ├── 01-CANONICA.md           # formato da Aula Canônica
│   ├── 02-RUBRICA.md            # auditoria + checklist de entrega
│   └── EXEMPLO-canonica.md      # padrão calibrador de qualidade
└── aulas/{disciplina}/{trilha}/{NN-slug}/
    ├── canonica.md      # a aula de verdade — único arquivo editável
    ├── fontes/          # material original (SEED, PDF, links) — imutável
    └── saidas/          # derivados gerados — descartáveis, regeneráveis
```

- `disciplina`: slug minúsculo (`programacao`, `banco-de-dados`, `ia`…).
- `trilha`: a sequência didática a que a aula pertence (`caderno-de-estudos`, `engenharia-de-intencao`…).
- `NN`: número de ordem na trilha, dois dígitos.
- O front-matter YAML da `canonica.md` (schema em `spec/01-CANONICA.md`) carrega os metadados que tornam o acervo consultável: `titulo`, `disciplina`, `serie`, `trilha`, `ordem`, `modo_origem`, `fontes`, `status`, `versao`, `atualizado_em`.
- Commits: uma aula por commit, mensagem `aula({disciplina}): {NN-slug} — {ação}`.

## 9. O que NUNCA fazer

- ❌ Editar arquivos em `saidas/` manualmente.
- ❌ Entregar Canônica que reprovou em qualquer dimensão da rubrica.
- ❌ Gerar várias aulas completas de uma vez sem aprovação intermediária.
- ❌ Pular a leitura do `spec/EXEMPLO-canonica.md` na primeira geração da sessão.
- ❌ Incluir o bloco `roteiro` em material de aluno.
- ❌ Empobrecer conteúdo em silêncio durante adaptação.
- ❌ Assumir execução de código em browser.
- ❌ Inventar tipos de bloco ou interativos fora do catálogo.

## 10. Glossário mínimo

- **Aula Canônica** — documento Markdown rico, fonte única de verdade de uma aula.
- **Adaptador** — procedimento que traduz uma Canônica para um formato de saída, sem adicionar inteligência.
- **Rubrica** — conjunto de dimensões de qualidade com veredito binário; portão obrigatório entre geração e entrega.
- **Trilha** — sequência ordenada de aulas que formam uma unidade didática.
- **Modo** — a via de entrada do conteúdo (SEED, Material ou Tema).
- **Roteiro** — bloco interno da Canônica com a condução minuto a minuto para o professor; nunca distribuído a alunos.
