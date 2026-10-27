print('***  Calcular el area y perimetro de un rectangulo ***')
'''
#? Formulas
#! area = base x altura
#! perimetro = 2 x (base + altura)
'''
base = float(input('Digite el valor de la base del rectangulo: '))
altura = float(input('Digite la altura del rectangulo: '))

area = base * altura
perimetro = 2 * (base + altura)
print(f'''
base: {base}
altura: {altura}
Resultado:
    area = {area}
    perimetro = {perimetro}
''')