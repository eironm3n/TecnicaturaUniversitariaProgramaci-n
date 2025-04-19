# Manejo de contexto WITH: sintaxis simplificada, abre y cierra el archivo
with open('prueba.txt', 'r', encoding='utf8') as archivo:
    print(archivo.read())

# No hace falta ni el try ni el finally
# En el contexto de with lo que se ejecuta de manera automatica
# Utiliza diferentes métodos: __enter__ este es el que abre
# Ahora el siguiente étodo es el que cierra: __exit__
