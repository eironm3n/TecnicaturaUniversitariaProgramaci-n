'use strict';
// veamos como evitar este error

//y = 10; 
//esto no arrojara error y no podrá continuar

try {
    x=10;
    miFuncion();
}
catch ( error ){    //catchamos el error
    console.log( error );
}
finally{
    console.log('Termina la revisión de errores')
}

console.log('Continuamos...');

// en este caso el programa se desbloquea y continua con la ejecución