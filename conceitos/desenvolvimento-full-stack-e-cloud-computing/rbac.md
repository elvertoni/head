---
conceito: RBAC
slug: rbac
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [role-based access control, controle de acesso baseado em papéis]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Estratégias de Cloud Computing/14 - Aula 14 - Gerenciamento e Governança em Serviços de Nuvem - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

RBAC concede permissões por meio de papéis atribuídos a identidades, em vez de configurar cada usuário diretamente. O modelo simplifica administração e auditoria quando os papéis refletem responsabilidades reais, mas pode acumular privilégios se não houver revisão e menor privilégio.

## Em uma frase

RBAC autoriza ações conforme o papel funcional atribuído à identidade.

## O que precisa saber

Papéis agrupam permissões; usuários e serviços recebem papéis conforme contexto e responsabilidade. [[autenticacao]] identifica a identidade, enquanto [[autorizacao]] aplica o papel e a política. O desenho deve lidar com herança, separação de funções, contas de serviço e revogação.

## Erros comuns

- Criar um papel administrador para cada necessidade.
- Não revisar papéis sem uso ou permissões excessivas.
- Confundir papel organizacional com autorização automática para todos os recursos.

## Onde aparece

- Estratégias de Cloud Computing, Aula 14, página 3.
- Relaciona-se a [[autorizacao]], [[autenticacao]], [[zero-trust]] e [[seguranca-em-nuvem]].

## Fontes

- Estratégias de Cloud Computing, Aula 14, slide sobre controle por papéis.
