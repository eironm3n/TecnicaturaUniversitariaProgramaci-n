# Preguntaremos cuantos elementos tiene una lista

nombres = ['Naty', 'Osvaldo','Lily', 'Ariel']
print(nombres)  

print(len(nombres)) # len es una funcion que cuenta los elementos de la lista

# Agregamos un elemento en la cola, siempre lo ingresará al final
nombres.append('Marcelo')
print(nombres)

# Ahora lo ingresaremos en el indice que le indiquemos
nombres.insert(1,'Alberto')
# El 1 toma el lugar del elemento
# Luego del lugar del elemento, se utilizaria el valor del elemento
# Esto tambien moveria a los elementos que contiene, hacia la derecha.
print(nombres)


# Eliminamos un elemento de la lista
nombres.remove('Alberto')
print(nombres)


# Eliminamos el último elemento de la lista
nombres.pop()
print(nombres)

# Eliminamos un elemento o indice especifico de la lista
del nombres[2]
print(nombres)

# Eliminar todos los elementos de la lista
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
print(nombres)