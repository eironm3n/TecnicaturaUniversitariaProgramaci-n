/*
Clase 3 - Autoboxing / Unboxing - Parte 2
 */
package test;


public class TestAutoboxingUnboxing2 {
    public static void main(String[] args) {
        //Clases envolventes o Wrapper
        
        int enteroPrim = 10;    // Tipo primitivo
        System.out.println("Soy un entero Primitivo: " + enteroPrim);
        
        Integer entero = 10;    // Tipo Object con la clase Integer
        // a esta forma de usar el objeto hacia un tipo distinto, se llama autoboxing
        System.out.println("Soy un entero tipo Object: " + entero.doubleValue());

        int entero2 = entero;   // a esto se le llama unboxing
        System.out.println("Ahora soy de tipo primitivo: " + entero2);
    }
}
