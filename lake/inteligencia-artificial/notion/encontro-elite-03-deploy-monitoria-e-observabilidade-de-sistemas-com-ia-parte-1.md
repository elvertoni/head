---
titulo: Encontro Elite #03 | Deploy, monitoria e observabilidade de sistemas com IA (parte 1)
disciplina: inteligencia-artificial
fonte: notion
origem: https://pickle-reading-bd9.notion.site/Encontro-Elite-03-Deploy-monitoria-e-observabilidade-de-sistemas-com-IA-parte-1-37a9956f3dc980ad9489f2aa743120b3
data: 2026-06-30
page_id: 37a9956f-3dc9-80ad-9489-f2aa743120b3
status: bruto
---

# Encontro Elite #03 | Deploy, monitoria e observabilidade de sistemas com IA (parte 1)


Desenhos: ‣


### Arquitetura de deploy do nosso projeto

Repositório do projeto: ‣

![imagem](attachment:11cd8af8-5cf9-463f-a641-294cc640ba84:arq_scsi.png)




### Workflow de IA Assistida + Deploy

Montar a arquitetura do deploy já começa no planejamento inicial do sistema, e no caso do nosso workflow de IA Assistida, já começa no nosso prompt bruto que irá gerar nosso PRD.md.

Prompts usados no SCSI: ‣ 

Nesse caso, deixei explícito o uso de Docker Compose para rodar o sistema localmente em desenvolvimento, e Docker Swarm para rodar o sistema em produção. Além de Celery para computação distribuída, e RabbitMQ como sistema de mensageria do Celery.

Detalhei ainda que os serviços da stack devem ser: o app Django, PostgreSQL do app, Celery Worker, Celery Beat, RabbitMQ para o Celery, Traefik como Web Server/Load Balancer.

Também adicionei uma demanda para ao final do projeto, na última sprint, criar um script Django Command para fazer uma carga inicial de dados (seed data) de dados demo para o sistema.

Esse mesmo prompt, template e stack pode ser reutilizado e replicado para qualquer outro projeto!

Com o PRD.md pronto, utilizamos o Workflow de IA Assistida que aprendemos no módulo IA para Devs do IA Master e/ou na Imersão IA para Devs e/ou na aula grátis do YouTube Workflow com IA Assistida (‣) para executar as sprints e construir o sistema e ter ele pronto e disponível no GitHub para começarmos nosso processo de deploy.




### Escolher e assinar uma VPS

Escolhi a KVM 4 da Hostinger, porém é possível começar com uma KVM 2 para a stack do nosso projeto, e escalar futuramente conforme necessidade. Não recomendo máquinas menores do que a KVM 2 (2 cpu e 8gb de ram).

‣


Podemos utilizar qualquer provedor da sua preferência, dentre eles algumas opções mais em conta, como:

‣

‣


Ou então provedores mais conhecidos, como:

‣

‣

‣


O importante para conseguir seguir o nosso modelo de deploy, é escolher como sistema operacional do seu servidor, o Linux Ubuntu na versão LTS (utilizarei a 24.04).




### Registro e configuração de domínio

Domínio comprado na Hostinger e gerenciado na Cloudflare.

- Passo a passo em imagens



### Configurações iniciais da VPS

Inicialmente, vamos gerar uma chave SSH no nosso computador, e então através do painel da Hostinger configurá-la no nosso servidor para conseguir acessá-lo de forma segura.

‣

‣

No seu computador, abra o terminal e execute:

```bash
# Gerar chave no seu computador
ssh-keygen -t ed25519 -C "seu_email@example.com"

# Ver conteúdo da chave gerada para copiar
cat ~/.ssh/id_ed25519.pub
```

Em seguida copie o conteúdo da chave gerada no seu terminal, cole e salve no painel da hostinger na sua VPS em:

VPS → Gerenciar → Chave SSH → + Chave SSH → Salvar


Agora podemos acessar nosso servidor por SSH com o comando:

```bash
ssh root@IP_DO_SERVIDOR
```


E então, vamos criar um usuário específico para deploy do sistema, pois não é recomendado utilizar o usuário root diretamente:

```bash
# Criar usuario
adduser deploy
# Preencha a senha quando solicitado

# Dar permissoes sudo
usermod -aG sudo deploy

# Copiar chaves SSH do root para o novo usuario
mkdir -p /home/deploy/.ssh
cp /root/.ssh/authorized_keys /home/deploy/.ssh/
chown -R deploy:deploy /home/deploy/.ssh
chmod 700 /home/deploy/.ssh
chmod 600 /home/deploy/.ssh/authorized_keys
```


Agora em um novo terminal, vamos acessar nosso servidor com o usuário criado “deploy”:

```bash
ssh deploy@IP_DO_SERVIDOR
```


Primeiro vamos atualizar nosso servidor, e instalar algumas ferramentas utilitárias nele:

```bash
# Atualizar servidor
sudo apt update && sudo apt upgrade

# Instalar utilitários
sudo apt install -y curl git htop iotop net-tools unzip

# Configurar timezone
sudo timedatectl set-timezone America/Sao_Paulo
timedatectl
```


Agora vamos instalar no nosso servidor a ferramenta Fail2ban, para monitorar e proteger contra ataques de força bruta:

```bash
sudo apt install -y fail2ban

sudo tee /etc/fail2ban/jail.local <<'EOF'
[ssh]
enabled = true
port = 22
filter = ssh
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600
findtime = 600
EOF

sudo systemctl enable fail2ban
sudo systemctl restart fail2ban
```


Endurecer regras de acesso SSH (Opcional)

```bash
# Editar config de SSH
sudo nano /etc/ssh/ssh_config

# Colar configs abaixo no arquivo e salvar
Port 22
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
MaxAuthTries 3
ClientAliveInterval 300
ClientAliveCountMax 2
```


Configurar swap de memória:

```bash
# Criar swap de 4 GB
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Persistir no boot
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# Verificar
free -h
# Deve mostrar 4 GB de swap
```


Configurar portas / firewall:

```bash
# Portas publicas
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp comment 'SSH'
sudo ufw allow 80/tcp comment 'HTTP'
sudo ufw allow 443/tcp comment 'HTTPS'

# Habilitar (confirme com 'y')
sudo ufw enable

# Verificar
sudo ufw status verbose
```


Otimizações extras / tuning para produção:

```bash
sudo tee -a /etc/sysctl.conf <<'EOF'

# === Production Tuning ===
# Network performance
net.core.somaxconn = 65535
net.ipv4.tcp_max_syn_backlog = 65535
net.ipv4.ip_local_port_range = 1024 65535
net.ipv4.tcp_tw_reuse = 1

# File descriptors
fs.file-max = 2097152
fs.inotify.max_user_watches = 524288

# Virtual memory
vm.swappiness = 10
vm.overcommit_memory = 1
EOF

sudo sysctl -p
```


Instalar Docker Engine:

```bash
# Remover versoes antigas
sudo apt remove -y docker docker-engine docker.io containerd runc 2>/dev/null

# Instalar via script oficial
curl -fsSL https://get.docker.com | sudo sh

# Adicionar usuario deploy ao grupo docker
sudo usermod -aG docker deploy

# Aplicar grupo sem re-login
newgrp docker

# Habilitar no boot
sudo systemctl enable docker
sudo systemctl start docker

# Verificar
docker --version
docker run hello-world
```


Configurar Docker para produção:

```bash
sudo tee /etc/docker/daemon.json <<'EOF'
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "20m",
    "max-file": "5"
  },
  "storage-driver": "overlay2",
  "default-ulimits": {
    "nofile": {
      "Name": "nofile",
      "Hard": 65536,
      "Soft": 65536
    }
  },
  "metrics-addr": "127.0.0.1:9323",
  "ipv6": false
}
EOF

sudo systemctl restart docker
```


Inicializar Docker Swarm:

```bash
# Usar o IP publico da VPS
docker swarm init --advertise-addr SEU_IP_VPS

# Verificar
docker node ls

```


Adicionar labels nos nodes (nesse caso, node único):

```bash
# Descobrir o hostname do node
HOSTNAME=$(docker node ls --format '{{.Hostname}}')

# Adicionar labels (infra = DB/Redis, app = Django)
docker node update --label-add infra=true $HOSTNAME
docker node update --label-add app=true $HOSTNAME

# Verificar
docker node inspect --pretty $HOSTNAME | grep -A5 Labels
```

Autenticar GitHub no servidor

```bash
# Gerar chave SSH no servidor
ssh-keygen -t ed25519 -C "vps-scsi" -f ~/.ssh/id_ed25519_github

# Copiar chave gerada
cat ~/.ssh/id_ed25519_github.pub
```

Adicione a chave gerada em github.com → Settings → SSH and GPG keys → New SSH key

Depois, se a VPS já tem um ~/.ssh/config, adicione; senão crie:

```bash
sudo nano .ssh/config
```

```bash
Host github.com
  IdentityFile ~/.ssh/id_ed25519_github
  IdentitiesOnly yes
```


Clonar o projeto no servidor

```bash
git clone https://github.com/pycodebr/scsi_v1.git
```


Configurar Registry (GHCR)

Usamos o GitHub Container Registry (gratuito para repositorios públicos, 500 MB free para privados).

```markdown
1. Acesse **github.com > Settings > Developer settings > Personal access tokens > Tokens (classic)**
2. **Generate new token (classic)**
3. Nome: `scsi-deploy`
4. Scopes: `read:packages`, `write:packages`, `delete:packages`
5. Copie o token gerado
```

Na VPS:

```bash
echo "SEU_GITHUB_TOKEN" | docker login ghcr.io -u SEU_USUARIO_GITHUB --password-stdin
```


Nesse ponto, recomendo fazer um snapshot do servidor!




### Configurando e rodando a stack na VPS

Aqui é importante sempre se atentar e verificar se as nomenclaturas de variáveis, nomes de serviços e domínios estão corretos. Sempre observe logs e erros com atenção, e sempre peça ajuda e análise da IA para correções de ajustes que podem ser simples. Mesmo a estrutura sendo replicável para outros projetos, cada projeto irá exigir algum ajuste pontual específico, e portanto a atenção devida deve ser dada e a IA nesses momentos economiza muito tempo.


Criar o .env:

```bash
cd scsi_v1
sudo nano .env

# colar o conteúdo do .env e salvar o arquivo
```

Criar a rede traefik_public primeiro (usada por todos os serviços públicos) (nome da rede deve bater com nome informado no docker-stack.yml)

```bash
docker network create --driver overlay --attachable traefik_public
```

Build e Push das Imagens

```bash
# Variaveis
export REGISTRY="ghcr.io/SEU_USUARIO_GITHUB"
export VERSION=$(git rev-parse --short HEAD)

# Build app
docker build -t $REGISTRY/scsi_v1:$VERSION -t $REGISTRY/scsi_v1:latest .

# Push
docker push $REGISTRY/scsi_v1:$VERSION
docker push $REGISTRY/scsi_v1:latest

# Testar o Pull
docker pull ghcr.io/SEU_USUARIO_GITHUB/scsi_v1:latest
```

Criar redes Overlay (nome da rede deve bater com nome informado no docker-stack.yml)

```bash
# Rede interna (app <-> db, redis — ISOLADA da internet)
docker network create --driver overlay --attachable --internal scsi_v1_internal

# Rede interna para egress (acesso liberado a internet mas sem acesso externo)
docker network create --driver overlay --attachable scsi_v1_egress

# Verificar
docker network ls --filter driver=overlay
```

Gere um basic Oauth para o dashboard do traefik

```bash
sudo apt install apache2-utils

# Gerar Hash
htpasswd -nbB admin 'SUA SENHA'
```

Depois adicione o hash da senha gerado no docker-stack.yml

```yaml
labels:
    # Dashboard
    - "traefik.enable=true"
    - "traefik.http.routers.traefik-dashboard.rule=Host(`traefik.scsi.digital`)"
    - "traefik.http.routers.traefik-dashboard.entrypoints=websecure"
    - "traefik.http.routers.traefik-dashboard.tls.certresolver=letsencrypt"
    - "traefik.http.routers.traefik-dashboard.service=api@internal"
    # Basic Auth (hash bcrypt de htpasswd -nbB admin; '$' duplicados p/ o Swarm)
    # Usuario: admin | Senha: sCs!@Tr@$fiK110726
    - "traefik.http.routers.traefik-dashboard.middlewares=traefik-auth"
    - "traefik.http.middlewares.traefik-auth.basicauth.users={HASH DA SENHA}"
    - "traefik.http.services.traefik-dashboard.loadbalancer.server.port=8080"
```


Criar um token de API na Cloudflare

O Traefik precisa de acesso a API do Cloudflare para criar registros TXT durante o challenge DNS-01 do Let's Encrypt. 

1. Acesse https://dash.cloudflare.com/profile/api-tokens 

2. Clique "Create Token" 

3. Use o template "Edit zone DNS" ou crie customizado com: 

- Permissions: 

- Zone Resources: 

4. Clique "Continue to summary" > "Create Token" 5. Copie e guarde o token — você não verá novamente

Colocar o Token gerado no serviço do Traefik no docker-stack.yml

```yaml
environment:
  # Token lido do secret via convenção _FILE (lego/Traefik leem o arquivo).
  CF_DNS_API_TOKEN_FILE: /run/secrets/CLOUDFLARE_DNS_API_TOKEN
secrets:
  - CLOUDFLARE_DNS_API_TOKEN
```

No servidor, coloque a API Token da Cloudflare no Docker Secret com:

```bash
printf 'SEU TOKEN DE API' | docker secret create CLOUDFLARE_DNS_API_TOKEN -
```


Deploy da stack

```bash
docker stack deploy -c docker-stack.yml scsi_v1

# Verificar
docker stack services scsi_v1
docker service ls
```


Verificação

```bash
# Logs do Traefik (emissão de certificado SSL)
docker service logs -f scsi_v1_traefik

# Acessar https://scsi.digital e validar cadeado (Let's Encrypt)

# Conferir volumes persistentes
docker volume ls | grep scsi_v1
```


Para fazer deploy após uma alteração

```bash
cd scsi_v1

./scripts/deploy.sh
```


Para rodar o seed data demo (carga inicial de dados):

```bash
APP=$(docker ps --filter name=scsi_v1_app -q | head -1)
docker exec -it "$APP" python manage.py seed_demo --force
```




## Extra

Prompt para implementar estrutura de deploy em projetos já existentes

```plain text
# CONTEXTO E PAPEL
Você é um engenheiro de plataforma especialista em Django + Docker Swarm. Eu
tenho um projeto Django **já existente** (o código está neste repositório) e
quero implementar nele uma arquitetura de deploy de produção em VPS, padronizada
e replicável — pense nela como um "template de deploy" que pode ser aplicado a
qualquer projeto Django. NÃO assuma nada sobre o projeto sem antes inspecionar o
código.

Parâmetros do meu deploy (use estes valores; se algum estiver vazio, pergunte ou
detecte a partir do projeto):
- Domínio: {{DOMINIO ex: meuapp.com}}
- Registry de imagens: {{REGISTRY ex: ghcr.io/usuario/projeto}}
- Nome do stack no Swarm: {{STACK_NAME ex: meuapp}}
- Provedor de DNS para TLS: Cloudflare (token de API com escopo DNS)
- Servidor: VPS Ubuntu, Docker Swarm single-node (deve poder escalar).



# ETAPA 1 — ANÁLISE DO PROJETO (faça antes de escrever qualquer coisa)
Inspecione o repositório e me devolva um diagnóstico curto cobrindo:
- Versões: Python, Django e libs relevantes (ler requirements/pyproject).
- Como o settings.py lê configuração (django-environ? os.environ? múltiplos
settings?) e onde estão ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS, DATABASE, segurança.
- Banco de dados usado e como a URL/credenciais são montadas.
- Se há Celery/RabbitMQ/Redis, cache, e-mail, armazenamento de media/estáticos.
- O que já existe de deploy: Dockerfile, docker-compose, entrypoint, scripts,
CI/CD, healthcheck, settings de produção.
- Servidor WSGI/ASGI usado (gunicorn/uvicorn) e como o app é servido.
- Quaisquer particularidades (multi-tenant, middlewares, websockets, etc.).
Liste explicitamente o que **falta** para a arquitetura-alvo abaixo.



# ETAPA 2 — ARQUITETURA DE DEPLOY ALVO (TEMPLATE A SER IMPLEMENTADO)
Implemente (no PRD) a seguinte arquitetura, **adaptando** ao que o projeto
realmente usa. Componentes condicionais (Celery/RabbitMQ/Redis) só entram se o
projeto os utilizar; caso contrário, simplifique e justifique.

## Orquestração e serviços
- Docker + Docker Compose para rodar localmente; Docker Swarm para produção na
VPS, via `docker stack deploy`.
- Serviços típicos do stack: app web (Django), banco (PostgreSQL), Traefik como
reverse proxy/load balancer e, **se aplicável**: celery worker, celery beat,
rabbitmq (broker) e redis (result backend/cache).
- A imagem da aplicação publicada em um registry ({{REGISTRY}}); o deploy usa
`docker stack deploy --with-registry-auth`.
- Volumes nomeados para persistência (banco, redis, rabbitmq, media,
staticfiles e certificados do Let's Encrypt).
- Redes overlay: uma pública (`traefik_public`, external, compartilhada com o
Traefik) e uma interna isolada (`internal: true`) para os serviços de backend.

## TLS / Traefik / Cloudflare
- Traefik emitindo certificado TLS **wildcard** ({{DOMINIO}} e *.{{DOMINIO}})
via Let's Encrypt usando o desafio **DNS-01** com o provider Cloudflare
(obrigatório para wildcard; não combinar tlschallenge e dnschallenge no mesmo
resolver).
- É preciso um **token de API do Cloudflare** com escopo DNS (Zone > DNS > Edit)
na zona do domínio. O token nunca em texto puro: deve virar um **Docker Secret**
(`CLOUDFLARE_DNS_API_TOKEN`) e ser lido pelo Traefik via convenção de arquivo
`CF_DNS_API_TOKEN_FILE=/run/secrets/CLOUDFLARE_DNS_API_TOKEN`.
- Traefik deve redirecionar http→https e confiar nas faixas de IP do Cloudflare
(`forwardedHeaders.trustedIPs`). Dashboard protegido por Basic Auth (hash gerado
com `htpasswd -nbB`, com os `$` duplicados para `$$` no stack file).
- Se usar o healthcheck do load balancer do Traefik (`loadbalancer.healthcheck`)
com `ALLOWED_HOSTS` restrito, defina também
`loadbalancer.healthcheck.hostname={{DOMINIO}}`. Sem isso, o Traefik envia o IP
interno da task (ex.: 10.0.x.x) no header Host e o Django responde
400 DisallowedHost, marcando o backend como unhealthy. (O healthcheck do próprio
container, que bate em 127.0.0.1, não tem esse problema porque localhost está em
ALLOWED_HOSTS.)

## Configuração (.env e settings)
- Configuração via `.env` na raiz (gitignored). O `.env` de produção da VPS é
separado do de desenvolvimento. Os serviços recebem variáveis via `env_file`
(lido direto pelo Docker, sem shell). Scripts que leem o `.env` devem usar um
**parser seguro** de KEY=VALUE (nunca `source`/`.`), pois valores com `& $ * @`
quebram o shell.
- `ALLOWED_HOSTS` e `CSRF_TRUSTED_ORIGINS` lidos como **lista separada por
vírgula**. Padrão:
`ALLOWED_HOSTS={{DOMINIO}},.{{DOMINIO}},localhost,127.0.0.1` (o ponto inicial
cobre subdomínios; localhost/127.0.0.1 são **obrigatórios** para o healthcheck
interno passar). `CSRF_TRUSTED_ORIGINS=https://{{DOMINIO}},https://*.{{DOMINIO}}`
(sempre com esquema; suporte a wildcard). Em ALLOWED_HOSTS vai só o hostname.
- Em produção (DEBUG=False), como o TLS termina no Traefik e o app recebe HTTP
interno, configurar `SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDED_PROTO','https')`
(evita loop de redirect) e isentar a rota de healthcheck do redirect HTTPS com
`SECURE_REDIRECT_EXEMPT`. Habilitar HSTS, cookies seguros, nosniff, etc.
- Segredos sensíveis (senha de banco/broker, token Cloudflare) preferir Docker
Secrets e/ou o `.env` gitignored da VPS — nunca versionados.

## Saúde, ordem de subida e migrations
- Endpoint leve `/health/` no Django retornando 200, **sem** acessar banco e
**sem** exigir autenticação. Usado pelo HEALTHCHECK do container e pelo
healthcheck do load balancer do Traefik.
- Healthcheck em todos os serviços: app (HTTP em /health/), postgres
(`pg_isready`), redis (`redis-cli ping`), rabbitmq
(`rabbitmq-diagnostics check_port_connectivity`), com `start_period` adequado.
- O Swarm ignora `depends_on` em runtime: a ordem é garantida por healthchecks +
um django command `wait_for_db` usado nos entrypoints.
- Migrations seguras com múltiplas réplicas: o entrypoint do **app** aguarda o
banco, aplica migrations com **advisory lock** do PostgreSQL (só uma réplica
migra por vez) e roda collectstatic. Celery (worker/beat) usa um **entrypoint
separado** que só aguarda o banco e NÃO migra nem coleta estáticos.

## Resiliência e zero-downtime
- `restart_policy` em todos os serviços (condition on-failure, delay,
max_attempts, window) e `resource limits` (limits/reservations de CPU e memória)
para evitar starvation na VPS.
- `update_config` do app com `order: start-first` e `failure_action: rollback`
(sobe réplica nova saudável antes de derrubar a antiga; rollback automático se o
healthcheck falhar) + `rollback_config`.
- Servidor de aplicação com configuração de produção (ex.: gunicorn com
worker-class apropriada, `--max-requests` para reciclar workers, timeouts).

## Scripts
- `scripts/deploy.sh` (executado na própria VPS) que faz o ciclo completo:
carrega `.env` com parser seguro, valida pré-condições (Swarm ativo, secret do
Cloudflare, rede `traefik_public`, DEBUG=False e localhost em ALLOWED_HOSTS),
git pull, build e push da imagem para o registry, `docker stack deploy
--with-registry-auth` e rollout forçado dos serviços da aplicação; com modo
`--skip-build` para redeploy sem rebuild.
- `scripts/backup.sh` para backup do banco e da media, com rotação.



# ETAPA 3 — ENTREGÁVEL 1: PRD.md
Gere um arquivo **PRD.md** (Product Requirement Document) na raiz, em markdown,
contendo:
1. Visão geral e objetivo do trabalho de deploy.
2. Diagnóstico do estado atual do projeto (da Etapa 1) e gap analysis.
3. Decisões de arquitetura e quais componentes condicionais se aplicam a ESTE
projeto (com justificativa).
4. Especificação técnica detalhada de cada item da arquitetura-alvo, já
adaptada ao projeto (nomes de serviços, variáveis, arquivos a criar/alterar).
5. **Sprints de implementação** em ordem lógica, com tarefas pequenas e bem
detalhadas, cada uma como checklist `[ ]` para marcar `[x]` quando concluída.
Cada tarefa deve dizer o arquivo afetado e o critério de pronto. Sugestão de
ordenação: (S0) preparação e análise; (S1) Dockerfile + entrypoints +
wait_for_db; (S2) settings/.env (ALLOWED_HOSTS, CSRF, proxy SSL, health);
(S3) endpoint /health/; (S4) docker-compose local; (S5) docker-stack.yml com
healthchecks/restart/limits/secrets/redes/volumes; (S6) Traefik + Cloudflare
DNS-01 wildcard; (S7) scripts deploy.sh/backup.sh; (S8) validação e hardening.
6. Riscos e pontos de atenção (ex.: arquitetura de build amd64 vs ARM, perda de
dados em volumes, rotação de segredos).

Regras: não quebre funcionalidades existentes; mudanças idempotentes; mantenha o
padrão de código do projeto; não exponha segredos; use placeholders onde o valor
for específico do ambiente.



# ETAPA 4 — ENTREGÁVEL 2: GUIA DE DEPLOY PASSO A PASSO
Inclua no PRD (ou em `docs/deploy.md`, se o projeto usar MkDocs) um **guia
completo de deploy do zero numa VPS Ubuntu**, com cada comando em blocos
copiáveis e explicação curta de cada passo, cobrindo no mínimo:
1. Provisionar a VPS: usuário não-root, atualização, firewall, instalação do
Docker Engine + Compose plugin.
2. `docker swarm init` e criação das redes overlay (traefik_public external +
rede interna).
3. Apontar o DNS no Cloudflare (A/AAAA + wildcard) e criar o **token de API**
com escopo DNS na zona do domínio; criar o **Docker Secret**
`CLOUDFLARE_DNS_API_TOKEN`.
4. Criar o `.env` de produção (DEBUG=False, ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS
no padrão definido, banco, e-mail, etc.) e os demais secrets necessários.
5. Login no registry e primeiro `docker stack deploy --with-registry-auth` (ou
`./scripts/deploy.sh`).
6. Verificar emissão do certificado wildcard via DNS-01 (logs do Traefik) e o
healthcheck dos serviços ficando `healthy`.
7. Operação do dia a dia: redeploy/atualização, ver logs, rollout, criar
superusuário, rodar comandos no container, e troubleshooting comum:
   - `DisallowedHost` por falta de `localhost`/`127.0.0.1` em ALLOWED_HOSTS (o
   healthcheck do container falha).
   - Backend marcado unhealthy + `400` de `Go-http-client` em `/health/` por
   falta de `loadbalancer.healthcheck.hostname` no Traefik quando ALLOWED_HOSTS
   é restrito (Traefik manda o IP da task como Host).
   - Loop de redirect HTTPS por falta de `SECURE_PROXY_SSL_HEADER` atrás do
   proxy.
   - `ACCESS_REFUSED` no broker por credencial divergente / RabbitMQ recriado.
   - Certificado não emitido por token/secret do Cloudflare errado ou por usar
   tlschallenge junto do dnschallenge.
   - `failed to resolve host 'db'` / tabela inexistente durante a subida —
   resolvido por healthchecks + wait_for_db (transitório).
8. Backup/restore e rotação de segredos.



# FORMATO DA RESPOSTA
Primeiro mostre o diagnóstico da Etapa 1. Em seguida, crie/atualize os arquivos
(PRD.md e, se aplicável, docs/deploy.md). Não comece a implementar o código do
deploy ainda — o objetivo desta tarefa é entregar o PRD com as sprints e o guia.
Ao final, liste os arquivos criados e um resumo do plano.

```
