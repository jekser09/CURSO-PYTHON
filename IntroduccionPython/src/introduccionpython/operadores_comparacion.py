
#? Operadores de igualdad
a, b = 5, 5
igualdad = a == b
diferencia = a != b
print(f'{a} = {b} ? {igualdad}')
print(f'{a} =/= {b} ? {diferencia}')
a, b = 5, 7
igualdad = a == b
diferencia = a != b
print(f'{a} = {b} ? {igualdad}')
print(f'{a} =/= {b} ? {diferencia}')

#? Menor
a, b = 5, 3
menor = a < b
print(f'{a} < {b} ? {menor}')
a, b = 3, 3
menor = a < b
print(f'{a} < {b} ? {menor}')
#? Menor o igual
a, b = 3, 5
menor = a <= b
print(f'{a} <= {b} ? {menor}')
a, b = 3, 3
igual = a <= b
print(f'{a} <= {b} ? {igual}')
a, b = 4, 3
diferente = a <= b
print(f'{a} <= {b} ? {diferente}')

#? Mayor
a, b = 5, 3
mayor = a > b
print(f'{a} > {b} ? {mayor}')
a, b = 3, 3
mayor = a > b
print(f'{a} > {b} ? {mayor}')
#? Mayor o igual
a, b = 3, 5
mayor = a >= b
print(f'{a} >= {b} ? {mayor}')
a, b = 3, 3
igual = a >= b
print(f'{a} >= {b} ? {igual}')
a, b = 4, 3
diferente = a >= b
print(f'{a} >= {b} ? {diferente}')
