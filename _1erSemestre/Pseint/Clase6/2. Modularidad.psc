//Procedimiento

SubProceso mitad(num)
	Definir m Como Real;
	m <- num/2;
	Escribir "La mitad del numero es: ",m;
FinSubProceso

Proceso Modularidad
	Definir num Como Real;
	Escribir Sin Saltar "Digite un numero: ";
	Leer num;
	mitad(num);
	
FinProceso
