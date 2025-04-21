// tipos de datos en una funcion

let x = function(a,b){return a + b};    //necesita cierre con punto y coma
resultado = x(5,6); //al llamarla se pone la variable y parentesis
console.log(resultado)

console.log(typeof miFuncion);

function miFuncion2(a,b){
    console.log(arguments); // para ver los argumentos asociados
    console.log(arguments.length);
}
miFuncion2(5,7,4,7);

//toString
var miFuncionTexto = miFuncion2.toString();
console.log(miFuncionTexto);
// toString convierte nuestra función a texto
