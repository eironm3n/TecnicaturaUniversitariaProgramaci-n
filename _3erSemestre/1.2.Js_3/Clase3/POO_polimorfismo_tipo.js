 
//Polimorfismo - Continuamos con lo trabajado la clase anterior


class Empleado {
    constructor(nombre, sueldo){
        this._nombre = nombre;
        this._sueldo = sueldo;
    }

    obtenerDetalles(){
        return `Empleado: nombre ${this._nombre},
        Sueldo: ${this._sueldo}`;
    }
}

class Gerente extends Empleado{
    constructor(nombre, sueldo, departamento){
        super(nombre, sueldo);
        this._departamento = departamento;
    }

    //Agregamos la sobreescritura
    obtenerDetalles(){
        return `Gerente: ${super.obtenerDetalles()}
        depto: ${this._departamento}`;
    }

}

//
function imprimir( tipo ){
    console.log( tipo.obtenerDetalles() );
}

// Objeto de la clase hija
let gerente1 = new Gerente("Carlos",5000,"Sistemas");
console.log(gerente1);

// Objeto de la clase padre
let empleado1 = new Empleado("Juan", 3000);
console.log(empleado1);

imprimir( gerente1 );
imprimir( empleado1 );

/* A traves de imprimir podemos ver los valores de cada una de estas instancias
Es decir, con tipo, podes obtener todos los valores referenciados a obtenerDetalles()
Entonces no es necesario pedir si existe 'un empleado' o 'un gerente', solo pedimos 
los etalles relacionados a obtenerDetalles.
Luego podemos directamente colocar imprimir y su elemento */
