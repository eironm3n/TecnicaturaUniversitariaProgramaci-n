"""
Ejercicio 3
Dada la siguiente tupla =>  tupla = (13, 1, 8, 3, 2, 5, 8)
Crear una lista que solo incluya los números menores a 5
E imprima por consola [1, 3, 2]
"""

tupla = (13, 1, 8, 3, 2, 5, 8)

lista = []

for numeros in tupla:
    if numeros>0 and numeros<5:
        lista.append(numeros)
        print('Agregados los numeros a la lista')
else:
    print('Eso es todo amigos.')

for numeros in lista:
    if numeros>=0 and numeros<5:
        print(numeros)