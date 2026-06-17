# -*- coding: utf-8 -*-
import json, datetime, re, io
NOW = datetime.datetime.now().isoformat()

def read(p):
    return io.open(p, encoding="utf-8").read()

def clean(t):
    t = t.replace("​", "").replace(" ", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    # normaliza bullets variados para "- "
    t = re.sub(r"(?m)^\s*[•●▪∙\*]\s*", "- ", t)
    lines = [ln.rstrip() for ln in t.split("\n")]
    return "\n".join(lines).strip()

def write(fname, titulo, aluno, tipo, secs, checks=None):
    d = {"capa_titulo": titulo, "capa_aluno": aluno, "capa_tipo": tipo}
    for i in range(1, 9):
        d["sec%d_texto" % i] = clean(secs.get(i, ""))
    if checks:
        d.update(checks)
    d["_savedAt"] = NOW
    io.open(fname, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2))
    print("wrote", fname)

# ============ parser ancorado no titulo da secao ============
TITLES = [
    (1, r"Problema"),
    (2, r"P[úu]blico"),
    (3, r"Solu[cç][ãa]o"),
    (4, r"Requisitos\s+Funcionais"),
    (5, r"Requisitos\s+N[ãa]o[\s-]*[Ff]uncionais"),
    (6, r"Arquitetura"),
    (7, r"Fluxo"),
    (8, r"Autoavalia"),
]

def split_titles(text):
    """Acha cada header (numero + palavra-chave do titulo) e fatia o corpo."""
    text = text.replace("​", "").replace("\xa0", " ")
    marks = []
    for n, kw in TITLES:
        rx = re.compile(r"(?im)^[#>\s]*%d\s*[.\-)]\s*%s[^\n]*\n" % (n, kw))
        m = rx.search(text)
        if m:
            marks.append((n, m.start(), m.end()))
    marks.sort(key=lambda x: x[1])
    out = {}
    for idx, (n, s, e) in enumerate(marks):
        end = marks[idx + 1][1] if idx + 1 < len(marks) else len(text)
        out[n] = text[e:end].strip()
    return out

def strip_R(body):
    m = re.search(r"(?m)^\s*R\s*[:\-]\s*", body)
    if m:
        body = body[m.end():]
    return body.strip()

def drop_prompt_lines(body):
    pats = (r"^Descreva", r"^Liste os perfis", r"^Use o formato",
            r"^Defina qualidade", r"^Para cada tecnologia", r"^Formato:",
            r"^Seja específico", r"^Não liste funcionalidades",
            r"^t[ée]cnico\]", r".*justificativa:\s*\[motivo")
    rx = re.compile("(?m)^(?:%s)[^\n]*\n?" % "|".join(pats))
    return rx.sub("", body).strip()

# ---------------- CARLOS ----------------
sec = split_titles(read("_carlos.txt"))
sec[8] = re.split(r"Blueprint de Software\s*[—\-]\s*Plataforma", sec[8])[0].strip()
write("carlos.blueprint.json",
      "Plataforma de Delivery de Comida Online", "Carlos", "Sistema web", sec)

# ---------------- MARIA ----------------
sec = split_titles(read("_maria.txt"))
sec = {k: strip_R(v) for k, v in sec.items()}
write("maria.blueprint.json",
      "ResumeTech", "Maria Luiza, Isabela e Flavia Juliane", "Plataforma web", sec)

# ---------------- NAT ----------------
sec = split_titles(read("_nat.txt"))
sec = {k: drop_prompt_lines(strip_R(v)) for k, v in sec.items()}
if 8 in sec:
    sec[8] = re.split(r"Este blueprint", sec[8])[0].strip()
write("nat.blueprint.json",
      "Leitura Asiática", "Nathalia Elisa e Gabriella Gomes",
      "Aplicativo mobile (Android) + web", sec)

# ---------------- MAIRA (markdown, 7 secoes + checklist) ----------------
t = read("_maira.txt")
sec = split_titles(t)
for k in sec:
    sec[k] = re.sub(r"(?m)^---\s*$", "", sec[k]).strip().replace("**", "")
if 7 in sec:
    sec[7] = re.split(r"##\s*Checklist", sec[7])[0].strip()
# sec8: extrai a checklist como texto de autoavaliacao
mck = re.search(r"##\s*Checklist[^\n]*\n(.*)", t, re.S)
chktxt = mck.group(1).strip() if mck else ""
chktxt = re.sub(r"(?m)^- \[x\]\s*", "- ", chktxt, flags=re.I)
sec[8] = ("Checklist de revisão da equipe (todos confirmados):\n" + chktxt +
          "\n\n[A FAZER] Escrever a autoavaliação em prosa: viabilidade no prazo, "
          "MVP x extras, riscos e mitigação.")
maira_checks = {}
for s, n in [(1, 5), (2, 3), (3, 4), (4, 4), (5, 4), (6, 5), (7, 5)]:
    for i in range(n):
        maira_checks["sec%d_chk%d" % (s, i)] = True
write("maira.blueprint.json",
      "Lumina", "Camila, Suzanna e Maira", "Aplicativo web mobile-first",
      sec, maira_checks)

# ---------------- DANIEL (estrutura diferente; fonte sem acentos) ----------------
write("daniel.blueprint.json",
      "BrVPN - Rede Privada Virtual Brasileira", "Daniel",
      "Infraestrutura de Rede / Seguranca da Informacao", {
1: u"""VPNs comerciais disponiveis no Brasil apresentam tres problemas principais:
- Alta latencia: servidores fora do Brasil aumentam o ping desnecessariamente.
- Falta de transparencia: o usuario nao sabe quais dados sao coletados ou como o trafego e tratado.
- Custo elevado: planos de R$ 30 a R$ 80/mes para funcionalidades replicaveis com hardware simples.

[MIGRADO DE ESTRUTURA DIFERENTE] Detalhar quem sofre (perfil de usuario) e um dado que dimensione o problema.""",
2: u"""[SECAO AUSENTE NO DOCUMENTO ORIGINAL - PREENCHER]
Sugestao a partir do contexto: usuarios brasileiros que querem privacidade e baixa latencia; usuarios tecnicos que querem uma VPN auditavel e open source; o proprio operador/administrador do servidor.""",
3: u"""O BrVPN e uma Rede Privada Virtual (VPN) desenvolvida do zero como projeto de TCC, com foco em baixa latencia para usuarios brasileiros e maxima seguranca. Diferente de solucoes comerciais que funcionam como caixas-pretas, e totalmente transparente, auditavel e open source. Usa o protocolo WireGuard - o mesmo adotado por NordVPN e ExpressVPN - configurado e operado de forma independente.

Objetivo geral: projetar, implementar e documentar uma VPN funcional baseada em WireGuard, demonstrando viabilidade tecnica com recursos minimos.
Objetivos especificos: configurar servidor WireGuard em Ubuntu Server; criptografia ponta a ponta com ChaCha20-Poly1305; hospedar na nuvem com IP publico fixo; criar interface web de distribuicao do cliente; documentar a arquitetura para replicacao.""",
4: u"""[MIGRADO DOS 'OBJETIVOS ESPECIFICOS' - converter para requisitos funcionais no formato 'O sistema deve...']
RF01 - O sistema deve estabelecer tunel VPN entre cliente e servidor via WireGuard.
RF02 - O sistema deve criptografar o trafego de ponta a ponta (ChaCha20-Poly1305).
RF03 - O sistema deve disponibilizar o servidor na nuvem com IP publico fixo.
RF04 - O sistema deve oferecer uma interface web para distribuicao do arquivo de cliente (.conf).
RF05 - O sistema deve renovar o handshake periodicamente (Perfect Forward Secrecy).""",
5: u"""Modelo de seguranca / atributos de qualidade:
- Zero logs: nenhum dado de navegacao e armazenado no servidor.
- Chaves geradas localmente: a chave privada nunca sai do dispositivo.
- Perfect Forward Secrecy: handshake renovado a cada 3 minutos.
- Codigo aberto: qualquer pessoa pode auditar a configuracao.
- Baixa latencia: minimizar o ping para usuarios brasileiros.

Pilha criptografica: ChaCha20-Poly1305 (dados), Curve25519 (troca de chaves ECDH), BLAKE2s (hash/autenticacao).""",
6: u"""Componentes principais:
- Servidor VPN - Ubuntu Server + WireGuard: ponto central, roteia e criptografa o trafego.
- Infraestrutura - Google Cloud (e2-micro): VM na nuvem com IP publico fixo.
- Cliente - App WireGuard (Android/iOS/Windows): dispositivo do usuario.
- Interface Web - HTML/CSS/JavaScript: pagina de distribuicao do cliente.

Infraestrutura atual: Google Cloud (e2-micro, 1 vCPU, 1GB RAM), Ubuntu Server 26.04 LTS, IP publico fixo, porta 51820/UDP, custo gratuito (Free Tier).""",
7: u"""Fluxo de conexao:
1. O dispositivo instala o arquivo .conf com as chaves criptograficas.
2. Ao ativar a VPN, o cliente realiza handshake com o servidor usando Curve25519.
3. O trafego e encapsulado em pacotes UDP na porta 51820 e criptografado com ChaCha20-Poly1305.
4. O servidor recebe, decifra e encaminha para a internet usando NAT (MASQUERADE).
5. O handshake e renovado a cada 3 minutos (Perfect Forward Secrecy).""",
8: u"""Fases de desenvolvimento (evidencia de viabilidade):
- Beta: servidor local em VM (WireGuard em rede local) - Concluido.
- Nuvem: servidor no Google Cloud (acessivel de qualquer rede) - Concluido.
- Interface: pagina web do BrVPN - Concluido.
- App: aplicativo mobile proprio - Futuro.

Trabalhos futuros: migrar servidor para datacenter no Brasil; app mobile com WireGuard embutido (React Native); multiplos nos para balanceamento; autenticacao de usuarios; benchmarks de latencia vs. VPNs comerciais.

[A FAZER] Escrever a autoavaliacao em prosa: por que cabe no prazo, MVP x extras, riscos."""
})

# ---------------- NICOLAS (stub) ----------------
stub = (u"[O documento original (.docx) tinha o conteudo em imagens, sem texto "
        u"extraivel. Refazer esta secao a partir do material do aluno.]")
write("nicolas.blueprint.json",
      "(preencher - Nicolas)", "Nicolas Filardo Maia", "(preencher)",
      {i: stub for i in range(1, 9)})

print("DONE")
