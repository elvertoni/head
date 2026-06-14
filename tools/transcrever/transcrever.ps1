# Wrapper: roda transcrever.py no venv local sem precisar ativar nada.
# Uso: .\transcrever.ps1 <video> --disciplina <slug> [opcoes]
param([Parameter(ValueFromRemainingArguments = $true)] $Rest)
$ErrorActionPreference = 'Stop'
$env:HF_HUB_DISABLE_SYMLINKS_WARNING = '1'
$py = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
if (-not (Test-Path $py)) { throw "venv nao encontrado. Rode: uv venv; uv pip install -r requirements.txt" }
& $py (Join-Path $PSScriptRoot 'transcrever.py') @Rest
