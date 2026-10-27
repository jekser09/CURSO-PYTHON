'''
Tipos basicos:
int (Integer): Numeros Enteros -> 8
float (Float): Numeros Decimales -> 8.5
str (String): Cadenas de texto -> "Hola mundo desde el año 1998 :D"
bool (Boolean): Verdad o falsedad -> True/False
'''
#? Enteros
numero_entero = 1
numero_entero = -1

#? Decimales
numero_decimal = 10
numero_decimal = 10.0
numero_decimal = -10.0

#? Strings
cadena_caracteres = 'Saludos 33 veces'
cadena_caracteres = '33'

#? Booleans
es_verdad = True
es_falso = False

#? Listas
alumnos = ["Johand","Laura","Rocio"]

#? Tuplas (Son inmutables)
alumnos = ("Johand","Laura","Rocio")

#? Set (Datos unicos, no se puede repetir)
cedulas = {"1018506713","52310760","1010013317"}

#? Diccionarios (Datos con una llave que los identifica)
personaje = {
    "Nombre":"Super man",
    "Debilidad":"Criptonita",
    "Poderes":["Vision de calor","Volar","Aliento frio","Super velocidad","Super fuerza"],
    "Edad":33,
    "Salud":100
}

#Como podemos saber de que tipo es una variable? -> Funcion type() nativa de python
print(type(numero_entero))
print(type(numero_decimal))
print(type(cadena_caracteres))
print(type(es_verdad))

#? Conversion de tipos de datos
numero_texto = "50"
numero_int = int(numero_texto)
total = numero_int + 10
print(f"El total es {total}")

'''
#? Que es bool en python a parte de ser la clase para datos booleanos
#? Si no que tambien nos sirve para comprobar datos Truthy y Falsy que son datos
#? que por defecto nos arrojan un valor verdadero o falso
'''
#! Datos Falsy (Representa "nada o vacio")
#! 0 / 0.0 => False
#! "" => False
#! [] => False
#! None => False
#* Datos Truthy (Representa "Existe") 
#* 1, -5, 3.14 => True
#* "Hola", " " => True
#* [0] => True
print("Datos Falsy")
print(f'Numero 0 => {bool(0)}')
print(f'Numero 0.0 => {bool(0.0)}')
print(f'String vacio "" => {bool("")}')
print(f'Lista vacia [] => {bool([])}')
print(f'Tupla vacia [] => {bool(())}')
print(f'Diccionario/set vacio {"{}"} => {bool({})}')
print(f'Dato None "" => {bool(None)}')
print("Datos Truthy")
print(f'Numero 1 => {bool(1)}')
print(f'Numero -3.0 => {bool(-3.0)}')
print(f'String "Hola" => {bool("Hola")}')
print(f'Lista [5] => {bool([5])}')
print(f'Tupla (4,) => {bool((4,))}')
print(f'Diccionario/set {{"dato":8}} => {bool({"dato":8})}')
