//Parametros por Valor
Funcion aumento<-aumentar(num)	//Parametro
	Definir aumento Como Entero;
	aumento <- num + 10;
FinFuncion


//Parametros por Referencia
SubProceso pedirDatos(num Por Referencia)		//Parametro
	Escribir Sin Saltar"Digite un numero: ";
	Leer num;
FinSubProceso

Proceso Modularidad
	Definir num Como Entero;
	pedirDatos(num);							//Argumento
	Escribir "El aumento es: ",aumentar(num);	//Argumento
FinProceso
