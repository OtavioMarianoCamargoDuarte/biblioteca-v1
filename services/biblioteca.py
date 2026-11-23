import json

from models.livro import Livro
from rich.table import Table
from services.interface import console


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
    criar_tabela_livros(livros, "Livros da Biblioteca")

def criar_tabela_livros(livros: list[Livro],titulo_tabela: str) -> None:
    tabela = Table(title = titulo_tabela, show_lines = True)

    tabela.add_column("Título", style = "bold cyan", min_width = 30)

    tabela.add_column("Autor", style = "bold green", min_width = 25)

    tabela.add_column("Ano", style = "bold yellow")

    tabela.add_column("Status", style = "bold magenta")

    for livro in livros:

        if livro.esta_disponivel():
            status = "✅ Disponível"
        else:
            status = "📕 Emprestado"

        tabela.add_row(livro.titulo, livro.autor, str(livro.ano), status)

    console.print(tabela, justify = "center")

def listar_livros_disponiveis(livros) -> None:
    livros_disponiveis = []

    for livro in livros:
        if livro.esta_disponivel():
            livros_disponiveis.append(livro)

    criar_tabela_livros(livros_disponiveis, "Livros Disponíveis")

def listar_livros_emprestados(livros) -> None:
    livros_emprestados = []

    for livro in livros:
        if not livro.esta_disponivel():
            livros_emprestados.append(livro)

    criar_tabela_livros(livros_emprestados, "Livros Emprestados")

def buscar_livro_por_titulo(
    livros: list[Livro],
    titulo: str,
):
    for livro in livros:
        if normalizar_texto(livro.titulo) == normalizar_texto(titulo):
            return livro

    return None

def buscar_livros_por_autor(livros: list[Livro],autor: str) -> list[Livro]:

    resultado = []

    for livro in livros:
        if normalizar_texto(livro.autor) == normalizar_texto(autor):
            resultado.append(livro)

    return resultado

def obter_livro_do_usuario(livros: list[Livro]) -> Livro | None:

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
    tabela = Table(title="Relatório da Biblioteca")

    tabela.add_column("Métrica",style="bold cyan")

    tabela.add_column("Quantidade",style="bold green")

    total_livros = len(livros)

    contador_disponiveis = 0
    contador_emprestados = 0

    for livro in livros:
        if livro.esta_disponivel():
            contador_disponiveis += 1
        else:
            contador_emprestados += 1

    tabela.add_row("Total de livros", str(total_livros))

    tabela.add_row("Disponíveis", str(contador_disponiveis))

    tabela.add_row("Emprestados", str(contador_emprestados))

    console.print(tabela)