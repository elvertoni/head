#!/usr/bin/env python
"""Transcreve video/audio em PT-BR com faster-whisper e salva .md no lake.

Uso:
    python transcrever.py <arquivo> --disciplina <slug> [opcoes]

Exemplo:
    python transcrever.py "C:\\videos\\aula-mcp.mp4" --disciplina inteligencia-artificial --titulo "MCP na pratica"

Saida: lake/{disciplina}/{slug}.md  (conteudo BRUTO, status: bruto)
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]   # C:\PROJETOS\PROF-TONI
LAKE = ROOT / "lake"


def slugify(texto: str) -> str:
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")
    texto = re.sub(r"[^\w\s-]", "", texto).strip().lower()
    return re.sub(r"[\s_-]+", "-", texto) or "transcricao"


def add_cuda_dlls() -> None:
    """No Windows, expoe as DLLs CUDA instaladas via pip (nvidia-*-cu12) ao loader."""
    if os.name != "nt":
        return
    import site
    dirs = list(site.getsitepackages())
    try:
        dirs.append(site.getusersitepackages())
    except Exception:
        pass
    dirs.append(str(Path(sys.executable).parent / "Lib" / "site-packages"))
    for sp in dirs:
        nv = Path(sp) / "nvidia"
        if nv.exists():
            for binp in nv.glob("*/bin"):
                try:
                    os.add_dll_directory(str(binp))
                except Exception:
                    pass


def fmt_ts(segundos: float) -> str:
    td = dt.timedelta(seconds=int(segundos))
    return str(td)


def carregar_modelo(modelo: str, device: str):
    """Tenta GPU; cai pra CPU se falhar. Retorna (model, device_real, compute_type)."""
    from faster_whisper import WhisperModel

    tentativas = []
    if device in ("auto", "cuda"):
        tentativas.append(("cuda", "float16"))
    tentativas.append(("cpu", "int8"))

    erro = None
    for dev, ct in tentativas:
        try:
            print(f"[info] carregando modelo '{modelo}' em {dev} ({ct})...", flush=True)
            model = WhisperModel(modelo, device=dev, compute_type=ct)
            return model, dev, ct
        except Exception as e:  # noqa: BLE001
            erro = e
            print(f"[aviso] falhou em {dev}: {e}", flush=True)
    raise SystemExit(f"[erro] nao foi possivel carregar o modelo. Ultimo erro: {erro}")


def main() -> None:
    p = argparse.ArgumentParser(description="Transcreve video/audio em PT-BR -> lake/{disciplina}/")
    p.add_argument("arquivo", help="caminho do video ou audio (mp4, mkv, mp3, wav, m4a, ...)")
    p.add_argument("--disciplina", required=True, help="slug da disciplina (pasta em lake/)")
    p.add_argument("--titulo", default=None, help="titulo legivel; default = nome do arquivo")
    p.add_argument("--modelo", default="large-v3", help="modelo whisper (default: large-v3)")
    p.add_argument("--device", default="auto", choices=["auto", "cuda", "cpu"], help="default: auto")
    p.add_argument("--idioma", default="pt", help="idioma (default: pt)")
    p.add_argument("--timestamps", action="store_true", help="prefixa cada trecho com [hh:mm:ss]")
    p.add_argument("--saida", default=None, help="caminho .md de saida (sobrescreve o default)")
    args = p.parse_args()

    entrada = Path(args.arquivo).expanduser()
    if not entrada.is_file():
        raise SystemExit(f"[erro] arquivo nao encontrado: {entrada}")

    destino_dir = LAKE / args.disciplina
    if not destino_dir.is_dir():
        existentes = ", ".join(sorted(d.name for d in LAKE.iterdir() if d.is_dir()))
        raise SystemExit(
            f"[erro] disciplina '{args.disciplina}' nao existe em lake/.\n"
            f"        disponiveis: {existentes}"
        )

    titulo = args.titulo or entrada.stem
    slug = slugify(titulo)
    saida = Path(args.saida).expanduser() if args.saida else destino_dir / f"{slug}.md"

    add_cuda_dlls()
    model, dev, ct = carregar_modelo(args.modelo, args.device)

    print(f"[info] transcrevendo: {entrada.name}", flush=True)
    segments, info = model.transcribe(
        str(entrada),
        language=args.idioma,
        vad_filter=True,                 # corta silencios -> mais rapido e limpo
        beam_size=5,
        condition_on_previous_text=True,
    )
    print(f"[info] idioma detectado: {info.language} (p={info.language_probability:.2f}) | "
          f"duracao: {fmt_ts(info.duration)}", flush=True)

    partes: list[str] = []
    ultimo = -1
    for seg in segments:
        txt = seg.text.strip()
        if args.timestamps:
            partes.append(f"[{fmt_ts(seg.start)}] {txt}")
        else:
            partes.append(txt)
        # progresso a cada ~30s de audio
        marco = int(seg.end) // 30
        if marco != ultimo:
            ultimo = marco
            print(f"\r[info] {fmt_ts(seg.end)} / {fmt_ts(info.duration)}", end="", flush=True)
    print()

    corpo = ("\n\n" if args.timestamps else " ").join(partes).strip()
    hoje = dt.date.today().isoformat()

    frontmatter = (
        "---\n"
        f"titulo: {titulo}\n"
        f"disciplina: {args.disciplina}\n"
        "tipo: transcricao\n"
        f"fonte: {entrada.name}\n"
        f"modelo: {args.modelo}\n"
        f"device: {dev}/{ct}\n"
        f"duracao: {fmt_ts(info.duration)}\n"
        f"idioma: {info.language}\n"
        f"transcrito_em: {hoje}\n"
        "status: bruto\n"
        "---\n\n"
    )
    md = frontmatter + f"# Transcricao — {titulo}\n\n> Conteudo BRUTO (lake). Insumo para curadoria pela skill prof-toni.\n\n" + corpo + "\n"

    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text(md, encoding="utf-8")
    print(f"[ok] salvo em: {saida}")


if __name__ == "__main__":
    main()
