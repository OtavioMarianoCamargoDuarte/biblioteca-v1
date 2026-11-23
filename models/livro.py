class Livro:
    def __init__(self, titulo: str, autor: str, ano: int, disponivel: bool = True) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel

    def mostrar_dados(self) -> None:
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")
        
        if self.disponivel:
            print("Status: Disponível")
        else:
            print("Status: Emprestado")

    def para_dicionario(self) -> dict:
        return {
            "titulo" : self.titulo,
            "autor" : self.autor,
            "ano" : self.ano,
            "disponivel" : self.disponivel
        }

    def emprestar(self) -> None:
        if self.disponivel:
            self.disponivel = False
            print(f"Livro: {self.titulo} emprestado com sucesso.")
        else:
            print("Livro já está emprestado.")

    def devolver(self) -> None:
        if not self.disponivel:
            self.disponivel = True
            print(f"Livro: {self.titulo} devolvido com sucesso.")
        else:
            print("Livro não foi emprestado.")

    def esta_disponivel(self) -> bool:
        return self.disponivel