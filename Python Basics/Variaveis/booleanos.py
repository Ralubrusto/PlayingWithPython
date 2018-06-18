# Alguns exemplos de uso de booleanos

# O resultado de comparações lógicas (maior, menor, igual...)
# É sempre booleano e pode ser atribuído a variáveis

idade = 15
is_adult = idade >= 18
print('É adulto: ', is_adult)    # False

# É possível encadear comparações lógicas
is_teenager = 12 <= idade <= 18
# Equivalente a 12 <= idade and idade <=18
print('É adolescente: ', is_teenager)

print()
# Equivalência de outros tipos para booleano
# Conversão explícita: usando função bool()

# Float e int
# Se nulos equivalem a False, do contrário equivalem a True
x = 5.6985
x_bool = bool(x)
print('x:', x)
print('x_bool:', x_bool)

y = 0
y_bool = bool(y)
print('y:', y)
print('y_bool:', y_bool)


print()
# Conjuntos: listas, tuplas, sets, dicionários...
# Se vazios equivalem a False, do contrário equivalem a True
lista = []
lista_bool = bool(lista)
print('lista:', lista)
print('lista_bool:', lista_bool)

tupla = (1, 2, 3)
tupla_bool = bool(tupla)
print('tupla:', tupla)
print('tupla_bool:', tupla_bool)

print()
# Conversão implícita para booleano
# Variáveis são convertidas implicitamente para booleano quando usadas
# como condição em blocos if-else ou em loops

vizinhos = ['Ana', 'Bruno', 'Carla']
# vizinhos = []

if vizinhos:
    print('Eu tenho vizinhos!')
else:
    print('Eu não tenho vizinhos..')
