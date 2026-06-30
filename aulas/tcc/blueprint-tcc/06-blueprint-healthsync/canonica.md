---
titulo: Blueprint · HealthSync
tema: Blueprints de TCC
disciplina: tcc
serie: 3a-serie
prerequisitos: []
objetivos:
  - Compreender a arquitetura e os requisitos do projeto HealthSync
trilha: blueprint-tcc
ordem: 6
slug: blueprint-healthsync
status: aprovada
versao: 1
atualizado_em: 2026-06-30
---

# Blueprint · HealthSync

Single Page Application (SPA) · Sistema web client-side · Carlos Eduardo de Souza da Silva, Francisco Krefta Silva e Samuel Guedin Souza

## Objetivos

Ao final desta leitura, você será capaz de compreender a arquitetura e os requisitos do projeto HealthSync.

## Problema e Contexto

Atualmente, consultórios e clínicas médicas de pequeno e médio porte sofrem com a desorganização de prontuários em formato físico (papel) e o uso de agendas de papel para marcação de consultas. Esse modelo arcaico provoca perda constante do histórico do paciente, lentidão no atendimento (a busca de pastas físicas exige tempo) e conflitos de horários (marcações duplicadas).

Além disso, a falta de segurança digital expõe informações altamente confidenciais dos pacientes a riscos físicos (extravio, incêndio) e a acessos não autorizados por terceiros, violando preceitos de ética e privacidade dos dados médicos.

## Público-Alvo

- **Recepcionista / Assistente**: gerencia o cadastro de pacientes (criar, visualizar, editar, excluir), realiza o agendamento de consultas com médicos credenciados e controla a fila de espera (status Pendente, Agendado, Atendido ou Cancelado).
- **Médico(a) / Profissional de Saúde**: acessa a agenda diária de atendimentos, visualiza o histórico do Prontuário Eletrônico do Paciente (PEP), registra a evolução clínica (sintomas, diagnóstico e observações), prescreve medicamentos e emite receitas médicas digitalmente.
- **Administrador**: acompanha o fluxo operacional da clínica pelo dashboard de estatísticas, visualizando o volume de atendimentos e gerenciando o cadastro de profissionais.

## Solução Proposta

O HealthSync é uma Single Page Application (SPA) responsiva desenvolvida para centralizar a gestão de clínicas médicas. O sistema integra a ficha cadastral do paciente, uma agenda de consultas flexível e o Prontuário Eletrônico do Paciente (PEP) em um fluxo unificado e de carregamento instantâneo. A solução foca na eliminação do papel, na melhoria da produtividade da equipe, na facilidade de uso e na persistência local segura dos dados.

## Requisitos Funcionais

- **RF01** — O sistema deve permitir o cadastro, a visualização, a edição e a exclusão (CRUD) de fichas de pacientes.
- **RF02** — O sistema deve permitir criar, reagendar e cancelar consultas médicas, definindo data, hora, médico e motivo.
- **RF03** — O sistema deve permitir gerenciar o status das consultas (Agendado, Pendente, Atendido, Cancelado).
- **RF04** — O sistema deve permitir o registro de evoluções clínicas contendo sintomas, diagnóstico, prescrição e observações.
- **RF05** — O sistema deve gerar receitas médicas formatadas para impressão ou geração de PDF direto pelo navegador.
- **RF06** — O sistema deve apresentar um painel estatístico (dashboard) com total de pacientes, atendimentos do dia e pendências.
- **RF07** — O sistema deve disponibilizar busca dinâmica por nome ou CPF nos módulos de pacientes e de prontuário.

## Requisitos Não Funcionais

- **RNF01** — O sistema deve rodar inteiramente no lado do cliente (Single Page Application), garantindo roteamento dinâmico sem recarga.
- **RNF02** — O sistema deve se adaptar automaticamente a telas de computadores, tablets e smartphones (design responsivo).
- **RNF03** — O sistema deve persistir as informações localmente no navegador via Web Storage API (LocalStorage), com dados estruturados em JSON.
- **RNF04** — O sistema deve permitir a alternância de temas (Dark Mode / Light Mode) e persistir a escolha no armazenamento do usuário.

## Arquitetura e Tecnologias

- **Linguagem / Framework back-end**: não aplicável (sistema 100% client-side) — justificativa: a lógica roda totalmente no navegador, eliminando infraestrutura e latência.
- **Banco de dados**: Web Storage API (LocalStorage) — justificativa: persiste registros de pacientes, agenda e evolução clínica sem dependência de SGBDs remotos.
- **Front-end / Interface**: HTML5, CSS3 puro com variáveis e JavaScript ES6 Vanilla — justificativa: alto desempenho de renderização, controle total de estilos e agilidade na manipulação do DOM.
- **Hospedagem / Deploy**: GitHub Pages ou Vercel — justificativa: ideal para SPAs estáticas, com deploy contínuo e CDN de alta performance sem custos.
- **Outras ferramentas**: FontAwesome (iconografia) e window.print() — justificativa: ícones melhoram a usabilidade e a impressão nativa gera receitas limpas via CSS.
- **Padrão arquitetural**: arquitetura modular em SPA com Hash Routing — justificativa: separa responsabilidades em scripts isolados (pacientes.js, prontuario.js, agenda.js) gerenciados pelo núcleo (app.js).

## Fluxo Principal do Usuário

1. O atendente abre a SPA do HealthSync e visualiza o painel (Dashboard) com os dados consolidados da clínica.
2. Vai à aba 'Pacientes' e pesquisa um paciente existente ou cria uma nova ficha de cadastro.
3. Acessa a aba 'Agenda', seleciona o paciente, escolhe o médico e confirma a consulta.
4. Quando o paciente chega à clínica, o atendente altera o status do agendamento para 'Pendente'.
5. O médico entra no módulo 'Prontuários' e clica no nome do paciente que já aparece no fluxo de espera clínica.
6. O médico analisa o histórico do PEP, abre o modal de 'Evolução', preenche sintomas, diagnóstico e receitas e salva.
7. O sistema exibe a receita formatada e o médico aciona a impressão para entregar ao paciente assinada.
8. A consulta é finalizada, o sistema atualiza o status para 'Atendido' e recalcula os contadores do dashboard.

## Autoavaliação do Escopo

O HealthSync é totalmente viável para entrega no prazo do TCC. Ao dispensar o desenvolvimento de um back-end relacional tradicional e de servidores remotos, a equipe direcionou todo o esforço na qualidade de UX/UI, na responsividade da interface e na consistência das operações.

O simulador de banco de dados baseado em LocalStorage (db.js) se comporta como um banco real nas operações CRUD, permitindo validação prática instantânea de todo o fluxo de uma clínica. O escopo focado em quatro submódulos integrados (Dashboard, Pacientes, Agenda e Prontuários) assegura uma entrega completa e de alta fidelidade técnica.
