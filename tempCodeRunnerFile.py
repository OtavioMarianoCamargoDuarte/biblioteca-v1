elif opcao == "5":

        limpar_tela()
        mostrar_titulo()

        resultado = obter_livro_do_usuario(livros)

        if resultado is not None:

            if resultado.emprestar():
                mostrar_sucesso("Livro emprestado com sucesso.")
                salvar_biblioteca(livros)

            else:
                mostrar_erro("Livro já está emprestado.")

        else:
            mostrar_erro("Livro não encontrado.")

        aguardar_usuario()