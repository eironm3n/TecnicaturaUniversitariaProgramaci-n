# Declaramos una variable
try:
    archivo = open('prueba.txt', 'w')  # la W es por write
    #este metodo nos ayuda para incluir información hacia un archivo o abrir otro
except Exception as e:
    print(e)
finally:    #siempre se ejecuta
    archivo.close() #Con esto se debe cerrar el archivo

    