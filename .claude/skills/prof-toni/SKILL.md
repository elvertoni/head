---
name: prof-toni
description: Cria e gerencia o acervo de aulas técnicas do Prof. Toni Coimbra (Curso Técnico em Desenvolvimento de Sistemas, SEED-PR, alunos 14–18, aula de 50 min). Gera uma AULA CANÔNICA rica (Markdown, fonte única de verdade) seguindo a spec em spec/, audita pela rubrica e salva no acervo local. Use SEMPRE que o Toni pedir para criar aula, planejar sequência didática, transformar um tema em aula(s), fatiar um material/PDF/livro/apostila em N aulas, ingerir slides+atividades da SEED-PR, ou revisar/atualizar conteúdo didático — mesmo que não diga as palavras "skill", "método" ou "canônica". Cobre os três modos de entrada: Tema, Material e SEED. NÃO renderiza saídas (site/apostila) — isso é trabalho de outras ferramentas que leem a Canônica.
license: Uso pessoal — Toni Coimbra
---

# prof-toni — Acervo de Aulas

Esta skill produz **Aulas Canônicas**: a fonte única de verdade de cada aula, em Markdown rico e neutro de plataforma. O ProfessorDash e a apostila standalone são consumidores dessa Canônica — não são problema seu aqui. Seu único produto é a `canonica.md` impecável.

## Onde está a inteligência (leia conforme a etapa)

A spec completa vive em `spec/`. **Não carregue tudo de uma vez** — siga o protocolo:

1. **`spec/00-PROTOCOLO.md`** — LEIA PRIMEIRO, SEMPRE. É o documento mestre: pipeline universal, os três modos, regras de ouro, estrutura do acervo. Ele aponta os demais arquivos na hora certa.
2. **`spec/01-CANONICA.md`** — antes de gerar ou editar qualquer aula. Anatomia, frontmatter, sintaxe dos blocos.
3. **`spec/02-RUBRICA.md`** — antes de auditar (etapa obrigatória).
4. **`spec/EXEMPLO-canonica.md`** — leia na primeira geração da sessão. É o padrão de qualidade a igualar.

A regra de ouro de tudo: **a inteligência mora na Canônica; gerar e renderizar são operações separadas.** O resto está na spec — esta skill não a repete, só a opera.

## Operação no dia a dia (a mecânica que a spec não cobre)

A spec descreve o *método*. Esta seção descreve *como trabalhar com o Toni*.

### Conversa
- Português brasileiro, informal e direto. Toni prefere **um passo por vez** — não despeje tudo de uma vez.
- O gate de aprovação do plano (Etapa 2 do protocolo) é real: apresente o plano enxuto e **espere o "pode ir"** antes de gerar conteúdo completo. Exceção da aula única vale (ver protocolo).
- Veredito da rubrica é reportado em uma linha (ex.: "Rubrica 7/7 ✓"), não em relatório, salvo se ele pedir.

### Onde salvar (o acervo)
Cada aula vive em `aulas/{disciplina}/{trilha}/{NN-slug}/canonica.md`, conforme `spec/00-PROTOCOLO.md §8`.

- `disciplina` e `trilha`: slugs minúsculos (`programacao`, `banco-de-dados`, `caderno-de-estudos`).
- `NN`: ordem na trilha, dois dígitos (`01`, `02`...).
- Antes de criar, **liste o que já existe** na trilha-alvo para não duplicar nem repetir número de ordem.
- Material de origem (PDF/PPT/docx da SEED) vai em `fontes/` ao lado da `canonica.md`, imutável.

### Frontmatter — preencher completo
Todo `canonica.md` abre com o frontmatter YAML do `spec/01-CANONICA.md §2`: `titulo`, `tema`, `disciplina`, `serie`, `prerequisitos`, `objetivos`, `trilha`, `ordem`, `slug`, `modo_origem`, `fontes`, `status` (começa `rascunho`), `versao` (começa 1), `atualizado_em`. Aula sem frontmatter íntegro não é entregue. `slug` = `{slug}` da pasta `{NN-slug}` e do manifesto.

### Contrato de import do portal (INVIOLÁVEL)
O ProfessorDash importa lendo `manifesto.json` + `aulas/**/canonica.md`. Regra inviolável (completo em `AGENTS.md §5.1` e `spec/01-CANONICA.md §2`):
- Frontmatter mínimo: `titulo, disciplina, trilha, ordem, slug, status: aprovada, versao, atualizado_em`.
- Caminho `aulas/{disciplina}/{trilha}/{NN}-{slug}/canonica.md` com `NN` = `ordem` em 2 dígitos; tudo casando com o manifesto.
- Portal só importa `status: aprovada`, e só re-importa aula existente se `versao` OU `atualizado_em` mudou — **bumpe sempre** que editar conteúdo publicado.
- **Sempre que adicionar/aprovar/editar aula, regere o manifesto:** `python tools/gerar_manifesto.py` (valide com `--check`). Nunca editar `manifesto.json` à mão.

### Entrega
- Salve a `canonica.md` no caminho correto do acervo e mostre o arquivo ao Toni (`present_files` ou caminho, conforme o ambiente).
- **Editar uma aula existente = nova versão**: incremente `versao`, atualize `atualizado_em`. Nunca sobrescreva silenciosamente o histórico conceitual.
- Esta skill termina na Canônica. Se o Toni pedir o site ou a apostila, isso é outra ferramenta (ProfessorDash / skill `aula-estatica`) lendo este mesmo arquivo.

### Imagens — brief por aula (padrão obrigatório)
Toda aula gerada acompanha um **brief de imagem**: o arquivo `imagens.md` na pasta da aula, neutro de plataforma. Isso **não cria bloco novo na Canônica** — imagem entra no corpo como Markdown `![alt](img/nome.png)`, sempre com justificativa pedagógica (vale o teste anti-decoração; sem justificativa, sai).

**Duas peças por aula, no máximo — e com perfil declarado.** O acervo tem dois formatos visuais distintos, definidos em `tools/imagen-generator/prompt.xml` (v6):

| perfil | arquivo | função | proporção | densidade |
|---|---|---|---|---|
| `capa` | `capa.png` | mapa da aula inteira; é o que o portal exibe | 3:2 | 4–10 blocos, rótulo + micro-parágrafo, subtítulo, faixa de rodapé |
| `infografico` | `img/{slug}.png` | ensina UM conceito difícil, no miolo | 16:9 | 2–5 blocos, só rótulos curtos, sem parágrafo, sem rodapé |

O `imagens.md` traz **exatamente um brief de `capa`** e **no máximo um de `infografico`** — o do conceito mais difícil da aula. Não liste propostas alternativas: escolher é trabalho da spec, não do Toni.

Para cada brief:
- **perfil** — `capa` ou `infografico`. Primeiro campo, sempre.
- **secao** — onde entra na aula (ex.: "Desenvolvimento › Anatomia do Harness"). Só para `infografico`.
- **objetivo** — o que o visual ensina (por que não é decoração).
- **alt** — texto alternativo (acessibilidade + fallback quando o renderer não suporta imagem).
- **prompt** — deixe **vazio ou como esboço de uma linha**. O prompt final é montado pela skill `gerar-imagem-aula` a partir do `prompt.xml` v6, que carrega paleta semântica, gramática visual e o catálogo de 12 defeitos conhecidos. Prompt escrito à mão aqui produz peça fora do design system.

Fluxo: imagem que **já existe** → referencia direto no corpo. Imagem que **falta** → aplicar `gerar-imagem-aula` (Modo A) para obter o prompt colável, gerar no ChatGPT do navegador, salvar, e voltar no Modo B para validação. As imagens finais de conteúdo vivem em `aulas/.../img/` em **versão web (≤500 KB)**; originais pesados ficam no `lake/` (fora do git).

Estado real dos renderers (verificado no código do portal): **nenhum dos dois entrega imagem de conteúdo ao aluno hoje.** O `import_acervo.py` copia só a capa da aula, e `img/` não tem rota no ProfessorDash — o `<img>` fica quebrado; o standalone (`aula-estatica`) sequer tem componente pra isso. Por isso o `alt` carrega a informação de verdade (regra em `spec/01-CANONICA.md` §4.1) e o brief continua existindo: ele é o ativo que fica pronto pra quando o portal servir `img/`.

**Capa é o caso que funciona.** Salve como `capa.png` na pasta da aula (ou aponte no frontmatter `imagem:`) — essa o importador copia e o portal exibe no card e no topo da aula.

## Limites desta skill

- ❌ Não renderiza HTML/site/apostila — só Canônica.
- ❌ Não inventa tipos de bloco ou interativos fora do catálogo da spec (6 callouts + `quiz` + `diagrama-progressivo`).
- ❌ Não entrega aula reprovada na rubrica.
- ❌ Não gera várias aulas completas sem aprovação intermediária do plano.
- ❌ Não inclui `:::roteiro` em nada destinado a aluno (mas ele faz parte da Canônica — quem omite é o renderizador, não você).
