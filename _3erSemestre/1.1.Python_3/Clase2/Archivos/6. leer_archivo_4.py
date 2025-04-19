
archivo = open('prueba.txt', 'r', encoding = 'utf8')
#print(archivo.read())

"""
print(archivo.read(16))
print(archivo.read(10))
print(archivo.readline())
print(archivo.readline())
"""

# vamos a iterar el archivo, cada d elas lineas
for linea in archivo:
    # print(linea)  --> para iterar todos los elementos del archivo
    # print(archivo.readlines()) --> Esto nos entregara todo como si fuera una lista
    print(archivo.readlines(1)) #Accedemos al archivo como si fuera una lista
    print(archivo.readlines()[11])  #En caso de hacerlo como si fuera una lista realmente utilizando corchetes
    
