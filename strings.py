# STRING!!!!!!!!!!!!!!

idade = input('Qual a sua idade? ')

try:
	idade = int(idade)
except ValueError:
	print('Você não merece ver o filme!')
else:
	idade = int(input('Vamos tentar de novo?'))
# idade = int(idade)
# INput sempre retorna string

if idade >= 18:
	print("Você pode assistir Deadpool")
else:
	print('Espere sair no torrent')
