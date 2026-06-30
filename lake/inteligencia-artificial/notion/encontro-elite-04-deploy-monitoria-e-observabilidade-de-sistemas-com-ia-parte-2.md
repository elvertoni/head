---
titulo: Encontro Elite #04 | Deploy, monitoria e observabilidade de sistemas com IA (parte 2)
disciplina: inteligencia-artificial
fonte: notion
origem: https://pickle-reading-bd9.notion.site/Encontro-Elite-04-Deploy-monitoria-e-observabilidade-de-sistemas-com-IA-parte-2-38b9956f3dc98154a15ed4a6d8068cbe
data: 2026-06-30
page_id: 38b9956f-3dc9-8154-a15e-d4a6d8068cbe
status: bruto
---

# Encontro Elite #04 | Deploy, monitoria e observabilidade de sistemas com IA (parte 2)


Desenhos: ‣



### Dicas e recomendações

Encontro Elite #03: Deploy, monitoria e observabilidade de sistemas com IA (parte 1)

Módulo 10 do IA Master: MCP




### Arquitetura de deploy do nosso projeto

Repositório do projeto: https://github.com/pycodebr/scsi_v1

![imagem](attachment:65d53e14-be1d-47f3-9c05-067bbb5736a2:arq_scsi.png)




### O que você vai saber fazer depois desta aula

- Subir uma stack de monitoramento completa no mesmo Docker Swarm do seu projeto Django
- Implementar um servidor MCP na aplicação Django usando a lib django-mcp, para que a IA tenha acesso a tools como CRUD completo do sistema, dados, relatórios, models, funções e commands
- Conectar o Grafana como MCP server no seu agente de IA, para consultar métricas e logs em tempo real de todos os serviços, aplicações e do servidor
- Criar notificações no sistema usando MCP via IA, sem abrir o Django admin ou o Grafana



### IA integrada em dois níveis da arquitetura

A IA está integrada em dois níveis distintos e complementares:


Nível 1: MCP na aplicação Django (lib django-mcp)

A IA tem acesso a tools como CRUD completo do sistema, consultas a models, relatórios, funções de domínio e commands. Ela executa ações diretamente no banco do Django, com autenticação admin-only. Esse é o MCP que opera o sistema.


Nível 2: MCP do Grafana

A IA tem acesso a métricas e logs em tempo real de todos os serviços, aplicações e do servidor. Ela consulta Prometheus, Loki e alertas sem precisar abrir o Grafana. Esse é o MCP que observa o sistema.

O fluxo completo: a IA opera (nível 1) e observa (nível 2) o sistema sem sair do chat.




### Stack de monitoramento

Para este projeto utilizamos a seguinte stack de observabilidade:

- Prometheus: coleta e armazenamento de métricas em série temporal (scrape em pull)
- Grafana: visualização de dashboards, alertas, datasources e MCP server
- Grafana MCP: servidor MCP do Grafana que expõe 65 tools para IA consultar métricas, logs, alertas e incidentes
- Loki: agregação e armazenamento de logs centralizados (indexação por labels, não full-text)
- Promtail: agente que coleta os logs dos containers e envia para o Loki
- cAdvisor: exportador de métricas de containers Docker (CPU, memória, rede, disco por container)
- node-exporter: exportador de métricas do servidor (CPU, memória, disco, rede do host)
#### Diagrama da arquitetura de monitoramento

![imagem](attachment:f24dec1f-62ba-42d1-8841-7e4da72c03b7:d67345f8-2dc9-44dd-8d12-98541691e734.png)

cAdvisor e node-exporter são os dois exportadores que alimentam o Prometheus. O cAdvisor coleta métricas de cada container do Docker (CPU, memória, rede, disco por container). O node-exporter coleta métricas do próprio servidor (CPU global, uso de disco, carga, temperatura, memória do host). Com os dois, o Prometheus tem visão completa: do host e de cada container.

Os serviços rodam como serviços adicionais no mesmo docker-stack.yml, na mesma rede overlay do Swarm. O Grafana fica exposto em um subdomínio via Traefik (ex: grafana.scsi.digital), com TLS automático pelo mesmo certificado wildcard do Let's Encrypt já configurado no Traefik.


#### Implementação da stack via prompt de IA

Podemos implementar a stack de duas formas:

1. Durante o planejamento inicial: incluir as definições de monitoramento no prompt bruto que gera o PRD, para que as sprints de implementação já contemplem a stack desde o início.
2. Em projeto já existente: usar um prompt dedicado para adicionar a stack de monitoramento em um projeto que já está em produção.
Para projetos já em produção, usamos o prompt abaixo, que instrui a IA a implementar toda a stack do zero:

- Prompt para implementar stack de monitoria em projetos existentes
- Prompt para implementar MCP server no sistema Django
Obs: Alguns ajustes podem ser necessários. Atenção e revisão são necessários, além de referências para a IA.


#### Por que essa stack e não outra

O ecossistema Prometheus + Grafana + Loki se tornou o padrão de fato para observabilidade em ambientes containerizados por três motivos: funciona nativamente com Docker, consome menos recursos que ELK, e tem integração de primeira classe com o Grafana (mesma empresa mantém Loki e Grafana). O Prometheus coleta métricas em pull (scrape), o que significa que os serviços expõem métricas e o Prometheus vai até elas. O Loki indexa logs por labels em vez de fazer full-text indexing como Elasticsearch, o que reduz o custo de armazenamento.

O cAdvisor e o node-exporter completam a coleta: o cAdvisor dá visão por container (CPU, memória, rede de cada serviço do Docker), e o node-exporter dá visão do host (CPU global, uso de disco, carga do sistema). Sem esses dois, o Prometheus só teria métricas da aplicação (Django via django-prometheus) e ficaria cego para a infraestrutura.




### Vamos para o deploy

Para facilitar o deploy, preparei um script guia que irá subir os serviços dessa stack. Esse script serve não apenas para esse projeto, mas pode ser reutilizado em outros projetos que seguem o mesmo padrão e a mesma stack.

‣

Obs: Alguns ajustes em .env podem ser necessários.


Após o deploy, acessar o Grafana para:

- Adicionar os dashboards
- Gerar um API Token para o MCP

Acessar o container do app Django para criar um super user do Django admin e gerar um base64 encode para usar no MCP do Django.




### Nível 1: MCP na aplicação Django (lib django-mcp-server)

O Model Context Protocol (MCP) é um protocolo aberto que permite que clientes de IA (Hermes, Claude, Cursor, VS Code) se conectem a sistemas externos e consumam tools. No SCSI, implementamos um servidor MCP dentro do próprio Django usando a lib django-mcp-server para que a IA consiga consultar e operar o sistema: CRUD completo, dados, relatórios, models, funções e commands.

‣

#### O que o MCP server do Django faz

O servidor MCP do Django expõe duas categorias de tools:

1. CRUD genérico de todas as entidades: listar, descrever, criar, atualizar e excluir registros de qualquer model do sistema, com paginação, busca textual e filtros ORM.
2. Métricas e uso do sistema: contagens, somatórios, status e indicadores específicos do domínio (clientes ativos, apólices por status, valores a receber).
Todas as tools exigem autenticação admin (is_staff ou is_superuser). O acesso é por HTTP Basic Auth, o mesmo backend de autenticação do Django. Não existe token separado: o cliente MCP envia Authorization: Basic com o base64 de um admin do Django, e o DRF valida contra o banco.

#### Como funciona a autenticação

![imagem](attachment:077b3854-5983-46ed-aced-3fa933d2cf39:417206af-57b1-4e73-b78c-4add74cd023d.png)

O fluxo funciona assim: o cliente de IA envia o header Authorization: Basic com o token em toda requisição. O django-mcp-server usa o BasicAuthentication do DRF para validar as credenciais contra o banco de usuários do Django. Cada tool chama _require_admin() no início, que levanta PermissionDenied se o usuário não for admin.

#### Gerando o token Basic de um admin

Para conectar um cliente de IA ao MCP do Django, você precisa de um token Basic gerado a partir das credenciais de um admin:

```bash
# Acessar o container do app
docker ps # Pegar id do container do app Django
docker exec -it <ID DO CONTAINER> /bin/bash # Acessar container
python manage.py createsuperuser # Criar user admin


# Gere o token a partir do email e senha de um admin do Django
echo -n 'admin@scsi.digital:SUA_SENHA' | base64
# Exemplo de saída: YWRtaW5Ac2NzaS5kaWdpdGFsOlNVQV9TRU5IQQ==
```

O header enviado em toda requisição é: Authorization: Basic seguido do token. Nunca versione o token em repositórios. Use sempre HTTPS. Para revogar, troque a senha do admin ou remova is_staff/is_superuser.


#### Conectar MCP em Harness de IA

Com simples prompt já podemos fazer isso

```plain text
Adicione a conexão do MCP do SCSI (Django) seguindo as configurações abaixo e
com o nome scsi_v1_django_mcp:
{
  "mcpServers": {
    "scsi_v1_django_mcp": {
      "url": "https://scsi.digital/mcp",
      "headers": {
        "Authorization": "Basic {{ BASE64_ENCODE_DE_ADMIN:SENHA }}"
      }
    }
  }
}

Gere o token com: echo -n 'EMAIL:SENHA' | base64
Use o .env para a variável da credencial, nunca hardcoded no config.
Usuário: pycodebr@gmail.com
Senha: teste123!
```


#### Exemplo de uso: criar notificações para as corretoras via MCP

Com o MCP do Django conectado, a IA pode consultar e operar o sistema SCSI diretamente do chat. Por exemplo, para criar uma notificação para todas as corretoras ativas:

```plain text
Liste todas as corretoras ativas do sistema e crie uma notificação para
cada uma avisando sobre a atualização do sistema neste sábado.
```

A IA vai:

1. Chamar list_records(entity="brokerage", filters={"is_active": True})
2. Para cada corretora retornada, chamar create_record(entity="notification", data={...})
3. Confirmar quantas notificações foram criadas
Tudo isso sem abrir o Django admin, sem fazer SSH na VPS, sem rodar nenhum comando. A IA consulta, processa e executa via MCP.




### Nível 2: MCP do Grafana (métricas e logs em tempo real)

O Grafana tem um servidor MCP oficial que expõe 65 tools para consultar dashboards, métricas, logs, alertas, incidentes e escalas de on-call. Com o MCP do Grafana conectado no Hermes, a IA tem acesso a métricas e logs em tempo real de todos os serviços, aplicações e do servidor, sem precisar abrir o painel.

#### O que dá pra fazer com o MCP do Grafana


#### Conectar MCP em Harness de IA

Com simples prompt já podemos fazer isso

```plain text
Adicione a conexão do MCP do Grafana do SCSI seguindo as configurações abaixo:

{
  "mcpServers": {
    "grafana-scsi": {
      "url": "https://mcp.scsi.digital/mcp",
      "headers": {
        "Authorization": "Basic {{ BASE64_ENCODE_DE_ADMIN:SENHA }}"
      }
    }
  }
}

Gere o token com: echo -n 'admin:SENHA' | base64
Use o .env para a variável da credencial, nunca hardcoded no config.
```


#### Exemplo de uso: checar a saúde do sistema via chat

Com o MCP do Grafana conectado, a IA pode monitorar o sistema inteiro diretamente do chat:

```plain text
Como está a aplicação e o servidor agora?
```

A IA vai:

1. Chamar list_datasources para ver o que está configurado (Prometheus, Loki, etc)
2. Chamar check_datasources_health para verificar se todos os datasources respondem
3. Chamar list_incidents para checar se há incidentes ativos
4. Chamar list_alert_groups com filtro state="new" para ver alertas não reconhecidos
5. Chamar query_prometheus com up{job="scsi_v1_app"} para ver se o Django está respondendo
6. Consolidar tudo em um relatório legível no chat
Outros exemplos de prompts para usar no dia a dia:

```plain text
Verifica se há algum erro nos logs do Django nas últimas 2 horas
Lista todos os alertas que estão disparando agora
Cria um incidente com severity "medium" título "Latência alta no endpoint /api/policies"
Gera um deeplink para o dashboard de containers passando o período das últimas 6 horas
Qual é o maior pico de erro do Traefik no Loki nos últimos 30 minutos?
```

A diferença entre ter o Grafana e ter o Grafana via MCP é que você não precisa sair do chat para diagnosticar um problema. A IA faz a consulta, processa o resultado e te entrega a conclusão pronta.




### Skill de operação do SCSI com MCP

Depois de conectar os dois MCPs (Django + Grafana), o próximo passo é criar uma skill no Hermes Agent que encapsula o conhecimento de operação do SCSI. A skill diz para a IA: este sistema tem essas entidades, esses fluxos, esses endpoints, e como usar o Grafana para monitorar.

#### Criando a skill via prompt

```plain text
Crie uma skill chamada "scsi-manager" que permita operar, observar e monitorar
o sistema SCSI via MCP do Django e MCP do Grafana.
A skill deve conter: entidades do sistema, fluxos de operação comuns (criar corretora,
notificação, consulta), endpoints do MCP, e como usar o Grafana para monitorar.
```

A IA usa o skill_manage(action='create') para criar a skill com o esqueleto. Depois é só refinar com prompts.




### Conclusão

Com a stack de monitoramento (Prometheus + Grafana + Grafana MCP + Loki + Promtail + cAdvisor + node-exporter) rodando no Docker Swarm e a IA integrada em dois níveis (MCP do Django para operar + MCP do Grafana para observar), você tem um ciclo fechado de observabilidade e operação via IA. A IA consulta métricas e logs em tempo real, executa ações no sistema, cria incidentes e notificações, e te entrega diagnóstico e solução no chat.

Recapitulando do Encontro #03 até aqui:

- Encontro #03: deploy da stack Django + Docker Swarm + Traefik + TLS + secrets
- Encontro #04: observabilidade + MCPs + operação via IA
O próximo passo natural é automatizar alertas que chamam a IA: um alerta dispara no Grafana, envia webhook para o Hermes Agent, e a IA diagnostica e abre um incidente automático. Isso fica para um o próximo encontro.
