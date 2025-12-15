print('Inventario iniciado')

import os, json
from datetime import datetime

FILE = "inventario.json"

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, 'r', encoding="utf-8") as f:
        return json.load(f)
        
def save(items):
    with open(FILE, 'w', encoding="utf-8") as f:
        json.dump(items, f, indent= 2, ensure_ascii= False)
        
def add(nome, quantidade, preco):
    items = load()
    for it in items:
        if nome.lower() == it["nome"].lower():
            it["quantidade"] += quantidade
            it["preco"] = preco
            it["nome"] = nome
            save(items)
            return
    items.append({"nome": nome, 
                  "quantidade": quantidade,
                  "preco": preco})
    save(items)
    return

def list_all():
    return load()

def remove(nome, quantidade=None):
    items = load()
    for it in items:
        if it["nome"].lower() == nome.lower():
            if quantidade is None or quantidade >= it["quantidade"]:
                items.remove(it)
            else:
                it["quantidade"] -= quantidade
            save(items)
            return True
    return False

def total_value():
    return sum(it["quantidade"] * it["preco"] for it in load())

if __name__ == "__main__":
    add("pera", 3, 1.25)
    print(list_all())
    print(total_value())
