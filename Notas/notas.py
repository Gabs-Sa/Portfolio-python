print('Gestor de notas iniciado')


# notas.py
import json, os
from datetime import datetime

FILE = "notas.json"

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save(notes):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)

def add(titulo, texto):
    notes = load()
    notes.append({
        "id": int(datetime.now().timestamp()*1000),
        "titulo": titulo,
        "texto": texto,
        "data": datetime.now().isoformat()
    })
    save(notes)

def list_all():
    for n in load():
        print(f"{n['id']} — {n['titulo']} ({n['data']})")

def find_by_title(q):
    return [n for n in load() if q.lower() in n["titulo"].lower()]

def edit(note_id, titulo=None, texto=None):
    notes = load()
    for n in notes:
        if n["id"] == note_id:
            if titulo: n["titulo"] = titulo
            if texto: n["texto"] = texto
            save(notes)
            return True
    return False

def remove(note_id):
    notes = load()
    notes = [n for n in notes if n["id"] != note_id]
    save(notes)
    
if __name__ == "__main__":
    add("Exemplo", "Esta é uma nota de teste.")
    print(list_all())

