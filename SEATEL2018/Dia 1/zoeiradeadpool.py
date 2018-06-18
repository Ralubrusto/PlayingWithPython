# STRING!!!!!!!!!!!!!!

idade = input('Qual a sua idade? ')	# Essa função captura dados do teclado até o usuário teclar ENTER
					# Sempre retorna uma string

try:
    idade = int(idade)
except:
    print('Você não merece ver o filme!')
	
# idade = int(idade)
# INput sempre retorna string

if idade >= 18:
    print("Você pode assistir Deadpool")
else:
    print('Espere sair no torrent')
