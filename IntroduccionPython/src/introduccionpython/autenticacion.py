print('*** Sistema autenticacion ***')
USUARIO = 'jekser'
CLAVE = 'admin'

entrada_usuario = input('Cual es tu usuario?: ')
entrada_clave = input('Cual es tu clave?: ')

es_correcto = entrada_usuario == USUARIO and entrada_clave == CLAVE
print(f'Datos Correctos?: {es_correcto}')
