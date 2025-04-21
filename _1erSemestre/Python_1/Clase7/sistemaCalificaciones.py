'''Ejercicio 5: Sistemas de Calificaciones
El objetivo del programa será crear un sistema de calificaciones de la siguiente manera:
Le pedimos al usuario que ingrese un valor del 0 al 10:
Si ingreso 0 o 10 imprimimos A
Entre 8 y menor a 9 imprimimos B
Entre 7 y menor a 8 imprimimos C
Entre 6 y menor a 7 imprimimos D
Entre 0 y menor a 6 imprimimos F
De lo contrario el valor ingresado es incorrecto
'''
nota = int(input('Digite su calificación: '))

calificacion = None     #Seteamos a calificacion como 'none'
if 9 < nota < 10:
    calificacion = 'A'
elif 8 <= nota < 9:
    calificacion = 'B'
elif 7 <= nota < 8:
    calificacion = 'C'
elif 6 <= nota < 7:
    calificacion = 'D'
elif 0 <= nota < 6:
    calificacion = 'C'
else:
    nota = 'El valor ingresado es incorrecto'


print(f'Tu nota es {nota} y mi calificación para ti es: {calificacion}')