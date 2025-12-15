print('Diário iniciado')

    with open(fn, 'r', encoding="utf-8") as f:
        return f.read()

def list_entries():
    ensure()
    return sorted(os.listdir(DIR))


if __name__ == "__main__":
    add_entry("Olá, o meu nome é Gabs, assim compensa")
    print(list_

