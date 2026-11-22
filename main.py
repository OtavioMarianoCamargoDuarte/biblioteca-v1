from sys import remote_exec

from services.biblioteca import (
    buscar_livro_por_titulo,
    criar_livros_iniciais,
    listar_livros,
    cadastrar_livro,
    remover_livro
)

livros = criar_livros_iniciais()

while True:
    print("========== MENU ==========")
    print("[1] - Listar livros")
    print("[2] - Buscar livro")
    print("[3] - Cadastrar livro")
    print("[4] - Remover livro")
    print("[0] - Sair")
    print("==========================")

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
