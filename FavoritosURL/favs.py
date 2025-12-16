print('Aplicação de Favoritos (links)')

import json, os

FILE = "favoritos.json"

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, 'r', encoding="utf-8") as f:
        return json.load(f)
    
def save(item):
    with open(FILE, 'w', encoding="utf-8") as f:
        return json.dump(item, f, indent=2, ensure_ascii=False)
    
def add(url, titulo= None, tags= None):
    item = load()
    item.append({"url": url,
                 "titulo": titulo or url,
                 "tags": tags or []})
    save(item)
    
def list_all():
    return sorted(load(), key=lambda x:["titulo"])

def filter_by_tag(tag):
    return [f for f in load() if tag in f.get("tags",[])]

def export_json(filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(load(), f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    add("https://example.com", "Example", ["teste","docs"])
    print("Por tag 'teste':", filter_by_tag("teste"))