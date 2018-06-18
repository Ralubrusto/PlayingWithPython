# exercicio 2

class Pessoa:
    def __init__(self, batismo):
        self.nome = batismo
        self.amigos = []
        # Criar uma propriedade nome e uma lista

    def ola(self):
        print('Olá! Eu sou {}'.format(self.nome))
        # Escrever uma saudação com seu self.nome
    def add_friend(self, migx):
        self.amigos.append(migx)
        print('Adicionei o amigo', migx)
        # Adicionar um amigo à lista de amigos
        # Dica: use append ;)
    def show_friends(self):
        for amigo in self.amigos:
            print(amigo)
        # imprime na tela sua lista de amigos

variavel = Pessoa('Umberto')
variavel.ola()
variavel.add_friend('Doisberto')
variavel.add_friend('Doisberto')
variavel.add_friend('Doisberto')
variavel.add_friend('Doisberto')
variavel.add_friend('Doisberto')
variavel.show_friends()
# variavel2 = Pessoa('Doisberto')
# variavel2.ola()
# variavel2.add_friend('John')
# variavel2.show_friends()
