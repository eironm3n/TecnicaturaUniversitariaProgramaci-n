/*
* Comienzo Proyecto UTN - Calculadora con IntelliJ
*
* */

import java.util.Scanner;

public class CalculadoraUTN {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("*********** Aplicacion Calculadora ***********");
        //Mostramos el menú
        System.out.println("""
                1. Suma
                2. Resta
                3. Multiplicación
                4. Division
                5. Salir
                """);
        System.out.print("Operacion a realizar ?");
        var operacion = Integer.parseInt(entrada.nextLine());

        if(operacion >= 1 && operacion <= 4){
            System.out.println("Digite el valor para el operando1: ");
            var operando1 = Integer.parseInt(entrada.nextLine());
            System.out.println("Digite el valor para el operando2: ");
            var operando2 = Integer.parseInt(entrada.nextLine());;
        }

    }
}
