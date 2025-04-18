"""
Con 'open' verificamos que si el archivo prueba.txt no existe, que lo genere e ingrese.
Luego con 'w' hacemos que "escriba" en él
De momento, este archivo prueba.txt, en caso de no encontrarlo dentro de la Raiz de esta carpeta, lo generará
Caso contrario, abrirá este mismo.
"""

try:
    archivo = open('prueba.txt', 'w')  # La W es por write
    # Este metodo nos ayuda para incluir información hacia un archivo o abrir otro
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Con esto terminamos.')

except Exception as e:
    print(e)
finally:    # Siempre se ejecuta
    archivo.close() # Con esto se debe cerrar el archivo

