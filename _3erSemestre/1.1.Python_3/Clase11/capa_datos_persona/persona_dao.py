"""
Se toma lo iniciado de la clase 8, 9 y 10. Esta es la Clase11 - Pool de conexiones parte2
DAO = Data Access Object
CRUD = 
    Create-> Insertar
    Read -> Seleccionar
    Update  -> Actualizar
    Delete  -> Eliminar
"""

from Persona import Persona
from conexion import Conexion
from logger_base import log

class PersonaDAO:
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    #Definimos los métodos de clase
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []  # creamos una lista
                for registro in registros:
                    persona = Persona(registro[0],registro[1],registro[2],registro[3])
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(cls,persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR,valores)
                log.debug(f'Persona Insertada: {persona}')
                return cursor.rowcount
            
    @classmethod
    def actualizar(cls,persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.debug(f'Persona Actualizada: {persona}')
                return cursor.rowcount
            
    @classmethod
    def eliminar(cls,persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR,valores)
                log.debug(f'Los objetos eliminados son: {persona}')
                return cursor.rowcount

if __name__=='__main__':

    """
    #Eliminar un registro
    persona1 = Persona(id_persona=1)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f'Resgistro de persona eliminada: {personas_eliminadas}')
    """

    """
    #Actualizar un registro
    persona1 = Persona(1,nombre='Homero',apellido='Ramos',email='promero@mail.com')
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f'Personas actualizadas: {personas_actualizadas}')
    """
    
    """
    # Insertar registro
    persona1 = Persona(nombre='Homero',apellido='Ramos',email='promero@mail.com')
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f'Personas insertadas: {personas_insertadas}')
    """

    # Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
    # puede llegar a generar conflictos en los otros metodos debido a que hay mas de un metodo en el mismo
    # al comentar el codigo de los otros metodos, no surgen inconvenientes.-