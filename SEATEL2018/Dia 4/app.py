import minhasfuncoes as mf
from mathseatel import medias

nome = input('Digite seu nome para receber oi: ')
tipo = input('Digite top se você for top: ')


mf.saudacao(nome, tipo)

nota1 = float(input('Digite sua nota 1: '))
nota2 = float(input('Digite sua nota 2: '))

mm = medias(nota1, nota2)
print('Sua media pode ser', mm[0], 'ou', mm[1])

mf.tchau()
