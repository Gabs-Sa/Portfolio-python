import json
from pathlib import Path

FILE = Path("data/tarefas.json")

def load():
    if not FILE.exists():
        return []
    return json.loads(FILE.read_text(encoding="utf-8"))

def save(data):
    FILE.parent.mkdir(exist_ok=True)
    FILE.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )