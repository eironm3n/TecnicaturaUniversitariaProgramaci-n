//Parametros por valor
Funcion aumento<-aumentar(num)	//Parametro
	Definir aumento Como Entero;
	aumento <- num + 10;
FinFuncion

Proceso Modularidad
	Definir num Como Entero;
	Escribir Sin Saltar "Digite un numero: ";
	Leer num;
	
	Escribir "El aumento es: ",aumentar(num);	//Argumento
FinProceso
