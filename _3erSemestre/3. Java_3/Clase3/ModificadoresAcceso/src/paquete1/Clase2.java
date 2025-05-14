/*
Modificadores de acceso default o package
Clase 3 Java
 */
package paquete1;


class Clase2 extends Clase1{
    String atributoDefault = "Valor del atributo default";
    
    /*
    Clase2(){
        System.out.println("Constructor default");
    }
    */
    
    public Clase2(){
        super();
        this.atributoDefault = "Modificacion del atributo default";
        System.out.println("atributo Default = " + this.atributoDefault);
        this.metodoDefault();
    }
    
    void metodoDefault(){
        System.out.println("Metodo Default");
    }
    
}
