---
titulo: Encontro Elite #01 | Agentes pessoais com Hermes Agent (parte 01)
disciplina: inteligencia-artificial
fonte: notion
origem: https://pickle-reading-bd9.notion.site/Encontro-Elite-01-Agentes-pessoais-com-Hermes-Agent-parte-01-35b9956f3dc980648b60cf7f6e1e74ec
data: 2026-06-30
page_id: 35b9956f-3dc9-8064-8b60-cf7f6e1e74ec
status: bruto
---

# Encontro Elite #01 | Agentes pessoais com Hermes Agent (parte 01)

> Nessa parte 01 vamos montar a base conceitual e prática para usar o Hermes Agent como agente pessoal de desenvolvimento e operação.



Desenhos: ‣


## 1. Visão geral da aula

Esse encontro abre uma sequência de duas aulas sobre agentes pessoais com Hermes Agent, ferramenta open-source da Nous Research que entrega um agente autônomo com memória persistente, skills auto-criadas e suporte a múltiplas plataformas de mensagem.

‣

‣

‣

‣



## 2. Contexto: por que falar de agentes pessoais agora

Em 2026 o ecossistema de IA para desenvolvimento amadureceu em três direções ao mesmo tempo:

- CLIs de programação com modelos potentes (Claude Code, Codex CLI, Gemini CLI, Qwen, Opencode) viraram padrão para quem programa sério.
- Skills, plugins e MCPs consolidaram um ecossistema reutilizável. Ferramentas como Superpowers, Caveman, claude-mem, frontend-design, agent-browser e dezenas de outras já existem prontas para instalar.
- Agentes autônomos com memória começaram a sair do papel — o agente que continua a conversa de ontem, lembra de você, cria suas próprias rotinas e responde no Slack/Telegram/WhatsApp como se fosse um colega remoto.
O ponto comum é: a IA deixou de ser um "chat na aba do navegador" e virou parte do tecido operacional do dia a dia técnico. O que muda com agentes pessoais é a continuidade. O agente não esquece quem você é entre sessões, não precisa de prompt longo de contexto toda vez, e pode ser invocado de qualquer canal — terminal, mensagem, voz, e-mail.

Para quem já segue o workflow ensinado em ‣ e ‣ — Spec-Driven Development com IA assistida — o agente pessoal entra como camada acima do harness CLI: ele opera continuamente, mantém contexto entre sprints, e pode ser distribuído como um time (Kratos, Zeus, Hera, Atena, Ares no caso do canon PycodeBR).

Hermes Agent é uma das opções mais robustas hoje para quem quer um agente pessoal real, open-source, com memória, skills auto-criadas e multi-platform. Ele é o que estamos usando como base para o time multi-agente da PycodeBR.




## 3. O que é o Hermes Agent

Em uma frase: Hermes Agent é um agente autônomo open-source da Nous Research, escrito em Python, que opera no seu servidor (local ou VPS), aprende com o uso, mantém memória persistente entre sessões e responde por múltiplas plataformas a partir de um único processo.

Citação direta da documentação oficial: "The agent that grows with you. The only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions."

### Para que tipo de tarefa ele faz sentido

- Programar (analisar projeto, alterar código, gerar testes, criar documentação) com revisão humana.
- Operar como assistente pessoal contextual — lembra de você, das suas preferências e dos projetos em andamento.
- Automatizar tarefas recorrentes via cron jobs internos (briefings matinais, varreduras, relatórios).
- Ser invocado via Slack, Discord, Telegram, WhatsApp, Signal, e-mail ou CLI — sempre o mesmo agente, sempre a mesma memória.
- Coordenar múltiplos agentes (cada um com perfil próprio) trabalhando como time, com delegação e auditoria.
### Como ele se encaixa no fluxo de um desenvolvedor

Pense no Hermes como uma camada acima das CLIs de programação. Você pode continuar usando Claude Code para sessão específica de código, e usar o Hermes para tudo que envolve continuidade: assistente pessoal, multi-platform, agendamentos, time multi-agente, automação.

Além disso, o Hermes tem skills nativas de controle e uso dos CLIs, como o Claude Code, Codex e Opencode. Portanto consegue orquestrar o uso dos seus CLIs conforme a sua demanda e necessidade.

### Como ele pode funcionar como agente pessoal

Cada perfil tem seu próprio diretório ~/.hermes/profiles/<nome>/ com personalidade (SOUL.md), identidade (IDENTITY.md), perfil do dono (USER.md), time (TEAM.md), ferramentas (TOOLS.md) e tarefas periódicas (HEARTBEAT.md). É exatamente o padrão que usamos para criar Kratos, Zeus, Hera, Atena e Ares — ver ‣.

### Exemplos de uso no contexto da PycodeBR

- Kratos (COO/orquestrador): recebe demandas no Slack, decompõe e delega para os outros agentes do time.
- Zeus (backend): chamado para análise de arquitetura ou implementação de endpoints Django/LangChain.
- Hera (frontend): chamada para ajustes no design system ou nas LPs do Maio Master.
- Atena (PO): refina specs e atualiza PRD.md de projetos como MentorIA ou finanpy.
- Ares (Scrum): organiza sprints e cobra cadência.
- Agente pessoal único do aluno: assistente que ajuda a estudar, organizar projetos, lembrar contexto entre semanas e responder via Telegram/Slack mesmo quando o aluno não está na frente do computador.

### Diferenciais do Hermes Agent

#### Memória persistente

A documentação oficial indica que o Hermes mantém dois arquivos de memória ativos em ~/.hermes/memories/:

- MEMORY.md (limite ~2.200 caracteres): fatos do ambiente, convenções de projeto, lições aprendidas sobre workflow e ferramentas.
- USER.md (limite ~1.375 caracteres): identidade do usuário, preferências de comunicação, hábitos de trabalho.
A memória é injetada como snapshot congelado no system prompt no início de cada sessão (preserva o prefix cache do LLM). Mudanças escritas durante a conversa persistem no disco imediatamente, mas só aparecem no prompt na próxima sessão.

Além disso, todas as sessões anteriores ficam indexadas via FTS5 (full-text search) em SQLite — o agente pode buscar conversas antigas por palavra-chave sem ocupar a janela de contexto ativa.

#### Aprendizado com o uso

A doc descreve um built-in learning loop: o agente é "cutucado" periodicamente (agent-curated memory com nudges) para revisar e consolidar o que aprendeu. Quando a memória chega no limite, ele consolida entradas em vez de descartar.

#### Criação independente e automática de skills

Após workflows complexos (5+ tool calls), erros recorrentes, ou descoberta de processos não-triviais, o agente escreve uma nova skill como memória procedural. Ela vai para ~/.hermes/skills/ seguindo o padrão aberto agentskills.io, e fica disponível para uso futuro via slash command (/<skill-name>) ou em conversa natural.

#### Multi-canais e integrações nativas

O Hermes é um único processo no servidor que se conecta simultaneamente a várias plataformas via comando dedicado (hermes gateway). Você joga uma tarefa pelo Slack do trabalho às 14h, pergunta o resultado pelo Telegram no jantar, e termina de revisar no terminal de manhã — mesmo agente, mesma sessão, mesma memória, mesmo histórico. A escolha de canal é preferência momentanea, não muda nada do que o agente sabe sobre você.

A documentação oficial lista 18 plataformas com integração nativa, todas operadas pelo mesmo processo hermes gateway:

- Locais: Terminal/TUI · Dashboard web (browser local)
- Mensagem ocidental: Slack · Telegram · Discord · WhatsApp · Signal · Microsoft Teams · Mattermost · Email
- Voz e mobile: Voice memo (transcrição cross-platform) · SMS via Twilio · iMessage via BlueBubbles
- Outros protocolos: Matrix
- Asiático: WeChat (Weixin) · DingTalk · Feishu/Lark · WeCom · QQ Bot · Yuanbao
- IoT: Home Assistant (automação residencial)

#### Multi-canais e integrações nativas

O Hermes é um único processo no servidor que se conecta a várias plataformas via comando hermes gateway. Mesmo agente, mesma sessão, mesma memória — você joga uma tarefa pelo Slack às 14h, pergunta o resultado pelo Telegram no jantar, termina no terminal de manhã. A doc oficial lista 18 plataformas nativas: Terminal/TUI, Dashboard web, Slack, Telegram, Discord, WhatsApp, Signal, Microsoft Teams, Mattermost, Email, SMS (Twilio), iMessage (BlueBubbles), Voice memo, Matrix, WeChat, DingTalk, Feishu, QQ Bot, Home Assistant. Ver 

Na prática: o agente pessoal pode ser invocado de qualquer lugar, não precisa estar na frente do PC. Para a PycodeBR, Kratos/Zeus/Hera/Atena/Ares hoje vivem no Slack #operacao e poderiam atender também no Telegram pessoal, WhatsApp da empresa ou e-mail de suporte — todos lendo da mesma memória. Cuidados: cada canal exige credenciais próprias (token Slack, bot Telegram, número Twilio para SMS, etc.); definir allowlists em produção (SLACK_ALLOWED_USERS etc.); multi-canal só funciona com servidor online — reforça a decisão de VPS + Host para agente sempre disponível.

Por que isso importa na prática:

- Para o aluno: o agente pessoal pode ser invocado de qualquer lugar. Não precisa estar na frente do PC. Funciona como um colega remoto sempre disponível — conversa pelo Telegram no almoço, manda voice memo dirigindo, retoma no terminal quando senta.
- Para o time PycodeBR: Kratos, Zeus, Hera, Atena e Ares hoje vivem no Slack #operacao (ver ‣). Os mesmos perfis poderiam atender no Telegram pessoal, no WhatsApp da empresa, em e-mails de suporte — todos lendo da mesma memória persistente.
- Para automação mãos-livres: Voice memo + SMS dão acesso quando você não está com as duas mãos no teclado. Joga a demanda dirigindo, ele te responde quando for relevante.
Cuidados:

- Cada canal exige credenciais próprias (token Slack, bot Telegram, número Twilio para SMS, etc.). Configurar uma plataforma por vez — não tentar ligar todas no primeiro setup.
- Em produção, definir explicitamente quem pode falar com o agente em cada canal (SLACK_ALLOWED_USERS, allowlists por bot, etc.). Agente em canal público sem filtro é convite para abuso e custos descontrolados.
- Multi-canal só funciona se o servidor estiver online — reforça a decisão de VPS + Host quando o caso é "agente sempre disponível" (ver matriz na seção 8).
- A doc oficial não detalha estágios de maturidade (estável/beta) por plataforma. Para a aula ao vivo, demonstrar com Slack ou Telegram que são os mais consolidados na comunidade Hermes.
#### Quando esses diferenciais ajudam em fluxos reais

- Trabalho de longa duração em um único projeto: o agente pega o fio da meada de uma sessão para outra.
- Padrões pessoais que não cabem em prompt: estilo de código, restrições operacionais, vocabulário próprio.
- Tarefas repetitivas que viram skill: deploy, geração de relatórios, varredura de código, análise de logs.
- Multi-canal: você joga uma tarefa no Slack de manhã, vê o resultado no terminal à tarde — mesma sessão, mesma memória.
#### Cuidados ao confiar em memória, aprendizado e skills criadas automaticamente

Memória automática não é ouro automático. A doc deixa claro que o sistema prevê duplicatas e escaneia entradas por riscos de segurança, mas a curadoria final é responsabilidade do usuário. Algumas atenções práticas:

- Revise periodicamente MEMORY.md e USER.md antes de operações sensíveis.
- Skills auto-criadas precisam ser auditadas — leia o conteúdo, valide o comportamento em ambiente isolado antes de aprovar para uso recorrente.
- A doc menciona níveis de confiança (builtin, official, trusted, community) para skills do hub. Para skills criadas pelo seu próprio agente, trate como "trusted" mas confirme.
- Em produção (agente operando em VPS no Slack 24/7), defina explicitamente quais ações o agente pode tomar sozinho e quais exigem aprovação humana — --yolo é cômodo em desenvolvimento, perigoso em produção operacional.



## 4. Claude Code, OpenClaw e Hermes Agent

Os três têm propósitos diferentes e podem coexistir no seu workflow. Não é escolha mutuamente exclusiva.

### Papel principal de cada ferramenta

### Onde se sobrepõem

- Os três aceitam usar modelos da Anthropic, OpenAI e outros provedores compatíveis via configuração.
- Os três suportam skills/plugins com ecossistemas próprios: Claude Code via plugins/skills (npx skills add ...), OpenClaw via ClawHub (registry oficial), e Hermes via agentskills.io. Skills no padrão aberto agentskills.io tendem a funcionar nos três, mas cada um tem seu hub principal.
- Os três permitem automação de tarefas de código (analisar projeto, criar arquivo, alterar código, rodar comando no terminal).
- Hermes e Claude Code aceitam MCP (Model Context Protocol) como mecanismo de extensão.
### Onde se complementam

- Claude Code brilha quando você está sentado na frente do código com sessão dedicada, especialmente com Opus 4.6/4.7 ou Sonnet 4.6 e o ecossistema de plugins/skills (Superpowers, claude-mem, frontend-design, find-skills). Ver setup completo em ‣.
- Hermes Agent brilha quando você quer continuidade entre sessões, multi-platform (responder no Slack/Telegram/WhatsApp), automação agendada, multi-agente coordenado e operação 24/7 em VPS.
- OpenClaw é o pioneiro do espaço de agentes pessoais open-source (lançado em nov/2025 por Peter Steinberger, hoje na OpenAI). Continua ativo, com comunidade enorme (247k+ stars) e integração nativa com OpenAI. É a opção mais consolidada para quem quer multi-platform agora, especialmente com stack TypeScript/Node e conta OpenAI. Para quem já usa OpenClaw e quer testar Hermes em paralelo, o hermes claw migrate importa SOUL.md, memórias, skills, API keys, configurações de mensagens e instruções de workspace — note que migrar não significa que o Hermes substitui o OpenClaw; são alternativas no mesmo espaço, com filosofias diferentes.
### Podemos usar Hermes e Claude Code no mesmo fluxo?

Sim, e é o uso recomendado para quem leva isso a sério:

- Use Claude Code para sessão dedicada de código com modelo top (Opus/Sonnet) — implementar uma sprint inteira, fazer um refactor pesado, debugar algo crítico.
- Use Hermes para o agente pessoal sempre online: lembrar contexto, responder Slack, agendar briefing matinal, executar varredura noturna, operar como time multi-agente.
- Eles podem inclusive compartilhar skills — skills no padrão agentskills.io funcionam em ambos.
### Exemplos práticos de quando usar cada uma




## 5. Arquitetura mental do Hermes Agent

Para usar bem, vale ter cinco peças desenhadas na cabeça:

```plain text
         ┌──────────────────────────────────┐
         │          VOCÊ (humano)           │
         └────────────────┬─────────────────┘
                          │
           CLI/TUI · Slack · Telegram · etc.
                          │
                          ▼
         ┌──────────────────────────────────┐
         │         HERMES AGENT             │
         │  (processo Python no servidor)   │
         └─┬──────────┬──────────┬─────────┘
           │          │          │
           ▼          ▼          ▼
       PROVEDOR    MEMÓRIA     SKILLS
      (LLM/API)   (SQLite)   (agentskills.io)
           │
           ▼
    BACKEND DE EXECUÇÃO
local · Docker · SSH · Modal
Singularity · Daytona · Vercel
```

- Provedor: o LLM em si. Pode ser Nous Portal, OpenAI, Anthropic, OpenRouter (200+ modelos), NVIDIA NIM, z.ai/GLM, Kimi/Moonshot, MiniMax, Hugging Face ou endpoint custom. Trocar de provedor é hermes model ou /model dentro do chat — sem mudança de código.
- Memória: dois arquivos curtos (MEMORY.md + USER.md) injetados no prompt no início da sessão, mais histórico completo de sessões em SQLite com FTS5 para busca.
- Skills: pacotes de instruções/conhecimento sob demanda em ~/.hermes/skills/, instaláveis do hub ou criadas autonomamente pelo agente. Padrão aberto agentskills.io.
- Terminal/TUI: a interface principal de interação direta com o agente.
- Gateway: processo que conecta o agente às plataformas de mensagem (Slack, Telegram, etc.). Roda separado do chat CLI.
- Backend de execução: onde o agente roda comandos de terminal, isolados do seu sistema. Sete opções para escolher entre velocidade, isolamento e custo.
Quando o agente está pensando, ele tem essas cinco peças à disposição. Quando ele responde, está coordenando entre elas.




## 6. Instalação do Hermes Agent

Documentação oficial: hermes-agent.nousresearch.com/docs · Repositório: github.com/NousResearch/hermes-agent

### Pré-requisitos

A doc oficial lista o seguinte como mínimo:

- Python 3.11+ instalado no sistema (o instalador resolve via uv quando possível)
- Node.js 20+ (algumas ferramentas built-in dependem)
- ripgrep (busca rápida)
- ffmpeg (processamento de áudio para voice mode)
- Git Bash (no Windows o instalador traz MinGit ~45MB)
- 512 MB de RAM mínimo (cabe num VPS de 5 dólares; recomendado 2 GB para multi-skill)
A maior parte é instalada automaticamente pelo script. O instalador usa uv (gerenciador de pacotes Python rápido).

### Comando oficial de instalação

#### macOS, Linux, WSL2 e Termux (Android)

```bash
# Comando único oficial
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# Após terminar
source ~/.bashrc   # ou ~/.zshrc, dependendo do shell
hermes setup       # wizard de configuração inicial
```

Alternativa via raw do GitHub (mesmo script):

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

#### Windows (PowerShell — beta nativa)

```powershell
irm https://hermes-agent.nousresearch.com/install.ps1 | iex
```

Alternativa raw do GitHub:

```powershell
irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1 | iex
```

Atenção Windows: a versão nativa Windows ainda está marcada como early beta na doc oficial. Para uso sério em produção, considerar WSL2 + script Linux como caminho mais estável.

### Possíveis problemas comuns na instalação

- Comando hermes não encontrado após instalar: rodar source ~/.bashrc (ou reabrir o terminal). O instalador adiciona o binário no PATH via ~/.local/bin ou similar.
- Erro de Python: o instalador exige Python 3.11+. Se a versão atual for antiga, instalar via pyenv, Homebrew (macOS), apt (Linux) ou diretamente do site oficial Python.
- Falha em baixar dependências: rede corporativa com proxy/firewall costuma bloquear o uv baixando pacotes. Validar com uv --version e ajustar variáveis de proxy.
- Erro de permissão: nunca rodar com sudo. O instalador trabalha com diretórios do usuário (~/.hermes/, ~/.local/bin).
### Como validar se a instalação funcionou

```bash
hermes --version       # exibe versão (deve mostrar v0.x.x)
hermes doctor          # diagnóstico completo
hermes status          # status do agente, auth, plataformas
```

hermes doctor é o ponto de partida quando algo dá errado — ele verifica configurações, dependências e conexões.




## 7. Local, VPS, host e Docker

Existem duas decisões independentes na hora de subir o Hermes:

- Onde rodar? Máquina local ou VPS na nuvem.
- Como rodar? Direto no host ou em container Docker.
### Local versus VPS na nuvem

#### Vantagens de rodar localmente

- Zero custo de servidor (você paga só os tokens do provedor).
- Latência baixíssima — conversa flui rápido no terminal.
- Acesso total aos arquivos do projeto sem precisar enviar para a nuvem.
- Privacidade — o agente vê só o que está na sua máquina.
#### Desvantagens de rodar localmente

- Quando você desliga o computador, o agente para. Se o gateway do Slack está conectado, fica offline e some das mensagens.
- Limitado pela bateria/energia da máquina.
- Não dá para responder mensagens fora do horário de trabalho sem deixar o PC ligado.
- Multi-platform 24/7 não funciona bem.
#### Vantagens de rodar em VPS

- Agente sempre online — responde Slack/Telegram/WhatsApp 24/7.
- Independente da sua máquina pessoal.
- Permite operar o agente como funcionário virtual real.
- VPS de 5-10 dólares já roda confortável (Hermes pede 512 MB de RAM mínimo).
- Boa para o cenário multi-agente (Kratos, Zeus, Hera, Atena, Ares no Slack da empresa).
#### Desvantagens de rodar em VPS

- Custo mensal recorrente (5-30 dólares dependendo do provedor).
- Setup inicial maior — SSH, segurança, firewall, monitoramento.
- O agente precisa de acesso aos seus repositórios via Git (clone/pull), não vê seu sistema de arquivos local.
- Latência maior na CLI quando você acessa via SSH.
#### Quando recomendar cada abordagem para alunos

- Está aprendendo, testando, programando do PC: rodar local é o caminho. Custo zero, debug fácil, retorno rápido.
- Quer agente pessoal sempre online ou multi-agente em equipe: ir para VPS. Hostinger, DigitalOcean, Vultr, Hetzner — opções de 5-10 dólares já bastam. Indicação: Hetzner (melhor custo/recurso; CX22 com 2 vCPU, 4 GB RAM e 40 GB SSD por ~€4,51/mês roda Hermes multi-agente com folga). Indicação de VPS barata: Hetzner (melhor relação custo/recurso hoje — plano CX22 com 2 vCPU, 4 GB RAM e 40 GB SSD por ~€4,51/mês / ~R$26 roda Hermes com folga, inclusive multi-agente; datacenters na Alemanha, Finlândia, EUA e Cingapura — hetzner.com/cloud).
- Modelo híbrido: agente principal em VPS para multi-platform, e Hermes adicional local para sessões intensas de código.
Indicação de VPS barata: Hetzner. Melhor relação custo/recurso hoje. Plano CX22 (2 vCPU, 4 GB RAM, 40 GB SSD) por ~€4,51/mês (~R$26) roda Hermes com folga, inclusive multi-agente. Datacenters em Falkenstein, Nuremberg, Helsinki, Ashburn, Hillsboro e Cingapura. Site: hetzner.com/cloud.

Indicação de VPS barata: Hetzner. Melhor relação custo/recurso do mercado hoje. O plano CX22 (2 vCPU · 4 GB RAM · 40 GB SSD) sai por ~€4,51/mês (~R$26) e roda Hermes com folga, inclusive multi-agente. Datacenters em Falkenstein/Nuremberg/Helsinki e novos em Ashburn/Hillsboro/Cingapura. Site: hetzner.com/cloud. Para começar simples, o plano CX11 ainda existe em algumas regiões por ~€3,29/mês e atende um único agente sem problema.

Indicação de VPS barata: Hetzner. Melhor relação custo/recurso do mercado hoje. O plano CX22 (2 vCPU · 4 GB RAM · 40 GB SSD) sai por ~€4,51/mês (~R$26) e roda Hermes com folga, inclusive multi-agente. Datacenters em Falkenstein/Nuremberg/Helsinki e novos em Ashburn/Hillsboro/Cingapura. Site: hetzner.com/cloud.

Indicação alternativa de VPS barata: Contabo. Provedor alemão conhecido pela maior quantidade de recursos por euro do mercado — costuma entregar 2–3x mais vCPU/RAM/SSD que concorrentes no mesmo preço. O plano VPS 10 SSD (3 vCPU · 8 GB RAM · 75 GB NVMe) sai por ~€4,50/mês e roda Hermes multi-agente com sobra. Datacenters na Alemanha, EUA, Reino Unido, Singapura, Japão, Índia e Austrália. Trade-off: performance de CPU/IO mais variável que Hetzner e setup inicial pode levar algumas horas (não é instantâneo). Para quem quer mais RAM/disco pelo mesmo preço e tolera latência um pouco maior, é a melhor escolha. Site: contabo.com/en/vps.

Indicação alternativa de VPS barata: Contabo. Provedor alemão reconhecido por entregar a maior quantidade de recursos por euro do mercado — costuma oferecer 2–3x mais vCPU/RAM/SSD que concorrentes no mesmo preço. O plano VPS 10 SSD (3 vCPU · 8 GB RAM · 75 GB NVMe) sai por ~€4,50/mês e roda Hermes multi-agente com sobra. Datacenters na Alemanha, EUA, Reino Unido, Singapura, Japão, Índia e Austrália. Trade-off: performance de CPU/IO mais variável que Hetzner e setup inicial pode levar algumas horas (não é instantâneo). Para quem quer mais RAM/disco pelo mesmo preço e tolera latência um pouco maior, é a melhor escolha. Site: contabo.com/en/vps.

### Host versus Docker

#### Diferenças práticas

- Direto no host: instalar com o script oficial e usar hermes diretamente. O agente roda como processo Python do seu usuário.
- Em Docker: encapsular o Hermes em um container, montar ~/.hermes/ como volume persistente, rodar o gateway como serviço de container.
#### Vantagens do host

- Caminho mais simples, mais documentado e mais alinhado com o setup multi-agente que já temos rodando.
- Menos camadas — debug direto.
- Acesso pleno ao sistema de arquivos sem mapear volumes.
- systemd (Linux), launchd (macOS) e Task Scheduler (Windows) cuidam do auto-start.
#### Desvantagens do host

- Menos isolamento entre o agente e o sistema operacional.
- Atualizações de Python/Node no host afetam o Hermes.
#### Vantagens do Docker

- Isolamento forte — o agente vive em um ambiente controlado.
- Portabilidade — mesma imagem em qualquer servidor.
- Reproduzibilidade — docker compose up e está rodando.
- Fácil escalar para múltiplos agentes (um container por perfil).
#### Desvantagens do Docker

- Camada extra a aprender e operar.
- Volumes precisam ser bem configurados para persistir .hermes/ (memória, sessões, skills).
- Acesso a recursos do host (clipboard, áudio para voice mode) fica mais difícil.
- Hoje, sem imagem oficial confirmada (ver alerta acima), é build próprio.
#### Quando usar cada abordagem em aula

- Aluno iniciando: instalar direto no host seguindo o script oficial. Mais rápido para chegar ao primeiro hermes setup funcional.
- Operação séria em VPS multi-agente: começar no host com systemd/launchd (o padrão consolidado em ‣) e considerar Docker como evolução depois que estiver dominando.



## 8. Configuração inicial do Hermes Agent

### Primeiros passos após a instalação

Logo após instalar, a sequência recomendada pela doc oficial é:

```bash
# 1. Recarregar shell para pegar o binário no PATH
source ~/.bashrc   # ou ~/.zshrc

# 2. Wizard interativo de configuração
hermes setup

# 3. Conferir que está tudo certo
hermes doctor
hermes status
```

O hermes setup cobre as seções principais (modelo, terminal/backend, gateway de mensagens, ferramentas, agent). Se preferir setar coisa a coisa:

```bash
hermes setup --quick           # só pergunta o que está faltando
hermes setup --non-interactive # usa defaults, sem perguntas
hermes setup --reset           # zera e refaz tudo
```

### Arquivos e variáveis principais

A documentação oficial e o repositório indicam:

- ~/.hermes/ — diretório raiz da instalação do usuário (configs, memórias, skills, sessões).
- ~/.hermes/.env — variáveis sensíveis (API keys, tokens Slack se gateway global, etc.).
- ~/.hermes/state.db — SQLite com sessões e índice FTS5.
- ~/.hermes/memories/MEMORY.md e USER.md — memória persistente do agente.
- ~/.hermes/skills/ — skills instaladas e auto-criadas.
- ~/.hermes/profiles/<nome>/ — quando você cria múltiplos perfis (Kratos, Zeus, etc.).
- Arquivo config.yaml (ou similar) por perfil — modelo, toolsets, configuração do Slack do perfil.
Comandos para inspecionar e editar:

```bash
hermes config show     # exibe configuração atual
hermes config edit     # abre o config no editor
hermes config set <chave> <valor>
hermes config path     # mostra caminho do arquivo de config
hermes config check    # valida config
```

### Como conectar provedores para usar modelos

Atualmente recomendo o uso dos seguintes provedores e modelos:

- OpenAI GPT-5.5 para trabalhos mais complexos e para configuração inicial e construção da memória.
- Opencode Go com modelos DeepSeek v4 Flash ou Pro para uso diário, já que suportam muito mais limites de uso.
- Anthropic Opus/Sonnet podem correr risco de serem banidos pela Anthropic.
A doc lista provedores nativos: Nous Portal, OpenRouter, OpenAI, Anthropic, NVIDIA NIM, Xiaomi MiMo, z.ai/GLM, Kimi/Moonshot, MiniMax, Hugging Face e Custom Endpoint. Trocar de provedor é uma linha de comando, sem refazer setup:

```bash
# Wizard guiado de provider/modelo (com OAuth quando suportado)
hermes model

# Alternativamente, passar como flag em sessão única
hermes chat -m "anthropic:claude-sonnet-4-6" -q "explica esse arquivo"

# Dentro do chat, pelo slash command
/model anthropic:claude-sonnet-4-6
/model --global   # persiste a troca na config
```

Para gerenciar credenciais (API keys e OAuth):

```bash
hermes auth list        # mostra pools cadastrados
hermes auth add         # adiciona key/oauth
hermes auth remove      # remove
hermes auth reset       # limpa cooldowns
```

Cuidados importantes com API keys, custos e limites:

- API keys vão para ~/.hermes/.env ou para o config do perfil. Nunca commit no Git. Verificar .gitignore se versionar configurações.
- Provedores cobram por token. Modelos top (Opus 4.6/4.7, GPT-5.x XHigh, Gemini 3.1 Pro) são caros. Para uso pessoal contínuo, considerar planos com limite (Z AI/GLM, Opencode Go, Minimax) ou OpenRouter Pay-as-You-Go.
- Modelo precisa ter pelo menos 64.000 tokens de contexto segundo a doc — modelos menores não funcionam bem.
- Em VPS multi-agente, custos somam: cada agente usa tokens em separado. Calcular orçamento mensal realista.
### Como validar se a configuração inicial está funcionando

```bash
hermes doctor          # passa em verde se tudo ok
hermes status          # mostra agent, auth, platforms
hermes status --deep   # checks estendidos
hermes auth list       # confirma se a chave está cadastrada
```

Depois disso, abrir o chat e mandar um prompt de teste (próxima seção).




## 9. Primeiras mensagens com o Hermes no terminal

### Como abrir o Hermes no terminal/TUI

```bash
hermes              # abre sessão interativa
hermes --tui        # interface TUI moderna (com modais, mouse)
hermes -c           # continuar última sessão (--continue)
hermes -r <ID>      # retomar sessão específica
hermes chat -q "pergunta direta"  # one-shot, sem entrar em modo interativo
```

A documentação oficial descreve a CLI como uma TUI completa — banner superior com modelo/diretório/ferramentas, área de conversa com streaming em tempo real, prompt fixo na base, e barra de status mostrando "modelo · tokens · barra de contexto · custo · duração".

### Keybindings que valem a pena guardar

### Slash commands principais

Digitar / no chat abre o autocomplete. Os mais úteis para começar:

- /help — ajuda
- /model — ver/trocar modelo dentro da sessão
- /tools — ferramentas habilitadas
- /skills — skills instaladas (e /<skill-name> para invocar uma)
- /personality <nome> — trocar persona (concise, pirate, kawaii, etc.)
- /save — salvar checkpoint
- /clear — resetar contexto da conversa
- /title <nome> — nomear a sessão
- /memory — consultar/atualizar memória
- /rollback — desfazer alterações no filesystem
- /background <prompt> — rodar tarefa em sessão paralela
- /voice on / /voice off — modo voz
- /reasoning high — aumentar esforço de raciocínio
- /verbose — ciclar nível de detalhe (off → new → all → verbose)
- /stop — interromper operação
- /quit — sair
### Primeiros prompts para testar o agente

Comece com tarefas pequenas para entender o comportamento antes de avançar para programação:

```plain text
# 1
Hermes, se apresenta. Qual o seu modelo atual,
quais ferramentas estão habilitadas, e o que
você sabe sobre mim?

# 2
Pesquise e analise todas as skills, plugins e MCPs
que eu tenho instalados no Claude Code, Codex e Opencode,
e em seguida instale e configure todos eles no Hermes.
Habilite e configure também a busca na web através da
ddg, de forma grátis.

# 3
Salva na sua memória que meu nome é Felipe,
moro em Sapiranga/RS, sou programador e sou fundador
da PycodeBR (escola online de programação Python e IA).
Meus projetos estão em /Users/azambuja/projects/.
Analise os projetos mais relevantes e salve informações
dos mesmos na memória, são eles: MentorIA, Notify, SGE,
schedule_messages, SCS, Finanpy, emissoes_nfs, todas as
páginas com final "_lp", design_system_lib, car_api.
Eu tenho assinatura Claude Code Max, GPT Plus, Opencode Go
e Google IA. Uso o Claude Code CLI, Codex CLI, Opencode CLI
e Gemini CLI geralmente para trabalhar nos meus projetos.
No meu notion tem detalhes sobre fluxos de trabalho que uso
e ensino, nas páginas da Imersão IA para Devs aula 01 e aula 02,
além de mais detalhes de como trabalho na página Elite Wiki do Notion.
Use o delegate task e suas skills de uso do Claude Code, do Codex e
do Opencode sempre que achar necessário para realizar um tarefa.
Tenho preferência por trabalhar em projetos de programação
com o Claude Code no modelo Opus 4.7 XHigh ou Max effort, com
o Codex com modelo GPT-5.5 XHigh, ou então com Opencode com modelo
GLM-5.1 através do Opencode Go.
Sempre verifique e use as skills necessárias para cada tarefa, sem que
eu precise indicar explicitamente a skill que deve ser usada. Fala
uma análise da tarefa e então decida qual skill utilizar, e caso tenha
dúvidas, me pergunte dando alternativas.
Use isso em sessões futuras.
```

O primeiro prompt valida que o agente está rodando e enxergando o ambiente. O segundo valida que o backend de execução de comandos funciona (terminal). O terceiro valida que a memória persiste — feche a sessão, abra de novo, e pergunte "qual meu nome".

### Como observar comportamento, memória e execução

- A barra de status na base mostra tokens consumidos e custo em tempo real.
- A animação de pensamento (com timer) indica que o agente está processando.
- Cada chamada de ferramenta aparece com ícone e duração: terminal ls -la (0.3s), web_search (1.2s).
- Use /verbose all para ver mais detalhes do raciocínio.
- Logs detalhados em hermes logs agent -n 100 ou hermes logs errors -n 50.
### Como pedir tarefas simples antes de avançar para programação

Comece simples, escale aos poucos. Padrão didático do material:

```plain text
1. Tarefa de leitura: "Lê esse arquivo X e me explica
   o que ele faz."

2. Tarefa de listagem: "Liste todas as pastas dentro
   de ~/projects."

3. Tarefa de cálculo: "Quantas linhas tem o arquivo
   Y? Use wc."

4. Tarefa de busca: "Procura no diretório atual por
   referências a 'Pacote Python Master'."

5. Tarefa de geração curta: "Gera um README curto
   para esse projeto baseado no que você ler."
```

Cada degrau dá oportunidade de revisar o que o agente fez antes de avançar. Esse hábito (revisar antes de aprovar) é fundação para o uso seguro de qualquer agente autônomo.




## 10. Hermes Dashboard web

A doc oficial confirma que existe um dashboard web invocável via comando dedicado. Ele expõe configuração, sessões e visualização — não substitui a TUI, é complementar.

### Como rodar o dashboard

```bash
hermes dashboard              # abre dashboard na porta padrão
hermes dashboard --port 8765  # porta customizada
hermes dashboard --no-open    # roda sem abrir browser automático
```

### Como acessar o dashboard

Após hermes dashboard, o terminal exibe a URL local (algo como http://localhost:<porta>). Se foi --no-open, abrir manualmente no browser. Em VPS, expor a porta com cuidado (firewall + autenticação) — não deixar dashboard exposto publicamente sem proteção.

### O que observar dentro da interface

A doc indica que o dashboard contempla:

- Visão geral de configuração do agente
- Lista de sessões com possibilidade de retomar/exportar/excluir
- Painel de chat (browser-based, em estágio inicial — requer POSIX PTY/WSL2 segundo a doc)
- Configurações editáveis pela interface
PONTO A CONFIRMAR: o dashboard web está descrito na doc como funcional mas em estágio inicial em alguns aspectos (chat browser-based, por exemplo). Validar versão exata e features disponíveis na v0.13.0+ antes da aula. Para aula ao vivo, mostrar o que estiver estável (lista de sessões, configuração) e marcar o resto como "em evolução".

### Extras sobre o dashboard

- Retomar uma sessão antiga via dashboard vs hermes -c na CLI.
- A TUI é a interface principal — o dashboard é janela auxiliar para visualizar/gerenciar.



## 11. Usando Hermes Agent para programar

Aqui o objetivo é ensinar a delegar tarefas de código ao Hermes com revisão sistemática. Mesma disciplina que aplicamos com Claude Code, Codex e Opencode — IA é copiloto, humano revisa.

### Como pedir para o Hermes analisar um projeto

```plain text
1. Abrir o Hermes na pasta raiz do projeto:
   cd ~/projects/finanpy
   hermes

2. Prompt inicial:
   "Analise a estrutura desse projeto. Me diga:
    - qual é o stack
    - quais são os módulos/apps principais
    - se existe README ou PRD.md, resuma
    - aponte 3 pontos que parecem precisar de
      atenção (qualidade, organização, dívida)"

3. Aguardar a análise. Revisar cada apontamento.
```

### Como pedir pequenas alterações de código

Comece com mudanças cirúrgicas. Não delegue refactor inteiro logo de cara.

```plain text
"No arquivo X linha Y, a função Z tem um bug:
 ela retorna None quando deveria retornar 0.
 Faça a correção, mostre o diff antes de
 aplicar, e explique o porquê."
```

Padrão a seguir sempre:

- Diff antes de aplicar — o agente mostra a mudança proposta, você aprova.
- Explicação curta do porquê — força o agente a justificar.
- Teste manual ou automatizado depois — você valida que a mudança fez o que devia.
### Como pedir explicações sobre a estrutura do projeto

```plain text
"Mapeie o fluxo de dados desde a request HTTP
 até o banco para o endpoint /api/v1/users/me.
 Liste cada middleware, view, serializer e
 modelo envolvido."
```

Esse tipo de pergunta cai bem antes de começar uma sprint nova — calibra o entendimento do agente sobre o projeto antes de pedir alterações.

### Como pedir criação de arquivos, documentação e testes

```plain text
1. "Crie um README.md curto para esse projeto
    baseado no PRD.md e no código existente.
    Foco em: o que é, como rodar local, como
    rodar testes."

2. "Gere testes unitários para a função X usando
    pytest. Cobertura para casos: feliz, edge
    case com input vazio, edge case com input
    inválido."

3. "Documente as principais decisões arquiteturais
    desse projeto em docs/ARCHITECTURE.md
    seguindo o template ADR (Architecture
    Decision Record)."
```

### Como revisar o que o Hermes fez antes de confiar no resultado

Disciplina de revisão (vale para Hermes, Claude Code, Codex e qualquer outro agente):

1. Ler o diff completo — nunca aprovar mudança sem ler.
2. Rodar testes se existirem — pytest, npm test, etc.
3. Rodar a aplicação localmente se a mudança afeta runtime.
4. Git diff antes de commitar — confirmar que só mudou o que esperava.
5. Commit feito por você, não pelo agente — controlar o histórico do projeto. (Esse é o padrão que ensino na ‣: não terceirizar Git para a IA.)
/rollback no chat desfaz alterações no filesystem — bom paraquedas quando algo saiu fora do esperado, mas não substitui revisão.

### Exemplos práticos no contexto da PycodeBR

- finanpy: pedir ao Hermes para mapear a modelagem de dados e sugerir melhorias de organização sem mudar código.
- MentorIA: pedir uma análise do agents/ e sugestão de estrutura para nova capability sem implementar.
- Pacote Python Master / IA Master: pedir para gerar README didático de um projeto-exemplo de aula.
- schedule_messages: pedir para revisar o tasks.py (APScheduler) e sugerir testes unitários.
- Aluno em projeto pessoal: usar o Hermes para fazer onboarding de si mesmo no próprio projeto que parou há 3 meses — "lê tudo aqui e me explica onde eu parei".



## Referências e materiais relacionados

- Documentação oficial Hermes Agent: hermes-agent.nousresearch.com/docs
- CLI reference oficial: hermes-agent.nousresearch.com/docs/reference/cli-commands
- Quickstart oficial: hermes-agent.nousresearch.com/docs/getting-started/quickstart
- Repositório oficial: github.com/NousResearch/hermes-agent
- Skills Hub aberto: agentskills.io
- ‣ — fundamentos de uso de IA assistida no dia a dia de desenvolvimento
- ‣ — workflow Spec-Driven Development com IA
- ‣ — biblioteca de prompts da Imersão
- ‣ — setups completos de IA usados na PycodeBR
- ‣ — material precursor sobre agentes pessoais (OpenClaw)
- ‣ — prompts brutos usados na auto-configuração do time Hermes
- ‣ — guia completo do time multi-agente (Kratos, Zeus, Hera, Atena, Ares) — base direta da parte 02
- ‣ — acervo central de IA aplicada ao desenvolvimento
- ‣ — índice central de materiais
