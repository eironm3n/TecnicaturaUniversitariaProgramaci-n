"""
Las listas se conocen en otros lenguajes como arreglos o vectores
"""

nombres = ['Naty', 'Osvaldo','Lily', 'Ariel']
print(nombres)

# Concatenación de listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1 + lista2
print(lista3)

lista3.extend([7,8,9])  #Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5))  # Funcion para acceder a un elemento especifico en la lista

print(lista3.count(1))  # Funcion para saber si hay valores repetidos en la lista
lista3.extend([1,1,1])
print(lista3)
print(lista3.count(1))  # Ahora deberia decirme cuantas veces el 1 está en la lista

lista3.reverse()    # Para dar la vuelta a una lista
print(lista3)

