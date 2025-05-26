"""
Comenzamos con atributos de clase
"""

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres' # es el owner dentro de ImAdmin
    _PASSWORD = 'admin'
    _DB_PORT = 5432
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None

    


