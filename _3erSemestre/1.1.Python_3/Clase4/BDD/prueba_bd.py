"""
utilización de librerias psycopg2, perteneciente a Postgresql 
Instalar en venv = 
pip install psycopg2

"""

import psycopg2
# Esto para conectarnos a Postgresql 

#conexion = psycopg2.connect()
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)
# con este metodo podemos conectarnos a la base de datos

# print(conexion)
# esto nos muestra una correcta ejecución del conector a la base de datos ya creada

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)   #De esta manera ejecutamos la sentencia
registros = cursor.fetchall()   # Recuperamos todos los registros que serán una lista
print(registros)





# Si al ejecutar este codigo arroja error, revisar si existe conflicto con la version de Python
