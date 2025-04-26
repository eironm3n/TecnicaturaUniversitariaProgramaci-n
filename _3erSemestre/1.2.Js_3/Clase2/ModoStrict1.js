/*
Según Google:
El modo estricto en JavaScript, también conocido como "strict mode", es una característica introducida en ECMAScript 5 (ES5) que permite a 
los programadores escribir código JavaScript de una manera más segura y controlada. Al activar el modo estricto, se aplican reglas más 
estrictas al motor de JavaScript, lo que puede ayudar a evitar errores comunes y mejorar la optimización del código...
Para activar el modo estricto, se debe agregar la directiva "use strict"; al principio de un archivo JavaScript o al principio de una función. 


https://arielfuggini.com/javascript-modo-estricto/#:~:text=El%20Modo%20Estricto%20es%20una,con%20producir%20c%C3%B3digo%20m%C3%A1s%20seguro; 
*/

"use strict";
// Según profesor se considera una mala practica, sobre todo en proyectos grandes

var p = 20; //solo mostrara este valor por estar definido
console.log(p);

x = 10; // strict mostrara que no 'no esta definida'
console.log(x);


