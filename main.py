from services.biblioteca import (
    buscar_livro_por_titulo,
    cadastrar_livro,
    criar_livros_iniciais,
    listar_livros,
    remover_livro,
)

# Criando uma lista de livros
livros = criar_livros_iniciais()

# Mostrar todos os livros da lista e seus detalhes.
listar_livros(livros)

# Buscando livro pelo titulo
buscador_titulo = input("Digite o nome do livro: ")

# Percorrendo lista para ver se livro existe ou não
livro_encontrado = buscar_livro_por_titulo(livros, buscador_titulo)
if livro_encontrado:
    livro_encontrado.mostrar_dados()

else:
    print("Livro não encontrado.")

# Criando um novo livro para a biblioteca
cadastrar_livro(livros)

listar_livros(livros)
print()

# Removendo um livro da biblioteca (caso ele exista).
remover_livro(livros)

print()
listar_livros(livros)


