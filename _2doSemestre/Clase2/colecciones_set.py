"""
Colecciones tipo set
No tiene un orden y no permite almacenar elementos duplicados, este no se puede modificar.
Pero se puede agregar o eliminar.
No es completamente inmutable, ni completamente mutable.
No mantiene ningun indice, es decir que su orden es aleatorio.
Para set, se utilizan llaves {}
"""

planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)

# Funciones para set
print(len(planetas))
# Revisar si un elemento existe
print('marte' in planetas)  # Actua como booleano
print('Marte' in planetas) # Tambien actúa con casesensitive, es decir, debe coincidir su valor para que sea True

planetas.add('Tierra')  #Adicion de elementos con .add
planetas.add('Tierra')  # Por más que volvamos a ejecutar la linea, no se realizara, ya que no admite elementos duplicados.

planetas.remove('Júpiter')  #Eliminación de elementos