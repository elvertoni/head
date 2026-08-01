---
conceito: Autenticação multifator
slug: autenticacao-multifator
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [MFA, multi-factor authentication]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Estratégias de Cloud Computing/14 - Aula 14 - Gerenciamento e Governança em Serviços de Nuvem - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Autenticação multifator exige dois ou mais fatores independentes para verificar uma identidade, combinando algo que a pessoa sabe, possui ou é. Ela reduz o impacto de uma senha exposta, mas depende da qualidade, recuperação e proteção dos fatores adicionais.

## Em uma frase

MFA combina fatores independentes para tornar a autenticação mais resistente a roubo de senha.

## O que precisa saber

Senha e código enviado ao mesmo dispositivo podem oferecer menos independência do que uma chave física ou aplicativo autenticador. MFA resolve autenticação, não autorização; políticas de [[zero-trust]] também precisam de [[rbac]] e menor privilégio. Recuperação de conta é parte do desenho de segurança.

## Erros comuns

- Contar dois canais controlados pelo mesmo invasor como fatores independentes.
- Não proteger recuperação e códigos de emergência.
- Confundir MFA com permissão ampla depois do login.

## Onde aparece

- Estratégias de Cloud Computing, Aula 14, página 3.
- Relaciona-se a [[autenticacao]], [[autorizacao]], [[zero-trust]] e [[seguranca-em-nuvem]].

## Fontes

- Estratégias de Cloud Computing, Aula 14, slide sobre autenticação forte.
