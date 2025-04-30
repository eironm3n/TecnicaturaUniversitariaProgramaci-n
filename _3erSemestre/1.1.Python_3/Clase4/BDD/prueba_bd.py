"""
utilización de librerias psycopg2, perteneciente a Postgresql 
Instalar en venv con = pip install psycopg2
"""

import psycopg2 
# Esto para conectarnos a Postgresql 

conexion = psycopg2.connect(
    user= 'admin',
    password= 'admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
# con este metodo podemos conectarnos a la base de datos

print(conexion)
