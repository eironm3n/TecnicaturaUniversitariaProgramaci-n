'''Problema 3: Dada una edad de una persona, determine si esta persona es mayor de edad'''

edad = int(input('¿Cual es tu edad? \n= '))
mayor = 18
elBooleano = edad >= mayor
if elBooleano == True:
    print('Es mayor de edad')
else:
    print('Es menor de edad')

print(elBooleano)   #para ver el estado del elBooleano 'true' o 'falso'