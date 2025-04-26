//Polimorfismo - Continuamos con instanceof

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

    //Sobreescritura
    obtenerDetalles(){
        return `Gerente: ${super.obtenerDetalles()}
        depto: ${this._departamento}`;
    }

}

function imprimir( tipo ){
    console.log( tipo.obtenerDetalles() );
    if( tipo instanceof Gerente){
        console.log('Es un gerente');
        console.log( tipo.departamento);    //esto dará undefined
        // sin embargo, podemos llavar al objeto dentro
        console.log( tipo._departamento); 
    }
    else if( tipo instanceof Empleado){
        console.log('Es un empleado')
        //pero aca no lo mostrará ya que solo pertenece a clase hija
        console.log( tipo._departamento); 
    }
    else if( tipo instanceof Object){
        console.log('Es de tipo objeto')
    }
}   


let gerente1 = new Gerente("Carlos",5000,"Sistemas");
console.log(gerente1);  // Objeto de la clase hija
let empleado1 = new Empleado("Juan", 3000);
console.log(empleado1); // Objeto de la clase padre

// uso de tipo
// segun el tipo que le pasemos, sera la información que obtendremos
imprimir( gerente1 );
imprimir( empleado1 );

