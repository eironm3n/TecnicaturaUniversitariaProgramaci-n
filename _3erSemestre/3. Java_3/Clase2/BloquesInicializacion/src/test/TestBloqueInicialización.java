/*
Se crea la clase Test y se testea la clase Domain.java
 */
package test;

import domain.Persona;


public class TestBloqueInicialización {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        System.out.println("persona1 = " + persona1);   //esto nos muestra la referencia del objeto
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);   //aqui nos mostraria la ejecución del NoEstatico
    }
}
