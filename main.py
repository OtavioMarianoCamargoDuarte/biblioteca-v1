from services.biblioteca import (
    buscar_livro_por_titulo,
    cadastrar_livro,
    criar_livros_iniciais,
    listar_livros,
    mostrar_menu,
    remover_livro,
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
