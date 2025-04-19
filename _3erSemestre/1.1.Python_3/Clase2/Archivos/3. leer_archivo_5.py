
archivo = open('prueba.txt', 'r', encoding = 'utf8')
#print(archivo.read())

# Anexamos información, copiamos a otro
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())
archivo.close()     #cerramos el primer archivo
archivo2.close()    #cerramos el segundo archivo

print('Se ha terminado el procesos de leer y copiar archivos')
