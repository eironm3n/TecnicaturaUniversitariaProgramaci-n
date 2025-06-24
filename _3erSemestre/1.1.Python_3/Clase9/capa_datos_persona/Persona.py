"""
Clase 8 Capa de Datos: Logging y Postgresql Parte 2

"""

from logger_base import log

class Persona:
    # def __init__(self, id_persona,nombre,apellido,email):
    # se modifica para que se pueda almacenar los valores eligiendo manualmente el lugar y seteando al resto como NONE
    def __init__(self, id_persona=None,nombre=None,apellido=None,email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self.apellido = apellido
        self._email = email


    def __str__(self):
        return f'''
            ID Persona: {self._id_persona},
            Nombre: {self._nombre},
            Apellido: {self._apellido},
            Email: {self._email}
        '''

    # Metodos Getters and Setters

    # Para id_persona
    @property
    def id_persona(self):
        return self._id_persona
    
    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    # Para nombre
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Para apellido
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    # Para email
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email


if __name__=='__main__':
    persona1 = Persona(1,'Juan','Perez','jperez@mail.com')
    log.debug(persona1)
    # se elige a mano para que no exista cruce de informacion
    persona2 = Persona(nombre='Jose',apellido='Leppez',email='jleppez@mail.com')
    log.debug(persona2)

    # esto elimina el contenido anterior, pero setea el indice 1
    persona1 = Persona(id_persona=1)
    log.debug(persona1)
