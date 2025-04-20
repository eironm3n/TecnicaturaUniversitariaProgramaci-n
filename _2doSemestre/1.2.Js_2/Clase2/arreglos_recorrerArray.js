
// Recorrer todos los elementos de un arreglo

const autos = ['Ferrari', 'Renault', 'BMW']
console.log(autos[0]);
// similar a java y python, se indica el elemento con corchetes
console.log(autos[-1]);

// recorremos el array con for
for(let i = 0; i < autos.length ; i++){
    console.log(i+' : '+autos[i])
}
