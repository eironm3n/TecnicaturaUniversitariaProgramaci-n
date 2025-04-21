'''
Ejercicio 2: Determinar la solución logica de la siguiente operación
( (3 + 5 * 8) < 3 AND ( ( -6 / 3 * 4) + 2 < 2 ) ) OR ( ( a > b) )
'''
print('Buenos dias a todos :D\n Hoy realizaremos la siguiente solución logica a la siguiente operación:\n')
print('\n( (3 + 5 * 8) < 3 AND ( ( -6 / 3 * 4) + 2 < 2 ) ) OR ( ( a > b) )\n')

a = 50
b = 5000
primerT = (3 + 5 * 8 ) < 3
segundoT = ((-6/3 * 4)+ 2  < 2)

resultado = primerT and segundoT or ( a > b)
print(f'El resultado agregando como valores de 50 a "a" y 5000 a "b" sería {resultado}')
print('')
