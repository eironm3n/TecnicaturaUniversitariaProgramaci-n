'''Calcular el área y el perímetro de un rectángulo'''
print('Vamos a calcular el area y el perimetro de un rectangulo')
alto = int(input('Ingrese el valor de alto del rectangulo: '))
ancho = int(input('Ingrese el ancho del rectangulo: '))
area = alto*ancho
perimetro = (alto+ancho)*2

print(f'El area del rectangulo es de {area} y el perimetro sería {perimetro}')
