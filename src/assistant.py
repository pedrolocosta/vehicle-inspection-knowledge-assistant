"""Deterministic status lookup and technical abstention demo.

This module does not implement retrieval-augmented generation or inspection logic.
"""

import json
import re
import sys
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "demo_records.json"
ABSTENTION = (
    "Não posso fornecer critério ou resultado de inspeção nesta demonstração. "
    "Não há aqui fonte técnica aplicável e aprovada pelo RT. "
    "Consulte as fontes controladas atuais e solicite revisão técnica."
)


def load_records(path=DATA_PATH):
    records = json.loads(Path(path).read_text(encoding="utf-8"))
    for record in records:
        if record["kind"] == "technical_requirement" and record["status"] != "approved":
            if record["answer"] is not None:
                raise ValueError("Registro técnico não aprovado não pode conter resposta")
    return records


def respond(question, records=None):
    """Return a demo answer only for an explicitly matched, approved status record."""
    if not question.strip():
        return ABSTENTION
    records = load_records() if records is None else records
    words = set(re.findall(r"\w+", question.casefold()))
    status_intent = bool(words & {"estado", "status", "validação", "validacao", "pendente", "mvp"})
    technical_intent = bool(words & {
        "critério", "criterio", "limite", "ensaio", "teste", "procedimento",
        "inspeção", "inspecao", "aprova", "reprova", "vazamento", "pt", "it",
    })
    if technical_intent or not status_intent:
        return ABSTENTION
    for record in records:
        if (record["kind"] == "project_status"
                and record["status"] == "approved_for_demo"
                and words & set(record["keywords"])):
            return f'{record["answer"]}\nOrigem: {record["provenance"]} [{record["id"]}]'
    return ABSTENTION


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit('Uso: python -m src.assistant "sua pergunta"')
    print(respond(" ".join(sys.argv[1:])))
