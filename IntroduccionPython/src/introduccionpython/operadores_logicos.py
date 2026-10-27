#============================================================
#? AND (y): es verdad cuando todos los valores son verdaderos
print('*'*10)
print('Operador and')
a = True
b = False
print(f"{a} y {b} => {a and b}")
#? Ejemplos AND
print("Ej:")
print('''
    Para aplicar a un descuento en una tienda,
    los clientes deberian comprar 10 o mas articulos
    y ser miembros de la tienda
''')

NUM_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input('Cuantos productos compraste hoy?: '))
es_miembro = input('Eres miembro de la tienda (Si/No)?: ')
tiene_descuento = cantidad_productos >= 10 and es_miembro.strip().lower() == 'si'
print(f'Tienes acceso al descuento?: {tiene_descuento}') 

#============================================================
#? OR (o): es verdad cuando al menos unos de los valores es verdaderos
print('*'*10)
print('Operador or')
a = True
b = False
print(f"{a} o {b} => {a or b}")
#? Ejemplos AND
print("Ej:")
print('''
    Para prestar un libro a un estudiante, debe cumplir almenos
    una de las siguientes condiciones:
    1. el estudiante debe tener credencial
    2. No debe vivir a mas de 3km de distancia
''')
DISTANCIA_PERMITIDA_KM = 3
tiene_credencial = input('Cuentas con credencial de estudiante (Si/No)?: ')
distancia_vivienda = int(input('A cuantos km vives de la biblioteca?: '))
permitir_prestamo = tiene_credencial.strip().lower() == 'si' or distancia_vivienda <= DISTANCIA_PERMITIDA_KM
print(f'Eres elegible para prestamo de libros?: {permitir_prestamo}')

#============================================================
#? NOT (~): Invertimos el valor booleano
print('*'*10)
print('Operador not')
a = True
b = False
print(f"a = {a} => ~a = {not a} | b = {b} => ~b = {not b}")
print("Ej:")
print('''
para entrar a una atraccion la persona no debe ser mayor de edad
''')
MAYORIA_EDAD = 18
edad_persona = int(input('Cual es tu edad?: '))
es_mayor = edad_persona >= MAYORIA_EDAD
puede_entrar = not es_mayor
print(f'Puedes entrar a la atraccion?: {puede_entrar}')

