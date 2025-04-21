//Llenar una matriz
Proceso Matrices
	Definir num,i,j Como Entero;
	Dimension num[3,3];
	
	//LLenar una matriz, comenzando las filas
	Para i<-0 Hasta 2 Con Paso 1 Hacer
		//LLenando las columnas
		Para j<-0 Hasta 2 Con Paso 1 Hacer
			Escribir Sin Saltar "Digite un numero [",i,"] [",j,"]: ";
			Leer num[i,j];
		FinPara
	FinPara
	
	//Mostrar una matriz
	Para i<-0 Hasta 2 Con Paso 1 Hacer
		Para j<-0 Hasta 2 Con Paso 1 Hacer
			Escribir Sin Saltar num[i,j], " ";
		FinPara
		Escribir "";
	FinPara
FinProceso
