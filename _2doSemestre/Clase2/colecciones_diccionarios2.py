"""
Los diccionarios estan compuesto por dos elementos.
Contiene Llave y Valor => dict(key,value), al finalizar un elemento del diccionario, se debe usar coma (,)
Para diccionarios se utilizan llaves {}
"""

diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programación Orientada a Objetos',
    'SABD':'Sistema de Administración de Base de Datos'
}
print(diccionario)

# Recorrer elementos 
for termino in diccionario:
    print(termino)

# Se puede recorrer la llave con for

"""for termino, valor in diccionario:
    print(termino,valor)"""
# Esto no se puede realizar por que no se puede acceder de forma directa a la key y value

# Necesitamos una función para recorrer un diccionario completamente.
for termino, valor in diccionario.items():
    print(termino,valor)

# Esto realiza lo mismo que la forma anteriore, pero utiliza una función
for termino in diccionario.keys():
    print(termino)

# Esto devuelve solo los values
for termino in diccionario.values():
    print(termino)

print('IDE' in diccionario) # Actua como booleano

diccionario['PK'] = 'Primary key'   # Agregar elementos al diccionario
print(diccionario)

diccionario.pop('SABD') # Esto eliminará la key y su value
print(diccionario)

diccionario.clear() # Esto limpiara el diccionario
print(diccionario)

del diccionario # Eliminación de diccionario
print(diccionario)  #Esto deberia arrojar error