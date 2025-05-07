'use strict';
// utilizaremos la clausula throw

try {
    x=10;
    throw'Mi error';
}
catch ( error ){    //catchamos el error
    console.log( error );
}
finally{
    console.log('Termina la revisión de errores')
}

console.log('Continuamos...');

let resultado = 5;

try{
    //y = 5;
    if( isNaN(resultado) ) throw 'No es un número';
    else if(resultado ==='') throw 'Es cadena vacia';
    else if( resultado >= 0) throw 'Es valor positivo';
}
catch(error){
    console.log(error);
    console.log(error.name);
    console.log(error.message);
}
finally{
    console.log('Termina la revision de errores')
}
