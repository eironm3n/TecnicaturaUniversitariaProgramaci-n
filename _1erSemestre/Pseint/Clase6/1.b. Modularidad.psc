//Funciones
//Funcion para sumar 2 numero
Funcion suma <- sumar(num1,num2) 	//Parametro
	Definir suma Como Entero;
	suma <- num1 + num2;
FinFuncion


Proceso Modularidad
	Definir num1,num2 Como Entero;
	Escribir Sin Saltar "Digite un numero: ";
	Leer num1;
	Escribir Sin Saltar "Digite otro numero: ";
	Leer num2;

	Escribir "La suma es: ",sumar(num1,num2);
	//En esta, utilizamos el Parametro, en el lugar del Argumento
FinProceso
