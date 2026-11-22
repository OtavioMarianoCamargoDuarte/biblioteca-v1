class Livro:
    def __init__(self, titulo: str, autor: str, ano: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def mostrar_dados(self) -> None:
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")