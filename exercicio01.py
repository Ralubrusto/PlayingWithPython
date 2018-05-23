# Pratica Python 01

# Passo#01 - 	Criar uma lista 
#				com 5 amigos (strings)
# Passo#02 - 	Pedir ao usuario que digite 
#				um nome (salve a resposta ;) )
# Passo#03 - 	Verificar se o nome está
#				na lista de amigos
# Se estiver, imprima uma saudação bem humorada
# Se não, convide a pessoa para ser sua amiga

# -----NOVOS PASSOS!!!!!!!-------#

# Passo#04 - 	Criar uma lista de novos amigos
# 				PS: a lista deve ser vazia
# Passo#05 - 	Adicionar o novo amigo à lista
# Passo#06 - 	Verificar se ele está na lista
# Passo#07 - 	"Você é meu novo amigo!!"

amigos = ('Umberto', 'Doisberto', 'Treisberto',
	'Quartoberto', "Cincoberto")
nome = input('Digite seu nome: ')
if nome in amigos:
	print('Você já é meu amigão!!!!!')
else:
	print('Você pode ser meu amiguinho!!!')
	novos_amigos = []
	novos_amigos.append(nome)
	if nome in novos_amigos:
		print('Você já é meu novo amiguinho!')
		print(novos_amigos)		






