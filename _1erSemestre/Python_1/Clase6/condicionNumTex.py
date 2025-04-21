num = int(input('Digite un numero en el rango del 1 al 3:\n'))
numTexto = ''

if num == 1:
    numTexto = 'Número uno'
elif num == 2:
    numTexto = 'Número dos'
elif num == 3:
    numTexto = 'Número tres'
else:
    numTexto = 'Has ingresado un numero fuera de rango'

print(f'El numero ingresado es: {num} - {numTexto}')

