/*
Clase 3 - Autoboxing / Unboxing - Parte 1
 */
package test;


public class TestAutoboxingUnboxing {
    public static void main(String[] args) {
        //Clases envolventes o Wrapper
        
        /*
        Clases envolventes de tipos primitivos
        int = la clase envolvente es Integer
        */
        
        int enteroPrim = 10;    // Tipo primitivo
        Integer entero = 10;    // Tipo Object con la clase Integer
        System.out.println("Soy un entero Primitivo: " + enteroPrim);
        System.out.println("Soy un entero tipo Object: " + entero.toString());  // esto es una cadena, por ende es tipo str
    }
}
