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
    mostrar_relatorio,
    obter_livro_do_usuario,
    remover_livro,
    salvar_livros_json,
)

from services.interface import (
    aguardar_usuario,
    limpar_tela,
    mostrar_menu,
    mostrar_titulo
)



dados_json = ler_livros_json()

livros = converter_json_para_livros(dados_json)

mostrar_titulo()

while True:

    limpar_tela()

    mostrar_titulo()
    mostrar_menu()

    opcao = input()

    if opcao == "0":
        print("PROGRAMA FINALIZADO!")
        break

    elif opcao == "1":
        listar_livros(livros)
        aguardar_usuario()

    elif opcao == "2":
        resultado = obter_livro_do_usuario(livros)

        if resultado:
            resultado.mostrar_dados()
        else:
            print("Livro não encontrado.")

        aguardar_usuario()

    elif opcao == "3":
        cadastrar_livro(livros)
        aguardar_usuario()

    elif opcao == "4":
        remover_livro(livros)
        aguardar_usuario()

    elif opcao == "5":
        resultado = obter_livro_do_usuario(livros)

        if resultado is not None:
            resultado.emprestar()
            dados = converter_livros_para_json(livros)
            salvar_livros_json(dados)
        else:
            print("Livro não encontrado.")

        aguardar_usuario()

    elif opcao == "6":
        resultado = obter_livro_do_usuario(livros)

        if resultado is not None:
            resultado.devolver()
            dados = converter_livros_para_json(livros)
            salvar_livros_json(dados)
        else:
            print("Livro não encontrado.")

        aguardar_usuario()

    elif opcao == "7":
        listar_livros_disponiveis(livros)
        aguardar_usuario()

    elif opcao == "8":
        listar_livros_emprestados(livros)
        aguardar_usuario()

    elif opcao == "9":
        mostrar_relatorio(livros)
        aguardar_usuario()

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

        aguardar_usuario()

    else:
        print("Opção inválida.")
