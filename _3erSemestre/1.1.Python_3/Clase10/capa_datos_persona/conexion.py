"""
Atributos de clase
Se toma lo iniciado de la clase 8 y 9.
Esta es la Clase10 - Pool de conexiones
"""
# import psycopg2 as bd
from psycopg2 import pool
# para traer el pool de psycopg2
from logger_base import *
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres' # es el owner dentro de ImAdmin
    _PASSWORD = 'admin'
    _DB_PORT = 5432
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None


    @classmethod
    def obtenerConexion(cls):
        pass
    """
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)

                log.debug(f'Conexión Exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrio un error: {e}')
                sys.exit()
        else:
            return cls._conexion
    """
    
    @classmethod
    def obtenerCursor(cls):
        pass
    """
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrio correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio un error: {e}')
                sys.exit
        else:
            return cls._cursor

if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()
    """

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool()
