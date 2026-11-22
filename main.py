from pydoc import ModuleScanner
from sys import remote_exec

from services.biblioteca import (
    buscar_livro_por_titulo,
    criar_livros_iniciais,
    listar_livros,
    cadastrar_livro,
    remover_livro,
    mostrar_menu
)

livros = criar_livros_iniciais()

while True:
    mostrar_menu()

    opcao = input("Escolha: ")

    if opcao == "0":
        print("PROGRAMA FINALIZADO!")
        break

    elif opcao == "1":
        listar_livros(livros)

    elif opcao == "2":
        titulo = input("Digite o titulo do livro: ")
        resultado = buscar_livro_por_titulo(livros, titulo)

        if resultado:
            resultado.mostrar_dados()
        else:
            print("Livro não encontrado.")

    elif opcao == "3":
        cadastrar_livro(livros)

    elif opcao == "4":
        remover_livro(livros)

    else:
        print("Opção inválida.")
