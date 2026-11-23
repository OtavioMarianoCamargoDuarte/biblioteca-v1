from models.livro import Livro
from services.biblioteca import (
    buscar_livros_por_autor,
    cadastrar_livro,
    converter_json_para_livros,
    converter_livros_para_json,
    ler_livros_json,
    listar_livros,
    listar_livros_disponiveis,
    listar_livros_emprestados,
    mostrar_menu,
    mostrar_relatorio,
    obter_livro_do_usuario,
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
        resultado = obter_livro_do_usuario(livros)

        if resultado:
            resultado.mostrar_dados()
        else:
            print("Livro não encontrado.")

    elif opcao == "3":
        cadastrar_livro(livros)

    elif opcao == "4":
        remover_livro(livros)

    elif opcao == "5":
        resultado = obter_livro_do_usuario(livros)

        if resultado is not None:
            resultado.emprestar()
            dados = converter_livros_para_json(livros)
            salvar_livros_json(dados)
        else:
            print("Livro não encontrado.")

    elif opcao == "6":
        resultado = obter_livro_do_usuario(livros)

        if resultado is not None:
            resultado.devolver()
            dados = converter_livros_para_json(livros)
            salvar_livros_json(dados)
        else:
            print("Livro não encontrado.")

    elif opcao == "7":
        listar_livros_disponiveis(livros)

    elif opcao == "8":
        listar_livros_emprestados(livros)

    elif opcao == "9":
        mostrar_relatorio(livros)

    elif opcao == "10":
        autor = input("Digite o nome do autor: ")
        print()
        resultado = buscar_livros_por_autor(livros, autor)

        if resultado:
            for livro in resultado:
                livro.mostrar_dados()
                print()
        else:
            print("Autor não encontrado.")

    else:
        print("Opção inválida.")
