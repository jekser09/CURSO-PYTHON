print('*** Valor dentro de rango')
VALOR_MIN = 0
VALOR_MAX = 10

entrada_usuario = int(input(f'Ingresa un numero entre {VALOR_MIN} y {VALOR_MAX}: '))

esta_dentro_rango = entrada_usuario >= VALOR_MIN and entrada_usuario <= VALOR_MAX
print(f'El valor esta dentro del rango?: {esta_dentro_rango}')


