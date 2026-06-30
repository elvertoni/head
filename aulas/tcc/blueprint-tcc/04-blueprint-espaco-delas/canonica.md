---
titulo: Blueprint · Espaço Delas
tema: Blueprints de TCC
disciplina: tcc
serie: 3a-serie
prerequisitos: []
objetivos:
  - Compreender a arquitetura e os requisitos do projeto Espaço Delas
trilha: blueprint-tcc
ordem: 4
slug: blueprint-espaco-delas
status: aprovada
versao: 1
atualizado_em: 2026-06-30
---

# Blueprint · Espaço Delas

Sistema web responsivo (mobile-first) de agendamento online · Nicolas Filardo Maia e Pedro Henrique dos Santos Costa

## Objetivos

Ao final desta leitura, você será capaz de compreender a arquitetura e os requisitos do projeto Espaço Delas.

## Problema e Contexto

Atualmente, no studio de beleza feminino Espaço Delas, todo o processo de agendamento de serviços é feito de forma manual via WhatsApp ou ligações telefônicas diretamente com as profissionais (Alessandra, Luana e Larissa). Isso gera sobrecarga operacional, pois elas precisam interromper os atendimentos presenciais para responder mensagens, consultar agendas em planilhas ou cadernos físicos e negociar horários com as clientes.

Como consequência direta dessa gestão manual, ocorrem problemas frequentes: conflito de horários (dois agendamentos no mesmo slot), esquecimento de marcações por ausência de lembretes automáticos — gerando alta taxa de no-shows (clientes que não comparecem) — e grande dificuldade em consolidar o histórico de atendimentos e os relatórios de faturamento do studio.

## Público-Alvo

- **Clientes (usuárias finais)**: mulheres que buscam serviços de manicure e design de sobrancelha. Interagem com a página institucional para conhecer serviços e profissionais, acessam o fluxo de agendamento em tempo real e realizam ou cancelam suas próprias reservas online de forma autônoma.
- Profissionais do Studio (Alessandra, Luana e Larissa): acessam o painel administrativo individual para visualizar a própria grade diária, gerenciar o status dos agendamentos (confirmar/cancelar) e bloquear horários específicos (folgas e férias) na grade de disponibilidade.
- **Administradora / Proprietária (Owner)**: acesso total ao painel; cadastra e edita serviços, gerencia as profissionais, configura as grades semanais (WorkingHours) de cada profissional e exporta relatórios gerais de agendamento em CSV.

## Solução Proposta

Um sistema web responsivo (mobile-first) composto por um website institucional e um sistema de agendamento integrado. O sistema automatiza as reservas de horário das clientes conforme a disponibilidade das profissionais em tempo real, gerencia bloqueios de grade, automatiza o envio de e-mails transacionais (confirmação, lembretes de 24h via Celery e cancelamento por link de token único) e oferece painéis de controle dedicados para as profissionais e para a proprietária.

## Requisitos Funcionais

- **RF01** — O sistema deve apresentar uma página inicial (Home) institucional com informações do studio, galeria e catálogo de serviços.
- **RF02** — O sistema deve disponibilizar um fluxo de agendamento online em etapas (seleção de serviço, profissional, data, horário e coleta de dados).
- **RF03** — O sistema deve permitir o cancelamento autônomo do agendamento pela cliente, via link com token único expirável enviado por e-mail.
- **RF04** — O sistema deve enviar e-mails de confirmação e cancelamento em tempo real, além de lembretes automáticos 24h antes do atendimento.
- **RF05** — O sistema deve fornecer um painel administrativo restrito para as profissionais visualizarem suas agendas diárias e bloquearem horários na grade.
- **RF06** — O sistema deve disponibilizar um painel administrativo consolidado para a Owner gerenciar serviços, profissionais e exportar agendamentos em CSV.
- **RF07** — O sistema deve permitir à Owner configurar e editar as grades de trabalho semanais (dias e horários) de cada profissional.

## Requisitos Não Funcionais

- **RNF01** — O tempo de carregamento da página inicial institucional deve ser inferior a 2 segundos em conexões móveis (4G).
- **RNF02** — A interface web deve ser totalmente responsiva (mobile-first), garantindo usabilidade a partir da resolução de 320px.
- **RNF03** — As senhas das profissionais e da proprietária devem ser protegidas no banco com hashing seguro (bcrypt).
- **RNF04** — O sistema deve usar transações atômicas com bloqueio no banco para evitar race conditions (dois agendamentos no mesmo slot).

## Arquitetura e Tecnologias

- **Linguagem / Framework back-end**: Python 3.12 + Django 5.x — justificativa: agilidade via ORM integrado, segurança robusta e painel administrativo nativo.
- **Banco de dados**: PostgreSQL 16 (SQLite em ambiente local) — justificativa: suporte eficiente a consultas concorrentes, transações atômicas robustas e confiabilidade.
- **Front-end / Interface**: Django Template Language + TailwindCSS 3.x — justificativa: criação rápida de componentes elegantes e responsivos, sem a complexidade de uma SPA separada.
- **Hospedagem / Deploy**: VPS Ubuntu ou Railway/Render — justificativa: deploy facilitado, suporte nativo a contêineres e integração com GitHub Actions para deploy contínuo.
- **Outras ferramentas**: Celery + Redis + SMTP (SendGrid) — justificativa: execução assíncrona de tarefas e lembretes automáticos sem travar a requisição HTTP da usuária.
- **Padrão arquitetural**: Monolito MTV (Model-Template-View) — justificativa: reduz a complexidade de deploy, rede e manutenção em comparação a microsserviços.

## Fluxo Principal do Usuário

1. A cliente acessa a página inicial do Espaço Delas e clica no CTA "Agendar Agora".
2. Seleciona o serviço de beleza desejado (ex.: Manicure) no catálogo exposto.
3. Seleciona a profissional de preferência para o atendimento (ou escolhe "Sem preferência").
4. Interage com o calendário, escolhendo um dia ativo disponível.
5. Seleciona um horário disponível na grade da profissional para o dia correspondente.
6. Preenche os dados de identificação e contato (nome completo, e-mail e WhatsApp/telefone).
7. Visualiza a tela de resumo com todas as informações e clica em "Confirmar Agendamento".
8. O sistema valida a concorrência, salva a reserva no banco e exibe a tela de sucesso com opções de exportar o agendamento.

## Autoavaliação do Escopo

O projeto é totalmente viável dentro do cronograma do TCC graças ao framework modular Django, que já fornece funcionalidades prontas e robustas para autenticação, upload de arquivos, persistência segura e um painel administrativo nativo, minimizando o código customizado.

Além disso, o escopo está estritamente focado em funcionalidades de alto valor e bem delimitadas (agenda pública, bloqueio manual e cancelamento autônomo), sem introdução de APIs REST ou comunicação em tempo real complexas. A estilização com TailwindCSS integrada aos templates Django acelera a prototipação, permitindo testes e homologações em menor tempo.
