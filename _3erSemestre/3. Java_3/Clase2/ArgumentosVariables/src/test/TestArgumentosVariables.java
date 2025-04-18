/*
    Clase 2 de Java

 */
package test;

public class TestArgumentosVariables {
    public static void main(String[] args) {
        imprimirNumeros(3, 4, 5);
        imprimirNumeros(1, 2);
        variosParametros("Juan","Perez", 7, 8, 9);
    }
    
    //Aqui se anexa otro Arreglo, en donde se incluye string y numeros
    private static void variosParametros(String nombre, String apellido, int ...numeros){
        System.out.println("Nombre: "+nombre);
        System.out.println("Apellido: "+apellido);
        imprimirNumeros(numeros);
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
