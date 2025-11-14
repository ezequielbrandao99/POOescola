class biblioteca:
    def __init__(self, titulo = None, autor = None, capitulos = None):

        self.titulo = titulo
        self.autor = autor
        self.capitulos = capitulos

    def mostrar_detalhes():
        
        print('-----INFORMAÇÕES DO LIVRO-----')
        
class livro(biblioteca):
    def __init__(self, titulo=None, autor=None, capitulos=None):

        if titulo is None:
            titulo = str(input('Digite o titulo do livro: '))

        if autor is None:
            autor = str('Digite o nome do autor do livro: ')

        if capitulos is None:
            capitulos = str(input('Digite quantos capitulos tem o livro: '))

        super().__init__(titulo, autor, capitulos)

    def mostrar_detalhes():
        base = super().mostrar_detalhes()

        print('-----INFORMAÇÕES DO LIVRO-----')
        print('o nome do livro é {self.titulo}') 

livro()