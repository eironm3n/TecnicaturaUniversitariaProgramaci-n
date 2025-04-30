"""
utilización de librerias psycopg2, perteneciente a Postgresql 
Instalar en venv con = pip install psycopg2
"""

import psycopg2
# Esto para conectarnos a Postgresql 

#conexion = psycopg2.connect()
conexion = psycopg2.connect(
    user= 'admin',
    password= 'admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)
# con este metodo podemos conectarnos a la base de datos

print(conexion)

# ESTE CODIGO NO FUNCIONA POR INCONVENIENTES CON EL NOMBRE DE USUARIO DE ORIGEN
# ERROR RELACIONADO CON UTF8 YA QUE EL USUARIO TIENE ACENTO EN SU NOMBRE, NO COMPATIBLE CON psycopg2
# INVESTIGAR PARA SOLVENTAR Y PROBAR QUE FUNCIONE
# continuar con video "Clase 4 Parte 6 python"
