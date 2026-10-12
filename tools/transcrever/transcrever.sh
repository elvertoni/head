#!/usr/bin/env bash
# Wrapper: roda transcrever.py no venv do WSL sem precisar ativar nada.
# Uso: ./transcrever.sh <video> --disciplina <slug> [opcoes]
# O venv fica fora do repo, no disco do WSL: em /mnt/d ele e lento.
set -euo pipefail
aqui="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
venv="${TRANSCREVER_VENV:-$HOME/.venvs/prof-toni-transcrever}"
py="$venv/bin/python"
if [[ ! -x "$py" ]]; then
  echo "venv nao encontrado em $venv. Rode:" >&2
  echo "  uv venv --python 3.12 \"$venv\"" >&2
  echo "  uv pip install --python \"$py\" -r \"$aqui/requirements.txt\"" >&2
  exit 1
fi
# No Linux o ctranslate2 acha cuBLAS e cuDNN pelo LD_LIBRARY_PATH; no Windows quem resolve e o add_cuda_dlls.
for lib in "$venv"/lib/python*/site-packages/nvidia/*/lib; do
  [[ -d "$lib" ]] && LD_LIBRARY_PATH="$lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
done
export LD_LIBRARY_PATH
exec "$py" "$aqui/transcrever.py" "$@"
