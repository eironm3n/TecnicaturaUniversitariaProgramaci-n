/*
 Creamos nuestra propias excepciones - continuamos
 */
package aritmetica;

import excepciones.OperacionExcepcion2;

public class Aritmetica2 {
    public static int division(int numerador, int denominador){
        if(denominador == 0){
            throw new OperacionExcepcion2("Division entre cero");
        }
        return numerador / denominador;
    }
}
