/* 
Polimorfismo
El polimorfismo en JavaScript permite a diferentes objetos responder al mismo método o 
propiedad de diversas maneras, a pesar de compartir una interfaz común. Esto se logra 
principalmente a través de la herencia prototípica y la sobrecarga de métodos. 
En esencia, significa que una función o método puede actuar de forma diferente dependiendo 
del objeto que la esté llamando.
*/

class Empleado {
    constructor(nombre, sueldo){
        this._nombre = nombre;
        this._sueldo = sueldo;
    }

    obtenerDetalles(){
        return `Empleado: nombre ${this._nombre}, sueldo: ${this._sueldo}`;
    }
}

class Gerente extends Empleado{
    constructor(nombre, sueldo, departamento){
        super(nombre, sueldo);
        this._departamento = departamento;
    }

    //Agregamos la sobreescritura
    obtenerDetalles(){
        return `Gerente: ${super.obtenerDetalles()} depto: ${this._departamento}`;
    }

}

// Objeto de la clase hija
let gerente1 = new Gerente("Carlos",5000,"Sistemas");
console.log(gerente1);

// Objeto de la clase padre
let empleado1 = new Empleado("Juan", 3000);
console.log(empleado1);


/*
En conclusión, obtiene de la clase padre(Empleado), las mismas caracteristicas
pero las sobreeescribe dentro de la clase hija
 */