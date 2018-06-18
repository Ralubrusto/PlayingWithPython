# Começando dia 3

# nome = input('Insira seu nome aqui ')
# print('Bem vindo ao dia 3 ',  nome)

# While 
 j = 1
 while j<5:
 	i = 0
 	while i<5:
 		print(i)
 		i = i+1
 		if i ==3:
 			break 		# palavra break sai do while "mais interno"
 	print('Estamos na iteração número', j)
 	j = j+1
	

# print('Acabou')

 profes = ['Ivan', 'Dartora', "Artuzi",  'Patrício', 'Elizete']
# profes = ('Ewaldo', 'Horácio', 'Odilon','Rogers')
# profes = 'ABCDE'

# print(profes)
# laço for atua sobre ITERÁVEIS (listas, tuplas, strings..)

for prof in profes:
	print(prof)
	
# prof é uma variável que vai assumindo sequencialmente o valor de cade
# elemento em um iterável

print('Este é o ultimo prof:', prof)

# Após sair do laço 'for', 'prof' estará armazenando o último elemento do iterável

# função range permite iterar sobre conjuntos de números

# for x in range(10):		# x assume valores de 0 até 9
# 	print(x)

# for x in range(1,10):		# x assume valores de 1 até 9
# 	print(x)	

for x in range(1,10, 2):	# x assume valores de 2 em 2 de 1 até 9 (1,3,5...)
	print(x)

# range(Começo, Fim+1, passo)
