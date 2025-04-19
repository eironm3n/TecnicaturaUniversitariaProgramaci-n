# Para set, se utilizan llaves {}


planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)

# Funciones para set
print(len(planetas))
print('marte' in planetas)  # Actua como booleano
print('Marte' in planetas) # Tambien actúa con casesensitive, es decir, debe coincidir su valor para que sea True
planetas.add('Tierra')  #Adicion de elementos con .add
planetas.add('Tierra')  # Por más que volvamos a ejecutar la linea, no se realizara, ya que no admite elementos duplicados.
planetas.remove('Júpiter')  #Eliminación de elementos

planetas.discard('Tierra')  #Tambien elimina el elemento
print(planetas)
planetas.discard('marte')  #Esto no genera error, pero tampoco realizará la acción.
print(planetas)

planetas.clear  # Para limpiar el set
print(planetas)

del planetas    # Eliminacion de conjunto