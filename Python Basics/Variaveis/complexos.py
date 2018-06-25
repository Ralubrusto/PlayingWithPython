# Definição de números complexos:
x_complex = 5 + 5j
print(x_complex)

x_complex = complex(3, 4)  # complex(real, imag)
print(x_complex)

# Método conjugate: retorna o complexo conjugado do número

x_conjug = x_complex.conjugate()
print(x_conjug)

# As partes real e imaginária são acessadas pelos atributos

print(x_complex.real)  # Float: parte real
print(x_complex.imag)  # Float: parte imaginária

# Exemplos módulo cmath - algumas operações simples com complexos

import cmath

# Função polar: recebe um complexo e retorna uma tupla com módulo e fase em radianos
x_complex_pol = cmath.polar(x_complex)
print(x_complex_pol)  # (módulo, fase)


# Função rect: recebe uma tupla cocm módulo e fase e retorna um complexo na forma retangular
x_complex_rect = cmath.rect(x_complex_pol[0], x_complex_pol[1])
print(x_complex_rect)

# Função abs() também retorna módulo de números complexos
print(abs(x_complex))
