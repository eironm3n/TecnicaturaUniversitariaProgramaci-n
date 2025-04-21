'''
Calcular la suma de "N" primeros números
'''

N = int(input('Ingresa un número por favor: ')) #Pedimos por pantalla se ingrese el número(N)

suma = 0    #Inicializamos la variable en 0
for i in range(1, N + 1):
    suma += i


print(f'La suma de los primeros {N} numeros es: {suma}')