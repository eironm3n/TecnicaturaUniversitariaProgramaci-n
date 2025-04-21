//Argumentos y Parametros

let sumar = function(a=4,b=8){
    console.log(arguments[0]);  //muestra el párametro de a
    console.log(arguments[1]);  //muestra el párametro de b
    // console.log(arguments[2]);
    // return a + b;
    return a + b + arguments[2];
}

resultado = sumar(3,5,9);
//resultado = sumar();
console.log(resultado); 
//esto arrojaria 17 ya que sobreescribe los valores indicados como argumentos en la linea 3

