
class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Pelicula: {self._nombre}'
    
    # metodo get
    @property
    def nombre(self):
        return self._nombre
    
    # metodo set
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

