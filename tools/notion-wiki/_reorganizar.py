"""Reorganiza elite-wiki em taxonomia tematica (decidido pela auditoria multi-agente)."""
import shutil
from pathlib import Path

BASE = Path(r"C:\PROJETOS\PROF-TONI\lake\inteligencia-artificial\elite-wiki")

# basename -> pasta-alvo (subpastas com '/')
MAP = {
    # fundamentos/ (conceito didatico curto)
    "como-escrever-prompts-mandatorios-usando-tags-xml.md": "fundamentos",
    "fundamentos-praticos-de-prompt-engineering-para-programadores.md": "fundamentos",
    "mcp-plugin-e-skill-o-que-muda-na-pratica.md": "fundamentos",
    "guia-inicial-usando-ia-como-desenvolvedor.md": "fundamentos",
    "imersao-ia-para-devs-aula-01.md": "fundamentos",
    # prompts/ (bibliotecas e exemplares)
    "prompts-scsi.md": "prompts",
    "imersao-ia-para-devs-prompts.md": "prompts",
    "prompts-curados-pycodebr.md": "prompts",
    "system-prompt-anti-ia.md": "prompts",
    "como-extrair-design-system-de-uma-pagina-de-referencia.md": "prompts",
    "como-criar-landing-pages-estaticas-com-ia.md": "prompts",
    "como-conversar-com-a-ia-para-resolver-problemas-tecnicos.md": "prompts",
    # agentes/
    "guia-completo-time-multi-agent-no-slack-com-hermes.md": "agentes",
    "segundo-cerebro-com-obsidian-claude-code-kratos.md": "agentes",
    "encontro-elite-01-agentes-pessoais-com-hermes-agent-parte-01.md": "agentes/encontros-elite",
    "encontro-elite-02-agentes-pessoais-com-hermes-agent-parte-02.md": "agentes/encontros-elite",
    "encontro-elite-03-deploy-monitoria-e-observabilidade-de-sistemas-com-ia-parte-1.md": "agentes/encontros-elite",
    # arquitetura/
    "blueprint-arquitetural-sistemas-escalaveis-com-django-ia-assistida.md": "arquitetura",
    "mentoria-pyia-pycodeia.md": "arquitetura",
    "blueprint-sistema-rag-para-suporte-a-alunos.md": "arquitetura",
    "blueprint-chatbot-whatsapp-com-python-e-ia.md": "arquitetura",
    "arquitetura-base-para-projetos-python-e-ia.md": "arquitetura",
    # skills-ferramentas/
    "skills-da-imersao-ia-para-devs-guia-de-instalacao-e-uso.md": "skills-ferramentas/imersao-skills",
    "imersao-prd-creator-conteudo-completo.md": "skills-ferramentas/imersao-skills",
    "imersao-prompt-refiner-conteudo-completo.md": "skills-ferramentas/imersao-skills",
    "imersao-feature-planner-conteudo-completo.md": "skills-ferramentas/imersao-skills",
    "imersao-bootstrap-conteudo-completo.md": "skills-ferramentas/imersao-skills",
    "imersao-sprint-executor-conteudo-completo.md": "skills-ferramentas/imersao-skills",
    "setups-de-ia-pycodebr.md": "skills-ferramentas",
    "setup-recomendado-de-ia-para-desenvolvimento.md": "skills-ferramentas",
    "plugins-recomendados.md": "skills-ferramentas",
    "recursos-uteis-ferramentas-marketplaces-e-modelos.md": "skills-ferramentas",
    # workflows/
    "spec-driven-development-com-ia-o-workflow-completo.md": "workflows",
    "imersao-ia-para-devs-aula-02.md": "workflows",
    "workflow-para-refatoracao-e-revisao-de-codigo-com-ia.md": "workflows",
    "checklist-projeto-ia-pronto-para-producao.md": "workflows",
    "como-validar-respostas-da-ia-antes-de-aplicar.md": "workflows",
    # _indice/ (mapas de navegacao Notion)
    "elite-wiki.md": "_indice",
    "ia-wiki.md": "_indice",
    # _descartar/ (lixo)
    "sem-titulo.md": "_descartar",
}

# coleta arquivos atuais por basename
atuais = {p.name: p for p in BASE.rglob("*.md")}
faltando = set(MAP) - set(atuais)
extra = set(atuais) - set(MAP)
if faltando:
    print("[aviso] no MAP mas nao no disco:", faltando)
if extra:
    print("[aviso] no disco mas nao no MAP:", extra)

movidos = 0
for nome, dest in MAP.items():
    src = atuais.get(nome)
    if not src:
        continue
    dst_dir = BASE / dest
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / nome
    if src.resolve() != dst.resolve():
        shutil.move(str(src), str(dst))
        movidos += 1

# remove diretorios antigos vazios (a arvore de scrape)
for d in sorted([p for p in BASE.rglob("*") if p.is_dir()], key=lambda x: -len(x.parts)):
    try:
        if not any(d.iterdir()):
            d.rmdir()
    except OSError:
        pass

print(f"[ok] {movidos} arquivos movidos")
print("[arvore]")
for d in sorted(p for p in BASE.iterdir() if p.is_dir()):
    n = len(list(d.rglob("*.md")))
    print(f"  {d.name}/  ({n} arquivos)")
