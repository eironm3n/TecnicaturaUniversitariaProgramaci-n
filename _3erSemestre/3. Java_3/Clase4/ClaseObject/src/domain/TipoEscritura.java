/*
Clase 5 - Casting

Se continua con proyecto Object
*/

package domain;

//Esto no es una clase, es una enumeración
public enum TipoEscritura {
    CLASICO ("Escritura a mano"),
    MODERNO ("Escritura digital");
    
    private final String descripcion;
    
    private TipoEscritura(String descripcion){  //Constructor
        this.descripcion = descripcion;
    }
    
    //Metodo get
    public String getDescripcion(){
        return this.descripcion;
    }
}
