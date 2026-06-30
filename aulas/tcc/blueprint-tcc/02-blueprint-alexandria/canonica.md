---
titulo: Blueprint · BrVPN
tema: Blueprints de TCC
disciplina: tcc
serie: 3a-serie
prerequisitos: []
objetivos:
  - Compreender a arquitetura e os requisitos do projeto BrVPN
trilha: blueprint-tcc
ordem: 2
slug: blueprint-alexandria
status: aprovada
versao: 1
atualizado_em: 2026-06-30
---

# Blueprint · BrVPN

Infraestrutura de Rede / Seguranca da Informacao · Daniel Moraes do Nascimento, Estevão Barbiot Nascendino e Lucas Czarnesky dos Santos

## Objetivos

Ao final desta leitura, você será capaz de compreender a arquitetura e os requisitos do projeto BrVPN.

## Problema e Contexto

VPNs comerciais disponiveis no Brasil apresentam tres problemas principais:
- **Alta latencia**: servidores fora do Brasil aumentam o ping desnecessariamente.
- **Falta de transparencia**: o usuario nao sabe quais dados sao coletados ou como o trafego e tratado.
- **Custo elevado**: planos de R$ 30 a R$ 80/mes para funcionalidades replicaveis com hardware simples.

[MIGRADO DE ESTRUTURA DIFERENTE] Detalhar quem sofre (perfil de usuario) e um dado que dimensione o problema.

## Público-Alvo

[SECAO AUSENTE NO DOCUMENTO ORIGINAL - PREENCHER]
Sugestao a partir do contexto: usuarios brasileiros que querem privacidade e baixa latencia; usuarios tecnicos que querem uma VPN auditavel e open source; o proprio operador/administrador do servidor.

## Solução Proposta

O BrVPN e uma Rede Privada Virtual (VPN) desenvolvida do zero como projeto de TCC, com foco em baixa latencia para usuarios brasileiros e maxima seguranca. Diferente de solucoes comerciais que funcionam como caixas-pretas, e totalmente transparente, auditavel e open source. Usa o protocolo WireGuard - o mesmo adotado por NordVPN e ExpressVPN - configurado e operado de forma independente.

Objetivo geral: projetar, implementar e documentar uma VPN funcional baseada em WireGuard, demonstrando viabilidade tecnica com recursos minimos.
Objetivos especificos: configurar servidor WireGuard em Ubuntu Server; criptografia ponta a ponta com ChaCha20-Poly1305; hospedar na nuvem com IP publico fixo; criar interface web de distribuicao do cliente; documentar a arquitetura para replicacao.

## Requisitos Funcionais

[MIGRADO DOS 'OBJETIVOS ESPECIFICOS' - converter para requisitos funcionais no formato 'O sistema deve...']
- **RF01** — O sistema deve estabelecer tunel VPN entre cliente e servidor via WireGuard.
- **RF02** — O sistema deve criptografar o trafego de ponta a ponta (ChaCha20-Poly1305).
- **RF03** — O sistema deve disponibilizar o servidor na nuvem com IP publico fixo.
- **RF04** — O sistema deve oferecer uma interface web para distribuicao do arquivo de cliente (.conf).
- **RF05** — O sistema deve renovar o handshake periodicamente (Perfect Forward Secrecy).

## Requisitos Não Funcionais

Modelo de seguranca / atributos de qualidade:
- **Zero logs**: nenhum dado de navegacao e armazenado no servidor.
- **Chaves geradas localmente**: a chave privada nunca sai do dispositivo.
- **Perfect Forward Secrecy**: handshake renovado a cada 3 minutos.
- **Codigo aberto**: qualquer pessoa pode auditar a configuracao.
- **Baixa latencia**: minimizar o ping para usuarios brasileiros.

Pilha criptografica: ChaCha20-Poly1305 (dados), Curve25519 (troca de chaves ECDH), BLAKE2s (hash/autenticacao).

## Arquitetura e Tecnologias

Componentes principais:
- **Servidor VPN - Ubuntu Server + WireGuard**: ponto central, roteia e criptografa o trafego.
- **Infraestrutura - Google Cloud (e2-micro)**: VM na nuvem com IP publico fixo.
- Cliente - App WireGuard (Android/iOS/Windows): dispositivo do usuario.
- **Interface Web - HTML/CSS/JavaScript**: pagina de distribuicao do cliente.

Infraestrutura atual: Google Cloud (e2-micro, 1 vCPU, 1GB RAM), Ubuntu Server 26.04 LTS, IP publico fixo, porta 51820/UDP, custo gratuito (Free Tier).

## Fluxo Principal do Usuário

Fluxo de conexao:
1. O dispositivo instala o arquivo .conf com as chaves criptograficas.
2. Ao ativar a VPN, o cliente realiza handshake com o servidor usando Curve25519.
3. O trafego e encapsulado em pacotes UDP na porta 51820 e criptografado com ChaCha20-Poly1305.
4. O servidor recebe, decifra e encaminha para a internet usando NAT (MASQUERADE).
5. O handshake e renovado a cada 3 minutos (Perfect Forward Secrecy).

## Autoavaliação do Escopo

Fases de desenvolvimento (evidencia de viabilidade):
- **Beta**: servidor local em VM (WireGuard em rede local) - Concluido.
- **Nuvem**: servidor no Google Cloud (acessivel de qualquer rede) - Concluido.
- **Interface**: pagina web do BrVPN - Concluido.
- **App**: aplicativo mobile proprio - Futuro.

Trabalhos futuros: migrar servidor para datacenter no Brasil; app mobile com WireGuard embutido (React Native); multiplos nos para balanceamento; autenticacao de usuarios; benchmarks de latencia vs. VPNs comerciais.

[A FAZER] Escrever a autoavaliacao em prosa: por que cabe no prazo, MVP x extras, riscos.
