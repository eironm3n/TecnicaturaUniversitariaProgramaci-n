// Ejercicio 12: Suma de matrices
// Realice un programa que calcule la suma de 2 matrices cuadradas de 3*3
// Se solicita que el usuario ingrese una matriz en forma Ascendente y 
// la otra en forma Descendente y el resultado al sumarlas, seria una matriz
// de solo 10 numeros
Proceso Matrices
	Definir matriz1, matriz2, i, j Como Entero;
	Dimensionar matriz1(3,3), matriz2(3,3);
	// Llenamos las matrices
	Escribir 'Usted debe ingresar una matriz ascendente';
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 2 Hacer
			Escribir 'Digite un numero[', i, '][', j, ']: 'Sin Saltar;
			Leer matriz1[i,j];
		FinPara
	FinPara
	Escribir '';
	Escribir 'Usted debe ingresar una matriz descendente';
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 2 Hacer
			Escribir 'Digite un numero[', i, '][', j, ']: 'Sin Saltar;
			Leer matriz2[i,j];
		FinPara
	FinPara
	Escribir '';
	// Mostramos las dos matrices
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 2 Hacer
			Escribir matriz1[i,j], ' 'Sin Saltar;
		FinPara
		Escribir '';
	FinPara
	Escribir '';
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 2 Hacer
			Escribir matriz2[i,j], ' 'Sin Saltar;
		FinPara
		Escribir '';
	FinPara
	Escribir '';
	// Mostramos las matrices sumadas
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 2 Hacer
			Escribir matriz1[i,j]+matriz2[i,j], ' 'Sin Saltar;
		FinPara
		Escribir '';
	FinPara
	Escribir '';
FinProceso
