// Ejercicio 14: Producto de matrices
// Realice un programa que calcule el producto de dos matrices cuadradas de 3*3(DiagramaFlujo)
Proceso Matrices
	Definir matriz1, matriz2, matriz3, i, j, k Como Entero;
	Dimensionar matriz1(3,3), matriz2(3,3), matriz3(3,3);
	// Llenamos y mostramos matriz1
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 2 Hacer
			matriz1[i,j] <- azar(10);
			Escribir Sin Saltar matriz1[i,j],' ';
		FinPara
		Escribir '';
	FinPara
	Escribir '';
	// Llenamos y mostramos matriz2
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 2 Hacer
			matriz2[i,j] <- azar(10);
			Escribir Sin Saltar matriz2[i,j], ' ';
		FinPara
		Escribir '';
	FinPara
	Escribir '';
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 2 Hacer
			// Limpiamos asignando un cero
			matriz3[i,j]<-0;
			Para k<-0 Hasta 2 Hacer
				matriz3[i,j]<- matriz3[i,j]+matriz1[i,j]*matriz2[k,j];
			FinPara
		FinPara
	FinPara
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 2 Hacer
			Escribir Sin Saltar matriz3[i,j], ' ';
		FinPara
		Escribir '';
	FinPara
	Escribir '';
FinProceso
