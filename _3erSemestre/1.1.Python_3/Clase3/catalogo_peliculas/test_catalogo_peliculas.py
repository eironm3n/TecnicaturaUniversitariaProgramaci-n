from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp
# cuando utilizamos 'as' es para renombrar el nombre completo mencionado en la importacion

opcion = None

while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Pelicula')
        print('2. Listar peliculas')
        print('3. Eliminar catalogo de peliculas')
        print('4. Salir')
        opcion = int(input('Digite una opcion de menu (1-4): '))
        if opcion == 1:
            nombre_pelicula = input('Digite el nombre de la pelicula: ')
            pelicula_nueva = Pelicula(nombre_pelicula)
            cp.agregar_peliculas(pelicula_nueva)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrió un error de tipo: {e}')
        opcion = None
    else:
        print('Salimos del programa')

