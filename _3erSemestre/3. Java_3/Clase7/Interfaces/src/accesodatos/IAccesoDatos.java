/*
Clase 7 - Interfaces en Java
Al crear el archivo .java, se debe elegir el archivo de"Interfaces"
Tambien al asignarle un nombre, debe colocarse la I al inicio
 */
package accesodatos;

// Pueden existir clases padres o hijas que sean 'interface'
public interface IAccesoDatos {
    int MAX_REGISTRO = 10;
    
    
    // Metodo insertar es abstracto y sin cuerpo
    void insertar();
    
    void listar();
    
    void actualizar();
    
    void eliminar();
    // esto tambien se utiliza asi para insertar en base de datos
}
