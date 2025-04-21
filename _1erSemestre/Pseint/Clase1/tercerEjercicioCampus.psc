Proceso Ejercicios
	//Ejercicio 3
	
	Definir a, b, aux Como Entero;
	Escribir "Digite el valor de a: ";		//ingresar 10
	Leer a;
	Escribir "Digite el valor de b: ";		//ingresar 5
	Leer b;
	
	aux <- a; //guardamos el valor de a dentro de aux
	a <- b; //pasamos el valor de b hacia a
	b <- aux; //pasamos el valor de aux(a) hacia b
	
	Escribir "El nuevo valor de a es: ", a;
	Escribir "El nuevo valor de b es: ", b;
	
	Escribir "Muchas gracias vuelvas prontos";
FinProceso
