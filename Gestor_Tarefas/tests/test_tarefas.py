from app.service import adicionar, listar

def test_adicionar():
    adicionar("Teste", 1)
    tarefas = listar()
    assert any(t["titulo"] == "Teste" for t in tarefas)
