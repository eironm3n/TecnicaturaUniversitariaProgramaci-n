/*
* Comienzo Proyecto UTN - Calculadora con IntelliJ
*
* */

import java.util.Scanner;

public class CalculadoraUTN {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        while (true){   //Ciclo infinito
            System.out.println("*********** Aplicacion Calculadora ***********");
            mostrarMenu();

            try {
                var operacion = Integer.parseInt(entrada.nextLine());
                if (operacion >= 1 && operacion <= 4) {
                    System.out.println("Digite el valor para el operando1: ");
                    var operando1 = Integer.parseInt(entrada.nextLine());
                    System.out.println("Digite el valor para el operando2: ");
                    var operando2 = Integer.parseInt(entrada.nextLine());
                    ;

                    //Generamos un switch para las opciones brindadas
                    int resultado;
                    switch (operacion) {
                        case 1 -> {
                            resultado = operando1 + operando2;
                            System.out.println("Resultado de la suma: " + resultado);
                        }
                        case 2 -> {
                            resultado = operando1 - operando2;
                            System.out.println("Resultado de la resta: " + resultado);
                        }
                        case 3 -> {
                            resultado = operando1 * operando2;
                            System.out.println("Resultado de la multiplicacion: " + resultado);
                        }
                        case 4 -> {
                            resultado = operando1 / operando2;
                            System.out.println("Resultado de la division: " + resultado);
                        }
                        default -> System.out.println("Opcion erronea" + operacion);
                    }   //Fin switch
                }   //Fin del IF
                else if (operacion == 5) {
                    System.out.println("Hasta pronto...");
                    break;  //Rompe el ciclo y sale
                } else {
                    System.out.println("Opcion erronea: " + operacion);
                }
                // Imprimimos un salto de linea antes de repetir el menú
                System.out.println();
            }//Fin del try y comienzo del catch
            catch (Exception e){
                System.out.println("Ocurrio un error: " + e.getMessage());
            }   //Fin del catch
        }   //Fin while
    }   //Fin main

    public static void mostrarMenu() {
        //Mostramos el menú
        System.out.println("""
                    1. Suma
                    2. Resta
                    3. Multiplicación
                    4. Division
                    5. Salir
                    """);
        System.out.print("¿Operacion a realizar? --> ");
    }
}   //Fin clase
