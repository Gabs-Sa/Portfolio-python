# Projeto Agenda de Contactos

Created on Fri Dec 12 08:06:17 2025

@author: gasa
"""

# notas.py
import os, csv

FILE = "contactos.csv"
HEADERS = ["nome", "telefone","email"]

def ensure():
    if not os.path.exists(FILE):
        with open(FILE, 'w', newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS)
            writer.writeheader()
            
def add(nome, telefone, email):
    ensure()
    with open(FILE, 'a', newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writerow({"nome": nome, "telefone":telefone, "email":email})
        
def list_all():
    ensure()
    with open(FILE, 'r', newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
    
def find(nome):
    return[c for c in list_all() if nome.lower() in c["nome"].lower()]

def remove_by_email(email):
    rows = [ r for r in list_all() if email != r["email"]]
    with open(FILE, 'w', newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldname = HEADERS)
        writer.writeheader()
        writer.writerows(rows)
        
if __name__ == "__main__":
    add("Ana Silva", "912345678", "ana@example.com")
    add("João Pereira", "923456789", "joao@example.com")
    print("Todos:", list_all())
    print("Procurar 'Ana':", find("Ana"))
    

if __name__ == "__main__":
    add("Ana Silva", "912345678", "ana@example.com")
    add("João Pereira", "923456789", "joao@example.com")
    print("Todos:", list_all())
    print("Procurar 'Ana':", find("Ana"))
