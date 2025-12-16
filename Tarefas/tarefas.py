print('Tarefas com prioridade')

import os, json
from datetime import datetime

FILE = "tarefas.json"

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, 'r', encoding="utf-8") as f:
        return json.load(f)
    
def save(tarefa):
    with open(FILE,'w', encoding="utf-8") as f:
        return json.dump(tarefa, f, indent=2, ensure_ascii=False)
    
def add(titulo, prioridade=5, data= None):
    tarefas = load()
    tarefas.append({"id": int(datetime.now().timestamp()*1000),
                    "titulo": titulo,
                   "prioridade": int(prioridade),
                   "data" : data or datetime.today().isoformat(),
                   "estado": "pendente"})
    save(tarefas)
 
def list_sorted():
    return sorted(load(), key=lambda x: (x["prioridade"], x["data"]))

def mark_done(task_id):
    tarefas = load()
    for i in tarefas:
        if task_id == i["id"]:
            i["estado"] = "concluido"
            save(tarefas)
            return True
    return False

    
if __name__ == "__main__":
    add("Estudar para teste", prioridade=1)
    add("Lavar roupa", prioridade=3)
    print("Tarefas ordenadas:", list_sorted())