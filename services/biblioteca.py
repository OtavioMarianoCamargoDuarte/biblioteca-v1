import json

from models.livro import Livro


def ler_livros_json() -> list:
    with open("data/livros.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados

def salvar_livros_json(dados: list) -> None:
    with open("data/livros.json", "w", encoding="utf-8") as arquivo:
        json.dump(
            dados,
            arquivo,
            ensure_ascii=False,
            indent=4
        )

def listar_livros(livros) -> None:
    print("======== LIVROS ========")
    print()
    for livro in livros:
        livro.mostrar_dados()
        print()
    print("========================")

def listar_livros_disponiveis(livros) -> None:
    print("===== Livros disponíveis =====")

    for livro in livros:
        if livro.esta_disponivel():
            livro.mostrar_dados()
            print()

def listar_livros_emprestados(livros) -> None:
    print("===== Livros emprestados =====")

    for livro in livros:
        if not livro.esta_disponivel():
            livro.mostrar_dados()
            print()

def buscar_livro_por_titulo(
    livros: list[Livro],
    titulo: str,
):
    for livro in livros:
        if normalizar_texto(livro.titulo) == normalizar_texto(titulo):
            return livro

    return None

def obter_livro_do_usuario(livros: list[Livro]):
    titulo = input("Digite o titulo do livro: ")
    resultado = buscar_livro_por_titulo(livros, titulo)
    return resultado

def cadastrar_livro(livros) -> None:
    print("====== CRIANDO NOVO LIVRO ======")
    novo_titulo = input("Título: ").strip()
    novo_autor = input("Autor: ").strip()
    novo_ano = int(input("Ano: "))

    novo_livro = Livro(novo_titulo, novo_autor, novo_ano)

    livros.append(novo_livro)
    dados = converter_livros_para_json(livros)
    salvar_livros_json(dados)

def remover_livro(livros) -> None:
    print("====== REMOVENDO UM LIVRO ======")
    buscador_titulo = input("Digite o nome do livro: ")
    titulo_encontrado = False

    for livro in livros:
        if normalizar_texto(buscador_titulo) == normalizar_texto(livro.titulo):
            titulo_encontrado = True
            print("Livro encontrado.")
            livros.remove(livro)

            dados = converter_livros_para_json(livros)
            salvar_livros_json(dados)

            print("Livro removido com sucesso.")
            break

    if not titulo_encontrado:
        print("Livro não foi encontrado em nossa biblioteca.")

def normalizar_texto(texto: str) -> str:
    return texto.lower().strip()

def mostrar_menu() -> None:
    print("========== MENU ==========")
    print("[1] - Listar livros")
    print("[2] - Buscar livro")
    print("[3] - Cadastrar livro")
    print("[4] - Remover livro")
    print("[5] - Emprestar livro")
    print("[6] - Devolver livro")
    print("[7] - Listar livros disponíveis")
    print("[8] - Listar livros emprestados")
    print("[9] - Mostrar relatório")
    print("[0] - Sair")
    print("==========================")

def converter_livros_para_json(livros: list[Livro]) -> list:
    dados = []

    for livro in livros:
        dados.append(livro.para_dicionario())
    return dados

def converter_json_para_livros(dados_json: list) -> list:
    dados = []

    for dado in dados_json:
        dados.append(Livro(dado["titulo"], dado["autor"], dado["ano"], dado["disponivel"]))
    return dados

def mostrar_relatorio(livros) -> None:
    print("===== Relatório =====")

    total_livros = len(livros)

    contador_disponiveis = 0
    contador_emprestados = 0

    for livro in livros:
        if livro.esta_disponivel():
            contador_disponiveis += 1
        else:
            contador_emprestados += 1

    print(f"Total de livros: {total_livros}")
    print(f"Disponíveis: {contador_disponiveis}")
    print(f"Emprestados: {contador_emprestados}")
    print("====================")