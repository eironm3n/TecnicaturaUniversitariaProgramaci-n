'''
Leer 10 numeros e imprimir cuantos son positivos, cuantos negativos y cuantos neutros
'''
positivos = 0
negativos = 0
neutros = 0

for i in range(10):
    numero = float(input(f'Ingrese el numero {i+1}: '))

    #Clasificamos el número
    if numero > 0:
        positivos += 1
    elif numero <0:
        negativos += 1
    else:
        neutros += 1

print(f'Numeros positivos: {positivos}')
print(f'Numeros negativos: {negativos}')
print(f'Numeros neutros: {neutros}')
