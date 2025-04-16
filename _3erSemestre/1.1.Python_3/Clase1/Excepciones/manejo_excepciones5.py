from NumerosIgualesException import NumerosIgualesException

resultado = None

try:
    a = int(input('Digite el primer número: '))
    b = int(input('Digite el segundo número: '))
    
    if a == b:
        raise NumerosIgualesException('Son números iguales')
    resultado = a / b 

except TypeError as e:
    print(f'TypeError - Ocurrió un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {type(e)}')

print(f'El resultado es: {resultado}')
print(f'seguimos...')

""" Con este archivo, ejecutamos la clase padre NumerosIgualesException, 
para comprobar si sus valores son iguales. Pero la ejecucion se realiza con error 0
"""