/*
Clase 3 - ForEach - parte 2
 */
package test;

import domain.Persona;

public class TestForEach2 {
    public static void main(String[] args) {
        int edades[] = {5, 6, 8, 9};
            for(int edad: edades) {    //sintaxis del forEach
                System.out.println("edad = " + edad);
            }
        
            Persona personas[] = {new Persona("Juan"), new Persona("Carla"), new Persona("Beatriz")};
            
             //ForEach
            for(var persona: personas){
            System.out.println("persona = " + persona );
            
         /*
         En clase se enseño esto, pero no funciona
         for(Persona persona: personas){
         System.out.println("persona = " + persona );
         */
        }
    }
}
