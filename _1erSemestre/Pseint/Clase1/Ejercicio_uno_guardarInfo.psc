//Clase 1 Capitulo: Elementos de entorno de algoritmo y programación ->  Ejercicios
//Ejercicio para determinar si una persona es mayor de edad

Proceso Ejercicios
	//en estas dos variables se almacenan solo caracteres o cadena de caracteres
	Definir nombre Como Caracter;
	Definir apellido Como Caracter;	
	Definir edad como Entero;		//en esta variable se almacenan elementos enteros, como: 1,2,15,29,199,etc
	Definir altura Como Real;		//en esta variable se estaran guardando elementos de tipo Real, como: 2.83, 10.14, etc
	Definir esMayorEdad Como Logico;	//en esta variable se estaran guardando elementos de tipo logico, puede ser el V o F
	
	//almacenamos los elementos y el tipo que vamos a guardar en estas variables
	nombre <- "Aron";
	apellido <- "Rojas";
	edad <- 28;
	altura <- 1.70;
	esMayorEdad <- (edad > 18);
	
	//con escribir mostramos por pantalla, lo que queremos que el usuario 'pueda ver'
	Escribir "Su nombre es: ", nombre;
	Escribir "Su apellido es: ", apellido;
	Escribir "Su edad es: ",edad,". Por ahora jaja";
	Escribir "Su altura es: ", altura,"mts.";
	Escribir "Es mayor de edad? ",esMayorEdad;
	
	Escribir "Muchas gracias vuelvas prontos";
	
FinProceso
