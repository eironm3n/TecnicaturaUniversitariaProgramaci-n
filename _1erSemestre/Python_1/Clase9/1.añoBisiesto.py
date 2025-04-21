'''
Ejercicio 1: Año Bisiesto
Diseñar un programa que ingresando un año, nos devuelva por consola si es un año bisiesto o no,
repetir la acción hasta que el usuario lo decida
'''
print('Comprobaremos que año es bisiesto')

año = 0
opcion = 1
stop = False

while stop==False and opcion ==1:
    año = int(input('Digame un año por favor: '))
    if opcion == 1 and opcion != 2:
        if ((año%4 ==0) and  (año % 100 != 0) or (año % 400 ==0)):
            print(f'El año es {año} y es BISIESTO')
            opcion=int(input('¿Quiere seguir jugando?\nPresione 1 para repetir, o 2 para salir: '))
        else:
            print(f'El año es {año} y NO es BISIESTO')
            opcion=int(input('¿Quiere seguir jugando?\nPresione 1 para repetir, o 2 para salir: '))
    else:
        stop = True
else:
    print('Fin del juego')

