"""
Ejercicio 2
Crear un rango de numeros de 2 a 6 e imprimelos

Ejemplo: 2,3,4,5,6
"""

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Los numeros son:')

for numero in numeros:
    if numero>=2 and numero<=6:
        print(numero)
else:
    print('Finalizado')
