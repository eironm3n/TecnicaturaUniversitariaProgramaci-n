// Otro ejemplo de polimorfismo

class Animal {
    constructor(nombre) {
      this.nombre = nombre;
    }
  
    hacerSonido() {
      return "No sé cómo hacer un sonido";
    }
  }
  
  class Perro extends Animal {
    hacerSonido() {
      return "Guau!";
    }
  }
  
  class Gato extends Animal {
    hacerSonido() {
      return "Miau!";
    }
  }
  
  const perro = new Perro("Max");
  const gato = new Gato("Luna");
  
  console.log(perro.hacerSonido()); // Output: Guau!
  console.log(gato.hacerSonido());   // Output: Miau!