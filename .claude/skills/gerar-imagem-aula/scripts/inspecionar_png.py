#!/usr/bin/env python3
"""Confere proporcao e resolucao de uma arte-base contra o perfil declarado.

Uso:
    python inspecionar_png.py capa <caminho.png> [<caminho.png> ...]
    python inspecionar_png.py infografico <caminho.png> [...]
    python inspecionar_png.py auto <caminho.png> [...]

Le so o header IHDR do PNG, entao nao precisa de Pillow nem de venv.
Existe porque a checagem de proporcao e o unico item do checklist que da pra
verificar por medida em vez de olho, e errar a proporcao (defeito D12) e o
defeito mais facil de passar batido numa peca bonita.
"""

import struct
import sys

PERFIS = {
    "capa": (3 / 2, "3:2", "1536x1024"),
    "infografico": (16 / 9, "16:9", "maior resolucao nativa"),
}

TOLERANCIA = 0.03  # 3% — o gerador entrega tamanhos nativos, nao milimetricos


def dimensoes(caminho):
    with open(caminho, "rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("nao e um PNG")
    return struct.unpack(">II", head[16:24])


def avaliar(perfil, largura, altura):
    ratio = largura / altura
    alvo, rotulo, res = PERFIS[perfil]
    desvio = abs(ratio - alvo) / alvo
    ok = desvio <= TOLERANCIA
    return ok, ratio, alvo, rotulo, desvio


def perfil_provavel(ratio):
    return min(PERFIS, key=lambda p: abs(ratio - PERFIS[p][0]))


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2

    perfil_pedido, caminhos = argv[1].lower(), argv[2:]
    if perfil_pedido not in PERFIS and perfil_pedido != "auto":
        print(f"perfil invalido: {perfil_pedido} (use capa, infografico ou auto)")
        return 2

    falhou = False
    for caminho in caminhos:
        try:
            largura, altura = dimensoes(caminho)
        except (OSError, ValueError) as erro:
            print(f"ERRO  {caminho}: {erro}")
            falhou = True
            continue

        ratio = largura / altura
        perfil = perfil_provavel(ratio) if perfil_pedido == "auto" else perfil_pedido
        ok, ratio, alvo, rotulo, desvio = avaliar(perfil, largura, altura)
        marca = "OK  " if ok else "D12 "

        print(
            f"{marca}{caminho}\n"
            f"      {largura}x{altura}  ratio={ratio:.4f}  "
            f"perfil={perfil} ({rotulo}, alvo {alvo:.4f})  desvio={desvio * 100:.1f}%"
        )
        if not ok:
            sugerido = perfil_provavel(ratio)
            print(
                f"      proporcao nao bate com o perfil declarado. "
                f"A medida corresponde ao perfil '{sugerido}'. "
                f"Regenerar, nao recortar."
            )
            falhou = True

    return 1 if falhou else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
