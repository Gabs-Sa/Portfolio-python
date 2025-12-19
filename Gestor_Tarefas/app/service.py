from datetime import datetime
from .storage import load, save

def adicionar(titulo, prioridade):
    tarefas = load()
    tarefas.append({
        "id": int(datetime.now().timestamp() * 1000),
        "titulo": titulo,
        "prioridade": prioridade,
        "data": datetime.now().date().isoformat(),
        "estado": "pendente"
    })
    save(tarefas)

def remover(tarefa_id):
    tarefas = [t for t in load() if t["id"] != tarefa_id]
    save(tarefas)

def listar():
    return sorted(
        load(),
        key=lambda x: (x["prioridade"], x["data"])
    )