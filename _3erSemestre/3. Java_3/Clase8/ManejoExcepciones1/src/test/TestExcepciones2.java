/*
Manejo de excepciones
 */
package test;

/*
public class TestExcepciones {
    public static void main(String[] args) {
        int resultado = 10/0;
        System.out.println("resultado = " + resultado);
        
        Esto dará una salida de error, lo siguiente, será para que el programa continue y no pare
        
    }
}
*/
public class TestExcepciones2 {
    public static void main(String[] args) {
        int resultado = 0;
        try{
            resultado = 10/0;
        }
        catch(Exception e){
            System.out.println("Ocurrio un error");
            e.printStackTrace(System.out);
        }   // esto se conoce como la pila de excepciones
        
        System.out.println("La variable de resultado tiene como valor = "+ resultado);
        /*
        Esto devolverá:
        run:
        Ocurrio un error
        java.lang.ArithmeticException: / by zero
        at test.TestExcepciones.main(TestExcepciones.java:21)
        La variable de resultado tiene como valor = 0
        */
    }
}