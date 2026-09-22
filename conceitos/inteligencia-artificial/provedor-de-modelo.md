---
conceito: Provedor de modelo
slug: provedor-de-modelo
disciplina: inteligencia-artificial
tipo: conceito
aka: [provedor de modelo, provedor de IA, model provider]
status: rascunho
fontes:
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/Encontro_Elite_09_resumo_e_transcricao.pdf
  - "lake/inteligencia-artificial/elite-wiki/_transcricoes/Imersão IA para Devs PycodeBR [Aula 01] - 2026_04_22 17_49 GMT-03_00 - Anotações do Gemini.docx"
aulas: []
atualizado_em: 2026-09-21
---

Provedor de modelo é a empresa ou infraestrutura que hospeda, disponibiliza e cobra pelo acesso a um ou mais modelos. Ele é uma camada diferente do [[llm]], que é o modelo em si, e do [[harness]], que organiza o uso do modelo, contexto, ferramentas e arquivos.

## Em uma frase

Quem fornece o modelo e define acesso, limites, preço e política de dados.

## O que precisa saber

Um provedor pode oferecer assinatura, API por uso, execução hospedada ou modelos de pesos abertos para rodar localmente. A escolha envolve disponibilidade, limites, latência, privacidade, região, suporte a ferramentas e estabilidade. O mesmo modelo pode produzir resultados diferentes quando muda o harness, o contexto ou a infraestrutura.

## Erros comuns

- Confundir provedor, modelo e interface de uso como se fossem a mesma coisa.
- Comparar assinaturas sem verificar limites, retenção e uso permitido dos dados.
- Acreditar que trocar de provedor preserva automaticamente comportamento e custos.
- Escolher uma integração antes de testar autenticação, limites e saída real.

## Onde aparece

- Encontro Elite #09 e Imersão IA para Devs #01, na separação entre modelo, provedor e harness.
- Conceitos vizinhos: [[llm]], [[harness]], [[selecao-de-modelo]], [[tokens]]

## Fontes

- `Encontro_Elite_09_resumo_e_transcricao.pdf` — camadas de uso, assinaturas, API e execução.
- `Imersão IA para Devs [Aula 01]` — distinção entre modelo, provedor e ferramenta de acesso.
