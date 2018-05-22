# while e for
# while [condição]:
# 	[executar isso enquanto condição for True]

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
		# continue
		break
print(novo) '''

# vetor = ['''Ana''', 'Berto', "Chico", "Dani"]
# # x = 5
# # dicio = {'Nome':'Nao eh rafael', 'idade':14}

# for nome in vetor:
# 	msg = 'Seja bem vindo, {}'.format(nome)
# 	print(msg)

# Formatando strings

alunos = ['Hanna', 'Jhonatan', 'Jazz','Caio', 'Lukas','Caio']

# print('{0[0]} esta do lado de {0[1]}, que esta do lado de {0[2]}, que esta na frente do {1}'.format(alunos, 'Rafael'))
# print('{2} esta do lado de {1}, que esta do lado de {0}'.format('Hanna', "Lukas", 'Jazz'))]

# print('{1} esta do lado de {2}, que esta do lado de {0}'.format(*alunos))
# dar uma olhada em s/c/scepalas

for aluno in alunos:
	if aluno == 'Caio':
		continue
		print('OI')
	# elif aluno=='Jhonatan': 
	# 	break
	else:
		print(aluno)