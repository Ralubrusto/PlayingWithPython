# Informações do sistema acerca dos floats
import sys

max_float, max_exp, max_10_exp, min_float, \
 min_exp, min_10_exp, dig, mant_dig, \
 epsilon, radix, rounds = sys.float_info

# # # Informações úteis:

print('Maior float que Python consegue representar')
print('Max:', max_float, '\n')

print('Menor float que Python consegue representar')
print('Min:', min_float, '\n')

print('Base do sistema de numeração')
print('Radix:', radix, '\n')

print('Número de casas decimais que se pode representar')
print('Dig:', dig, '\n')

print('Diferença entre 1 e o menor float representável maior do que 1')
print('Epsilon:', epsilon, '\n')

print('Maior inteiro X tal que [radix ** (X-1)] é um float representável')
print('Max_exp:', max_exp, '\n')

print('Menor inteiro X tal que [radix ** (X-1)] é um float representável')
print('Min_exp:', min_exp, '\n')

print('Maior inteiro X tal que [10 ** X] é um float representável')
print('Max_10_exp:', max_10_exp, '\n')

print('Menor inteiro X tal que [10 ** X] é um float representável')
print('Min_10_exp:', min_10_exp, '\n')

print('''Modo de arredondamento:
    Se -1- Indeterminado
    Se 0 - Para mais próximo de 0
    Se 1 - Para o mais peóximo (padrão)
    Se 2 - Para o mais positivo
    Se 3 - Para o mais negativo''')
print('Rounds:', rounds, '\n')
