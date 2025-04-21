//Ejercicio7
//Hacer un programa para rellenar una matriz pidiendo al usuario el numero de filas y columnas
//posteriormente mostrar la matriz en pantalla
Proceso Matrices
	Definir matriz,filas, columnas,i,j Como Entero;
	Dimension matriz[100,100]; //Esto cuando no sabemos la Dimension
	
	//Pedimos el numero de filas al usuario
	Escribir "Digite el numero de filas para la matriz: ";
	Leer filas;
	//Pedimos el numero de columnas al usuario
	Escribir "Digite el numero de columnas para la matriz: ";
	Leer columnas;
	
	//Llenamos la matriz
	Para i<-0 Hasta filas-1 Con Paso 1 Hacer
		Para j<-0 Hasta columnas-1 Con Paso 1 Hacer
			Escribir Sin Saltar "Digite un numero[",i,"][",j,"]: ";
			Leer matriz[i,j];
		FinPara
	FinPara
	Escribir "";
	
	//Mostramos la matriz
	Escribir "";
	Para i<-0 Hasta filas-1 Con Paso 1 Hacer
		Para j<-0 Hasta columnas-1 Con Paso 1 Hacer
			Escribir Sin Saltar matriz[i,j];
		FinPara
		Escribir "";
	FinPara
	Escribir "";
	
FinProceso
