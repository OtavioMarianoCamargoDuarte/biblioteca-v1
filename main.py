from models.livro import Livro


def listar_livros(livros) -> None:
    print("======== LIVROS ========")
    print()
    for livro in livros:
        livro.mostrar_dados()
        print()
    print("========================")

# Criando livros
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("1984", "George Orwell", 1949)
livro3 = Livro("O Hobbit", "J. R. R. Tolkien", 1937)

# Criando uma lista de livros
livros = [
    livro1,
    livro2,
    livro3
]

# Mostrar todos os livros da lista e seus detalhes.
listar_livros(livros)

# Buscando livro pelo titulo
buscador_titulo = input("Digite o nome do livro: ")
titulo_encontrado = False

# Percorrendo lista para ver se livro existe ou não
for livro in livros:
    if buscador_titulo.lower().strip() == livro.titulo.lower().strip():
        titulo_encontrado = True
        print()
        print("Livro encontrado!\n")
        livro.mostrar_dados()
        break

if not titulo_encontrado:
    print("Livro não encontrado.")
print()

# Criando um novo livro para a biblioteca
print("====== CRIANDO NOVO LIVRO ======")
novo_titulo = input("Título: ")
novo_autor = input("Autor: ")
novo_ano = int(input("Ano: "))
novo_livro = Livro(novo_titulo, novo_autor, novo_ano)
livros.append(novo_livro)

listar_livros(livros)
print()

# Removendo um livro da biblioteca (caso ele exista).
print("====== REMOVENDO UM LIVRO ======")
buscador_titulo = input("Digite o nome do livro: ")
titulo_encontrado = False

for livro in livros:
    if buscador_titulo.lower().strip() == livro.titulo.lower().strip():
        titulo_encontrado = True
        print("Livro encontrado.")
        livros.remove(livro)
        print("Livro removido com sucesso.")
        break

if not titulo_encontrado:
    print("Livro não foi encontrado em nossa biblioteca.")

print()
listar_livros(livros)


