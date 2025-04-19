"""
Las listas son mutables y modificables.
Las tuplas, se organizan igual que las listas, pero NO SON MUTABLES
Las tuplas se almacenan en paréntesis
"""
cocina = ('Cuchara', 'Cuchillo', 'Tenededor')
print(cocina)

# Las funciones anteriores, tambien se pueden aplicar en las tuplas
# Algunas son similares

print(len(cocina))  # cantidad de elementos
print(cocina[0])    # Elemento 0 de la tupla
print(cocina[-1])   # Elemento -1 de la tupla, inversa.
print(cocina[0:1])  # Rango de 0 a 1

# Dato importante
# Una tupla de 1 SOLO ELEMENTO debe llevar una coma al final, para que no confunda con un string
ejemplo = ('soyElEjemplo' ,)
print(ejemplo)
