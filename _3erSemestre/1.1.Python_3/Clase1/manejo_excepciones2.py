# para capturar la excepcion, debemos ingresarlo al bloque try-except
resultado = None
a = '10'
b = 0

try:
    resultado = a / b #modificamos
except Exception as e:
    print(f'Ocurrió un error: {e}')

print(f'El resultado es: {resultado}')
print(f'seguimos...')

# No es necesario usar ZeroDivisionError en vez de Exception, ya que no 
# trabajamos de forma tan especifica. Preferir el generico, Exception.