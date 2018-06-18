# Funções com argumentos nomeados, 
# e argumentos padrão
# minhasfuncoes.py = nome do arquivo

def saudacao(nome, tipo='comum'):
    if tipo=='comum':
        print('Olá {}'.format(nome))
        # cout << 'olá' << nome;
    elif tipo=='top':
        print('Salve, salve {} '.format(nome))
    else:
        print('Po {}...  passe um tipo que existe'
            .format(nome))

def tchau():
    '''Obj: escrever tchau
    equivalente a print('Tchaaaaau')
    '''
    print('Tchaaaaaaau')
