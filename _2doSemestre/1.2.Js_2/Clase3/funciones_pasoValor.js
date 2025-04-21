
// Tipos primitivos

let k = 10;   //variable global

function cambiarValor(a){   //Paso por valor
    a = 20; //variable dentro de la estructura
}

cambiarValor(k);
console.log(k);
