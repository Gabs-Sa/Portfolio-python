print('Biblioteca iniciada')

import csv, os

FILE = "biblioteca.csv"
HEADERS = ["titulo", "autor", "ano", "disponivel"]

def ensure():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS)
            writer.writeheader()

def add(titulo, autor, ano):
    ensure()
    with open(FILE, "a", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writerow({"titulo": titulo, "autor": autor, "ano": ano, "disponivel": "True"})

def list_all():
    ensure()
    with open(FILE, newline='', encoding="utf-8") as f:
        return list(csv.DictReader(f))

def lend(titulo):
    rows = list_all()
    changed = False
    for r in rows:
        if r["titulo"].lower() == titulo.lower() and r["disponivel"]=="True":
            r["disponivel"] = "False"
            changed = True
            break
    if changed:
        with open(FILE, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(rows)
    return changed

def give_back(titulo):
    rows = list_all()
    for r in rows:
        if r["titulo"].lower() == titulo.lower():
            r["disponivel"] = "True"
    with open(FILE, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    add("1984", "George Orwell", "1949")
    add("O Senhor dos Anéis", "Tolkien", "1954")
    print("Todos:", list_all())
    print("Lista depois:", list_all())