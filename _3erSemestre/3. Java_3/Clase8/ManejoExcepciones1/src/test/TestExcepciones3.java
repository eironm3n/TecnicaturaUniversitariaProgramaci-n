/*
Manejo de excepciones - parte 3
 */
package test;

import aritmetica.Aritmetica;

public class TestExcepciones3 {
    public static void main(String[] args) {
        int resultado = 0;
        try{
            resultado = Aritmetica.division(10, 0);
        }
        catch(Exception e){
            System.out.println("Ocurrio un error");
            e.printStackTrace(System.out);
        }   // esto se conoce como la pila de excepciones
        
        System.out.println("La variable de resultado tiene como valor = "+ resultado);
    }
}