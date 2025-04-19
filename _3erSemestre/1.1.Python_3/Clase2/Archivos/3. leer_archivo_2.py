# Utilizaremos 'a' de append, es para anexar información, diferente de 'w'
# que escribira encima del mismo

archivo = open('prueba.txt', 'a', encoding = 'utf8')
# Las letras hasta ahora son w, r y a
# La letra 'x' sirve para crear el archivo, sin embargo tirará error si no existe
print(archivo.read())
