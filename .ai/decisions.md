# Registro de Decisões

<!-- Entradas mais recentes no topo. Não apagar entradas antigas. -->
<!-- Numeração cronológica. Entradas "(inferida)" foram reconstruídas do histórico git, do antigo CLAUDE.md e das páginas do ai-memory em 2026-09-28. -->

## #040 — Portal remove aulas órfãs no import (`--prune`); números repetidos eram renumerações antigas
- **Data:** 2026-11-05
- **Status:** Aceita; pedido do Toni ("me incomoda aparecer 2 aulas com o mesmo número e fora de sequência"; "implemente e faça você mesmo a correção").
- **Contexto:** O acervo não tinha número repetido. O `import_acervo` casa por `(disciplina, trilha, ordem, slug)` e não apagava o que saía do manifesto, e o "Sincronizar aulas" da turma publicava tudo o que estava aprovado. Por isso as renumerações de #038 deixaram 31 órfãs publicadas ao lado das novas: JS 01–20 (turma 2º Ano A Manhã) e UX/AMS 01–11 (1º Ano A Manhã). Ao contrário do que #038 registrou, as 01–11 de AMS já tinham sido importadas.
- **Decisão:** No ProfessorDash (`a051cdd`), `import_acervo --prune [--dry-run]`. A publicação da órfã migra para a sucessora (mesmo slug na mesma trilha) quando a turma ainda não a tem, levando o progresso. A duplicata vazia é descartada junto com a notificação. Caso com dado de aluno é mantido e listado. Capa e figuras compartilhadas não são apagadas. O comando recusa rodar com manifesto vazio. Os botões "Importar do GitHub" e "Sincronizar aulas" rodam com o prune. A reorganização por renumeração foi descartada: o problema não era a numeração do acervo.
- **Execução:** Em produção, o dry-run listou 31 órfãs, todas sem progresso ou material e com sucessora já publicada na mesma turma. O prune removeu as 31 e descartou 31 publicações duplicadas. O portal ficou com 120 aulas (= manifesto), nenhum número repetido, 100 capas e 21 figuras íntegras e `/health/` 200.
- **Consequência:** Renumerar deixa de gerar duplicata no portal, desde que o reimport seja feito pela UI ou com `--prune`. Continua valendo evitar renumerar: publicação com progresso numa turma que já tem a sucessora fica bloqueada para decisão humana.

## #039 — Quiz do ProfessorDash mantém gabarito nativo até inicializar a interação
- **Data:** 2026-11-04
- **Status:** Aceita; retomada do A24 autorizada pelo Toni.
- **Decisão:** O HTML do parser inclui lista estática com gabarito em `<details>`; `quiz.js` oculta essa lista apenas após inicializar (`is-quiz-ready`). Não basta detectar a presença de Alpine: a falha do próprio componente também precisa preservar a leitura. Na apresentação, o controle acompanha a escala da TV e os controles inertes ficam ocultos sem JavaScript.
- **Consequências:** Implementação e validação no repo ProfessorDash, documentadas nos PRDs e no DESIGN de lá; não altera a canônica nem o manifesto. Aulas já importadas precisam de reimportação com `--force` após o deploy do parser.
- **Publicação:** Autorizada depois pelo Toni: commit `14ed2ff`, push SSH (elvertoni), deploy Easypanel concluído e 120 aulas reimportadas com `--force`; validação de catálogo/aluno/apresentação em produção passou. Os 31 registros antigos fora do manifesto foram preservados e não receberam o novo HTML.

## #038 — Aulas de JavaScript renumeradas para 19–38, depois das outras trilhas de front-end
- **Data:** 2026-11-04
- **Status:** Aceita; pedido do Toni ("a numeração não bate; organizar para ficarem no final"). Substitui a numeração própria 1–20 da #035.
- **Contexto:** Na disciplina `programacao-front-end`, as aulas 1 (HTML semântico), 2–6 (Git) e 7–18 (Landing Page) já ocupavam a sequência; a trilha JavaScript recomeçava em 1 e o catálogo mostrava números repetidos.
- **Decisão:** Pastas, `ordem` e manifesto passam a 19–38 (mesmos slugs); as 67 referências internas "aula NN" das canônicas foram deslocadas em +18; as referências ao RCO (78–97) ficaram intactas. `versao` +1 em todas.
- **Consequência (exceção consciente ao "nunca renumerar"):** as aulas 1–20 já tinham sido importadas. O import não remove órfãs e a chave inclui `ordem`, então o reimport cria as 19–38 e mantém as 1–20 antigas: o Toni precisa apagá-las no admin do portal (conferir antes se alguma foi publicada para turma). Os adaptadores locais `scratch/javascript-aula-01..20` geram as aulas 19..38.

## #038 — Trilha de Usabilidade e Design de Serviços numerada 87–97, na sequência SEED
- **Data:** 2026-11-04
- **Status:** Aceita; pedido do Toni ("observe a numeração das aulas pra não ficarem repetidas e bagunçadas"). Substitui a numeração 01–11 de #037.
- **Contexto:** Em AMS, a trilha `metodologias-ageis` usa os números da sequência SEED (33–41, 53, 54). Com 01–11, as aulas de UX (conteúdo do 3º trimestre) apareciam antes do Scrum na disciplina.
- **Decisão:** Renumerar para 87–97 (01→87 … 11→97), alinhado ao início dos decks SEED 87–95 e deixando 55–86 livres para as aulas futuras do 2º e 3º trimestre. Renumeração feita **antes do primeiro import** no portal (confirmado pelo Toni), então não gera duplicata. Pastas movidas com `git mv`; referências internas entre as aulas atualizadas; menções aos decks SEED preservadas.
- **Convenção para AMS daqui em diante:** `ordem` acompanha o número da aula SEED de origem, para a disciplina se ordenar sem colisão entre trilhas.

## #037 — Trilha "Usabilidade e Design de Serviços" redistribuindo as aulas SEED 87–95
- **Data:** 2026-11-04
- **Status:** Aceita; plano de 11 aulas aprovado pelo Toni. Canônicas produzidas em três lotes autorizados, aprovadas em 2026-11-04. **A numeração própria 01–11 foi substituída por #038 (87–97).**
- **Decisão:** Abrir `analise-e-metodos-para-sistemas/usabilidade-e-design-de-servicos`, com numeração própria (01–11), sem seguir os números RCO, porque os 9 decks foram redistribuídos em 11 aulas: as 10 heurísticas viraram 2 aulas de 5 mais um laboratório de avaliação heurística (87–88 → 01–03); 89 → 04; 90/91, que se repetiam, viraram conceito de serviço (05) e jornada/frontstage/backstage (06); 92 → 07; 93 → 08; 94/95 viraram uma aula por ferramenta (09 Lean Canvas, 10 Service Blueprint) mais o projeto integrador FilaZero (11). O rótulo foi registrado em `LABELS_TRILHA`.
- **Fontes:** os PPTX e o docx da SEED ficam em `lake/analise-e-metodos-para-sistemas/seed-87-95/` (binários gitignored, como os decks 34–55 da mesma disciplina), não em `fontes/` das aulas.
- **Correções da origem registradas nas canônicas (`revisao: true`):** comentário da Q1 do docx 87 ("heurísticas não tratam de estética"; a heurística 8 trata); "Erro 504 — operação inválida" no deck 88 (504 é Gateway Timeout); resposta "Lei de Hick" colada no desafio do deck 90; princípios do Design de Serviços atualizados da edição de 2011 (5) para a de 2018 (6).

## #036 — Imagens de aula saem finais, sem marca (prompt v8); action do Photoshop descontinuada
- **Data:** 2026-11-04
- **Status:** Aceita. O Toni informou que a action do Photoshop não existe mais e delegou a decisão ao ASTRA (Codex `gpt-6-astra`), que escolheu a opção B. Substitui a parte de branding externo de #008 e a reserva de cantos do prompt v6/v7.
- **Decisão:** `tools/imagen-generator/prompt.xml` v8, modo `arte_final_sem_branding`. O PNG auditado vai direto para `capa.png`/`img/`, sem normalização de canvas. As zonas reservadas (R1) dão lugar à margem segura de 8% e ao título usando o topo inteiro. Continua proibido o modelo desenhar logo, "TC", nome ou curso, porque o portal e a apostila exibem a marca ao redor da imagem. D7 foi aposentado (o id não é reaproveitado); D6 passa a cobrir também cantos deixados vazios.
- **Evidência:** o importador do ProfessorDash salva os bytes da capa e o card a exibe como está, sem sobrepor marca; as capas aprovadas de `landing-page-mvp` não têm logo aplicada.
- **Consequências:** `montar_prompt.py` exige v8; skills `gerar-imagem-aula`, `aula-estatica` e `prof-toni`, LEIA-ME (renomeado para v8), `schema-wiki.md` e `AGENTS.md` foram atualizados. Os `imagens.md` de aulas já aprovadas ficam como registro histórico. A rubrica ganhou dois itens: sintoma de `:::atencao` verificado e `diagrama-progressivo` onde o processo pede.

## #035 — Trilha JavaScript na prática com retomada preparatória
- **Data:** 2026-11-03
- **Status:** Aceita; sequência de 20 encontros aprovada pelo Toni. As 20 aulas foram produzidas em lotes autorizados (2026-11-03/04), passaram por rubrica independente com correções (v2 nas aulas 12, 16, 17 e 18) e foram aprovadas para publicação em 2026-11-04.
- **Decisão:** Abrir `programacao-front-end/javascript-na-pratica`, com numeração própria (1–20; **substituída por #038**: 19–38), preservando as identidades das aulas existentes; registrar o rótulo em `LABELS_TRILHA`. A chave do portal inclui a trilha (`disciplina, trilha, ordem, slug`), então as ordens 1–18 das outras trilhas de front-end não colidem.
- **Produção:** Canônica como fonte única; apostila offline derivada pela skill `aula-estatica`, em `saidas/`. Plano e sequência em `docs/plano-apostila-javascript.md`.

## #034 — Caixa de mensagens como serviço separado (laboratório para outros projetos)
- **Data:** 2026-10-27
- **Status:** Aceita; Toni pediu serviço separado no Compose para guardar mensagens/fotos de clientes e lê-las num painel.
- **Decisão:** `infra/mensagens/app.py`, Python stdlib + SQLite (sem dependências, fácil de copiar), imagem `python:3.13-alpine` por digest. Recebe cópia de tudo pelo webhook global da Evolution Go (`WEBHOOK_URL=http://mensagens:8001/webhook`, `WEBHOOK_FILES=true`), independente da ponte da bancada; confere `instanceToken` do `zap.json`. Painel em `/mensagens/` atrás do login do gateway, só `toni`.
- **Dados:** mensagens individuais recebidas/enviadas (texto, foto, vídeo, áudio, documento, figurinha, localização, contato); grupos/status/reações fora. Mídia em `mensagens/dados/midia/`; busca sem acento por todas as palavras. Retenção 180 dias com limpeza dos arquivos; sem log de acesso; sem backup automático.
- **Histórico (2026-10-28):** importa `HISTORICO_DIAS`=7 do HistorySync (só na conexão por QR) e baixa fotos/áudios/vídeos/documentos por fila própria (`downloads`) via `/message/downloadmedia`, das mais recentes às antigas; desiste após 4 falhas (mídia expirada no WhatsApp).
- **Efeitos colaterais:** instância assina `MESSAGE,SEND_MESSAGE`; painel Node-RED com `apiMaxLength: 50mb` (webhook traz base64); Evolution com 512 MB.

## #033 — Ponte WhatsApp na Evolution Go; Evolution 2.3.7 apagada
- **Data:** 2026-10-27
- **Status:** Aceita; Toni pediu trocar para `evoapicloud/evolution-go` e apagar a versão antiga sem backup. Substitui o uso da Evolution 2.3.7 de #029–#032.
- **Decisão:** Evolution Go 0.7.2 (digest fixado) + Postgres dedicado dentro do Compose `/opt/automacao-zap-esp32`. Manager/API em `https://evolution.tonicoimbra.com` pelo túnel Cloudflare do projeto, atrás do login HTTP do painel e só para `toni` (turma 403); `127.0.0.1:8090` na VPS para os scripts. Postgres em rede `internal`. O webhook vai direto para `http://painel:1880/zap/webhook` pela rede do Compose, e o gateway perdeu a rota pública sem login. A autenticação usa o `instanceToken` do corpo, porque a Go não envia cabeçalho próprio.
- **Licença:** gratuita, mas obrigatória (503 até ativar; atrelada ao e-mail do Toni; heartbeat ao servidor de licenças). Aviso de uso exigido pela licença no rodapé da caixa de mensagens (saiu do cartão do painel a pedido do Toni em 2026-10-28) e no README.
- **Armadilha:** `GET /instance/qr` inicia um cliente sem webhook; só `POST /instance/connect` grava webhook/eventos. A tela sempre chama connect antes de ler o QR. `/instance/status` real responde `{Connected, LoggedIn, Name}` (sem JID), diferente da doc; com o chip logado, `GET /instance/qr` reinicia o cliente — só pedir QR quando `LoggedIn` for falso. `rejectCall` recusa para a conta inteira: desligado, pois o chip conectado é o número pessoal do Toni.
- **Remoção:** projeto `evolution-teste` do EasyPanel (API 2.3.7, Postgres com 159.749 mensagens do …8701, Redis) destruído sem backup; volume de sessões, `/opt/evolution-manager`, backups do Manager na VPS/PC e o módulo `infra/evolution-manager/` removidos. Chip …1014 (1ª instância, device_removed) saiu da lista de autorizados; ponte usa chip novo.

## #032 — Remoção integral do MinIO e dos dados associados
- **Data:** 2026-10-23
- **Status:** Aceita; Toni autorizou remover o MinIO inteiro, inclusive registros e backups, após esclarecimento de que o armazenamento também atendia `teste_ok`.
- **Decisão:** Desabilitar S3 no ambiente persistente do EasyPanel e no serviço da Evolution, removendo suas credenciais S3; aplicar atualização stop-first. Excluir o serviço MinIO, domínios e volume, o coletor/vigia e suas unidades systemd.
- **Dados:** Removidos 1.358 registros de `Media` e 1.357 campos `message.mediaUrl` apontando ao MinIO. A transação preservou as 154.599 mensagens existentes; URLs originais do WhatsApp não foram alteradas. Backups associados de banco/sessões/mídias desta recuperação, backup preventivo do MinIO, logs do coletor e credenciais/cópias de configuração locais removidos. Configurações antigas do Manager tiveram apenas os dados S3 retirados; seus assets foram preservados.
- **Cópia externa:** A exportação anterior de fotos para o Google Drive não estava acessível pelos caminhos registrados; Toni confirmou que já a excluiu pessoalmente.
- **Validação:** Somente `teste_ok` permanece e reconectou em `open`; `S3_ENABLED=false`, serviço e volume MinIO ausentes, tabela `Media` vazia. A instância `oficina-esp32` havia sido excluída a pedido do Toni. Nenhuma mensagem enviada pelo agente.
- **Consequência:** Não há armazenamento MinIO nem backups de recuperação associados disponíveis. Não reativar o coletor, S3 ou a instância antiga sem novo pedido. Substitui #027 e #030.

## #031 — Tentativa seletiva de recuperar a sessão antiga da Evolution
- **Data:** 2026-10-23
- **Status:** Tentativa autorizada por Toni após esclarecimento sobre possíveis avisos automáticos do WhatsApp; recuperação permanente não obtida.
- **Decisão:** Preservar `teste_ok` e o roteamento do painel; recriar somente `oficina-esp32`, sem reinício global, e restaurar suas credenciais do backup pré-exclusão. Fazer backup atual do banco antes; não sobrepor histórico nem configurações da instância ativa.
- **Restrições:** Não enviar mensagens; leitura automática, presença online e respostas a chamadas desativadas. Webhook desabilitado explicitamente após verificar que a criação havia aplicado o padrão habilitado, porém com URL vazia.
- **Evidência:** Handshake isolado com protocolo atualizado foi aceito, e a restauração chegou a `open`; segundos depois o WhatsApp encerrou a sessão com `401/conflict/device_removed`. Aceitação inicial não comprova recuperação estável. As chaves complementares antigas do Redis estavam ausentes.
- **Resultado:** `oficina-esp32` permanece cadastrada e desconectada; nenhuma nova tentativa automática deve ser iniciada. `teste_ok` segue conectada. Novo pareamento requer pedido do Toni; histórico antigo continua disponível no backup privado.
- **Atualização posterior (2026-10-23):** Toni solicitou exclusão; o cadastro desconectado `oficina-esp32` foi removido e a API confirmou somente `teste_ok` conectada. Remoção do MinIO depende da definição de escopo, pois atende a instância ativa.

## #030 — Salvamento de vídeos na Evolution/MinIO
- **Data:** 2026-10-22
- **Status:** Aceita; Toni autorizou habilitar, reiniciar a Evolution e recuperar o último vídeo como teste. **Substituída por #032.**
- **Diagnóstico:** Evolution 2.3.7 exige `S3_SAVE_VIDEO=true`; variável ausente era interpretada como false, com vídeo ignorado no log.
- **Decisão:** Habilitar a variável no ambiente persistente do EasyPanel e recriar somente a Evolution em stop-first, preservando sessão, volumes e montagem do Manager. Backup privado da configuração antes da mudança.
- **Validação:** Uma réplica, variável ativa e WhatsApp `open` após reconexão automática. Último vídeo do histórico (2026-10-22 23:11:32 UTC, 20 s, 2.333.081 bytes) recuperado pela API de mídia, salvo no MinIO e vinculado à mensagem/registro de mídia. Download HTTP 200 com SHA-256 idêntico. Backup privado do registro anterior; nenhum envio de mensagem.
- **Limite:** Habilitação não recupera automaticamente vídeos anteriores; apenas o último foi recuperado nesta operação. Coletor histórico permanece exclusivo de imagens.


## #029 — Contatos LID e nomes do cadastro no Evolution Manager
- **Data:** 2026-10-22
- **Status:** Aceita; Toni autorizou aplicar a otimização de exibição.
- **Problema:** Manager embarcado na Evolution 2.3.7 filtrava contatos por `@s.whatsapp.net`, ocultando 79 das 82 conversas individuais; 52 conversas sem nome tinham nome no cadastro. Lista também ficava oculta em telas pequenas.
- **Decisão:** Reconstruir o Manager a partir do upstream `a53029ff84a1691161cf22afcc00696d14424384`, validado por SHA-256, com fontes/adaptações em `infra/evolution-manager/`. Incluir LIDs, complementar nome/foto pelo cadastro, buscar por nome/número, ordenar por mensagem recente e alternar lista/conversa no celular com menu compacto.
- **Identidade:** Agrupar visualmente somente pares LID/telefone explícitos e unívocos em `remoteJid`/`remoteJidAlt`; nunca inferir pelo nome. Cada histórico continua acessível pela sua rota/JID, sem fusão ou exclusão no banco. Nomes ausentes não são inventados; mensagens enviadas não atribuem o nome do dono ao destinatário.
- **Publicação:** Bind persistente no EasyPanel/Swarm `/opt/evolution-manager/dist` → `/evolution/manager/dist`; backups privados antes da troca. Primeira instalação em stop-first, `zeroDowntime=false` persistente para impedir duas réplicas na mesma sessão. API/imagem 2.3.7 e volume de sessões preservados; próximas publicações trocam assets/index sem reinício. Compatibilidade deve ser revista ao atualizar a API.
- **Validação:** Nove testes do modelo, checagem TypeScript, build e QA de prévia/público em 1440/1024/768/390/320 px. Resultado: 81 contatos com 82 históricos individuais, 24 grupos, um par agrupado; busca, nomes, cabeçalho, histórico com 17 mensagens e fallback do cadastro validados. Sem envio de mensagens. Após publicação: WhatsApp open, webhook autenticado ativo, S3 ativo e download de JPEG HTTP 200.

## #028 — Reconstrução da trena de altura por etapas de bancada
- **Data:** 2026-10-22
- **Status:** Reconstrução autorizada pelo Toni; modelos dos módulos ainda não confirmados.
- **Decisão:** Manter o sketch anterior intacto e preparar testes separados em `aulas/robotica/trena_digital_arduino/`: sensor com distância bruta na Serial e scanner I²C. Definir teste visual e integração após identificar sensor, controlador e resolução do OLED e validar a bancada. Não é aula canônica.
- **Consequências:** Pinagem TRIG D9/ECHO D10 serve de referência ao teste condicional para HC-SR04. O cálculo final usará distância real do sensor ao chão menos distância à cabeça; ausência de eco não poderá virar altura. Alimentação do OLED depende da identificação do módulo. Compilar não comprova funcionamento físico.
- **Continuação:** HC-SR04 respondeu na COM10; Toni aceitou o teste a aproximadamente 30 cm e pediu avançar para OLED com título `TRENA DIGITAL 1A`. Teste visual usa U8g2 2.36.19/buffer paginado, com tentativa SH1106 e alternativa SSD1306 por configuração; controlador e resolução ainda sem confirmação visual. Alimentação inicial de teste em 3,3 V, sem concluir defeito em caso de falha.

## #027 — MinIO e coletor de imagens da Evolution restaurados
- **Data:** 2026-10-22
- **Status:** Aceita; Toni pediu reativar o serviço para baixar fotos como anteriormente. **Substituída por #032.**
- **Decisão:** Recriar `evolution-teste/minio` no EasyPanel, com volume próprio e domínios anteriores de console/S3; usar `pgsty/minio` fixado no digest `sha256:b6bfe7239bfc83fb90d31612d9704d86039dd714f7904b3f1ad68f211e602372`. Restaurar S3 no ambiente persistente da Evolution, preservando credenciais e a instância conectada.
- **Coleta:** Código anterior recuperado e instalado em `/root/evolution-teste/vigia`; timer systemd a cada minuto, espera de 180 s após detectar instância conectada e coleta única de imagens dos últimos sete dias. Exclusão anterior do número pessoal mantida no arquivo privado. Novas mídias seguem pela integração S3 da Evolution.
- **Consequências:** Arquivos excluídos anteriormente não são recuperados do volume antigo; a coleta depende de histórico no banco e disponibilidade da mídia no WhatsApp. Credenciais e logs ficam fora do Git. Console e saúde S3 HTTP 200; upload/download/remoção de fixture validados.

## #026 — Relógio interpolado nos painéis do sinal escolar
- **Data:** 2026-10-21
- **Status:** Aceita; Toni solicitou avanço visual a cada segundo.
- **Decisão:** Os painéis local e remoto avançam o mostrador com tempo monotônico do navegador entre amostras da placa, mantendo a comunicação a cada 2 s. Extrapolação limitada a 2 s; RTC inválido ou desconexão não sustentam avanço. Timer Vue liberado ao desmontar.
- **Consequências:** Apenas apresentação; ajuste do RTC e execução da agenda permanecem no ESP32. Testes cobrem virada de dia e ausência de amostras.

## #025 — Programação do sinal escolar próxima à interface original
- **Data:** 2026-10-21
- **Status:** Aceita; Toni autorizou adaptar os painéis local e remoto, sem acessar a placa USB de outro projeto.
- **Decisão:** Relógio e controles no topo, agenda em tabela com as colunas do original, repetição por botão e “Salvar programação”. Identificação/remoção ficam ao final; tabela rola horizontalmente em telas pequenas.
- **Consequências:** Mantidos os temas e o protocolo de confirmação/versão; alteração nas fontes e geração dos artefatos, sem gravar firmware ou comandar dispositivos.

## #024 — Configuração Wi-Fi estável e acesso pelo IP na automação
- **Data:** 2026-10-21
- **Status:** Aceita; Toni pediu corrigir definitivamente a troca de rede e perguntou pelo acesso via IP.
- **Decisão:** Firmware `2026-10-21-wifi-2` desativa a reconexão implícita e separa tentativas de conexão (até 20 s) do portal AP. O AP automático aguarda dois minutos sem cliente antes de nova tentativa; com cliente, ou solicitado manualmente, permanece disponível. Falha na rede abre o portal também após perda de conexão em uso.
- **Acesso local:** WiFiManager serve configuração pelo IP DHCP quando conectado e por 192.168.4.1 no AP. Login `toni`, senha de configuração já existente, HTTP Digest, gravação por POST com origem local; rotas internas de apagar memória, reiniciar e atualizar firmware bloqueadas. Continua restrito à rede local, sem publicação pela VPS.
- **Consequências:** Trocar a rede não depende de apagar NVS. A configuração salva e as credenciais de MQTT continuam privadas; após salvar, a sessão MQTT é refeita. A proteção anterior, que só pausava com cliente já associado, não protegia a entrada no AP. Complementa #020.

## #023 — Projetos de robótica separados por turma, com sinal escolar autônomo
- **Data:** 2026-10-20
- **Status:** Aceita; Toni pediu implementar o sinal web e separar os painéis por turma; confirmou segundo ESP32, ainda sem USB.
- **Decisão:** Domínio `sinal.tonicoimbra.com`, Compose/rede/broker/contas/dados/túnel próprios em `/opt/sinal-escolar-esp32`; oficina mantém endereço e execução. Mesma identidade Volta Atelier claro/escuro distribuída nos dois projetos, sem links de controle cruzado. Conta da turma apenas no gateway, professor com conta administrativa privada.
- **Firmware:** Agenda e relógio DS1307 no ESP32; rede em tarefa separada com filas. Até 20 horários, versão confirmada pelo dispositivo, comandos WSS não retidos com validade de 20 s. RTC inválido bloqueia automações; página local incorporada permite editar agenda/Wi-Fi sem internet. Migração lê slots do sketch antigo sem sobrescrevê-los; configuração e minuto tocado persistem em novo namespace.
- **Consequências:** Falha de internet/VPS não suspende agenda local. Nenhum comando/gravação na placa atual. Porta e montagem do segundo ESP32 serão verificadas antes da gravação; compilação e testes lógicos não substituem ensaio de RTC/relé nessa bancada. Código original preservado; dependências/implantação em `campainha_esp32/README.md`.

## #022 — Tema claro/escuro no navegador do painel
- **Data:** 2026-10-20
- **Status:** Aceita; Toni pediu a opção claro/escuro no painel.
- **Decisão:** Botão no cabeçalho alterna tokens sem enviar ações ao servidor. Primeira visita segue `prefers-color-scheme`; escolha manual persiste em `localStorage` (`toni-oficina-tema`), com fallback para a visita se o armazenamento estiver indisponível. Marca TC e favicon acompanham o tema; variante clara adapta superfícies/textos/status sem trocar fontes ou vermelho da identidade.
- **Consequências:** Complementa #021. Preferência por navegador, independente da conta e das automações. Publicação parcial de `tela.format`, sem reinício do motor/MQTT.

## #021 — Painel da automação adota o Volta Atelier do portfólio
- **Data:** 2026-10-20
- **Status:** Aceita; Toni pediu aplicar o design system de `https://tonicoimbra.com/` ao painel existente.
- **Decisão:** Substituir a identidade própria verde/clara pelo Volta Atelier extraído do CSS público do portfólio: fundo #141414, superfícies escuras, vermelho #fb3732, títulos Archivo e texto JetBrains Mono. Reutilizar os arquivos de fonte do site e a marca TC em variante escura, com licenças OFL. Tokens em `design-system.css`, componentes em `dashboard.css`; o gerador incorpora fontes/marca ao template para evitar dependência externa no navegador.
- **Consequências:** Layout e funções do painel preservados. Atualização visual via API privada Node-RED, limitada aos campos `tela.format` e `tema.colors`, com revisão, backup privado e deploy parcial de nós; não reiniciar motor/MQTT com placa e rotinas em uso. Verificação visual/funcional sem comandos ao relé em 1440/1024/768/390/320 px. O ESP32 já aparece online e recebe comandos do usuário; ponte WhatsApp segue pendente.

## #020 — Firmware WSS com configuração Wi-Fi por portal local
- **Data:** 2026-10-20
- **Status:** Aceita para a bancada ESP32; Toni conectou a placa e escolheu rede particular de 2,4 GHz.
- **Contexto:** Painel e túnel da #019 estavam publicados; o DevKit na COM6 ainda executava apenas o teste Serial. Nome e senha da rede particular não foram fornecidos e não devem entrar no código versionado.
- **Decisão:** Firmware próprio em `aulas/robotica/automacao_zap_esp32/firmware/`, usando core ESP32 3.3.12, WiFiManager 2.0.17, WebSockets 2.7.2 e MQTTPubSubClient 0.3.2 (ArxContainer 0.7.0/ArxTypeTraits 0.3.2). Rede de configuração `Toni-ESP32-01`, protegida por senha gerada, e portal local em 192.168.4.1. Credenciais Wi-Fi ficam na configuração da placa; conta MQTT e senha do portal são acrescentadas a um sketch privado em diretório externo ao Git. TLS verifica raízes públicas e depende de NTP. FQBN com `PartitionScheme=huge_app`, sem OTA.
- **Consequências:** Firmware compilado e gravado no ESP32-D0WD-V3/COM6, com verificação de hash; rede de configuração detectada pelo Windows. Relé no GPIO 4 inicializa OFF e preserva o estado durante perda de rede. Heartbeat de estado a cada 30 s, LWT offline e comandos não retidos. Conexão real ao painel e teste remoto do relé dependem da configuração da rede particular pelo Toni; WPA2-Enterprise fica fora deste firmware.

## #019 — Painel Node-RED e MQTT/WSS por túnel Cloudflare dedicado
- **Data:** 2026-10-20
- **Status:** Aceita; Toni aprovou a proposta e o subdomínio `automacao.tonicoimbra.com`.
- **Contexto:** O broker da #018 funciona por Tailscale, mas a conexão direta do PC à porta 8883 era encerrada durante o TLS. Toni pediu subdomínio com Cloudflare Tunnel e painel com automações.
- **Decisão:** Publicar o painel Node-RED 5.0.8/FlowFuse Dashboard 1.33.0 e MQTT sobre WSS em 443 no mesmo subdomínio, caminho `/mqtt`. Túnel dedicado `automacao-zap-esp32`, gateway Nginx com login HTTP no painel/API/Socket.IO e editor acessível apenas pela VPS/SSH. Credenciais MQTT e ACLs continuam no Mosquitto; WebSocket 9001 restrito à rede do Compose. Imagens base fixadas por digest; fontes e testes em `aulas/robotica/automacao_zap_esp32/infra/painel/`.
- **Consequências:** O futuro firmware precisa suportar MQTT sobre WebSocket, validar o certificado público Cloudflare e emitir estado/presença periódicos. Painel não presume sucesso após enviar comando; programação diária e temporizador não enviam quando a placa está offline, e comandos não são retidos. Contexto/histórico persistem fora do Git; reinício cancela temporizador e volta a aguardar sinal atual. WSS, login/ACLs e interface foram testados; firmware físico e ponte WhatsApp ainda pendentes. Complementa a #018 e concretiza o acesso público por 443.

## #018 — Broker MQTT isolado para a automação ESP32/WhatsApp
- **Data:** 2026-10-20
- **Status:** Aceita; implantação autorizada pelo Toni na sessão.
- **Contexto:** O ESP32 DevKit e o relé de 3 V já foram testados pela Serial. A próxima etapa precisa de um broker para conectar a placa e uma futura ponte WhatsApp.
- **Decisão:** Mosquitto 2.1.2 em Docker Compose independente do EasyPanel, na VPS `vmi2626506`, em `/opt/automacao-zap-esp32`. Imagem fixada por digest; somente porta 8883 com TLS, CA própria para validar o IP, duas contas (`esp32_01` e `ponte_zap`) e ACLs por tópico. Código/configuração pública em `aulas/robotica/automacao_zap_esp32/infra/`; senhas e chaves privadas fora do repositório.
- **Consequências:** Clientes precisam carregar `ca.crt` e ter relógio correto. O certificado do servidor vence em 21/11/2027 e tem renovação manual documentada. Testes passaram na VPS e via Tailscale; o TLS direto do PC para o IP público foi encerrado, com causa ainda não isolada. O caminho da rede da escola para o ESP32 segue pendente; alternativa em 443 via Traefik depende de DNS e não foi implantada.

## #017 — Texto proporcional opcional e resumo por tema nas apostilas standalone
- **Data:** 2026-10-16
- **Status:** Aceita para a apostila de revisão DS, a pedido do Toni (pontos da revisão do Codex).
- **Contexto:** A apostila DS tem cerca de 43 mil palavras em mono; faltavam um roteiro de estudo, uma revisão de véspera e uma versão impressa sem respostas.
- **Decisão:** O template `aula-estatica` ganha `body[data-texto="proporcional"]` (Archivo 400 no texto corrido; código, rótulos e títulos de parte seguem em JetBrains Mono), o bloco `.resumo` (BLOCOS §19) e o botão "PDF sem respostas" (`data-print-mode="treino"`). A Archivo embutida passa a ser declarada de 400 a 900 (o arquivo já é variável).
- **Consequências:** Outras apostilas continuam em mono, a menos que ativem o atributo. A apostila DS ganhou roteiro de 18 sessões, oito resumos e o PDF completo caiu de 202 para 194 páginas (182 no PDF sem respostas).

## #016 — Leitura ampla opcional nas apostilas standalone
- **Data:** 2026-10-16
- **Status:** Aceita para a apostila de revisão DS, a pedido do Toni.
- **Contexto:** A página tinha 1120 px disponíveis no desktop, mas os parágrafos usavam apenas 682 px e os exercícios tinham outra largura.
- **Decisão:** O template `aula-estatica` oferece `body[data-layout="amplo"]`: texto e componentes alinhados na largura disponível, com limite de 1200 px, adaptação ao celular e regras de impressão A4. Aplicado à apostila DS por regeneração do CSS a partir do template, preservando conteúdo e JavaScript.
- **Consequências:** Outras apostilas só usam a largura ampla quando ativada explicitamente. Mantidas as fontes Archivo e JetBrains Mono. A revisão DS continua standalone; cópia anterior, regenerador e evidências visuais ficam em `scratch/revisao-visual/` (local-only).

## #015 — Schema da wiki sai do `AGENTS.md` para `docs/schema-wiki.md`
- **Data:** 2026-09-28
- **Status:** Aceita
- **Contexto:** O padrão de memória portável exige um `AGENTS.md` curto (~150 linhas), carregado em toda sessão por todos os harnesses. O `AGENTS.md` antigo tinha 303 linhas com o schema da wiki Karpathy, e o `CLAUDE.md` tinha mais 210 linhas de arquitetura.
- **Decisão:** O schema vai inteiro para `docs/schema-wiki.md`, com a mesma numeração de seções (§1–§7). O `AGENTS.md` novo guarda o protocolo, as invariantes, as convenções e os comandos. A arquitetura do antigo `CLAUDE.md` vai para `.ai/context.md`. As referências "`AGENTS.md` §N" no README, na skill `prof-toni`, nas skills do Hermes e no `gerar_manifesto.py` foram atualizadas.
- **Alternativas descartadas:** Manter o schema no `AGENTS.md` com o protocolo acrescentado (~350 linhas carregadas em toda sessão).
- **Consequências:** Antes de `ingest`/`query`/`lint` o agente precisa abrir `docs/schema-wiki.md` explicitamente. O Quíron só vê a mudança depois do redeploy das skills na VPS (`git pull` + `cp -r hermes/skills/prof-toni ~/.hermes/skills/`).

## #014 — Handoff local-only porque o repo é público
- **Data:** 2026-09-28
- **Status:** Aceita
- **Contexto:** `elvertoni/head` é público (confirmado com `gh repo view` em 2026-09-28). O portal lê o tarball do GitHub, então o repo precisa continuar acessível.
- **Decisão:** `.ai/handoff.md` e `.ai/sessions/` ficam no `.gitignore`. `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.ai/context.md`, `.ai/decisions.md` e `.ai/prompts/` são versionados.
- **Alternativas descartadas:** Versionar o handoff como no ESIMBA (exporia o estado de sessão publicamente).
- **Consequências:** A continuidade entre harnesses funciona na mesma máquina. Outra máquina não recebe o handoff pelo git.

## #013 — Memória portável no repositório; ai-memory passa a ser complemento
- **Data:** 2026-09-28
- **Status:** Aceita
- **Contexto:** Desde a #009 a memória durável vivia no ai-memory (MCP). O padrão de memória portável põe o contexto no repositório para qualquer harness, conta ou modelo retomar sem depender de um servidor.
- **Decisão:** `AGENTS.md` + `.ai/` são a memória primária. Decisões técnicas vão para este arquivo; arquitetura para `.ai/context.md`; estado de sessão para `.ai/handoff.md`. O ai-memory guarda só conhecimento revisado e útil entre projetos, sem duplicar handoff nem decisões.
- **Alternativas descartadas:** Manter o ai-memory como primário e usar `.ai/` só para handoff e contexto.
- **Consequências:** As ADRs e regras pinadas do ai-memory deste projeto foram trazidas para cá como entradas inferidas (#002, #005, #008, #009). Substitui a #009.

## #012 — Triagem RCO: o código decide, o Jev só ordena
- **Data:** 2026-09-22 (inferida)
- **Status:** Aceita
- **Contexto:** Chegaram 516 aulas RCO da SEED, e era preciso saber quais já têm aula aprovada equivalente (commit `bed391d`).
- **Decisão:** `extrair_rco.py` extrai de forma determinística para `lake/{disciplina}/rco/`. `triar_rco.py` casa títulos idênticos no código e pergunta o resto ao Jev (TypeSafe), com os `objetivos` de cada aula aprovada como contexto. Equivalência abaixo de 0,7 recebe ⚠. A saída (`docs/rco-triagem.md`) nunca cria, promove nem edita conceito ou aula.
- **Alternativas descartadas:** Comparar só com títulos das aulas aprovadas (o Jev dava confiança baixa até em pares corretos).
- **Consequências:** Custo de cerca de US$ 0,07 na triagem inteira. Ainda há pares errados com confiança alta (0,88–0,96), então a triagem é auxílio, nunca decisão.

## #011 — Publicação em quatro passos com reimport forçado
- **Data:** 2026-08-23 (inferida)
- **Status:** Aceita
- **Contexto:** O portal ficou 13 aulas e 14 capas defasado sem erro nenhum, porque o reimport não foi feito (commit `f910e52`).
- **Decisão:** Publicar = `gerar_manifesto.py` → push do acervo → deploy do portal → reimport com `--force`. Confirmada pelo Toni em 2026-09-28.
- **Alternativas descartadas:** — (nenhuma considerada)
- **Consequências:** O reimport é passo explícito do fluxo (invariante 6 do `AGENTS.md`).

## #010 — Geração de imagem delegada ao Codex CLI
- **Data:** 2026-08-10 (inferida)
- **Status:** Aceita
- **Contexto:** A #008 tirou a geração de dentro do agente por qualidade. A ferramenta nativa de imagem do Codex CLI passou a entregar arte no padrão (commit `2bc296e`).
- **Decisão:** O agente monta o prompt v6 resolvido, delega a geração ao Codex CLI e audita o PNG contra os 12 defeitos da regra `R3`. O Projeto do ChatGPT no navegador continua como alternativa. Entregar o XML cru ao modelo é proibido, porque gera fundo claro e cantos ocupados.
- **Alternativas descartadas:** Ferramenta de imagem interna do Claude Code (qualidade abaixo do acervo).
- **Consequências:** O loop de geração volta a ser automatizável. A logo continua fora do modelo.

## #009 — Memória do projeto no ai-memory, não nos arquivos locais
- **Data:** 2026-07-29
- **Status:** Substituída por #013
- **Contexto:** O ai-memory (MCP) e o `MEMORY.md` local do Claude Code rodavam em paralelo e desalinhados.
- **Decisão:** O ai-memory virou o sistema de memória do projeto; a pasta `~/.claude/projects/C--PROJETOS-PROF-TONI/memory/` foi congelada como histórico.
- **Alternativas descartadas:** Manter os dois sistemas.
- **Consequências:** O ai-memory passou a ter ADRs pinadas e regras deste projeto; os arquivos locais não recebem mais nada.

## #008 — Prompt de imagem v6 com dois perfis; geração fora do agente
- **Data:** 2026-07-29
- **Status:** Aceita quanto aos perfis; o local de geração foi substituído por #010; o branding externo pelo Photoshop foi substituído por #036
- **Contexto:** A auditoria das 54 imagens aprovadas mostrou que o prompt v5 estava calibrado abaixo do acervo, e a ferramenta de imagem do Claude Code saía pior que o ChatGPT (commit `c12bac6`).
- **Decisão:** `tools/imagen-generator/prompt.xml` v6 tem dois perfis — `capa` (3:2, 4–10 blocos com micro-parágrafo, subtítulo e faixa de rodapé) e `infografico` (16:9, 2–5 blocos só com rótulos). Declarar o perfil é o passo 0. Paleta com fundo navy quase preto e ciano como âncora. `imagens.md` traz um brief de `capa` e no máximo um de `infografico`, sem prompt escrito à mão. O branding é aplicado depois pelo Photoshop.
- **Alternativas descartadas:** Fundir os dois formatos num spec só; manter a geração no Claude Code; proibir render 3D (aparece em ~15 das 54 aprovadas).
- **Consequências:** Auditoria objetiva pela regra `R3` (12 defeitos reais já publicados).

## #007 — Manifesto exporta `conceitos[]` para o portal
- **Data:** 2026-07-27 (inferida)
- **Status:** Aceita
- **Contexto:** Slugs não têm acento, então o portal mostraria "aprendizado de maquina" ao derivar o nome do slug (commit `38da690`).
- **Decisão:** `manifesto.json` leva `conceitos[]` com `{slug, nome, disciplina}` de todo nó não obsoleto. Nas aulas, preferir `[[slug|rótulo]]`; o mapa é a rede de segurança.
- **Alternativas descartadas:** O portal derivar o nome do slug (sem acento; mostraria "aprendizado de maquina" ao aluno).
- **Consequências:** O contrato do portal (§5.1 do schema) inclui `conceitos[]`.

## #006 — Notion como projeção de mão única do índice de aulas
- **Data:** 2026-07-27 (inferida)
- **Status:** Aceita
- **Contexto:** O workspace "Toni's Brain" precisava listar as aulas sem virar segunda fonte de verdade (commit `97cb97e`).
- **Decisão:** `sync_notion.py` espelha só metadados + link do ProfessorDash na base `Aulas`, com chave `Caminho`. O Notion nunca é entrada. A escrita é opt-in (`--apply`).
- **Alternativas descartadas:** Notion como lugar regular de autoria de aulas. Usar o Notion para uma aula é só pontual, quando o Toni quer algo bem rápido — não é regra (confirmado pelo Toni em 2026-09-28).
- **Consequências:** Toda mudança de aula nasce no repo; o Notion é regenerável. Uma aula feita pontualmente no Notion não é fonte de verdade nem aparece no portal enquanto não virar `canonica.md`.

## #005 — Nunca rebaixar a canônica para o formato do repo legado
- **Data:** 2026-06-14 (inferida — data da memória legada `acervo-legado-regerar-do-zero.md`)
- **Status:** Aceita
- **Contexto:** O repo `elvertoni/ProfToniCoimbra` tem ~70 aulas no formato antigo do ProfessorDash, sem callouts, quiz, diagrama nem roteiro.
- **Decisão:** O repo legado é só referência histórica da grade de disciplinas. As aulas seguem a skill `prof-toni`; nunca retrofitar para o frontmatter mínimo antigo. Em conflito entre "compatível com o antigo" e "melhor para o aluno", ganha o aluno.
- **Alternativas descartadas:** Adaptar a canônica ao formato antigo para ter paridade (o Toni prefere refazer tudo do zero).
- **Consequências:** Aulas antigas são refeitas, não convertidas.

## #004 — Manifesto gerado por script, tools só com stdlib
- **Data:** 2026-06-21 (inferida)
- **Status:** Aceita
- **Contexto:** O ProfessorDash importa pelo `manifesto.json`; edição manual divergia dos arquivos (commit `a7eb0b7`).
- **Decisão:** `tools/gerar_manifesto.py` é a única fonte do manifesto, deriva a identidade do caminho e valida com `--check`. As tools usam só stdlib (parser YAML mínimo em `wiki_core.py`, sem PyYAML).
- **Alternativas descartadas:** Manifesto mantido à mão, como no commit `71f6e21` (inferida).
- **Consequências:** Contrato de import inviolável (§5.1 do schema). As tools rodam em qualquer Python sem instalar nada.

## #003 — Wiki de conceitos no modelo llm-wiki do Karpathy
- **Data:** 2026-06-15 (inferida)
- **Status:** Aceita
- **Contexto:** O conhecimento era reextraído a cada material, sem compor entre disciplinas (commit `0b7e337`).
- **Decisão:** Camada `conceitos/` com nós atômicos ligados por `[[slug]]`, `index.md` regenerável, `log.md` append-only e workflows `ingest`/`query`/`lint`; o LLM mantém e o Toni aprova fusão e obsolescência.
- **Alternativas descartadas:** Plugin *Karpathy LLM Wiki* do Obsidian como motor (fica só como navegação opcional).
- **Consequências:** Schema em `docs/schema-wiki.md`; o lint só propõe, nunca corrige conteúdo.

## #002 — `elite-wiki/` fica só local
- **Data:** 2026-06-14 (inferida)
- **Status:** Aceita
- **Contexto:** `lake/inteligencia-artificial/elite-wiki/` é material literal de curso pago de terceiro, puxado do Notion público (commit `4ef537d`).
- **Decisão:** `lake/**/elite-wiki/` é gitignored. Informa as aulas, mas a canônica reescreve com voz própria.
- **Alternativas descartadas:** —
- **Consequências:** Um clone novo não tem esses arquivos; recriar com `python tools/notion-wiki/puxar_notion.py`.

## #001 — Arquitetura lake → warehouse com a canônica como fonte única
- **Data:** 2026-06-14 (inferida)
- **Status:** Aceita
- **Contexto:** As aulas precisavam sair em vários formatos (portal, apostila HTML, PDF) sem divergir (commits `a066e59`, `71f6e21`). Também era preciso um lugar de ingestão inicial: o conhecimento de um material tem que continuar no vault mesmo que o original seja apagado depois (motivo confirmado pelo Toni em 2026-09-28).
- **Decisão:** `lake/` é o ponto de entrada e guarda o bruto imutável; o conhecimento extraído vive em `conceitos/` e `aulas/.../canonica.md`, que é a fonte única da aula; `**/saidas/` é derivado e não versionado.
- **Alternativas descartadas:** Trabalhar direto sobre os arquivos originais, sem etapa de ingestão — o conhecimento ficaria preso ao original e se perderia junto com ele.
- **Consequências:** Erro de conteúdo se corrige na canônica e a saída é regerada; nunca se edita o `.html`. Perder o bruto não apaga o conhecimento: os avisos `source-missing` do lint (fonte que não está nesta máquina) são esperados e não significam conteúdo perdido; a lacuna de proveniência só precisa ficar explícita.
