meu_dict = {'Chave1': 'Valor1', 'Chave2': 'Valor2'}  # Dicionário - {chave : valor}
print(type(meu_dict))  # <class 'dict'>

# Dicionários são conjuntos de pares chave-valor
# Para acessar elementos de dicionários utilizamos as chaves

print(meu_dict['Chave1'])  # Valor1

# Adicionando elementos a dicionários
notas = {'Fulano': 8.5, 'Cicrano': 6.5}
print(notas)
notas['Beltrano'] = 10.0
print(notas)

# Dicionários não aceitam chaves repetidas, mas não se importam com valores repetidos

print(len(meu_dict))  # 2

print(max(notas))