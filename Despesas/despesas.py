import os, json
from datetime import datetime, date

FILE = "despesas.json"

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, 'r', encoding="utf-8") as f:
        return json.load(f)
        
def save(desp):
    with open(FILE, 'w', encoding="utf-8") as f:
        json.dump(desp, f, indent=2, ensure_ascii=False)
        
def add(categoria, valor, data = None, nota = ""):
    desp = load()
    desp.append({"id": int(datetime.now().timestamp()*1000),
                 "categoria": categoria,
                 "valor": float(valor),
                 "data": data or date.today().isoformat(),
                 "nota": nota})
    save(desp)

def total_por_categoria():
    totals = {}
    for r in load():
        totals.setdefault(r["categoria"], 0)
        totals[r["categoria"]] += r["valor"]
    return totals
    
def total_mes(ano, mes):
    s = 0
    for r in load():
        y,m,_ = r["data"].split("-")
        if int(y)==ano and int(m)==mes:
            s += r["valor"]
    return s


if __name__ == "__main__":
    add("saude", 32.5, None, "Foi remédio")    
    add("saude", 21)
    add("Alim", 40)
    print(total_por_categoria())