'''Solicitamos a que el usuario ingrese un numero'''
num = int(input('Ingrese un numero: '))

if num % 2 ==0:
    print(f'El valor de del numero es{num} y es un numero par')
else:
    print(f'El valor de del numero es{num} y es un numero impar')
