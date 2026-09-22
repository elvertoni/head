#!/usr/bin/env python3
"""Cliente minimo (stdlib) para o Jev, modelo System One da TypeSafe.

O Jev nao gera texto: recebe um `state` e um mapa de perguntas tipadas e devolve
julgamentos com probabilidade — `noul` (sim/nao), `choice` (uma opcao de um
conjunto) e `score` (nivel numa escala). Usamos para triagem e verificacao em
lote, onde o codigo decide o fluxo e o modelo so da o julgamento semantico.

A chave vem de $TYPESAFE_API_KEY. Referencia: https://docs.typesafe.ai/api.md

    from tools.jev import system_one, noul, choice, score
    r = system_one({"texto": "..."}, {"e_revisao": noul("A aula `texto` e so revisao?")})
    r["answers"]["e_revisao"]["noul"]
"""
from __future__ import annotations

import json
import os
import random
import time
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional, Union

API_URL = "https://api.typesafe.ai/v1/systemone"
MODELO_PADRAO = "jev-latest"
RETENTAVEIS = {429, 500, 502, 503, 504, 529}

Texto = Union[str, Dict[str, Any], List[Any]]


class JevError(RuntimeError):
    def __init__(self, status: int, corpo: str):
        super().__init__(f"TypeSafe HTTP {status}: {corpo[:500]}")
        self.status = status
        self.corpo = corpo


def noul(instructions: Texto, sim: Optional[Texto] = None, nao: Optional[Texto] = None) -> Dict[str, Any]:
    q: Dict[str, Any] = {"type": "noul", "instructions": instructions}
    if sim is not None or nao is not None:
        q["criteria"] = {k: v for k, v in (("true", sim), ("false", nao)) if v is not None}
    return q


def choice(instructions: Texto, criteria: Dict[str, Optional[Texto]]) -> Dict[str, Any]:
    if not 2 <= len(criteria) <= 255:
        raise ValueError("choice aceita de 2 a 255 opcoes")
    return {"type": "choice", "instructions": instructions, "criteria": criteria}


def score(instructions: Texto, niveis: List[Texto]) -> Dict[str, Any]:
    if not 2 <= len(niveis) <= 10:
        raise ValueError("score aceita de 2 a 10 niveis")
    return {"type": "score", "instructions": instructions, "criteria": niveis}


def system_one(
    state: Texto,
    questions: Dict[str, Dict[str, Any]],
    model: str = MODELO_PADRAO,
    api_key: Optional[str] = None,
    tentativas: int = 5,
    timeout: float = 90.0,
) -> Dict[str, Any]:
    """POST /v1/systemone. Devolve o JSON da resposta (model, answers, usage)."""
    chave = api_key or os.environ.get("TYPESAFE_API_KEY")
    if not chave:
        raise JevError(401, "defina TYPESAFE_API_KEY")
    corpo = json.dumps({"state": state, "model": model, "questions": questions}, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        API_URL,
        data=corpo,
        method="POST",
        headers={"Authorization": f"Bearer {chave}", "Content-Type": "application/json"},
    )
    espera = 1.0
    for tentativa in range(1, tentativas + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            texto = exc.read().decode("utf-8", "replace")
            if exc.code not in RETENTAVEIS or tentativa == tentativas:
                raise JevError(exc.code, texto) from None
            retry_after = exc.headers.get("retry-after") if exc.headers else None
            pausa = float(retry_after) if retry_after and retry_after.replace(".", "", 1).isdigit() else espera
        except (urllib.error.URLError, TimeoutError) as exc:
            if tentativa == tentativas:
                raise JevError(0, str(exc)) from None
            pausa = espera
        time.sleep(pausa + random.uniform(0, 0.5))
        espera = min(espera * 2, 30.0)
    raise AssertionError("inalcancavel")


if __name__ == "__main__":
    # fumaça: python tools/jev.py
    r = system_one(
        "A aula apresenta o ciclo de vida do software: requisitos, projeto, implementação, testes e manutenção.",
        {"e_conceitual": noul("O texto apresenta conceitos técnicos (em vez de só uma dinâmica ou revisão)?")},
    )
    print(json.dumps(r, ensure_ascii=False, indent=2))
