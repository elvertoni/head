#!/usr/bin/env python3
"""Monta o prompt de arte-base a partir do prompt.xml (v7) e de um brief em JSON.

Uso:
    python .claude/skills/gerar-imagem-aula/scripts/montar_prompt.py brief.json saida.txt

Por que existe: o prompt precisa ir ao gerador MONTADO, seção por seção, sem
nenhum [insert ...] sobrando (ver references/delegar-ao-codex.md). Montar à mão
é onde as seções somem e os perfis se misturam. Este script pega o modelo do
perfil certo direto do XML, preenche cada lacuna com o brief e recusa a montagem
se faltar campo ou sobrar lacuna.

Brief (JSON):
{
  "perfil": "infografico",                 # ou "capa"
  "aula": "título exato da aula-alvo",
  "titulo": "título curto da imagem",
  "palavra_chave": "palavra do título que fica em vermelho",
  "conceito": "o único conceito (infografico)",
  "mensagem_3s": "o que entender em 3 segundos (infografico)",
  "composicao": "side-by-side comparison | 3-5 step cycle | input-to-output flow | layered hierarchy | before/after",
  "objetivo": "o que a aula inteira ensina (capa)",
  "estrutura": "(a) | (b) | (c) | (d) descrita em inglês (capa)",
  "subtitulo": "promessa em 1-2 linhas (capa)",
  "faixa_rotulo": "EM RESUMO | IDEIA CENTRAL | ERRO COMUM | LEMBRE-SE | REGRA DE OURO (capa)",
  "faixa_frase": "frase de fechamento (capa)",
  "blocos": [
    {"rotulo": "CPU", "icone": "processor chip", "cor": "signal", "texto": "micro-parágrafo (só capa)",
     "detalhe": "opcional: relação visual em inglês"}
  ]
}
Cores aceitas: signal, esmeralda, ambar, volt, ceu, neutro, erro.
"""
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]          # .../PROF-TONI
XML = RAIZ / 'tools' / 'imagen-generator' / 'prompt.xml'

CORES = {
    'signal': 'signal red #FB3732 (main concept)',
    'esmeralda': 'emerald #10B981 (correct / input / done)',
    'ambar': 'amber #FFA31A (attention / output)',
    'volt': 'volt blue #3B49E4 (support layer / internal processing)',
    'ceu': 'sky blue #38BDF8 (definition / neutral data)',
    'neutro': 'graphite panel with bone-white label (no special meaning)',
    'erro': 'grayed panel with a red ✗ mark (error / antipattern)',
}
LIMITES = {'capa': (4, 10), 'infografico': (2, 5)}


def falhar(msg):
    sys.exit(f'✗ {msg}')


def modelo(perfil):
    raiz = ET.parse(XML).getroot()
    if raiz.get('versao') != '7.0' or raiz.get('modo') != 'arte_base_para_branding_externo':
        falhar(f'prompt.xml fora do esperado (versao={raiz.get("versao")}, modo={raiz.get("modo")}). Reporte antes de gerar.')
    for p in raiz.findall('prompt_arte_base'):
        if p.get('perfil') == perfil:
            return p.text.strip()
    falhar(f'perfil "{perfil}" não existe no XML')


def blocos_em_texto(brief):
    perfil = brief['perfil']
    blocos = brief.get('blocos') or []
    lo, hi = LIMITES[perfil]
    if not lo <= len(blocos) <= hi:
        falhar(f'perfil {perfil} pede de {lo} a {hi} blocos (o brief tem {len(blocos)})')
    linhas = []
    for i, b in enumerate(blocos, 1):
        cor = CORES.get(b.get('cor', 'neutro'))
        if not cor:
            falhar(f'bloco {i}: cor "{b.get("cor")}" inválida; use {", ".join(CORES)}')
        rotulo = b.get('rotulo', '').strip()
        if not rotulo:
            falhar(f'bloco {i} sem rótulo')
        if perfil == 'infografico' and len(rotulo.split()) > 4:
            falhar(f'bloco {i}: rótulo "{rotulo}" passa de 4 palavras (perfil infografico)')
        linha = f'{i}. Label "{rotulo}" — icon: {b.get("icone", "thin-line icon matching the label")} — color: {cor}'
        if perfil == 'capa':
            if not b.get('texto'):
                falhar(f'bloco {i}: perfil capa exige micro-parágrafo em "texto"')
            linha += f'. Micro-paragraph (Brazilian Portuguese, render exactly): "{b["texto"]}"'
        elif b.get('texto'):
            falhar(f'bloco {i}: perfil infografico não aceita micro-parágrafo')
        if b.get('detalhe'):
            linha += f'. {b["detalhe"]}'
        linhas.append(linha)
    if perfil == 'infografico':
        total = sum(1 for b in blocos) + sum(len(b.get('rotulos_extras', [])) for b in blocos)
        if total > 8:
            falhar('perfil infografico admite no máximo 8 rótulos na peça')
    return '\n'.join(linhas)


def montar(brief):
    perfil = brief.get('perfil')
    if perfil not in LIMITES:
        falhar('perfil deve ser "capa" ou "infografico"')
    texto = modelo(perfil)
    comuns = {
        'insert the exact lesson title': brief.get('aula'),
        'insert title': brief.get('titulo'),
        'insert keyword': brief.get('palavra_chave'),
    }
    if perfil == 'infografico':
        especificos = {
            'insert the single concept': brief.get('conceito'),
            'insert what the student must understand': brief.get('mensagem_3s'),
            'choose one: side-by-side': brief.get('composicao'),
            'for each block': blocos_em_texto(brief),
        }
    else:
        especificos = {
            'insert what the whole lesson teaches': brief.get('objetivo'),
            'choose one: (a)': brief.get('estrutura'),
            'for each block': blocos_em_texto(brief),
            'insert subtitle': brief.get('subtitulo'),
            'insert footer label': brief.get('faixa_rotulo'),
            'insert footer sentence': brief.get('faixa_frase'),
        }
    campos = {**comuns, **especificos}

    def troca(m):
        dentro = m.group(1)
        for chave, valor in campos.items():
            if dentro.startswith(chave):
                if not valor:
                    falhar(f'o brief não preencheu a lacuna "[{dentro[:50]}...]"')
                return str(valor)
        return m.group(0)

    texto = re.sub(r'\[((?:insert|choose one|for each block)[^\]]*)\]', troca, texto)
    sobra = re.findall(r'\[(?:insert|choose one|for each block)[^\]]*\]', texto)
    if sobra:
        falhar(f'lacunas sem preencher: {sobra}')
    if brief.get('palavra_chave') and brief['palavra_chave'] not in (brief.get('titulo') or ''):
        falhar('a palavra_chave precisa estar dentro do titulo')
    return texto + '\n'


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    brief = json.loads(Path(argv[1]).read_text(encoding='utf-8'))
    texto = montar(brief)
    Path(argv[2]).write_text(texto, encoding='utf-8')
    print(f'✓ prompt {brief["perfil"]} montado em {argv[2]} ({len(texto.split())} palavras, nenhuma lacuna)')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
