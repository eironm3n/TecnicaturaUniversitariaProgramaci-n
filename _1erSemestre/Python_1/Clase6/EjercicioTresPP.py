'''Ejercicio 3: Intercambiar el valor de dos variables
Intercambiar el valor de dos variables.
Por ej: a = 10  -->  a = 5
        b = 5   -->  b = 10
'''

a = float(input('Tipea un valor de a: '))
b = float(input('Tipea un valor de b: '))

print(f'El valor elegido para "a"={a} y el valor de "b"={b}')

# Intercambiamos valores
a , b = b , a

print(f'Ahora los valores de "a"={a} y "b"={b}')

