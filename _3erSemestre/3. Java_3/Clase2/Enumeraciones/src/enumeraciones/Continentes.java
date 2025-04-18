/*
Repetimos lo aprendido con Dias.java
 */
package enumeraciones;

public enum Continentes {
    AFRICA(53, "1.2 billones"),
    EUROPA(46, "1.1 billones"),
    ASIA(44, "9 billones"),
    AMERICA(34, "12 billones"),
    OCEANIA(14, "90 billones");
    // en el otro archivo dias, no se agrego punto y coma al lado de Domingo, pero aca lo incluiremos.
    // solo es necesario el punto y coma, cuando vamos a seguir agregando elementos
    
    private final int paises;
    private String habitantes;
    
    Continentes(int paises, String habitantes){
        this.paises = paises;
        this.habitantes = habitantes;
    }
    
    //Metodo Get
    public int getPaises(){
        return this.paises;
    }
    public String getHabitantes(){
        return this.habitantes;
    }
}   
