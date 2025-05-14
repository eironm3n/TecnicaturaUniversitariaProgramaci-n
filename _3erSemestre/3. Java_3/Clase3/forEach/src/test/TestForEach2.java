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
        System.out.println("Se ejecuta el bloque de personas");
        
        //ForEach
        for(Persona persona: personas){
            System.out.println("persona = " + persona );
        }  
        /*
        Se uso la funcionalidad del Java:
        Menú: Run --> Clean and Build Project
        Luego: Run --> Run File sobre TestForEach2.java
         */
        
    }
}
