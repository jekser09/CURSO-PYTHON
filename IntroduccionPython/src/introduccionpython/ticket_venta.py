print('*** Generacion de Ticket de Venta ***')
precio_leche = float(input('Precio leche: '))
precio_pan = float(input('Precio pan: '))
precio_lechuga = float(input('Precio lechuga: '))
precio_platanos = float(input('Precio platanos: '))

descuento = int(input(r'Descuento a aplicar (0% a 100%): '))

sub_total = precio_leche + precio_pan + precio_lechuga + precio_platanos
descuento_total = sub_total * (descuento/100)
sub_total_descuento = sub_total - descuento_total
impuesto = sub_total_descuento * 0.19 #? iva 19%
costo_total = sub_total_descuento + impuesto

print(f'''
Sub total: {sub_total}
descuento: {descuento_total}
Sub total con descuento: {sub_total_descuento}
Impuesto: {impuesto}
Costo total: {costo_total}
''')