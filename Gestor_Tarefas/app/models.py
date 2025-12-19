from dataclasses import dataclass
from datetime import date

@dataclass
class Tarefa:
    id: int
    titulo: str
    prioridade: int
    data: str
    estado: str = "pendente"  