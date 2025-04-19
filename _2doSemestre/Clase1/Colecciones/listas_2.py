#Ahora recuperaremos un rango de la lista

nombres = ['Naty', 'Osvaldo','Lily', 'Ariel']
print(nombres)  
print(nombres[0:2]) # Se visualiza un rango de elementos, menos el que se ubica en el 2
print(nombres[ :3]) # Aca estaremos con el espacio estaremos diciendo que tome desde el indice 0 hasta 3
print(nombres[1: ]) # Aca estaremos diciendo que tome desde el indice 1 y el espacio seria hasta el final

#Ahora modificaremos un elemento de la lista
nombres[3] = 'Liliana'
print(nombres)

# Iteraremos una lista
for nombre in nombres:
    print(nombre)
else:
    print('Se acabarn los elementos de la lista')
# 'nombre' funciona como la i, y seria el que iría saltando uno por uno en cada elemento de la lista

