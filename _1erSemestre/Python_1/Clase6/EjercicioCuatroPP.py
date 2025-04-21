'''Ejercicio 4: Area y Longitud de un Circulo
Hacer un programa para ingresar el radio de un circulo y se reporte su área y la longitud
de la circunferencia
Area=Pi*r2
Longitud = 2 * Pi * r
'''
import math

radio = float(input("Ingrese el valor del radio: "))

area = math.pi * radio**2
long = 2 * math.pi * radio

print(f"El area del circulo es {area} y su longitud es {long}")