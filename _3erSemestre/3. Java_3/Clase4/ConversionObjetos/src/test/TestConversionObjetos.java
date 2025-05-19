/*
Se inicia con la clase 5 - Casting

Se continua con la parte 2 y completado de TestConversionObjetos.java
 */
package test;

import domain.*;

public class TestConversionObjetos {
    public static void main(String[] args) {
        Empleado empleado;
        empleado = new Escritor("Juan", 5000, TipoEscritura.CLASICO);
        System.out.println("empleado = "+empleado);
        /*
        System.out.println(empleado.obtenerDetalles()); //Si queremos acceder a metodos Escritor
        
        //DownCasting
        //((Escritor)empleado).getTipoEscritura();
        
        Escritor escritor = (Escritor)empleado;
        escritor.getTipoEscritura();
        
        //Upcasting
        Empleado empleado2 = escritor;
        System.out.println(empleado2.obtenerDetalles());
*/
    }
}
