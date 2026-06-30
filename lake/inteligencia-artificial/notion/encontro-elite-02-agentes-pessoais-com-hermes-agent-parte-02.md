---
titulo: Encontro Elite #02 | Agentes pessoais com Hermes Agent (parte 02)
disciplina: inteligencia-artificial
fonte: notion
origem: https://pickle-reading-bd9.notion.site/Encontro-Elite-02-Agentes-pessoais-com-Hermes-Agent-parte-02-36a9956f3dc9805785c3c70517672f75
data: 2026-06-30
page_id: 36a9956f-3dc9-8057-85c3-c70517672f75
status: bruto
---

# Encontro Elite #02 | Agentes pessoais com Hermes Agent (parte 02)

> Nessa parte 02 vamos instalar e configurar o Hermes em uma VPS, além de conectar e configurar ferramentas externas para o Hermes ter acesso ao nosso ecossistema.



Desenhos: ‣



### Configurações da VPS Contabo

VPS preços: ‣

Painel: ‣




#### Configuração do Firewall

![imagem](attachment:2722926f-a69c-48bd-b784-69193f4440d8:image.png)




#### Acesso SSH

Conecte na VPS como root usando o IP e senha definidos no painel da Contabo:

```bash
ssh root@IP_DA_VPS
```

---

#### Setup da VPS (primeiros comandos)

Execute os comandos abaixo em ordem para preparar o servidor.

1. Atualizar o sistema

```bash
sudo apt update && sudo apt upgrade -y
```

2. Criar usuário para o Hermes

É recomendado usar um usuário diferente do root para rodar o Hermes:

```bash
adduser hermes
# Preencha a senha quando solicitado

usermod -aG sudo hermes

# Copiar chaves SSH do root para o novo usuário
mkdir -p /home/hermes/.ssh
cp /root/.ssh/authorized_keys /home/hermes/.ssh/
chown -R hermes:hermes /home/hermes/.ssh
chmod 700 /home/hermes/.ssh
chmod 600 /home/hermes/.ssh/authorized_keys
```

Agora reconecte como usuário hermes:

```bash
ssh hermes@IP_DA_VPS
```

3. Instalar ferramentas base

```bash
sudo apt install -y curl git htop iotop net-tools unzip
```

4. Instalar Node.js via NVM

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash
source "$HOME/.nvm/nvm.sh"
nvm install 24
node -v  # Deve imprimir v24.x
npm -v   # Deve imprimir 11.x
```

5. Instalar Docker

```bash
# Remover versões antigas (se houver)
sudo apt remove -y docker docker-engine docker.io containerd runc 2>/dev/null

# Instalar via script oficial
curl -fsSL https://get.docker.com | sudo sh

# Adicionar usuário hermes ao grupo docker
sudo usermod -aG docker hermes
newgrp docker

# Habilitar na inicialização
sudo systemctl enable docker
sudo systemctl start docker

# Verificar
docker --version
docker run hello-world
```

6. Configurar timezone

```bash
sudo timedatectl set-timezone America/Sao_Paulo
timedatectl
```

7. Configurar chave SSH para o GitHub

```bash
ssh-keygen -t ed25519 -C "seu_email@example.com"
cat ~/.ssh/id_ed25519.pub
```

Copie a chave gerada e adicione no GitHub: Settings → SSH and GPG Keys → New SSH Key




### Instalar e configurar Hermes e outros CLIs na VPS

```shell
# Instalar Hermes
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# Add ao path
source ~/.bashrc

# Setup Hermes
hermes setup

# Pode começar por Quick setup e selecionar o provedor de modelos
# e o modelo que irá utilizar inicialmente.
# Canais de mensagens podemos deixar para depois por enquanto (skip).

# Para configurar conta do ChatGPT/Codex como provedor
hermes model

# Então selecione OpenAI/Codex. Um link será gerado - abra-o no navegador,
# faça login na sua conta e informe o código gerado no servidor.
# Em seguida selecione o modelo desejado (GPT-5.5)
```

Irei utilizar como provedor de modelo minha assinatura Opencode Go.

Link para assinar: OpenCode Go | Low cost coding models for everyone


Também utilizarei minha assinatura do ChatGPT Plus para usar modelos da OpenAI.




Recomendações de modelos

Para o dia a dia utilizo o modelo Deepseek v4 flash pela assinatura da Opencode Go devido aos limites elevados.

Para tarefas mais complexas, utilizo o modelo GPT-5.5 pela minha assinatura do ChatGPT/Codex.

Para criação de contexto e memórias iniciais do Hermes, utilize bons modelos, como:

- GPT-5.5 pela OpenAI
- GLM-5.1, Qwen 3.7 Max ou Kimi K2.6 pela Opencode Go



#### Instalar outros CLIs

Utilizaremos também no nosso servidor Claude Code CLI, Codex CLI e Opencode, portanto precisamos instalar as ferramentas e autenticar.

```shell
# Claude Code
npm install -g @anthropic-ai/claude-code

# Codex
npm install -g @openai/codex

# Opencode
npm install -g opencode-ai

```

Abra cada uma das CLIs e autentique com suas contas.




#### Habilitar busca na Web com DuckDuck Go

```plain text
Instale e configure no Hermes a busca na web usando DuckDuck Go (grátis).
```




#### Importar skills, plugins e MCPs (OPCIONAL)

Primeiro, na nossa máquina local, abra alguma CLI de sua preferência e execute o seguinte prompt:

```plain text
Faça uma lista com nome, descrição, link do site/repositório e comando de
instalação de todas as skills, plugins e MCPs que estão configurados nessa
máquina no Claude Code CLI, Codex CLI e no Opencode. (Exceto plugins, skills
e MCPs customizados/personalizados).
Coloque tudo em um arquivo setup_cli.md.
Essas informações serão usadas para importar em uma nova IA e ela instalar e
configurar todas essas ferramentas em um novo ambiente.
```


Na VPS, vamos abrir o Hermes em modo yolo (hermes —yolo), e então executar o prompt:

```plain text
Instale e configure todas as skills, plugins e MCPs listados abaixo. Instale
para o Hermes, Claude Code CLI, Codex e Opencode de forma global.
<CONTEÚDO DO setup_cli.md GERADO>
```


Alguns MCPs podem solicitar autenticação, chaves de APIs e Keys. Portanto podemos pedir para o hermes nos ajudar a autenticar:

```plain text
Verifique todos os MCPs servers que necessitam de login/autenticação no Hermes,
Claude Code CLI, Codex e Opencode.
Os que ainda não estiverem autenticados e funcionando, me peça por aqui tudo
o que você precisa para autenticar. Salve todas as credenciais que enviarei no
.env do Hermes.
```




#### Configurar acesso ao Notion e ao WhatsApp (Evolution API)

Para o Notion, podemos gerar uma API Token e fornecer para o Hermes usar sua skill nativa de Notion: Notion | Where teams and agents work together


Atualmente eu uso o Evolution API para WhatsApp, e forneço o acesso a minha instância para o Hermes utilizar. Caso ainda não tenha uma instância do Evolution API, podemos pedir para o Hermes subir no servidor para nós, e configurar o acesso:

```plain text
Instale e suba no servidor com Docker, o Evolution API. Use volumes
persistidos. Crie uma chave de acesso e a utilize (coloque no .env do Hermes).
Após a instalação, salve na memória e crie uma skill para usar a API do
Evolution sempre que eu solicitar algo relacionado ao WhatsApp.

Siga a documentação e suba todos os serviços necessários para isso:
https://doc.evolution-api.com/v2/pt/install/docker
https://github.com/evolution-foundation/evolution-api

E por fim, deixe o manager do Evolution disponível para acesso externo HTTP.
Suba e me passe a URL e as credenciais de acesso.
```

Liberar no Firewall do servidor no painel da Contabo, as portas HTTP 8080 e 3000.


Sempre que conectar uma instância no Evolution, informe ao Hermes o nome e o propósito dela:

```plain text
Salve isso na memória:
Criei no Evolution uma instância chamada <SUA_INSTANCIA>. Esse é o meu WhatsApp
pessoal, e usaremos para você me informar sobre relatórios diários,
pesquisas e buscas quando eu solicitar.
```


Após completar a etapa de setup do Hermes e da VPS, recomendo fazer um snapshot através do painel da Contabo.




#### Hermes no GitHub

Manter o ~/.hermes versionado no GitHub garante backup, histórico e a possibilidade de restaurar a configuração em outro servidor. Aqui está o setup que usamos.

> Atenção: o diretório ~/.hermes contém tokens e chaves de API. O .gitignore precisa excluir esses arquivos para não vazar segredos.

1. Criar repositório no GitHub

Crie um repositório privado (ex: hermes_vps).

2. Configurar o .gitignore

Edite ~/.hermes/.gitignore com pelo menos:

```shell
# Secrets — NUNCA versionar
.env
auth.json
google_token.json
google_client_secret.json
# Runtimes e caches (recriáveis)
node/
audio_cache/
image_cache/
cache/
sandboxes/
bin/
# Travas de execução
\*.lock
\*.pid
```

3. Primeiro commit

```shell
cd ~/.hermes
git init
git add .
git commit -m "feat: setup inicial Hermes"
git branch -M main
git remote add origin git@github.com:SEU_USUARIO/hermes_vps.git
git push -u origin main
```

Abra o Hermes e dê o seguinte comando no chat:

```shell
Crie um cron job que roda todo dia às 23h para sincronizar o diretório
/home/hermes/.hermes com o GitHub.
```

O Hermes vai usar a tool cronjob para criar o job automaticamente. Você pode verificar com:

```shell
hermes cron list                  # job deve aparecer como active
hermes cron run hermes-vps-sync   # testar execução manual
cd ~/.hermes && git log --oneline # ver histórico de commits
```

> Alternativa via CLI: se preferir, pode criar direto no terminal com hermes cron create "0 23 * * *" --name "hermes-vps-sync" --workdir /root/.hermes --prompt '...'

5. Verificar

```shell
hermes cron list                  # job deve aparecer como active
hermes cron run hermes-vps-sync   # testar execução manual
cd ~/.hermes && git log --oneline # ver histórico de commits
```

Como fica o fluxo

- Durante o dia, você configura skills, ajusta MCPs, mexe em profiles — tudo no ~/.hermes
- Às 23h o job roda automaticamente: git add . && git commit && git push
- Seu GitHub fica sempre espelhando o estado atual do Hermes na VPS
- Para restaurar em outro servidor: git clone git@github.com:SEU_USUARIO/hermes_vps.git ~/.hermes
> Segurança: antes de qualquer git push, revise o diff para garantir que nenhum token vazou: git diff --cached | grep -E 'xoxb-|xapp-|sk-[A-Za-z0-9]'.

> Dica extra: se quiser versionar também o vault ~/life (segundo cérebro), use o mesmo padrão com outro repositório e outro job diário.




#### Multi Canais — Slack

O Hermes pode operar em canais do Slack, respondendo a menções e DMs. Aqui está o essencial para conectar.

> Guia completo com arquitetura multi-agente (Kratos, Zeus, Hera, Atena, Ares no mesmo canal): Guia Completo: Time Multi-Agent no Slack com Hermes

1. Criar o app no Slack

Acesse api.slack.com/apps, clique Create New App → From Scratch. Nomeie (ex: "Hermes") e escolha o workspace.

2. Habilitar socket mode

Socket Mode → Enable Socket Mode

Digite um nome qualquer, por exemplo, Hermes. Em seguida salve o App Key gerado.

3. Configurar permissões

Em OAuth & Permissions, adicione os scopes de Bot Token:

- app_mentions:read, channels:history, channels:read, channels:join
- chat:write, chat:write.customize, chat:write.public, files:write , files:read
- groups:history, groups:read, groups:write
- im:history, im:read, im:write
- mpim:history, mpim:read, mpim:write
- reactions:read, reactions:write
- users:read, team:read
Instale o app no workspace e copie o Bot User OAuth Token (xoxb-...).

4. Configurar Event Subscriptions

Em Event Subscriptions, ative On e defina Request URL como https://seu-dominio:9090/slack/events (use o IP da VPS ou um túnel como ngrok para teste).

Em Subscribe to Bot Events, adicione:

- app_mention — responde quando mencionado
- message.channels — mensagens em canais públicos
- message.groups — mensagens em grupos públicos
- message.im — DMs
5. Configurar no Hermes

Use o comando abaixo e depois selecione "Slack". Após isso basta informar o App Token e Bot Token gerados acima:

```shell
hermes gateway setup
```

Obs: copie o seu ID de membro do Slack e configure como usuário permitido. Em seguida copie o ID do canal que deseja que o bot tenha acesso.

Defina o comportamento:

```shell
hermes config set slack.require_mention true
hermes config set slack.free_response_channels '<ID_DO_CANAL>'
```

6. Iniciar o gateway

```shell
hermes gateway run          # direto no terminal (teste)
hermes gateway install      # instalar como serviço
hermes gateway start        # iniciar como serviço de fundo
hermes gateway status       # verificar se está conectado
```

7. Convidar o bot para o canal

No Slack, vá até o canal desejado (ex: #operacao) e digite /invite @Hermes.

8. Testar

No canal, mencione o bot: @Hermes, qual a previsão do tempo hoje?

> Configuração Multi-Agente: para rodar múltiplos agentes (Kratos, Zeus, Hera, etc.) no mesmo canal, cada um precisa de um profile Hermes separado com seu próprio bot token Slack. O guia completo linkado acima detalha profiles, mention-only routing e systemd services.

9. Mensagem na DM (OPCIONAL)

App Home → (Always Show My Bot as Online, Home Tab, Messages Tab, Allow users to send Slash commands and messages from the messages tab)




#### Outras integrações

Além do Slack, WhatsApp e Notion, o Hermes pode se conectar a várias outras ferramentas do ecossistema:

---

Google Workspace (Gmail, Calendar, Drive)

Permite o Hermes ler e-mails, verificar agenda e buscar arquivos no Drive. Usamos a skill google-workspace do Hermes com autenticação OAuth.

Passo a passo:

1. Criar credenciais OAuth no Google Cloud Console (uma vez):
2. Rodar o setup de autenticação:
```shell
python ~/.hermes/skills/productivity/google-workspace/scripts/setup.py --client-secret ~/.hermes/google_client_secret.json
```

1. Gerar URL de autorização:
2. Trocar o código pelo token:
3. Verificar:
Depois de autenticado, o Hermes pode usar comandos como:

- $GAPI gmail search "is:unread" — ler e-mails não lidos
- $GAPI calendar list — ver próximos eventos
- $GAPI drive search "relatório" — buscar arquivos no Drive
> Dica: a skill também permite enviar e-mails, criar eventos no calendário, criar planilhas e documentos. Sempre confirme com o usuário antes de executar ações destrutivas.

---

Geração de imagens (GPT-Image-2)

O Hermes pode gerar imagens com o modelo GPT-Image-2 da OpenAI usando a assinatura do ChatGPT/Codex.

Pré-requisito: ter o plugin de image_gen habilitado e autenticação com OpenAI Codex configurada (via hermes login --provider openai-codex ou configurada no hermes model).

Configuração:

1. Habilite o plugin de image_gen:
2. Configure o provider e modelo no ~/.hermes/config.yaml:
3. Habilite a toolset de image_gen:
4. Faça um /reset no Hermes para recarregar as tools.
Uso: após configurado, basta pedir no chat:

- "Gere uma imagem de um dashboard futurista com tema dark"
- "Crie um banner para um curso de Python com fundo tecnológico azul"
O Hermes usa a tool image_generate que entrega a imagem diretamente.

> Nota: para usar o FAL como backend alternativo, configure image_gen.provider: fal e defina a env var FAL_KEY.


Ou então:

```plain text
Configure a tool image_gen para usar gpt-image-2 através da minha assinatura da
OpenAI/Codex.
```

---

X (Twitter) API

O Hermes pode postar, buscar, responder e interagir com o X usando o CLI oficial xurl — que é o que usamos aqui com o app pycodebr.

Pré-requisito: conta de desenvolvedor no developer.x.com com um app criado no plano pago (Free ou Basic).

Passo a passo:

1. Instalar o xurl:
2. Criar um app no X Developer Portal:
3. Registrar e autenticar o app (rodar manualmente, fora do Hermes):
Esse passo abre o navegador para o OAuth. Se estiver em uma VPS sem interface gráfica, use um túnel SSH:

1. Salvar as credenciais no .env do Hermes:
```shell
echo "X_APP_NAME=pycodebr" >> ~/.hermes/.env
echo "X_CLIENT_ID=..." >> ~/.hermes/.env
echo "X_CLIENT_SECRET=..." >> ~/.hermes/.env
echo "X_REDIRECT_URI=http://localhost:8080/callback" >> ~/.hermes/.env
```

1. Verificar:
Comandos úteis:

> Importante: para postar, prefira o raw API: xurl --app pycodebr -X POST /2/tweets -d '{"text":"..."}'. O comando xurl post tem um bug conhecido que retorna 403 mesmo com auth válida.

---

Meta / Instagram Graph API

O Hermes pode acessar a conta profissional do Instagram e métricas da página do Facebook via Graph API direta com curl.

Pré-requisito: conta de desenvolvedor no developers.facebook.com com um app criado e uma página do Facebook conectada a um perfil profissional do Instagram.

Passo a passo:

1. Criar o app no Meta Developer:
2. Obter token de acesso de longa duração:
3. Descobrir o Instagram User ID:
4. Salvar no .env do Hermes:
5. Criar cron job de refresh do token (opcional):
Comandos úteis:

```shell
# Listar posts recentes
source ~/.hermes/.env
GRAPH="https://graph.facebook.com/${META_GRAPH_API_VERSION:-v25.0}"
curl -s "$GRAPH/${IG_USER_ID}/media?fields=id,media_type,media_url,permalink,timestamp,caption,like_count,comments_count&limit=10&access_token=${META_PAGE_ACCESS_TOKEN}"

# Listar stories ativos (expiram em 24h)
curl -s "$GRAPH/${IG_USER_ID}/stories?fields=id,media_type,media_url,thumbnail_url,permalink,timestamp,caption&access_token=${META_PAGE_ACCESS_TOKEN}"

# Ver métricas de um post
curl -s "$GRAPH/MEDIA_ID/insights?metric=impressions,reach,saved&access_token=${META_PAGE_ACCESS_TOKEN}"
```

> Dica: os tokens expiram a cada 60 dias. Para renovar automaticamente, peça ao Hermes um cron job:

```plain text
Crie um cron job que roda a cada 45 dias para renovar o token da Meta/Instagram.
```




### Integrações com Composio

Uma opção mais prática para as integrações com ferramentas externas, é usar o serviço de broker de integrações ‣

Podemos pedir para o Hermes no ajudar a configurar o CLI e o MCP do Composio:

```plain text
Instale e configure o CLI e o MCP do Composio. Usaremos algumas integrações com
ferramentas externas através do Composio.
Pesquise como configurar.
MCP URL: https://connect.composio.dev/mcp
Api Key: SUA_API_KEY_DO_COMPOSIO
```




### Base de contexto (segundo cérebro)

O segundo cérebro é um vault Obsidian versionado no GitHub que serve como base de conhecimento permanente para seu Hermes. É onde o agente busca contexto sobre você (rotina, finanças, saúde, projetos, família) e onde ele registra tudo que acontece.

Use o tutorial completo do Segundo Cérebro como guia. Ele contém o passo a passo detalhado, o prompt mestre de entrevista e construção (já ajustado para funcionar em qualquer CLI), templates, convenções de nomenclatura e regras de módulos.

#### Requisitos

- CLI de IA: pode usar qualquer um (Claude Code, Codex, Cursor, OpenCode, Hermes Agent, etc.).
- Modelo recomendado: use um modelo de ponta para a criação inicial — GPT-5.5 (OpenAI), Claude Opus 4.7 (Anthropic), GLM-5.1 ou Kimi K2.6 (OpenCode Go). Modelos fortes produzem uma base mais rica e consistente.
- Onde criar: pode fazer no seu computador local ou direto na VPS. Se fizer local, depois sobe os arquivos para a VPS via Git. Se fizer na VPS, lembre-se de instalar o Obsidian nela ou editar os arquivos manualmente (são markdown puro).
#### Pré-configure as integrações

Antes de rodar a entrevista, conecte as ferramentas que o CLI de IA escolhido vai usar para enriquecer o contexto:

- Notion — gere um token de integração em notion.so/my-integrations e autorize acesso às suas páginas
- GitHub — configure a chave SSH (já fizemos isso nos passos anteriores)
- Google Workspace (opcional) — conecte Gmail, Calendar e Drive para o agente ler compromissos e documentos
- Qualquer outra base de conhecimento que você usa
- Busca na web — DuckDuckGo ou outra ferramenta de busca configurada
#### Passo a passo

1. Acesse a VPS via SSH como usuário hermes (ou abra o terminal local onde vai criar a base).
2. Crie a pasta do vault:
```shell
mkdir -p ~/life
cd ~/life
```

1. Abra o CLI de IA na pasta e cole o prompt mestre de criação do Segundo Cérebro. Basta copiar o prompt da página (os dois blocos de código em sequência) e colar no terminal.
2. Responda a entrevista — o agente vai fazer uma pergunta por vez. Seja detalhista. Quanto mais completo você responder, melhor será a base.
3. Aprove o plano apresentado pelo agente. Ele vai exibir a árvore de pastas e arquivos que serão criados.
4. Aguarde a construção — o agente cria toda a estrutura: arquivo de contexto raiz, pastas por módulo (Financeiro, Saúde, Trabalho, Rotina, Journal, Conhecimento, Pessoal), templates, logs do Kratos.
5. Valide a entrega — confira se os arquivos fazem sentido, se os módulos escolhidos estão lá, se as regras de gatilhos estão claras.
6. Abrace o sistema editando os arquivos de contexto sempre que precisar ajustar regras — não recrie tudo.
> Dica: se criou localmente, suba os arquivos para a VPS com scp ou clone o repositório Git na VPS depois de criar o repositório (próximo passo).

#### Versionar no GitHub

A base precisa estar versionada para funcionar como fonte de verdade entre sessões e dispositivos.

1. Crie um repositório no GitHub (ex: life), privado.
2. Na pasta do vault:
3. Verifique se .gitignore inclui:
Depois de criado, clone na VPS:

#### Ensinar o Hermes a usar e manter a base

Após criar a base no servidor, salve estas instruções na memória do Hermes executando o prompt abaixo no Hermes (no diretório da base ~/life):

```plain text
Salve na sua memória como um bloco permanente:


BASE DE CONTEXTO: ~/life

Este diretório é um vault Obsidian versionado no Git que contém TODO o meu contexto pessoal e profissional.

Estrutura:
- Arquivo de contexto raiz (CLAUDE.md, INDEX.md, .cursorrules, etc — varia conforme o CLI)
- Pastas por módulo: Financeiro/, Saude/, Trabalho/, Rotina/, Journal/, Conhecimento/, Pessoal/, Kratos/
- Cada módulo com seu próprio arquivo de contexto e regras específicas
- Kratos/Logs/ com logs de todas as sessões
- Recursos/Templates/ com modelos prontos

REGRAS DE USO:
1. SEMPRE que eu iniciar uma conversa, execute cd ~/life && git pull para ter a versão mais recente
2. Consulte a base para responder QUALQUER pergunta sobre mim — não invente fatos
3. Quando eu mencionar algo que deva ser registrado (gasto, treino, reunião, ideia), atualize o arquivo correspondente seguindo as regras do módulo
4. Ao final de cada sessão produtiva, registre um log em Kratos/Logs/YYYY-MM-DD-HHmm.md e atualize o índice
5. SEMPRE que alterar ou criar um arquivo na base, execute:
   cd ~/life && git add . && git commit -m "descrição" && git push
6. Se encontrar informação desatualizada ou conflitante, atualize e commite
7. Antes de qualquer operação que dependa de contexto atual, faça git pull primeiro
```

Depois de salvar na memória, o Hermes automaticamente aplica essas regras em toda sessão.


#### Fluxo diário com a base

A partir de agora, seu dia com o Hermes na VPS fica:

```plain text
1. Abre terminal na VPS
2. cd ~/life && git pull
3. hermes chat (ou o CLI escolhido)
4. "bom dia, me dá um briefing" → Kratos cruza os módulos e resume o dia
5. Durante o dia: "gastei R\$80 no almoço", "treinei hoje", "reunião com X"
6. Fim do dia: "fecha a sessão" → Kratos cria log e commita as alterações
```

Tudo versionado, tudo pesquisável, nenhuma informação perdida entre sessões.



---

### Dicas e Casos de Uso

Com o Hermes rodando na VPS, conectado a Slack, WhatsApp, Notion, Google Workspace, GitHub e segundo cérebro, um mundo de automações se abre. Aqui estão ideias práticas do que fazer com o setup completo.

---

Com o segundo cérebro + Google Calendar + Gmail:

```plain text
"bom dia, me dá um briefing"
```

Kratos cruza: compromissos do dia (Calendar), e-mails não lidos importantes (Gmail), última movimentação financeira, treino agendado e tarefas pendentes do log de ontem.

---

#### Gestão financeira simplificada

Com o segundo cérebro + Google Sheets (planilha real):

```plain text
"gastei R\$ 80 no almoço"
"recebi R\$ 5.000 de cliente X"
"como tá meu mês financeiro?"
```

Kratos registra no vault e pode sync com a planilha no Google Sheets.

---

#### Postagem em múltiplos canais

Com X API + Meta/Instagram API + Evolution API:

```plain text
"Gere um post sobre agentes de IA e publique no X e no Instagram"
"Cria um carrossel educativo sobre Python e posta no Insta"
"Envia um resumo do encontro de hoje no grupo do WhatsApp"
```

O Hermes gera o conteúdo, adapta o formato para cada plataforma e publica.

---

#### Geração de imagens para conteúdo

Com GPT-Image-2:

```plain text
"Cria um banner 16:9 para o post do Instagram sobre agentes de IA"
"Gera uma thumbnail para o vídeo de hoje no YouTube"
"Faz uma imagem de fundo para o story do WhatsApp"
```

Imagens geradas com qualidade profissional e enviadas diretamente no canal.

---

#### Pesquisa e curadoria de conteúdo

Com busca na web + Notion:

```plain text
"Pesquisa as 5 melhores práticas de RAG em 2026 e salva na base de conhecimento"
"Busca referências sobre fine-tuning e adiciona no Notion"
"Monitora o feed de lançamentos da OpenAI e me resume"
```

Hermes busca, filtra, organiza e salva direto na sua base ou Notion.

---

#### Organização de reuniões e projetos

Com Google Calendar + Slack + segundo cérebro:

```plain text
"Agenda reunião com o Zucchi amanhã 14h sobre tráfego"
"Registra a reunião de ontem com o cliente e salva no vault"
"Cria uma task no ClickUp para ajustar a página de vendas"
```

Kratos cria o evento, registra ata no vault e notifica no Slack.

---

#### Automações noturnas com cron jobs

Jobs que rodam automáticos na VPS:

- 23:00 — Sync do ~/.hermes com GitHub (backup das configurações)
- 11:00 — Relatório de referências do grupo CoCrie no WhatsApp
- 14:00 — Análise de conteúdo diário do Instagram
- 23:00 — Triagem automática de solicitações de acesso no MentorIA
Para criar seus próprios:

```plain text
Gere um briefing matinal completo: leia os logs recentes, verifique o
calendário e me entregue um resumo do dia com tarefas pendentes,
compromissos e saúde todo dia às 08h no meu WhatsApp pessoal (51999999999).
```

---

#### Resumo visual do mês

Com Google Sheets + GPT-Image-2:

```plain text
"Puxa os dados financeiros do mês da planilha e gera um infográfico resumindo
receitas, despesas e saldo"
```

Hermes lê a planilha, processa os números e gera uma imagem com o resumo.

---

#### Checklist de boas práticas

- Skills: sempre que resolver um problema complexo (5+ calls) ou descobrir um workflow novo, peça: "salva isso como skill"
- Memória: informações estáveis sobre você (preferências, dados fixos) vão na memória. Progresso de tarefas, não.
- Snapshots: após configurar tudo, faça um snapshot no painel da Contabo — se algo quebrar, restaura em 5 minutos.
- Segurança: revise o .gitignore do ~/.hermes antes de qualquer push. Tokens vazados = acesso ao seu ecossistema.
- Modelos: dia a dia use modelos rápidos (Deepseek v4 flash). Para criação de contexto, use modelos de ponta (GPT-5.5, Claude Opus 4.7).
- Manutenção: de tempos em tempos, peça: "hermes doctor --fix" e "hermes config check" para manter tudo saudável.
---

> Próximo passo: veja a Parte 01 para entender os conceitos por trás do Hermes Agent, ou explore o Guia Multi-Agent no Slack para montar seu time de agentes.
