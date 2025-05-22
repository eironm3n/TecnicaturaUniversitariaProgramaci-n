/*
Se realiza test de las implementaciones
 */
package test;

import accesodatos.*;

public class TestInterfaces {
    public static void main(String[] args) {
        IAccesoDatos datos = new ImplementacionMySQL();
        datos.listar();
    }
}
