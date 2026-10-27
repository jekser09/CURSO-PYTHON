from random import randint
'''
Pedir nombre, apellidos, año de nacimiento

para generar un ID unico
2 primeras letras del nombre MAYUS
2 primeras letras del apellido MAYUS
2 ultimos digitos del año de nacimiento
un numero aleatorio de 4 digitos
'''

print("*** ID UNICO ***")
nombre = input('Digite su nombre: ').strip()
apellido = input('Digite su apellido: ').strip()
anio = input('Digite su año de nacimiento: ').strip()
#print*()
num = randint(1000,9999)
id = nombre[:2].upper() + apellido[:2].upper() + anio[2:] + str(num)
print(f'''
Hola {nombre},
    Tu nuevo numero de identificacion (ID) generado por el sistema es:
    {id}
    Felicidades!!!
''')