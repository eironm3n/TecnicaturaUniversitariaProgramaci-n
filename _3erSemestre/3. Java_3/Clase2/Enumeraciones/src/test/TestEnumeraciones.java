/*
 Aqui testeamos enumeraciones.Dias
*/
package test;

import enumeraciones.Dias;


public class TestEnumeraciones {
    public static void main(String[] args) {
        System.out.println("Dia 1: "+Dias.LUNES);       //Las enumeraciones se tratan como cadena
        indicarDiaSemana(Dias.LUNES);
        //Ahora no se deben utilziar comillas, se accede a traves de el operador de punto
        System.out.println("Dia 2: "+Dias.MARTES);
        indicarDiaSemana(Dias.MARTES);
         System.out.println("Dia 3: "+Dias.MIERCOLES);
        indicarDiaSemana(Dias.MIERCOLES);
         System.out.println("Dia 4: "+Dias.JUEVES);
        indicarDiaSemana(Dias.JUEVES);
         System.out.println("Dia 5: "+Dias.VIERNES);
        indicarDiaSemana(Dias.VIERNES);
    }
    
    //Metodo para imprimir que dia de la semana estamos usando
    private static void indicarDiaSemana(Dias dias){
        switch(dias){
            case LUNES:
                System.out.println("Primer dia de la semana");
                break;
            case MARTES:
                System.out.println("Segundo dia de la semana");
                break;
            case MIERCOLES:
                System.out.println("Tercer dia de la semana");
                break;
            case JUEVES:
                System.out.println("Cuarto dia de la semana");
                break;            
            case VIERNES:
                System.out.println("Quinto dia de la semana");
                break;
            case SABADO:
                System.out.println("Sexto dia de la semana");
                break;
            case DOMINGO:
                System.out.println("Septimo y  dia de la semana");
                break;
        }
    }
}
