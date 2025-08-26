from capa_datos_persona.usuario_dao import UsuarioDAO
from logger_base import log

opcion = None

while opcion != 5:
    print('Opciones: ')
    print('1. Listar usuarios')
    print('2. Agregar usuarios')
    print('3. Modificar usuarios')
    print('4. Eliminar usuarios')
    print('5. Salir')
    opcion = int(input('Digite la opcion (1-5): '))

    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)

else:
    log.info('Salimos de la aplicacion, Hasta pronto!!!')