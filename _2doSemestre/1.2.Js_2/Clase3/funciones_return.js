/* return
Esta instrucción 'return' en JavaScript se utiliza para finalizar la 
ejecución de una función y devolver un valor al origen de la llamada.
Permite que la función proporcione resultados útiles, como números, 
cadenas u objetos, que pueden usarse en otras partes del código.
*/

function miFuncion(a,b){
    return a + b;
}

// Definimos la variable y dentro ingresamos la funcion y le damos valores
let resultado = miFuncion(6,7);
console.log(resultado); // esto mostrara 13 ya que toma la logica que ocurre en miFuncion

