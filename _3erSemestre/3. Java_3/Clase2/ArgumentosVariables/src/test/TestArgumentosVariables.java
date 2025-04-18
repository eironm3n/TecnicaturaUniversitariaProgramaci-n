/*
    Clase 2 de Java

 */
package test;

public class TestArgumentosVariables {
    public static void main(String[] args) {
        
    }
    // Metodo Imprimir Numeros
    public static void imprimirNumeros(int ...numeros) {
        //los ... pertenecen al argumento variable
        //int ...numeros esto es un arreglo que indica que se agregara una cantidad indefinida de argumentos
        
        for (int i = 0; i < numeros.length; i++){
            System.out.println("Elementos: "+numeros[i]);
        }
    }
}
