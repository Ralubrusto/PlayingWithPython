# Tipos embutidos (built-in) do Python
# Função type retorna o tipo da variável passada como argumento

#         TIPOS NUMÉRICOS

x = True  # booleano (True or False)
print(type(x))  # <class 'bool'>

y = 1  # inteiro
print(type(y))  # <class 'int'>

z = 1.0  # float - difere do int pela presença do ponto decimal
print(type(z))  # <class 'float'>

c = 1 + 5j  # complexo
# Adicionar 'j' após um número (sem espaços entre 'j' e o número)
# faz com que ele seja interpretado como um número complexo
print(type(c))  # <class 'complex'>
