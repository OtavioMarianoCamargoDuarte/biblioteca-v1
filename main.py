from models.livro import Livro
from services.biblioteca import (
    buscar_livro_por_titulo,
    cadastrar_livro,
    converter_json_para_livros,
    converter_livros_para_json,
    ler_livros_json,
    listar_livros,
    mostrar_menu,
    remover_livro,
    salvar_livros_json,
)

dados_json = ler_livros_json()

livros = converter_json_para_livros(
    dados_json
)

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

    elif opcao == "5":
        titulo = input("Digite o titulo do livro: ")
        resultado = buscar_livro_por_titulo(livros, titulo)

        if resultado is not None:
            resultado.emprestar()
            dados = converter_livros_para_json(livros)
            salvar_livros_json(dados)
        else:
            print("Livro não encontrado.")

    elif opcao == "6":
        titulo = input("Digite o titulo do livro: ")
        resultado = buscar_livro_por_titulo(livros, titulo)

        if resultado is not None:
            resultado.devolver()
            dados = converter_livros_para_json(livros)
            salvar_livros_json(dados)
        else:
            print("Livro não encontrado.")

    else:
        print("Opção inválida.")
