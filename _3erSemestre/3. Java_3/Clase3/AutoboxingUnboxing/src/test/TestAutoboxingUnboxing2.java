/*
Clase 3 - Autoboxing / Unboxing - Parte 2
 */
package test;


public class TestAutoboxingUnboxing2 {
    public static void main(String[] args) {
        //Clases envolventes o Wrapper
        
        /*
        Clases envolventes de tipos primitivos
        int = la clase envolvente es Integer
        long = la clase envolvente es Long
        float = la clase envolvente es Float
        double = la clase envolvente es Double
        boolean = la clase envolvente es Boolean
        byte = la clase envolvente es Byte
        char = la clase envolvente es Character
        short = la clase envolvente es Short
        */
        
        int enteroPrim = 10;    // Tipo primitivo
        System.out.println("Soy un entero Primitivo: " + enteroPrim);
        
        Integer entero = 10;    // Tipo Object con la clase Integer
        // a esta forma de usar el objeto hacia un tipo distinto, se llama autoboxing
        System.out.println("Soy un entero tipo Object: " + entero.doubleValue());

        int entero2 = entero;   // a esto se le llama unboxing
        System.out.println("Ahora soy de tipo primitivo: " + entero2);
    }
}
