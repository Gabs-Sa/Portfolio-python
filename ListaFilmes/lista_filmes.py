print('Lista de Filmes iniciada')

import os, json
from datetime import datetime, date

FILE = "filmes.json"

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, 'r', encoding="utf-8") as f:
        return json.load(f)
    
def save(movie):
    with open(FILE, 'w', encoding="utf-8") as f:
        return json.dump(movie, f, indent=2, ensure_ascii=False)
    
def add(titulo, genero, rating=None, estado="por ver"):
    movie = load()
    movie.append({"titulo": titulo,
                  "genero" : genero,
                  "rating": rating,
                  "estado": estado})
    save(movie)
    
def list_by_estado(estado):
    return [f for f in load() if f["estado"].lower() == estado.lower()]

def search_by_genre(g):
    return [f for f in load() if f["genero"].lower() == g.lower()]

if __name__ == "__main__":
    add("O Exemplo", "Drama", rating=8.2, estado="visto")
    add("Série X", "Sci-Fi", estado="por ver")
    print("Por ver:", list_by_estado("por ver"))
    print("Sci-Fi:", search_by_genre("sci"))