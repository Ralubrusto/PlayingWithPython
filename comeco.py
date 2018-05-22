# Variaveis em Python
# Sublime Text - editor de texto recomendado

#Python não exige declaração prévia de variáveis, basta atribuir um valor e começar a usar.
#Python não exige nenhum caracter de fim de linha. C exige ';', por exemplo

#COMENTÁRIOS COMEÇAM COM HASHTAG!!!

x = 15		# Inteiro
y = 15.0	# Float
z = True	# Booleano

print(x)		# Função que imprime na tela, equivalente ao cout do C
print(type(x))		# Imprimindo na tela o tipo da variável x (<class 'int'> - corresponde a inteiro)
print('Este é o x: ', x) # Função print aceita vários argumentos e imprime todos em sequência separados por espaços

#Condicionais
x = 6
y = 5
		
# Repare na sintaxe
# if [condicao] :
# ....o bloco que vêm abaixo do IF deve ser INDENTADO, alinhado no mínimo 2 (4 por padrão) espaços à direita

if x>10:
    print('x é maior do que 10')
    print('Este é o y: ', y)
elif x>5:				# elif é uma abreviação para else if
    print('x é maior do que 5  e menor que 10')
else:
    print('x não é maior do que 10')
    y = 150
	
# repare como a indentação deixou bonito o código :D além de mais organizado
print('Será mesmo esse o y?', y)
