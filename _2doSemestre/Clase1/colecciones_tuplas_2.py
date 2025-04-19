
cocina = ('Cuchara', 'Cuchillo', 'Tenededor')
print(cocina)

# Para recorrer elementos con un iterador, tambien es igual a las listas
for cocinar in cocina:
    print(cocinar)
    print(cocinar, end=' ') # de esta forma podemos hacer una impresion sin el salto de linea

# cocina[0] = 'plato'
# Esto arrojaria un error, ya que son inmutables

# Como hacer para modificar estos valores ? Convertir la tupla a lista
cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple(cocinaLista) # No olvidar devolverla a su estado anterior para mantenerla
print(cocina)

# PERO ESTAS NO SON BUENAS PRACTICAS RECOMENDADAS


# para eliminar una tupla, podemos usar del
del cocina
print(cocina)