# 02-RUBRICA — Auditoria Técnico-Pedagógica

> **Versão:** 1.0 · **Herda de:** METODO.md v1.1 §6 + §10.1 (validado em uso real)
> Leia este arquivo antes de auditar qualquer Canônica (Etapa 4 do pipeline). A rubrica é o que transforma "aula gerada" em "aula auditada". Critérios **verificáveis** (sinal de falha claro), não impressões. A rubrica é o auditor independente do gerador.

---

## 1. Quando a rubrica roda (três papéis)

1. **Como guia** — durante a geração da Canônica, orientando as escolhas.
2. **Como auditor** — depois de gerada, a aula é checada contra os critérios; falha = corrige antes de entregar.
3. **Sobre a origem** — nos modos SEED e Material, a rubrica audita o **conteúdo-fonte** antes do fatiamento. É daqui que saem os achados do parecer do plano (Etapa 2).

## 2. As 7 dimensões (cada uma com gatilho de falha)

| # | Dimensão | Passa quando… | **Falha quando…** |
|---|---|---|---|
| 1 | **Correção conceitual** | tecnicamente correto e atual | há erro factual, conceito obsoleto, ou versão/prática depreciada apresentada como vigente |
| 2 | **Adequação 14–18** | vocabulário e exemplos acessíveis a 1º–3º ano técnico | pressupõe bagagem profissional, jargão não explicado, ou exemplo do "mundo corporativo adulto" sem ponte |
| 3 | **Carga cognitiva** | ≤ ~5 conceitos novos; ≤ 4 elementos top-level por seção `##`; cabe em 50 min | parede de texto, conceitos demais, seção sobrecarregada |
| 4 | **Teoria↔prática** | ≥1 ponte explícita com a profissão (`:::dica`) | conceito flutua sem aplicação concreta |
| 5 | **Qualidade dos exemplos** | ≥1 exemplo concreto/analogia; no prático, ≥1 erro comum **real e diagnosticável** (`:::atencao`) | exemplo genérico, erro inventado ou improvável |
| 6 | **Justificativa do interativo** | cada bloco do catálogo ensina o que o estático ensinaria pior | interativo decorativo → *remover* (anti-*seductive-details*) |
| 7 | **Alinhamento da avaliação** | o `quiz` mede exatamente os `objetivos` do frontmatter | quiz testa trivialidade ou algo não ensinado na aula |

## 3. O teste do interativo (dimensão 6, detalhada)

Para cada `quiz` / `diagrama-progressivo`, responder **sim** a:

> *"Se eu trocar este bloco por um parágrafo de texto, o aluno aprende pior?"*

Se a resposta é não, o bloco é decoração e sai. Sem exceção.

## 4. Auditoria de origem (modos SEED e Material)

Antes de fatiar ou reestruturar, a rubrica varre o material de origem e classifica cada achado:

- **Desatualizado** — prática/versão/ferramenta superada → reportar + ensinar a vigente.
- **Contraditório** — o material discorda de si mesmo ou de consenso técnico → reportar + adotar a correta.
- **Incorreto** — erro factual → reportar + corrigir.
- **Lacuna** — falta algo essencial para a faixa 14–18 → complementar (Postura 2).

Cada achado entra no **parecer do plano** (Etapa 2); a correção aplicada vira **marcação inline** na Canônica (`:::atencao` ou nota de revisão) e liga `revisao: true` no frontmatter.

### 4.1 Particularidades do Modo SEED

O material da SEED-PR (slides + docx de atividades) tem natureza diferente de um livro, e a auditoria reflete isso:

- **Slides são esqueleto, não texto** — bullets soltos não são "lacuna" por si; a lacuna é pedagógica: o que falta para o tema ficar ensinável em 50 min. Avalie o *escopo curricular implícito*, não a prosa.
- **Achado extra: "desconexão"** — quando a atividade do docx não mede o que os slides ensinam (equivalente da dimensão 7 aplicado à origem) → reportar + redesenhar a atividade alinhada aos objetivos.
- **Atividades do docx são candidatas, não obrigações** — cada uma passa pelo mesmo crivo das dimensões 4, 5 e 7; o que não passa é substituído, com registro no parecer.
- A SEED define o *quê* (escopo curricular); a rubrica e a Postura 2 definem o *como*. Liberdade total de reestruturação, fidelidade ao escopo.

### 4.2 Honestidade epistêmica

A detecção de desatualização depende do conhecimento do modelo. Com acesso a busca/web, **confirmar antes de afirmar** "está obsoleto". Sem busca, sinalizar como *suspeita a verificar*, nunca como fato.

## 5. Checklist de entrega da Canônica

Rodar antes de entregar toda Canônica. Veredito binário: falhou um item → corrige e re-roda.

- [ ] Frontmatter completo conforme `spec/01-CANONICA.md` §2 (incl. campos de acervo: trilha, ordem, modo_origem, status, versao).
- [ ] Anatomia na ordem fixa; **sem `#` no corpo**.
- [ ] As **7 dimensões** da seção 2 passam.
- [ ] Cada interativo passa no teste da seção 3 (não é decoração).
- [ ] Quiz da Avaliação mede os `objetivos` do frontmatter.
- [ ] Só os 6 callouts e 2 interativos oficiais; código é fence.
- [ ] `:::roteiro` não contém conteúdo essencial ao aluno.
- [ ] Volume cabe em 50 min (≤5 conceitos novos, ≤4 elementos por seção).
- [ ] Nos modos SEED/Material: achados da origem refletidos como marcação inline; `revisao: true` se houve correção.

## 6. Veredito

Qualquer falha → corrigir e re-rodar a rubrica inteira. Só se entrega aula que passa em tudo. O veredito é binário, não nota — **não existe aula "7 de 10" entregue**.

A auditoria é processo interno: o relatório completo **não** é anexado à Canônica entregue. Reporte ao Toni apenas o veredito final em uma linha (ex.: "Rubrica: 7/7 PASS, checklist OK") — exceto se ele pedir o detalhamento.
