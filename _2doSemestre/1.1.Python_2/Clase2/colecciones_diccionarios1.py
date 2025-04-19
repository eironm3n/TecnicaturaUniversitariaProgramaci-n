"""
Los diccionarios estan compuesto por dos elementos.
Contiene Llave y Valor => dict(key,value)
Al finalizar un elemento del diccionario, se debe usar coma (,)
Para diccionarios se utilizan llaves {}

Ejemplo:
'Maradona':10
"""

diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programación Orientada a Objetos',
    'SABD':'Sistema de Administración de Base de Datos'
}
print(diccionario)

print(len(diccionario)) #verificar cantidad de elementos en un diccionario

# Acceder a un diccionario con la llave (key)
print(diccionario['IDE'])   # Esto nos arrojara el valor de la misma
#print(diccionario['ide'])   # Los datos deben ser precisos, ya que esto arrojará un error

print(diccionario.get('POO'))   # Otra forma de obtener el valor de un elemento

# Modificación de elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
# Esto modificará el valor de la llave 'IDE'