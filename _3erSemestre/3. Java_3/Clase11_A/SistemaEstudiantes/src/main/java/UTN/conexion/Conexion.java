/*
* Hacemos la conexión con la base de datos
* */

package UTN.conexion;

import com.mysql.cj.jdbc.Driver;

import java.sql.Connection;
import java.sql.DriverManager;

public class Conexion {
    public static Connection getConnection(){
        Connection conexion = null;

        //Variables para conectarnos a la base de datos
        var baseDatos = "estudiantes2025";
        var url = "jdbc:mysql://localhost:3306/"+baseDatos;
        //Esta es la url
        var usuario = "root";
        var password = "admin";

        // Cargamos la clase del driver de mysql
        Class.forName("com.mysql.cj.jdbc.Driver");
        conexion = DriverManager.getConnection(url,usuario,password);
    }

}
