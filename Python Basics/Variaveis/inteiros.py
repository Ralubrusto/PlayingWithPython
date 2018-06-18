# Alguns exemplos de usos de inteiros

# Algumas funções retornam inteiros diretamente

# # Função int()
# Converte o float/bool para inteiro

# Se for bool: False => 0, True => 1
print(int(False))  # 0
print(int(True))  # 1

# Se for float, trunca a parte decimal
print(int(3.0001))  # 3
print(int(5.5639))  # 5
print(int(9.9999))  # 9


# # Função pow()
# Equivalente à sintaxe **

res = pow(2, 5)  # equivale a  2 ** 5
print(res)  # 32

res = pow(2, 5, 10)  # argumento opcional - equivale a (2 ** 5) % 10
print(res)  # 2

# # Função divmod()
# Retorna quociente e resto de uma divisão inteira

D, R = divmod(47, 5)  # equivale a 47 // 5, 47 % 5
print(D, R)  # 9 2

