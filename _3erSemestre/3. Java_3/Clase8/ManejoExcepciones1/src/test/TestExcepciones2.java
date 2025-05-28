/*
Manejo de excepciones
 */
package test;

public class TestExcepciones2 {
    public static void main(String[] args) {
        int resultado = 0;
        resultado = 10/0;
        /*
        try{
            resultado = 10/0;
        }
        catch(Exception e){
            System.out.println("Ocurrio un error");
            e.printStackTrace(System.out);
        }   // esto se conoce como la pila de excepciones
        */
        System.out.println("La variable de resultado tiene como valor = "+ resultado);

    }
}