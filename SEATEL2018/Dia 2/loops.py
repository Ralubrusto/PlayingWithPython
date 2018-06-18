# while e for
# while [condição]:
# 	[executar isso enquanto condição for True]

# Quando abrimos e fechamos 3 aspas criamos uma string multi-linha
# Útil para criar textos em variáveis ou para criar comentários de várias linhas

'''vetor = [1,2,'PC',3,4,]
novo = []
cont = 0
print(novo)
while cont<len(vetor):
	if type(vetor[cont]) == int:
		novo.append(vetor[cont]**4)
		cont +=1
	else:
		# cont +=1
		break		# Palavra Break é especial pois faz sair do Loop
print(novo) '''

# vetor = ['''Ana''', 'Berto', "Chico", "Dani"]
# # x = 5
# # dicio = {'Nome':'Nao eh rafael', 'idade':14}

# Laço 'for':
# itera sobre os elementos de um iterável, que pode ser uma lista, tupla, dicionário, string...
# iteráveis são, em geral, tipos que possuem mais de um elemento discernível entre eles

# for nome in vetor:
# 	msg = 'Seja bem vindo, {}'.format(nome)		# Formatação de Strings
# 	print(msg)					# Método format insere variáveis em meio a strings


alunos = ['Hanna', 'Jhonatan', 'Jazz', 'Fulano', 'Caio', 'Lukas','Caio']

# print('{0[0]} esta do lado de {0[1]}, que esta do lado de {0[2]}, que esta na frente do {1}'.format(alunos, 'Rafael'))
# print('{2} esta do lado de {1}, que esta do lado de {0}'.format('Hanna', "Lukas", 'Jazz'))]
# print('{} esta do lado de {}, que esta do lado de {}'.format('Hanna', "Lukas", 'Jazz'))]

# print('{1} esta do lado de {2}, que esta do lado de {0}'.format(*alunos))

for aluno in alunos:
	if aluno == 'Fulano':
		continue		# Palavra usada em laços 'for'
					# continue faz o laço ignorar a iteração e partir para a próxima
	# elif aluno=='Jhonatan': 
	# 	break
	else:
		print(aluno)
