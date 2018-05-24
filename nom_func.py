# Funções com argumentos nomeados, 
# e argumentos padrão
# nom_func.py = nome do arquivo

def saudacao(nome, tipo):
    if tipo=='comum':
        print('Olá {}'.format(nome))
        # cout << 'olá' << nome;
    elif tipo=='top':
        print('Salve, salve {} '.format(nome))
    else:
        print('Po {}...  passe um tipo que existe'
            .format(nome))
