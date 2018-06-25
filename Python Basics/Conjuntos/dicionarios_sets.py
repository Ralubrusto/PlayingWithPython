meu_set = {10, 27, 38}  # Set - chaves {}
print(type(meu_set))  # <class 'set'>

meu_dict = {'Chave1': 1, 'Chave2': 2}  # Dicionário - {chave : valor}
print(type(meu_dict))  # <class 'dict'>

# Sets não aceitam elementos repetidos. Útil para remover duplicatas.
# Dicionários não aceitam chaves repetidas, mas não se importa com valores

# Adicionando elementos a sets

set_nomes = {'Alynne', 'Pablo', 'Wellington'}
print(set_nomes)
set_nomes.add('Rafael')
print(set_nomes)

# Note como sets não mantém a ordem dos elementos igual à original
# Isso ocorre porque sets não se preocupam com a posição dos elementos, apenas com os elementos em si
# Por isso sets não permitem indexação. A linha a seguir gera um erro
# print(set_nomes[0])




# # Aceitam algumas das funções usadas em listas e tuplas
# Função LEN()

print(len(meu_set))  # 3

print(len(meu_dict))  # 2

# Funções MAX() e MIN() - para conjuntos exclusivamente numéricos

print(max(meu_set))


