"""
Comenzamos con atributos de clase
"""
import psycopg2 as bd
from logger_base import *
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres' # es el owner dentro de ImAdmin
    _PASSWORD = 'admin'
    _DB_PORT = 5432
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None


    @classmethod
    def obtenerConexion(cls):
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
