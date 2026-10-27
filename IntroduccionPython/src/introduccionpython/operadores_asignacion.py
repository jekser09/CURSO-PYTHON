
#? Operdores de asignacion
numero = 5 #* Estandar
print(f'Numero = {numero}')
numero, texto, verdad = 10, 'Hola Python', True #* Asignacion multiple
print(f'Numero = {numero}, texto = {texto}, verdad = {verdad}')
variable1 = variable2 = variable3 = 'Mismo valor' #* Asignacion encadenada
print(f'variable1 = {variable1}, variable2 = {variable2}, variable3 = {variable3}')

#? Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f'x = {x}, y = {y}')
x, y = y, x
print(f'x = {x}, y = {y}')

#? Recibir multiples valores de la entrada del usuario
nombre, apellido = input('Ingrese su nombre y apellido separados por coma: ').split(',')
print(f'Nomnre: {nombre} Apellido: {apellido}')

#? Operadores de asignacion compuesto
suma = 0
suma += 1
print(f'Suma: {suma}')
resta = 0
resta -= 1
print(f'Resta: {resta}')
multi = 10
multi *= 2
print(f'Multiplicacion: {multi}')
potencia = 10
potencia **= 3
print(f'Potencia: {potencia}')
div = 10
div /= 2
print(f'Division: {div}')
div_int = 10
div_int //= 2
print(f'Division entera: {div_int}')
div_mod = 10
div_mod %= 2
print(f'Division modulo: {div_mod}')
