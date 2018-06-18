# Listas, tuplas, dicionarios e sets

# lista
x = []
print(x)		# []
x.append(1)		# Adiciona um elemento no fim da lista
print(x)		# [1]
x.insert(0,-15)		# Adiciona o elemento -15 no índice 0 da lista
print(x)		# [-15, 1]

# Numeração de índices segue o padrão de C: 0 para o primeiro
# Possui indexação negativa tbm
# x = [10, 11, 12, 13, 14]
#       0   1   2   3   4
#      -5  -4  -3  -2  -1

# elemento -1 é sempre o último

# Tupla
y=(5,6,4)	# É imutavel, não permite alteração direta de seus elementos

# Sets
meu_set = {1,2,3} 	# Conjuntos matemáticos
seu_set = {4,5,1}

if 1 in meu_set:
	print('Deu boa')
	
meu_set.add(1)	# Não repete elementos, permanece igual a {1,2,3}
inter_set = meu_set & seu_set # intersecção {1}
union_set = meu_set | seu_set # união {1, 2, 3, 4, 5}

#Dicionario

notas = {'Fis':9.5, 'Qui':8.0, 'Mat':5.0}
print(notas['Fis'])		#imprime 9.5
print(notas['Qui'])		#imprime 8.0
notas['Por'] = 7.0		#adicionar chave "Por"
						# com valor 7.0
	
