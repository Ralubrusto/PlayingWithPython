# Alguns exemplos de usos de floats

# É possível usar notação científica
eps = 8.854e-12
googol = 10e100

print(eps)  # 8.854e-12
print(googol)  # 1e+101

# Função round()
# Arredonda float para uma dada quantidade de casas decimais

pi = 3.14159265

print(round(pi))  # O padrão é arredondar para inteiro
print(round(pi, 2))  # 3,14
print(round(pi, 4))  # 3,1416

# # Função float()
# Converte variáveis para float, se possível

# Se for um int - apenas acrescenta ponto decimal

print(float(55))
print(float(-126))

# Se for bool: True = > 1.0; False => 0.0

print(float(True))
print(float(False))
