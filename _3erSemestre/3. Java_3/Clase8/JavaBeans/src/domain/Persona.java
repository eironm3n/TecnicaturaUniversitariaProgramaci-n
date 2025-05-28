/*
Clase 8 - JavaBeans

Serializacion es convertir nuestro objeto en 0 y 1
 */
package domain;

import java.io.Serializable;

public class Persona implements Serializable{
    private String nombre;
    private String apellido;
    
    // Constructor vacio: esto es obligatorio para el Javabeans
    public Persona(){
        
    }
    
    public Persona(String nombre, String apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }

    //Se agregan Getters and Setters y se agrega encapsulamiento
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }
    
    //Se agregan toString

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + ", apellido=" + apellido + '}';
    }
    
}
