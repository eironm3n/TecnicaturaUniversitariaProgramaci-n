/*
Continuamos con Bloques de Inicialización
Tenemos bloques de Inicialización estáticos y NoEstaticos.
Ambos se van a ejecutar antes del constructor, de lo que es nuestra clase
 */
package domain;


public class Persona {
    private final int idPersona;
    private static int contadorPersonas;
    
    //creamos bloque de inicialización estatico
    static{
        System.out.println("Ejecución del bloque estático");
        ++Persona.contadorPersonas;
        //idPersona = 10; --> Esto genera un error, ya que no es un atributo estatico
    }
    
    { //creamos bloque de inicialización NoEstatico o ContextoDinámico
        System.out.println("Ejecución del bloque NO estático");
        this.idPersona = Persona.contadorPersonas++; //Incrementamos el atributo
    }
    
    //Los bloques de incialización se ejecutan antes del constructor.
    public Persona(){
        System.out.println("Ejecución del constructor");
    }

    public int getIdPersona() {
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
    
    
    
}
