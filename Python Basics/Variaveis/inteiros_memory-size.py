# Propriedade interessante quanto ao tamanho dos inteiros
import sys

# Python não impõe limite para tamanho de inteiros.
# O limite é memória do computador em que se programa

var_little = 255
var_medium = var_little ** 10
var_big = var_medium ** 10
var_huge = var_little ** var_little

print(var_little)  # 3 dígitos
print(var_medium)  # 25 dígitos
print(var_big)     # 241 dígitos
print(var_huge)    # 614 dígitos

# A função getsizeof do módulo sys retorna o espaço ocupado em bytes

print(sys.getsizeof(var_little))  # 14
print(sys.getsizeof(var_medium))  # 24
print(sys.getsizeof(var_big))   # 120
print(sys.getsizeof(var_huge))  # 144

