usuario = ' Johand Castro '
print('Nombre usuario: ',usuario)
nombre_usuario = usuario.strip().lower().replace(' ','.')
print('Nombre usuario: ',nombre_usuario)
empresa = ' Global Mentoring '
print('Empresa: ',empresa)
extension_dominio = '.com.co'
print('Extension del dominio: ',extension_dominio)
dominio = f'@{empresa.lower().replace(' ','')}{extension_dominio}'
print('Dominio: ',dominio)
email_final = nombre_usuario + dominio
print('Email: ', email_final)