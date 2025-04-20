
// Modificar los elementos de un arreglo

const autos = ['Ferrari', 'Renault', 'BMW']

// Modificamos el elemento 1 del arreglo
autos[1] = 'Volvo';
console.log(autos[1]);

// Agregamos nuevos valores al arreglo
autos.push('Audi'); // Agregamos el elemento al final del arreglo
console.log(autos);

// Segunda forma de agregar elementos
autos[autos.length] = 'Porsche'
console.log(autos);

// Tercer forma de agregar elementos pero CUIDADO
autos[6] = 'Renault';
console.log(autos)
// esto estirara el arreglo hasta donde lo especifiquemos en los corchetes


