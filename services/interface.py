from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text


console = Console()


def limpar_tela() -> None:
    console.clear()


def aguardar_usuario() -> None:
    input("\nPressione ENTER para continuar...")


def mostrar_titulo() -> None:
    painel = Panel(
        Align.center(
            "📚 Biblioteca V1\n"
            "Gerenciamento de Livros"
        ),
        title="Sistema",
        border_style="bold blue",
        width=40
    )

    console.print(painel)


def mostrar_menu() -> None:

    menu = Text()

    menu.append("[1] ", style="bold cyan")
    menu.append("- Listar livros\n")

    menu.append("[2] ", style="bold cyan")
    menu.append("- Buscar livro\n")

    menu.append("[3] ", style="bold cyan")
    menu.append("- Cadastrar livro\n")

    menu.append("[4] ", style="bold cyan")
    menu.append("- Remover livro\n")

    menu.append("[5] ", style="bold cyan")
    menu.append("- Emprestar livro\n")

    menu.append("[6] ", style="bold cyan")
    menu.append("- Devolver livro\n")

    menu.append("[7] ", style="bold cyan")
    menu.append("- Listar livros disponíveis\n")

    menu.append("[8] ", style="bold cyan")
    menu.append("- Listar livros emprestados\n")

    menu.append("[9] ", style="bold cyan")
    menu.append("- Mostrar relatório\n")

    menu.append("[10] ", style="bold cyan")
    menu.append("- Buscar por autor\n")

    menu.append("[0] ", style="bold red")
    menu.append("- Sair")

    painel_menu = Panel(menu,title="Menu",border_style="bold blue",width=50)

    console.print(painel_menu)

    console.print("\n👉 Escolha uma opção:",style="bold yellow")