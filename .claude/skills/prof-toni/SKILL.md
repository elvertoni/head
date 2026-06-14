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
Todo `canonica.md` abre com o frontmatter YAML do `spec/01-CANONICA.md §2`: `titulo`, `tema`, `disciplina`, `serie`, `prerequisitos`, `objetivos`, `trilha`, `ordem`, `modo_origem`, `fontes`, `status` (começa `rascunho`), `versao` (começa 1), `atualizado_em`. Aula sem frontmatter íntegro não é entregue.

### Entrega
- Salve a `canonica.md` no caminho correto do acervo e mostre o arquivo ao Toni (`present_files` ou caminho, conforme o ambiente).
- **Editar uma aula existente = nova versão**: incremente `versao`, atualize `atualizado_em`. Nunca sobrescreva silenciosamente o histórico conceitual.
- Esta skill termina na Canônica. Se o Toni pedir o site ou a apostila, isso é outra ferramenta (ProfessorDash / skill `aula-estatica`) lendo este mesmo arquivo.

### Imagens — brief por aula (padrão obrigatório)
Toda aula gerada acompanha um **brief de imagem**: o arquivo `imagens.md` na pasta da aula, neutro de plataforma. Isso **não cria bloco novo na Canônica** — imagem entra no corpo como Markdown `![alt](img/nome.png)`, sempre com justificativa pedagógica (vale o teste anti-decoração; sem justificativa, sai).

Para cada visual sugerido, `imagens.md` traz:
- **secao** — onde entra na aula (ex.: "Desenvolvimento › Anatomia do Harness").
- **objetivo** — o que o visual ensina (por que não é decoração).
- **alt** — texto alternativo (acessibilidade + fallback quando o renderer não suporta imagem).
- **prompt** — prompt pronto pra colar num gerador (Gemini Nano Banana / GPT) e produzir a imagem.

Fluxo: imagem que **já existe** → referencia direto no corpo. Imagem que **falta** → Toni pega o `prompt`, gera, salva em `img/`. As imagens finais de conteúdo vivem em `aulas/.../img/` em **versão web (≤500 KB)**; originais pesados ficam no `lake/` (fora do git).

Lembrete de renderer: o standalone (`aula-estatica`) **não tem componente de imagem de conteúdo** (o design system proíbe imagem externa obrigatória) — lá a imagem degrada com marcação explícita; ela brilha no ProfessorDash. Isso não altera a Canônica: o brief existe sempre.

## Limites desta skill

- ❌ Não renderiza HTML/site/apostila — só Canônica.
- ❌ Não inventa tipos de bloco ou interativos fora do catálogo da spec (6 callouts + `quiz` + `diagrama-progressivo`).
- ❌ Não entrega aula reprovada na rubrica.
- ❌ Não gera várias aulas completas sem aprovação intermediária do plano.
- ❌ Não inclui `:::roteiro` em nada destinado a aluno (mas ele faz parte da Canônica — quem omite é o renderizador, não você).
