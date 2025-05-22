/*
Implementacion de comportamiento de Interface-sql
 */
package accesodatos;

public class ImplementacionMySQL implements IAccesoDatos{
    // elegimos la opcion 'Implement all abstract methods'
    
    @Override
    public void insertar() {
        System.out.println("Insertar desde MySQL");
    }

    @Override
    public void listar() {
        System.out.println("Listar desde MySQL");
    }

    @Override
    public void actualizar() {
        System.out.println("Actualizar desde MySQL");
    }

    @Override
    public void eliminar() {
        System.out.println("Eliminar desde MySQL");
    }
    
}
