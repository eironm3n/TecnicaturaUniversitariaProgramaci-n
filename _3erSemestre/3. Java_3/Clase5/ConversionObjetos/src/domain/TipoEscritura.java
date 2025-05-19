/*
Se inicia con la clase 5 - Casting

Si es de la clase padre a la clase hija se llama DownCasting
Si es de la clase hija a la clase padre, se llama UpCasting
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
