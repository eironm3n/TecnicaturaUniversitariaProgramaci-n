'''Ejercicio 3: Intercambiar el valor de dos variables
Intercambiar el valor de dos variables.
Por ej: a = 10  -->  a = 5
        b = 5   -->  b = 10
'''

a = float(input('Tipea un valor de a: '))
b = float(input('Tipea un valor de b: '))

temp = a        #guardar el valor de a en un temp
a = b           #asignar el valor de b a a
b = temp        #asignar el valor de temp a b


print(f'El valor de "a"={a} y "b"={b}')
