/*
Clase 3 - Modificadores de acceso protected
Esta es la clase hija o subclase de la clase 1
Sirve para traer el objecto protected
 */
package paquete2;

import paquete1.Clase1;

public class Clase3 extends Clase1{
    public Clase3(){
        super("protected");
        this.atributoProtected = "Accedemos desde la clase hija";
        System.out.println("Atributo Protected = " + atributoProtected);
        this.atributoPublic = "es totalmente publico";
    }
}
