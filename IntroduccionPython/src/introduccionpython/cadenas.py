'''
Que es un String?
Es un texto que python interpreta como un conjunto de caracteres
Las cadenas en python son inmutables
'''
#Comillas simples (Uso comun)
fruta = 'Manzana'
#Comillas dobles (Funciona igual)
color = "Rojo"
#3. Por que existen las dos? Para poner comillas dentro de texto
cita = 'El maestro dijo: "Estudien mucho"'
libro = "Lei el libro 'El principito'"
print(cita)
print(libro)

#Cadenas multilinea se definen con triple comilla doble o simple

#Ejemplo 1: Menu restaurante
menu_dia = """
MENU DEL DIA
-----------------------------
1. Tacos al pastor
2. Enchiladas verdes
3. Quesadillas
"""
print(menu_dia)
#Ejemplo 2: Redactar un correo
correo = """
Hola equipo:
Les aviso que ya termine la terea de python
El codigo funciona perfecto!
"""
print(correo)

#Caracteres especiales
#Escapar " y '
texto = "Ella dijo \"hola\" al entrar"
print(texto)
texto = 'El libro es del año \'1998\''
print(texto)
#salto de liea
texto = "Carlos\nCastro"
print(texto)
#tabulacion
texto = "Gianfranco\tSanchez"
print(texto)
#Evitar que python interprete \ como caracter especial
texto = "c:\\usuario\\Documentos"
print(texto)
#Cadenas cruda (raw string) colocar r al inicio del string
texto = r"c:\usuario\Documentos"
print(texto)
#Concatenacion de cadenas, unir dos o mas cadenas para formar una sola
texto = "Hola " + "Mundo"
print(texto)
#F-strings: Inyecta valores directamente en el string
nombre = "Johand"
texto = f"Buenos dias {nombre} como estas?"
print(texto)

#? Funciones con cadenas

#? Extraer un caracter
texto = "Esteban"
print(f"Extraer nel primer caracter de {texto} -> {texto[0]}")

#? Slicing de cadenas (extraer una subcadena) texto[inicio:fin:paso]
texto = "1998-10-15"
print(texto[0:4])
print(texto[:4])
print(texto[::2])
print(texto[4:])
print(texto[-5:-1])
print(texto[::-1])


#?Saber el numero de caracteres de una cadena, podemos utilizar la funcion len() nativa de python
texto = "Esteban"
print(f"La palabra '{texto}' tiene {len(texto)} caracteres")

#? Transformar una cadenas a mayusculas o minuscula
texto = "texto en minuscula".upper()
print(texto)
texto = "TEXTO EN MAYUSCULA".lower()
print(texto)

#? Capitalizar un texto: esteban = Esteban
texto = "esteban".capitalize()
print(texto)

#? Reemplazar cadenas replace(cadena,reemplazo,veces a reemplazar(opc.))
texto = "Johand Castro".replace('Castro','Rodriguez')
print(texto)

#? Multiplicacion de cadenas String * entero+
texto = "Palabra " * 3
print(texto)

'''
#? Buscar subcadenas
El metodo find devuelve el indice del primer caracterer
de la primera aparicion de la subcadena
si no se encuentra devuelve -1
# '''
texto = 'Hola, Mundo!'
indice = texto.find('Mundo')
print(f'Indice de la subcadena mundo: {indice}')
