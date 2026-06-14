# transcrever — vídeo/áudio → texto (lake)

Transcreve vídeo-aulas e áudios em **PT-BR** com `faster-whisper` rodando **local na GPU** (grátis) e salva um `.md` bruto direto no `lake/{disciplina}/`. É o degrau de entrada do data lake: insumo cru pra depois a skill `prof-toni` curar e virar Canônica.

## Setup (uma vez)

Já feito nesta máquina. Pra refazer em outra:

```powershell
cd tools\transcrever
uv venv --python 3.12
uv pip install -r requirements.txt
```

Roda na **GPU NVIDIA** (RTX 3050 detectada, `float16`). Sem GPU, cai automático pra CPU (`int8`, mais lento). Não precisa instalar ffmpeg — o decode de vídeo vem embutido (PyAV).

## Uso

```powershell
# forma simples (wrapper)
.\transcrever.ps1 "C:\videos\aula-mcp.mp4" --disciplina inteligencia-artificial --fonte ia-coders

# com título legível e marcação de tempo
.\transcrever.ps1 "C:\videos\aula-mcp.mp4" --disciplina inteligencia-artificial --fonte ia-coders --titulo "MCP na prática" --timestamps
```

Saída: `lake/inteligencia-artificial/ia-coders/mcp-na-pratica.md` (frontmatter + transcrição, `status: bruto`).

O `--fonte` organiza por origem do conteúdo (curso/instituição) dentro da disciplina — ex.: `ia-coders`, `ia-master`, `ufpr`. A subpasta é criada se não existir.

### Opções

| Flag | Default | Pra quê |
|---|---|---|
| `--disciplina` | (obrigatório) | slug da pasta em `lake/` (valida se existe) |
| `--fonte` | (nenhuma) | subpasta da origem dentro da disciplina (`ia-coders`, `ufpr`…); criada se faltar |
| `--titulo` | nome do arquivo | título legível; vira o slug do `.md` |
| `--modelo` | `large-v3` | qualidade máxima PT-BR. Use `medium`/`small` se quiser mais velocidade |
| `--device` | `auto` | `cuda`, `cpu` ou `auto` (GPU com fallback) |
| `--timestamps` | off | prefixa cada trecho com `[hh:mm:ss]` |
| `--idioma` | `pt` | força o idioma |
| `--saida` | lake/... | caminho `.md` alternativo |

## Notas

- **1ª execução baixa o `large-v3`** (~3 GB, do Hugging Face) e fica em cache. Depois é offline.
- Formatos aceitos: mp4, mkv, mov, mp3, wav, m4a, etc.
- `vad_filter` corta silêncios → mais rápido e limpo.
- Disciplinas válidas = as pastas em `lake/` (ver `manifesto.json`).
