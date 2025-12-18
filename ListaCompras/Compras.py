print('Lista de Compras')

import os, json

FILE = "listaCompras.json"

def load():
    if not os.path.exists(FILE):
        return[]
    with open(FILE, 'r', encoding="utf-8") as f:
        return json.load(f)
    
def save(item):
    with open(FILE, 'w', encoding="utf-8") as f:
        return json.dump(item, f, indent=2, ensure_ascii=False)
    
def add(produto, quantidade=1):
    item = load()
    for i in item:
        if produto == i["produto"]:
           i["quantidade"] += quantidade 
           i["produto"] = produto
           save(item)
           return
    item.appen({"produto": produto,
                "quantidade": quantidade,
                "comprado": False})
    save(item)
    
def remove(produto, quantidade= None):
    item = load()
    for i in item:
        if produto == i["produto"]:
            if quantidade is None or quantidade >= i["quantidade"]:
                item.remove(item)
            else:
                i["quantidade"] -= quantidade
        save(item)
        return True
    return False

def mark_bought(produto):
    item = load()
    for i in item:
        if i["produto"].lower == produto:
            i["comprado "] = True
    save(item)
        
            
def export_final(filename):
    bought = [it for it in load() if it["comprado"]]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(bought, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    add("Leite", 2)
    add("Pão", 1)
    mark_bought("Leite")
    print("Lista:", load())
    export_final("compras_finalizadas.json")
