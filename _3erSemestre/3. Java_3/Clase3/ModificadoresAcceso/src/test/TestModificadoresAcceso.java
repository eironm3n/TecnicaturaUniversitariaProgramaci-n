/*
Clase 3 - Modificadores de acceso public
 */
package test;

import paquete1.Clase1;
import paquete2.Clase3;

public class TestModificadoresAcceso {
    public static void main(String[] args) {
        Clase1 clase1 = new Clase1();
        System.out.println("clase1 = " + clase1.atributoPublic);
        
        clase1.metodoPublico();
        //esto tambien se mostrará
        
        Clase3 clasehija = new Clase3();
        System.out.println("claseHija = " + clasehija);
    }
}
