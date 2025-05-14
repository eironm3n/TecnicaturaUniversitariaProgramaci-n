/*
Modificadores de acceso default o package - parte2
Clase Hija 2 de la Clase 2
 */
package paquete1;

public class ClaseHija2 extends Clase2{
    public ClaseHija2(){
        super();
        this.atributoDefault = "Modificacion del atributo default";
        System.out.println("atributoDefault = " + this.atributoDefault);
        this.metodoDefault();
    }
}
