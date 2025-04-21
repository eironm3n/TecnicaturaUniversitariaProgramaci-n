//Funciones
//Funcion para sumar 2 numero
Funcion suma <- sumar(num1,num2) 	//Parametro
	Definir suma Como Entero;
	suma <- num1 + num2;
FinFuncion


Proceso Modularidad
	Definir num1,num2,resultado Como Entero;
	Escribir Sin Saltar "Digite un numero: ";
	Leer num1;
	Escribir Sin Saltar "Digite otro numero: ";
	Leer num2;
	
	resultado <- sumar(num1,num2); 	//Argumento
	Escribir "La suma es: ",resultado;
	//En esta funcion utilizamos el Argumento, aclarandolo dentro del modulo.
FinProceso
