/*
 Creamos nuestra propias excepciones - parte 1
 */
package excepciones;


public class OperacionExcepcion extends Exception{
    // Constructor
    public OperacionExcepcion(String mensaje){
        super(mensaje);
    }
}
