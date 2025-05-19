/*
Formas de utilizar los Callbacks
Aqui se utilizará setTimeout
*/

// Llamadas asincronas con uso setTimeout
function miFuncionCallback(){
    console.log('Saludo asincrono despues de 3 segundos')
}
//esta funcion toma los valores de segundos, en Milisegundos
//investigar medidas de tiempo tomadas
setTimeout(miFuncionCallback,3000)
//esto son 3 segundos

setTimeout( function(){ console.log('Saludo Asincrono 2') },4000 );
//estos son 4 segundos

setTimeout( () => console.log('Saludo Asincrono 3'), 5000 );
//estos son 5 segundos
