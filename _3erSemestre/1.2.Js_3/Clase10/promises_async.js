/*
Clase 10 de JS3
Promises
*/

// async indica que una funcion regresa una promesa
async function miFuncionConPromesa(){
    return 'Saludos con promesas y asinc';
}
miFuncionConPromesa().then(valor => console.log(valor));

