/*
 Aqui testeamos enumeraciones.Continentes
*/
package test;
import enumeraciones.Continentes;


public class TestContinentes {
    public static void main(String[] args) {
        System.out.println("Continente No.4: "+Continentes.AMERICA);
        System.out.println("No. de paises en el 4to Continente: "
                +Continentes.AMERICA.getPaises());
        //Esta forma de sout, utilizando un enter de por medio de la linea, tambien se puede realizar.
        System.out.println("No. de habitantes en el 4to Continente: "
                +Continentes.AMERICA.getHabitantes());
        
        
        System.out.println("Continente No.1: "+Continentes.AFRICA);
        System.out.println("No. de paises en el 1er Continente: "
                +Continentes.AFRICA.getPaises());
        System.out.println("No. de habitantes en el 1er Continente: "
                +Continentes.AFRICA.getHabitantes());
        
        System.out.println("Continente No.2: "+Continentes.EUROPA);
        System.out.println("No. de paises en el 2do Continente: "
                +Continentes.EUROPA.getPaises());
        System.out.println("No. de habitantes en el 2do Continente: "
                +Continentes.EUROPA.getHabitantes());
        System.out.println("Continente No.1: "+Continentes.ASIA);
        System.out.println("No. de paises en el 3er Continente: "
                +Continentes.ASIA.getPaises());
        System.out.println("No. de habitantes en el 3er Continente: "
                +Continentes.ASIA.getHabitantes());
        System.out.println("Continente No.1: "+Continentes.OCEANIA);
        System.out.println("No. de paises en el 5to Continente: "
                +Continentes.OCEANIA.getPaises());
        System.out.println("No. de habitantes en el 5to Continente: "
                +Continentes.OCEANIA.getHabitantes());
        
    }

}
