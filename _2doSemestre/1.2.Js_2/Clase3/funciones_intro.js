/*
Introducción a Funciones
Para las funciones se utiliza CamelCase (averiguar si se puede otro tipo de escritura)

*/ 

miFuncion(8,2)      // a esto se lo conoce como hoisting, se puede hacer el llamado a la funcion incluso antes de definirla

function miFuncion(a,b){
    console.log("Sumamos: "+ (a+b));
}

// Llamamos a la función
miFuncion(5,4);

