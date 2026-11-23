from services.biblioteca import (
    buscar_livros_por_autor,
    cadastrar_livro,
    converter_json_para_livros,
    converter_livros_para_json,
    criar_tabela_livros,
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
    mostrar_erro,
    mostrar_aviso,
    mostrar_menu,
    mostrar_titulo,
)

dados_json = ler_livros_json()

livros = converter_json_para_livros(dados_json)

while True:

    limpar_tela()

    mostrar_titulo()
    mostrar_menu()

    opcao = input()

    if opcao == "0":
        mostrar_aviso("PROGRAMA FINALIZADO")
        break

    elif opcao == "1":

        limpar_tela()
        mostrar_titulo()

        listar_livros(livros)

        aguardar_usuario()

    elif opcao == "2":

        limpar_tela()
        mostrar_titulo()

        resultado = obter_livro_do_usuario(livros)

        if resultado:
            criar_tabela_livros(
                [resultado],
                "Livro Encontrado"
            )
        else:
            mostrar_erro("Livro não encontrado.")

        aguardar_usuario()

    elif opcao == "3":

        limpar_tela()
        mostrar_titulo()

        cadastrar_livro(livros)

        aguardar_usuario()

    elif opcao == "4":

        limpar_tela()
        mostrar_titulo()

        remover_livro(livros)

        aguardar_usuario()

    elif opcao == "5":

        limpar_tela()
        mostrar_titulo()

        resultado = obter_livro_do_usuario(livros)

        if resultado is not None:
            resultado.emprestar()

            dados = converter_livros_para_json(livros)
            salvar_livros_json(dados)

        else:
            mostrar_erro("Livro não encontrado.")

        aguardar_usuario()

    elif opcao == "6":

        limpar_tela()
        mostrar_titulo()

        resultado = obter_livro_do_usuario(livros)

        if resultado is not None:
            resultado.devolver()

            dados = converter_livros_para_json(livros)
            salvar_livros_json(dados)

        else:
            mostrar_erro("Livro não encontrado.")

        aguardar_usuario()

    elif opcao == "7":

        limpar_tela()
        mostrar_titulo()

        listar_livros_disponiveis(livros)

        aguardar_usuario()

    elif opcao == "8":

        limpar_tela()
        mostrar_titulo()

        listar_livros_emprestados(livros)

        aguardar_usuario()

    elif opcao == "9":

        limpar_tela()
        mostrar_titulo()

        mostrar_relatorio(livros)

        aguardar_usuario()

    elif opcao == "10":

        limpar_tela()
        mostrar_titulo()

        autor = input("Digite o nome do autor: ")

        resultado = buscar_livros_por_autor(
            livros,
            autor
        )

        if resultado:
            criar_tabela_livros(
                resultado,
                "Livros do Autor"
            )
        else:
            mostrar_erro("Autor não encontrado.")

        aguardar_usuario()

    else:

        mostrar_erro("Opção inválida.")

        aguardar_usuario()