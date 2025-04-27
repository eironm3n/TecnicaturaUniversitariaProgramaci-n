""" Vamos a arrojar una excepcion, como por ejemplo esta division entre cero
Para poder procesar esta excepcion y que nuestro programa no se cierre de forma
abrupta, lo colocamos dentro de un obj.
e -> funciona como una variable de error zero"""

try:
    10/0
except Exception as e:
    print(f'Ocurrió un error: {e}')

# para capturar la excepcion, debemos ingresarlo al bloque try-except
