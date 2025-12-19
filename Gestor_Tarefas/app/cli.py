
import argparse
from app.service import adicionar, remover, listar

def main():
    parser = argparse.ArgumentParser(
        description="Gestor de Tarefas (JSON)"
    )

    subparsers = parser.add_subparsers(
        dest="comando",
        required=True
    )

    # ---------- add ----------
    parser_add = subparsers.add_parser(
        "add", help="Adicionar tarefa"
    )
    parser_add.add_argument(
        "--titulo", required=True, help="Título da tarefa"
    )
    parser_add.add_argument(
        "--prioridade", type=int, default=5, help="Prioridade (1-5)"
    )

    # ---------- rm ----------
    parser_rm = subparsers.add_parser(
        "rm", help="Remover tarefa"
    )
    parser_rm.add_argument(
        "--id", type=int, required=True, help="ID da tarefa"
    )

    # ---------- ls ----------
    subparsers.add_parser(
        "ls", help="Listar tarefas"
    )

    args = parser.parse_args()

    if args.comando == "add":
        adicionar(args.titulo, args.prioridade)
        print("✅ Tarefa adicionada")

    elif args.comando == "rm":
        remover(args.id)
        print("🗑️ Tarefa removida")

    elif args.comando == "ls":
        tarefas = listar()
        if not tarefas:
            print("📭 Nenhuma tarefa")
        for t in tarefas:
            print(f"[{t['id']}] {t['titulo']} (prioridade {t['prioridade']})")

if __name__ == "__main__":
    main()

