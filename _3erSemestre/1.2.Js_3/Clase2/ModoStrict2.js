// "use strict";

var p = 20; //solo mostrara este valor por estar definido
console.log(p);

function miFuncion(){
    "use strict"
    x = 10; // strict mostrara que no 'no esta definida'
    console.log(x);
}
miFuncion();

/* 
En ocasiones al ejecutar con quokka, ocurre que puede no tomar la funcionalidad de 
'use strict' dentro de funciones o por separado..
El ejemplo de la ejecucion de arriba , se puede probar al usar 2 veces use strict e 
intentar ejecutar..
*/