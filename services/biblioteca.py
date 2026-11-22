from models.livro import Livro


def listar_livros(livros) -> None:
    print("======== LIVROS ========")
    print()
    for livro in livros:
        livro.mostrar_dados()
        print()
    print("========================")

def buscar_livro_por_titulo(
    livros: list[Livro],
    titulo: str,
):
    for livro in livros:
        if normalizar_texto(livro.titulo) == normalizar_texto(titulo):
            return livro

    return None

def cadastrar_livro(livros) -> None:
    print("====== CRIANDO NOVO LIVRO ======")
    novo_titulo = input("Título: ")
    novo_autor = input("Autor: ")
    novo_ano = int(input("Ano: "))
    novo_livro = Livro(novo_titulo, novo_autor, novo_ano)
    livros.append(novo_livro)

def remover_livro(livros) -> None:
    print("====== REMOVENDO UM LIVRO ======")
    buscador_titulo = input("Digite o nome do livro: ")
    titulo_encontrado = False

    for livro in livros:
        if normalizar_texto(buscador_titulo) == normalizar_texto(livro.titulo):
            titulo_encontrado = True
            print("Livro encontrado.")
            livros.remove(livro)
            print("Livro removido com sucesso.")
            break

    if not titulo_encontrado:
        print("Livro não foi encontrado em nossa biblioteca.")

def criar_livros_iniciais() -> list[Livro]:
    return [
        Livro("Dom Casmurro", "Machado de Assis", 1899),
        Livro("1984", "George Orwell", 1949),
        Livro("O Hobbit", "J. R. R. Tolkien", 1937)
    ]

def normalizar_texto(texto: str) -> str:
    return texto.lower().strip()