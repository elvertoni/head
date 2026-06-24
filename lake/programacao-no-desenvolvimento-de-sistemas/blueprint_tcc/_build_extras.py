# -*- coding: utf-8 -*-
"""Constroi os 3 blueprints novos (HealthSync, Espaco Delas, Gold Fit) e
aplica nomes completos + titulo oficial do projeto nos 6 ja existentes.
Remove carlos/nicolas (substituidos). Idempotente."""
import io, json, os, datetime

NOW = datetime.datetime.now().isoformat()


def write(fname, titulo, aluno, tipo, secs):
    d = {"capa_titulo": titulo, "capa_aluno": aluno, "capa_tipo": tipo}
    for i in range(1, 9):
        d["sec%d_texto" % i] = secs[i].strip()
    d["_savedAt"] = NOW
    io.open(fname, "w", encoding="utf-8").write(
        json.dumps(d, ensure_ascii=False, indent=2))
    print("wrote", fname)


def patch(fname, titulo, aluno):
    d = json.load(io.open(fname, encoding="utf-8"))
    d["capa_titulo"] = titulo
    d["capa_aluno"] = aluno
    d["_savedAt"] = NOW
    io.open(fname, "w", encoding="utf-8").write(
        json.dumps(d, ensure_ascii=False, indent=2))
    print("patched", fname)


# ============================== HEALTHSYNC ==============================
healthsync = {
1: """Atualmente, consultórios e clínicas médicas de pequeno e médio porte sofrem com a desorganização de prontuários em formato físico (papel) e o uso de agendas de papel para marcação de consultas. Esse modelo arcaico provoca perda constante do histórico do paciente, lentidão no atendimento (a busca de pastas físicas exige tempo) e conflitos de horários (marcações duplicadas).

Além disso, a falta de segurança digital expõe informações altamente confidenciais dos pacientes a riscos físicos (extravio, incêndio) e a acessos não autorizados por terceiros, violando preceitos de ética e privacidade dos dados médicos.""",
2: """- Recepcionista / Assistente: gerencia o cadastro de pacientes (criar, visualizar, editar, excluir), realiza o agendamento de consultas com médicos credenciados e controla a fila de espera (status Pendente, Agendado, Atendido ou Cancelado).
- Médico(a) / Profissional de Saúde: acessa a agenda diária de atendimentos, visualiza o histórico do Prontuário Eletrônico do Paciente (PEP), registra a evolução clínica (sintomas, diagnóstico e observações), prescreve medicamentos e emite receitas médicas digitalmente.
- Administrador: acompanha o fluxo operacional da clínica pelo dashboard de estatísticas, visualizando o volume de atendimentos e gerenciando o cadastro de profissionais.""",
3: """O HealthSync é uma Single Page Application (SPA) responsiva desenvolvida para centralizar a gestão de clínicas médicas. O sistema integra a ficha cadastral do paciente, uma agenda de consultas flexível e o Prontuário Eletrônico do Paciente (PEP) em um fluxo unificado e de carregamento instantâneo. A solução foca na eliminação do papel, na melhoria da produtividade da equipe, na facilidade de uso e na persistência local segura dos dados.""",
4: """RF01 — O sistema deve permitir o cadastro, a visualização, a edição e a exclusão (CRUD) de fichas de pacientes.
RF02 — O sistema deve permitir criar, reagendar e cancelar consultas médicas, definindo data, hora, médico e motivo.
RF03 — O sistema deve permitir gerenciar o status das consultas (Agendado, Pendente, Atendido, Cancelado).
RF04 — O sistema deve permitir o registro de evoluções clínicas contendo sintomas, diagnóstico, prescrição e observações.
RF05 — O sistema deve gerar receitas médicas formatadas para impressão ou geração de PDF direto pelo navegador.
RF06 — O sistema deve apresentar um painel estatístico (dashboard) com total de pacientes, atendimentos do dia e pendências.
RF07 — O sistema deve disponibilizar busca dinâmica por nome ou CPF nos módulos de pacientes e de prontuário.""",
5: """RNF01 — O sistema deve rodar inteiramente no lado do cliente (Single Page Application), garantindo roteamento dinâmico sem recarga.
RNF02 — O sistema deve se adaptar automaticamente a telas de computadores, tablets e smartphones (design responsivo).
RNF03 — O sistema deve persistir as informações localmente no navegador via Web Storage API (LocalStorage), com dados estruturados em JSON.
RNF04 — O sistema deve permitir a alternância de temas (Dark Mode / Light Mode) e persistir a escolha no armazenamento do usuário.""",
6: """- Linguagem / Framework back-end: não aplicável (sistema 100% client-side) — justificativa: a lógica roda totalmente no navegador, eliminando infraestrutura e latência.
- Banco de dados: Web Storage API (LocalStorage) — justificativa: persiste registros de pacientes, agenda e evolução clínica sem dependência de SGBDs remotos.
- Front-end / Interface: HTML5, CSS3 puro com variáveis e JavaScript ES6 Vanilla — justificativa: alto desempenho de renderização, controle total de estilos e agilidade na manipulação do DOM.
- Hospedagem / Deploy: GitHub Pages ou Vercel — justificativa: ideal para SPAs estáticas, com deploy contínuo e CDN de alta performance sem custos.
- Outras ferramentas: FontAwesome (iconografia) e window.print() — justificativa: ícones melhoram a usabilidade e a impressão nativa gera receitas limpas via CSS.
- Padrão arquitetural: arquitetura modular em SPA com Hash Routing — justificativa: separa responsabilidades em scripts isolados (pacientes.js, prontuario.js, agenda.js) gerenciados pelo núcleo (app.js).""",
7: """1. O atendente abre a SPA do HealthSync e visualiza o painel (Dashboard) com os dados consolidados da clínica.
2. Vai à aba 'Pacientes' e pesquisa um paciente existente ou cria uma nova ficha de cadastro.
3. Acessa a aba 'Agenda', seleciona o paciente, escolhe o médico e confirma a consulta.
4. Quando o paciente chega à clínica, o atendente altera o status do agendamento para 'Pendente'.
5. O médico entra no módulo 'Prontuários' e clica no nome do paciente que já aparece no fluxo de espera clínica.
6. O médico analisa o histórico do PEP, abre o modal de 'Evolução', preenche sintomas, diagnóstico e receitas e salva.
7. O sistema exibe a receita formatada e o médico aciona a impressão para entregar ao paciente assinada.
8. A consulta é finalizada, o sistema atualiza o status para 'Atendido' e recalcula os contadores do dashboard.""",
8: """O HealthSync é totalmente viável para entrega no prazo do TCC. Ao dispensar o desenvolvimento de um back-end relacional tradicional e de servidores remotos, a equipe direcionou todo o esforço na qualidade de UX/UI, na responsividade da interface e na consistência das operações.

O simulador de banco de dados baseado em LocalStorage (db.js) se comporta como um banco real nas operações CRUD, permitindo validação prática instantânea de todo o fluxo de uma clínica. O escopo focado em quatro submódulos integrados (Dashboard, Pacientes, Agenda e Prontuários) assegura uma entrega completa e de alta fidelidade técnica.""",
}
write("healthsync.blueprint.json", "HealthSync",
      "Carlos Eduardo de Souza da Silva, Francisco Krefta Silva e Samuel Guedin Souza",
      "Single Page Application (SPA) · Sistema web client-side", healthsync)


# ============================== ESPACO DELAS ==============================
espacodelas = {
1: """Atualmente, no studio de beleza feminino Espaço Delas, todo o processo de agendamento de serviços é feito de forma manual via WhatsApp ou ligações telefônicas diretamente com as profissionais (Alessandra, Luana e Larissa). Isso gera sobrecarga operacional, pois elas precisam interromper os atendimentos presenciais para responder mensagens, consultar agendas em planilhas ou cadernos físicos e negociar horários com as clientes.

Como consequência direta dessa gestão manual, ocorrem problemas frequentes: conflito de horários (dois agendamentos no mesmo slot), esquecimento de marcações por ausência de lembretes automáticos — gerando alta taxa de no-shows (clientes que não comparecem) — e grande dificuldade em consolidar o histórico de atendimentos e os relatórios de faturamento do studio.""",
2: """- Clientes (usuárias finais): mulheres que buscam serviços de manicure e design de sobrancelha. Interagem com a página institucional para conhecer serviços e profissionais, acessam o fluxo de agendamento em tempo real e realizam ou cancelam suas próprias reservas online de forma autônoma.
- Profissionais do Studio (Alessandra, Luana e Larissa): acessam o painel administrativo individual para visualizar a própria grade diária, gerenciar o status dos agendamentos (confirmar/cancelar) e bloquear horários específicos (folgas e férias) na grade de disponibilidade.
- Administradora / Proprietária (Owner): acesso total ao painel; cadastra e edita serviços, gerencia as profissionais, configura as grades semanais (WorkingHours) de cada profissional e exporta relatórios gerais de agendamento em CSV.""",
3: """Um sistema web responsivo (mobile-first) composto por um website institucional e um sistema de agendamento integrado. O sistema automatiza as reservas de horário das clientes conforme a disponibilidade das profissionais em tempo real, gerencia bloqueios de grade, automatiza o envio de e-mails transacionais (confirmação, lembretes de 24h via Celery e cancelamento por link de token único) e oferece painéis de controle dedicados para as profissionais e para a proprietária.""",
4: """RF01 — O sistema deve apresentar uma página inicial (Home) institucional com informações do studio, galeria e catálogo de serviços.
RF02 — O sistema deve disponibilizar um fluxo de agendamento online em etapas (seleção de serviço, profissional, data, horário e coleta de dados).
RF03 — O sistema deve permitir o cancelamento autônomo do agendamento pela cliente, via link com token único expirável enviado por e-mail.
RF04 — O sistema deve enviar e-mails de confirmação e cancelamento em tempo real, além de lembretes automáticos 24h antes do atendimento.
RF05 — O sistema deve fornecer um painel administrativo restrito para as profissionais visualizarem suas agendas diárias e bloquearem horários na grade.
RF06 — O sistema deve disponibilizar um painel administrativo consolidado para a Owner gerenciar serviços, profissionais e exportar agendamentos em CSV.
RF07 — O sistema deve permitir à Owner configurar e editar as grades de trabalho semanais (dias e horários) de cada profissional.""",
5: """RNF01 — O tempo de carregamento da página inicial institucional deve ser inferior a 2 segundos em conexões móveis (4G).
RNF02 — A interface web deve ser totalmente responsiva (mobile-first), garantindo usabilidade a partir da resolução de 320px.
RNF03 — As senhas das profissionais e da proprietária devem ser protegidas no banco com hashing seguro (bcrypt).
RNF04 — O sistema deve usar transações atômicas com bloqueio no banco para evitar race conditions (dois agendamentos no mesmo slot).""",
6: """- Linguagem / Framework back-end: Python 3.12 + Django 5.x — justificativa: agilidade via ORM integrado, segurança robusta e painel administrativo nativo.
- Banco de dados: PostgreSQL 16 (SQLite em ambiente local) — justificativa: suporte eficiente a consultas concorrentes, transações atômicas robustas e confiabilidade.
- Front-end / Interface: Django Template Language + TailwindCSS 3.x — justificativa: criação rápida de componentes elegantes e responsivos, sem a complexidade de uma SPA separada.
- Hospedagem / Deploy: VPS Ubuntu ou Railway/Render — justificativa: deploy facilitado, suporte nativo a contêineres e integração com GitHub Actions para deploy contínuo.
- Outras ferramentas: Celery + Redis + SMTP (SendGrid) — justificativa: execução assíncrona de tarefas e lembretes automáticos sem travar a requisição HTTP da usuária.
- Padrão arquitetural: Monolito MTV (Model-Template-View) — justificativa: reduz a complexidade de deploy, rede e manutenção em comparação a microsserviços.""",
7: """1. A cliente acessa a página inicial do Espaço Delas e clica no CTA "Agendar Agora".
2. Seleciona o serviço de beleza desejado (ex.: Manicure) no catálogo exposto.
3. Seleciona a profissional de preferência para o atendimento (ou escolhe "Sem preferência").
4. Interage com o calendário, escolhendo um dia ativo disponível.
5. Seleciona um horário disponível na grade da profissional para o dia correspondente.
6. Preenche os dados de identificação e contato (nome completo, e-mail e WhatsApp/telefone).
7. Visualiza a tela de resumo com todas as informações e clica em "Confirmar Agendamento".
8. O sistema valida a concorrência, salva a reserva no banco e exibe a tela de sucesso com opções de exportar o agendamento.""",
8: """O projeto é totalmente viável dentro do cronograma do TCC graças ao framework modular Django, que já fornece funcionalidades prontas e robustas para autenticação, upload de arquivos, persistência segura e um painel administrativo nativo, minimizando o código customizado.

Além disso, o escopo está estritamente focado em funcionalidades de alto valor e bem delimitadas (agenda pública, bloqueio manual e cancelamento autônomo), sem introdução de APIs REST ou comunicação em tempo real complexas. A estilização com TailwindCSS integrada aos templates Django acelera a prototipação, permitindo testes e homologações em menor tempo.""",
}
write("espacodelas.blueprint.json", "Espaço Delas",
      "Nicolas Filardo Maia e Pedro Henrique dos Santos Costa",
      "Sistema web responsivo (mobile-first) de agendamento online", espacodelas)


# ============================== GOLD FIT ==============================
goldfit = {
1: """Praticantes de academia enfrentam dificuldades para organizar, registrar e acompanhar a evolução dos treinos de forma sistemática. A ausência de um registro centralizado impede que o usuário visualize o progresso ao longo do tempo, dificulta a aplicação da sobrecarga progressiva e aumenta o risco de lesões por execução incorreta dos exercícios.

Atualmente, muitos alunos usam cadernos de papel, planilhas genéricas ou dependem apenas da memória, o que resulta em treinos inconsistentes, perda de motivação e abandono da prática. No Brasil, a falta de modo offline em apps similares é uma barreira adicional, já que academias frequentemente têm conexão instável ou inexistente.""",
2: """- Praticante iniciante: cria seu perfil, consulta a biblioteca de exercícios com vídeos demonstrativos e segue treinos sugeridos pelo app.
- Praticante intermediário/avançado: cria treinos personalizados, registra cargas, séries e RPE, monitora PRs e acompanha gráficos de evolução.
- Usuário focado em metas: define objetivos (hipertrofia, emagrecimento, força), recebe sugestões automáticas de ajuste de carga e acompanha o progresso pelo calendário.
- Usuário de wearables: sincroniza Apple Watch, Samsung Health, Google Fit ou Strava para enriquecer os dados de treino e saúde.""",
3: """O Gold Fit é um aplicativo mobile de academia e fitness que centraliza o planejamento, o registro e o acompanhamento de treinos em uma única plataforma. A solução combina uma biblioteca rica de exercícios com vídeos demonstrativos, um motor de personalização que aprende com o histórico do usuário e sugere ajustes de carga automáticos (sobrecarga progressiva), e um painel visual de evolução que transforma dados de treino em motivação concreta.

O app é projetado para funcionar integralmente sem internet, garantindo usabilidade em qualquer academia. Toda a experiência é orientada a manter o usuário consistente, reduzir lesões por técnica inadequada e tornar visível o progresso que costuma passar despercebido sem registro sistemático.""",
4: """RF01 — O sistema deve permitir cadastro e autenticação via e-mail, Google ou Apple ID, com coleta de dados de perfil (peso, altura, nível e objetivo).
RF02 — O sistema deve disponibilizar uma biblioteca com no mínimo 300 exercícios, com vídeo/animação de execução, músculos trabalhados e instruções de segurança.
RF03 — O sistema deve permitir criar treinos personalizados por grupo muscular, divisão semanal (A/B, PPL, full body) e métodos avançados (superset, drop set, circuito).
RF04 — O sistema deve registrar cada série com peso (kg), repetições, tempo de descanso, notas livres e RPE (esforço percebido).
RF05 — O sistema deve exibir gráficos de evolução de carga, volume semanal, Personal Records (PRs) e estimativa de 1RM por exercício.
RF06 — O sistema deve sugerir automaticamente a carga da próxima sessão com base no histórico, aplicando sobrecarga progressiva.
RF07 — O sistema deve disponibilizar um timer de descanso configurável entre séries, com notificação sonora e vibração.
RF08 — O sistema deve registrar medidas corporais (braço, peito, cintura, quadril) e fotos de progresso vinculadas a datas.
RF09 — O sistema deve sincronizar dados com wearables (Apple Watch, Samsung Health, Google Fit e Strava) quando conectado.
RF10 — O sistema deve enviar notificações e lembretes de treino conforme a agenda semanal configurada.""",
5: """RNF01 — O sistema deve funcionar completamente offline, sincronizando com o servidor quando houver conexão (disponibilidade e modo offline).
RNF02 — O sistema deve carregar as telas principais em no máximo 2 segundos em hardware intermediário (desempenho).
RNF03 — O sistema deve armazenar senhas com hash bcrypt e dados sensíveis criptografados em repouso e em trânsito via HTTPS/TLS 1.3 (segurança).
RNF04 — A interface deve ser operável com uma mão durante o treino, com botões de ação de no mínimo 48dp de área de toque (usabilidade).
RNF05 — O sistema deve suportar ao menos 10.000 usuários simultâneos sem degradação perceptível (escalabilidade).""",
6: """- Front-end / Mobile: React Native + Expo — justificativa: desenvolvimento multiplataforma (iOS e Android) com base de código única, reduzindo custo e prazo do TCC.
- Back-end: Node.js + Express — justificativa: ecossistema JavaScript unificado com o front-end, alta performance em I/O e ampla comunidade.
- Banco de dados: PostgreSQL — justificativa: relacional robusto, suporta consultas complexas de histórico/séries e é gratuito para deploy em nuvem.
- Offline / Sync: SQLite (local) + Sync API — justificativa: armazenamento local nativo para modo offline e sincronização incremental ao reconectar.
- Hospedagem: Railway / Render — justificativa: plataformas de deploy gratuitas/low-cost ideais para o escopo de TCC, com suporte a Node.js e PostgreSQL.
- Autenticação: Firebase Auth — justificativa: login social (Google/Apple) pronto, segurança gerenciada e SDK para React Native.
- Padrão arquitetural: MVC + REST API — justificativa: separação clara de responsabilidades e API REST que facilita integração com wearables e escalabilidade futura.""",
7: """1. O usuário baixa o app e se cadastra informando nome, e-mail (ou login social), peso, altura, gênero, nível de experiência e objetivo principal (ex.: hipertrofia).
2. O sistema gera uma sugestão inicial de divisão de treino com base no perfil (ex.: A/B para iniciante, PPL para avançado).
3. O usuário personaliza ou aceita o plano, podendo adicionar, remover ou reorganizar exercícios da biblioteca e configurar séries, repetições e cargas iniciais.
4. No dia do treino, abre o app, seleciona o treino do dia e inicia a sessão, registrando carga, repetições e RPE de cada série.
5. O timer de descanso é acionado automaticamente entre séries, alertando com som e vibração ao fim do intervalo.
6. Ao concluir, o sistema calcula o volume total da sessão, detecta novos PRs e exibe um resumo comparativo com a sessão anterior.
7. O sistema atualiza os gráficos de evolução (carga × tempo, volume semanal) e registra a sessão no calendário de treinos.
8. Com base no desempenho, o app sugere ajuste de carga para a próxima sessão do mesmo treino, aplicando sobrecarga progressiva personalizada.""",
8: """O escopo do Gold Fit foi dimensionado para ser viável dentro do prazo de um TCC semestral desenvolvido em grupo. O projeto usa tecnologias amplamente documentadas (React Native, Node.js, PostgreSQL), com grande disponibilidade de tutoriais, bibliotecas prontas e comunidade ativa, reduzindo o risco técnico.

O desenvolvimento em grupo permite divisão de responsabilidades — front-end mobile, back-end/API e banco podem evoluir em paralelo. Funcionalidades mais complexas, como integração com wearables e personalização via IA, foram classificadas como incrementais: o MVP entregável no prazo cobre cadastro, biblioteca de exercícios, registro de treinos, histórico e gráficos de evolução.

O modo offline é suportado por SQLite, tecnologia madura e de integração direta com React Native, sem infraestrutura adicional. O deploy em plataformas gratuitas (Railway/Render) elimina custo operacional durante o desenvolvimento. A equipe avalia o projeto como tecnicamente viável e com escopo compatível com o prazo.""",
}
write("goldfit.blueprint.json", "Gold Fit",
      "Lucca Dória Loiola, Victor Emanuel Furtado de Oliveira e Pedro Miguel da Silva",
      "Aplicativo mobile (iOS/Android) de academia e fitness", goldfit)


# ============================== PATCH EXISTENTES ==============================
patch("nat.blueprint.json", "Alexandria",
      "Gabriella Gomes de Almeida Miranda, Marlon Gabriel Perissute e Nathalia Elisa Prestes Fujikawa")
patch("maira.blueprint.json", "Lumina",
      "Camila Sara Stauffer Rodrigues, Maíra de Andrade Ribeiro e Suzanna Heliza Goncalves de Freitas")
patch("maria.blueprint.json", "ResumeTech",
      "Flávia Juliane Lemos, Isabela Silva de Meira e Maria Luiza Aguiar da Cunha")
patch("daniel.blueprint.json", "BrVPN",
      "Daniel Moraes do Nascimento, Estevão Barbiot Nascendino e Lucas Czarnesky dos Santos")
patch("hobbyquest.blueprint.json", "HobbyQuest",
      "Maysa Rogaleski Rodrigues, Raquel Heloize Kutz de Bastos e Victor Gabriel Silvestre Melo")
patch("annyvvmake.blueprint.json", "A.N.N Beauty",
      "Anny Isabely Coradassi, Nicoly Holtz da Silva e Nivea Caroline da Silva Matos")


# ============================== REMOVE SUBSTITUIDOS ==============================
for old in ("carlos.blueprint.json", "nicolas.blueprint.json"):
    if os.path.exists(old):
        os.remove(old)
        print("removed", old)

print("DONE")
