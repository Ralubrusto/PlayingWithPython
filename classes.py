# Classes - Orientação a Objeto

# def meus_livros(nome):
#         return [nome]

# def add_livro(livro, biblio):
#     biblio.append(livro)
#     print('Adicionei o livro {}'.format(livro))

# biblioteca = meus_livros('Rafael')
# print(biblioteca)
# add_livro('Harry Potter', biblioteca)
# add_livro('Dom Casmurro', biblioteca)
# print(biblioteca)

class Biblioteca:

    def __init__(self, nome):
        '''Funções em classes se chamam métodos'''
        self.dono = nome
        # self.liv_fav = 'Eu, Robô'
        # self.nao_li = 'Game of Thrones'
        self.livros = []
        self.address = ''

    def add_livro(self, livro):
        self.livros.append(livro)

    def set_address(self, address):
        self.address = address


x = Biblioteca('Rafael')    # x é uma instância 
                    # da classe Biblioteca
print(x.dono)
print(x.livros)
x.add_livro('123')
print(x.livros)
print(x.address)
x.set_address('Jd Américas')
print(x.address)

# x = ['Rafael', 'HP', '123']
