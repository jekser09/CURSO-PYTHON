from math import pi
'''
    Las constantes en python se escriben totalmente en mayusculas
    aunque el lenguaje no impide cambiar su valor se entiende
    que es una convension, al ver una variable totalmente escrita en mayusculas
    debemos interpretar que no debemos cambiar su valor
'''
print('*** Constantes en python ***')

PI=3.14159
print('El valor de PI es: ',PI)

NOMBBRE_BASE_DATOS = 'clientes_db'
print('Nombre de la base de datos: ',NOMBBRE_BASE_DATOS)

#Esto NO se debe hacer, no se debe modificar el valor de una constante
NOMBBRE_BASE_DATOS = 'listado_clientes_db'

# Usar una constante del lenguaje Python, aunque en este caso no esta en mayusculas
print('Valor de pi en la libreria math: ',pi)

x = 5
y = x
x = 10
print(y)