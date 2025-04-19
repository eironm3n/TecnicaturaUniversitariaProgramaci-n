"""
Ejercicio 1
Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3

Ejemplo= 0,3,6,9
"""

numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('Los numeros son:')

for numero in numeros:
    if numero%3 == 0:
        print(numero)
else:
    print('Finalizado')  
