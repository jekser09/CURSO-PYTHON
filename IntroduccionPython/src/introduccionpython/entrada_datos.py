#? Entrada de datos por consola
'''
nombre = input("Digite su nombre: ") #! Esta funcion devuelve siempre un str
edad = input("Por favor digite su edad: ") #! Entonces necesitamos hacer la respectiva conversion
edad = int(edad)
print(f"Hola {nombre} bienvenido")
print(f"Tienes {edad} años, te faltan {30 - edad} para los 30 :O")
'''

print("***Sistema empleados***")
nombre_empleado = input('Nombre del empleado: ')
edad_empleado = int(input('Edad del empleado: '))
salario_empleado = float(input('Salario del empleado: '))
es_jefe_departamento = input("Es jefe de departamento? (Si/No): ")

#? convertir a bool es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == 'si'

print("="*10)
print("Datos del empleado")
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {salario_empleado:.2f}')
print(f'Es jefe de departamento?: {es_jefe_departamento}')
print("="*10)
