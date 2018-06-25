# Princíos básicos de listas

# Aceitam elementos de tipos diferentes

exemplo = ['lista', 0.0, 'teste']
print(exemplo)

# Elementos são acessados utilizando índices a partir de 0

print(exemplo[0])
print(exemplo[2])

# Permite índices negativos: último é -1, penúltimo -2 e assim por diante
print(exemplo[-1])
print(exemplo[-3])

# Lista = [item1, item2,  item3, ..., itemn-1, itemn]
# Index +    0      1       2           n-2     n-1
# Index -   -n   -(n-1)  -(n-2), ...,   -2       -1

# # Permite atribuição direta de valores às posições da lista
exemplo[1] = 5
print(exemplo)


# EXEMPLOS DE MÉTODOS DE LISTAS

# # LISTAS PERMITEM ADIÇÃO DINÂMICA DE ELEMENTOS
# # INSERÇÃO NO FIM DA LISTA - APPEND

exemplo.append(5)  # Adiciona 5 ao fim da lista
exemplo.append('fim')
print(exemplo)

# # INSERÇÃO EM INDEX ESPECÍFICO - INSERT
exemplo.insert(3, 'BOB')  # insere 'BOB' no índice 3
print(exemplo)

# # ELIMINA PRIMEIRA OCORRÊNCIA DE ELEMENTO - REMOVE
exemplo.remove(5)
print(exemplo)

# # REMOVE ELEMENTO DE POSIÇÃO ESPECÍFICA - POP
# É possível com pop armazenar o valor do elemento excluído
nome = exemplo.pop(2)
print(nome)
print(exemplo)

# É possível converter outros tipos de conjuntos em listas

minha_listupla = (1, 2, 3, 'sopa')
minha_lisset = {1, 6, 'jogo'}
print(type(minha_listupla))
print(type(minha_lisset))

minha_listupla = list(minha_listupla)
minha_lisset = list(minha_lisset)
print(type(minha_listupla))
print(type(minha_lisset))
