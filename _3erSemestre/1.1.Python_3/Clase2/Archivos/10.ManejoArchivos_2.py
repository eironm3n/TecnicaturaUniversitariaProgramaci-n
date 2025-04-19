
from ManejoArchivos_1 import ManejoArchivos

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
