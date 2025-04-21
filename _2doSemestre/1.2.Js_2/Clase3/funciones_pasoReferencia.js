
//Tipos primitivos

// Paso por Referencia

const persona = {
    nombre: 'Juan',
    apellido: 'Lepez'
}
console.log(persona);

function cambiarValorObjeto(p1){
    p1.nombre = 'Ignacio';
    p1.apellido = 'Perez';
}   //aunque la funcion finalice y se destruya, los valores que se modifican quedan modificados.

cambiarValorObjeto(persona);
console.log(persona);
// aca se muestra que esta funcion deja los valores de un const de forma directa
