/* funciones de tipo expresión
Podemos asignar una funcion a una variable sin mencionar el nombre de la funcion.
Tambien son llamadas funciones anonimas

*/

// Declaramos funcion de tipo expresion o anonima
let x = function(a,b){return a + b};    //necesita cierre con punto y coma
resultado = x(5,6); //al llamarla se pone la variable y parentesis
console.log(resultado)

/*
Las expresiones de función son más adecuadas para funciones anidadas, 
funciones de devolución de llamada (callbacks) o funciones que se pasan como argumentos.
*/