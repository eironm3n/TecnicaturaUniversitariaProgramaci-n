from conexion import Conexion
from logger_base import *

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del étodo with y __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self,tipo_exception,valor_exception,detalle_exception):
        log.debug('Se ejecuta el metodo exit')
        if valor_exception:
            self._conexion.rollback()
            log.debug(f'Ocurrio una excepcion: {valor_exception}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transacción')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


if __name__=='__main__':
    with CursorDelPool() as cursor:
        log.debug('Estamos dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())
