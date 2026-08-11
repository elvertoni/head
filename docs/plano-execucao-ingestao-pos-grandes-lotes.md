# Plano de execução — ingestão das duas pós em grandes lotes

**Data:** 2026-08-01  
**Status:** concluído (Onda 1 + Onda 2 + auditoria de fechamento — ver `conceitos/log.md` 2026-08-01, entradas "Onda 1 completa", "Onda 2 completa" e "review | auditoria completa"). Só 1 lacuna real restou ([[etica-em-ia]]), já criada.  
**Escopo:** `lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/` e `lake/desenvolvimento-full-stack-e-cloud-computing/`

## Decisão de escopo

Há 1.207 PDFs nas duas pós, mas slides e resumos são frequentemente duas representações da mesma aula. A normalização atual encontrou 621 unidades de tema: 253 em IA/Robótica e 368 em Full Stack/Cloud.

Até agora, 346 unidades têm pelo menos um conceito apontando para uma fonte: 137 na primeira pós e 209 na segunda. Restam 276 unidades sem nenhum conceito extraído: 117 em IA/Robótica e 159 em Full Stack/Cloud.

A ingestão deve cobrir o conhecimento durável das fontes, não transformar automaticamente cada PDF em `canonica.md`. Resumos servem para conferência e lacunas; não criam duplicatas. Exercícios, ferramentas, projetos, HTMLs e blueprints continuam artefatos de apoio, salvo conceito durável claramente definido. As fontes em `lake/` são imutáveis.

## Estratégia de lotes

Cada lote será uma unidade temática de 20–40 temas, com no máximo seis agentes em paralelo. O particionamento final por subpasta será congelado antes da leitura para evitar sobreposição.

| Lote | Área | Temas ainda sem conceito | Onda |
|---|---|---:|---:|
| IA-01 | IA/Robótica — Módulo I | 11 | 1 |
| IA-02 | IA/Robótica — Módulo II | 20 | 1 |
| IA-03 | IA/Robótica — Módulo III, faixa A | 28 | 1 |
| IA-04 | IA/Robótica — Módulo III, faixa B | 28 | 1 |
| IA-05 | IA/Robótica — Módulo III, faixa C | 29 | 1 |
| FS-01 | Full Stack/Cloud — Módulo I | 24 | 1 |
| FS-02 | Full Stack/Cloud — Módulo II, faixa A | 30 | 2 |
| FS-03 | Full Stack/Cloud — Módulo II, faixa B | 31 | 2 |
| FS-04 | Full Stack/Cloud — Módulo III, faixa A | 37 | 2 |
| FS-05 | Full Stack/Cloud — Módulo III, faixa B | 37 | 2 |
| **Total** |  | **276** |  |

As faixas A/B/C serão definidas pelo inventário de subpastas e pelos números das aulas, não por divisão arbitrária de páginas.

## Papéis dos agentes

1. **Investigadores de fonte:** leem apenas os PDFs primários do lote e devolvem uma planilha estruturada: fonte/páginas, slug candidato, definição própria, conceitos reutilizados, duplicatas/aliases, exclusões e confiança.
2. **Especialista de taxonomia:** cruza os candidatos de todos os lotes, resolve slugs globais, `aka`, conceitos obsoletos e colisões entre as duas pós.
3. **Integrador do vault:** cria/atualiza páginas em `conceitos/`, adiciona wikilinks, atualiza `## Onde aparece`, `conceitos/index.md` e anexa uma linha em `conceitos/log.md`. Nenhum agente escreve índice/log compartilhado em paralelo.
4. **Revisor:** verifica frontmatter, anatomia, fontes existentes, links mortos, duplicatas e se o lote não promoveu artefato de apoio a aula.
5. **Graphify/continuidade:** atualiza o grafo ao final de cada onda, registra diff e confirma que os novos nós estão conectados às comunidades esperadas.

Os investigadores serão `cavecrew-investigator` em modo somente leitura. A integração de muitos arquivos fica centralizada no agente principal; `cavecrew-builder` só será usado para edição cirúrgica de até dois arquivos, conforme a regra da skill.

## Ciclo obrigatório de cada onda

1. Rodar `python tools/gerar_manifesto.py --check` e `git status --short`.
2. Congelar a lista de fontes do lote; nunca ler resumos como lote primário quando já houver slides.
3. Disparar até seis investigadores em paralelo, com escopos de fonte disjuntos.
4. Fazer deduplicação e reconciliação de slugs antes de escrever.
5. Integrar páginas como `status: rascunho`, com `fontes` e `aulas: []`; não criar `canonica.md` sem solicitação explícita de publicação.
6. Atualizar índice e log append-only uma vez por onda.
7. Rodar `python tools/gerar_manifesto.py` e depois `--check`; validar conceitos, links, fontes e `git diff --check`.
8. Rodar `graphify update .`, guardar o diff de nós/arestas e executar a checagem de saúde do grafo.
9. Fechar todos os agentes concluídos e registrar o resultado da onda no ai-memory.

## Critérios de conclusão

- As 276 unidades pendentes foram auditadas, mesmo quando o resultado for “nenhum conceito novo”.
- Cada conceito aceito tem fonte primária, slug global único, frontmatter completo e anatomia do schema.
- Resumos duplicados, bibliotecas, marcas, exercícios e projetos específicos foram registrados como exclusões quando necessário.
- `manifesto.json` permanece válido; as 73 aulas aprovadas existentes não sofrem alteração sem mudança intencional de conteúdo.
- O graphify contém os novos nós e arestas sem editar manualmente `graphify-out/`.
- O fechamento não implica 621 aulas canônicas: publicação no ProfessorDash será uma etapa separada e deliberada.

## Próxima execução recomendada

Começar pela Onda 1 completa: IA-01 a IA-05 e FS-01. Ela usa seis agentes, fecha toda a lacuna dos Módulos I/II da primeira pós e do Módulo I da segunda, e deixa a Onda 2 focada nos 159 temas restantes de Full Stack/Cloud.
