#!/usr/bin/env python3
"""Empacota as skills de .claude/skills/ em .zip para subir no claude.ai.

Uso:
    python tools/empacotar_skills.py               # grava saidas/skills/{skill}.zip
    python tools/empacotar_skills.py --check       # só valida, não grava
    python tools/empacotar_skills.py --saida DIR   # outra pasta de saída

Também empacota as skills só do claude.ai, de docs/skills-claudeai/.

Cada .zip tem a pasta da skill na raiz ({skill}/SKILL.md, ...), que é o formato
que o claude.ai aceita em "Capabilities > Skills > Upload". Antes de gravar,
confere o que o claude.ai exige do frontmatter: `name` igual ao nome da pasta,
só minúsculas, dígitos e hífen, até 64 caracteres; `description` com até 1024
caracteres e sem tags (< >).

Arquivos que vivem fora da pasta da skill mas que ela precisa entram no pacote
pela tabela EXTRAS (o repo continua com uma fonte só). Ficam de fora caches de
Python e propostas de imagem.

As saídas vão para `saidas/`, que é gitignored: o zip é derivado, nunca se edita.
Só usa a biblioteca padrão.
"""
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path
from typing import Dict, List, Optional

RAIZ = Path(__file__).resolve().parent.parent
SKILLS = RAIZ / '.claude' / 'skills'
# Skills só do claude.ai (fora de .claude/skills/ para o Claude Code não carregar em dobro)
SO_CLAUDEAI = RAIZ / 'docs' / 'skills-claudeai'

# skill -> {caminho dentro do pacote: arquivo no repo}
EXTRAS: Dict[str, Dict[str, Path]] = {
    'gerar-imagem-aula': {'references/prompt.xml': RAIZ / 'tools' / 'imagen-generator' / 'prompt.xml'},
}
IGNORAR_DIRS = {'__pycache__', '.git'}
IGNORAR_SUFIXOS = ('.pyc', '.proposta.png')
IGNORAR_NOMES = {'.DS_Store', 'Thumbs.db'}
NOME_VALIDO = re.compile(r'^[a-z0-9-]{1,64}$')


def frontmatter(texto: str) -> Dict[str, str]:
    if not texto.startswith('---'):
        return {}
    fim = texto.find('\n---', 3)
    if fim < 0:
        return {}
    campos: Dict[str, str] = {}
    for linha in texto[3:fim].splitlines():
        m = re.match(r'^([A-Za-z_-]+):\s*(.*)$', linha)
        if m:
            campos[m.group(1)] = m.group(2).strip().strip('"\'')
    return campos


def validar(pasta: Path) -> List[str]:
    """Problemas que impediriam o upload no claude.ai (lista vazia = ok)."""
    problemas: List[str] = []
    skill_md = pasta / 'SKILL.md'
    if not skill_md.is_file():
        return [f'{pasta.name}: sem SKILL.md']
    fm = frontmatter(skill_md.read_text(encoding='utf-8'))
    nome, desc = fm.get('name', ''), fm.get('description', '')
    if not nome:
        problemas.append(f'{pasta.name}: frontmatter sem `name`')
    elif nome != pasta.name:
        problemas.append(f'{pasta.name}: `name` ({nome}) diferente do nome da pasta')
    elif not NOME_VALIDO.match(nome):
        problemas.append(f'{pasta.name}: `name` só aceita minúsculas, dígitos e hífen (até 64)')
    if not desc:
        problemas.append(f'{pasta.name}: frontmatter sem `description`')
    elif len(desc) > 1024:
        problemas.append(f'{pasta.name}: `description` com {len(desc)} caracteres (máximo 1024)')
    elif '<' in desc or '>' in desc:
        problemas.append(f'{pasta.name}: `description` não pode ter < ou >')
    for destino, origem in EXTRAS.get(pasta.name, {}).items():
        if not origem.is_file():
            problemas.append(f'{pasta.name}: extra {destino} aponta para arquivo inexistente ({origem})')
    return problemas


def arquivos(pasta: Path) -> List[Path]:
    saida = []
    for p in sorted(pasta.rglob('*')):
        if not p.is_file():
            continue
        partes = set(p.relative_to(pasta).parts)
        if partes & IGNORAR_DIRS or p.name in IGNORAR_NOMES or p.name.endswith(IGNORAR_SUFIXOS):
            continue
        saida.append(p)
    return saida


def empacotar(pasta: Path, destino: Path) -> Path:
    destino.mkdir(parents=True, exist_ok=True)
    zip_path = destino / f'{pasta.name}.zip'
    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for p in arquivos(pasta):
            zf.write(p, f'{pasta.name}/{p.relative_to(pasta).as_posix()}')
        for dentro, origem in EXTRAS.get(pasta.name, {}).items():
            zf.write(origem, f'{pasta.name}/{dentro}')
    return zip_path


def skills(raiz_skills: Path) -> List[Path]:
    if not raiz_skills.is_dir():
        return []
    return sorted(p for p in raiz_skills.iterdir() if p.is_dir() and (p / 'SKILL.md').is_file())


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--saida', type=Path, default=RAIZ / 'saidas' / 'skills')
    parser.add_argument('--check', action='store_true', help='só valida, não grava')
    args = parser.parse_args(argv)

    encontradas = skills(SKILLS) + skills(SO_CLAUDEAI)
    problemas = [p for s in encontradas for p in validar(s)]
    if problemas:
        for p in problemas:
            print('✗ ' + p)
        return 1
    if args.check:
        print(f'✓ {len(encontradas)} skill(s) prontas para empacotar: {", ".join(s.name for s in encontradas)}')
        return 0
    for s in encontradas:
        z = empacotar(s, args.saida)
        with zipfile.ZipFile(z) as zf:
            n = len(zf.namelist())
        print(f'✓ {z.relative_to(RAIZ) if z.is_relative_to(RAIZ) else z}  ({n} arquivos, {z.stat().st_size // 1024} KB)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
