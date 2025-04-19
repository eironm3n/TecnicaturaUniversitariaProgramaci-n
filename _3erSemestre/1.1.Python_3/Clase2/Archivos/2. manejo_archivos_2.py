# Continuamos con lo aplicado en el archivo manejo_archivos_1.py

try:
    archivo = open('prueba.txt', 'w', encoding = 'utf8')
    #agregamos encoding = 'utf8' para que el txt que recibe la información, soporte acentos
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n')
    archivo.write(' Las letras son:\nr= read, \na= append, \nw= write, \nx= crea un archivo')
    archivo.write('\nt= esta es para texto o text, \nb= para archivos binarios, \nw+=lee y escribe, son iguales a r+ ')
    archivo.write('Saludos a todos los alumnos de la tecnicatura\n')
    archivo.write('Con esto terminamos.')

except Exception as e:
    print(e)
finally:    # Siempre se ejecuta
    archivo.close() # Con esto se debe cerrar el archivo

# archivo.write('Todo quedo perfecto')
# Esta linea de arriba, genera un error y no permitira que se incluya la información 
# Ya que el archivo se ha cerrado