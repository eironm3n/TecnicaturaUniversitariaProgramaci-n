// Ejercicio 11: Matriz transpuesta
// Realice un programa que lea una matriz de 3*3 y cree su matriz transpuesta.
// La matriz transpuesta es aquella en la que la columna i era la fila i de la matriz (DiagramaNS)
// Ejemplo: 		1 2 3 	    	1 4 7
// 											4 5 6		-->		2 5 8
// 											7 8 9							3 6 9
Proceso Matrices
	Definir matriz,i,j Como Entero;
	Dimension matriz[3,3];
	// Llenar matriz
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 2 Hacer
			Escribir "Digite un numero[",i,"][",j,"]: ";
			Leer matriz[i,j];
		FinPara
	FinPara
	Escribir "";
	// Mostrar matriz transpuesta
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 2 Hacer
			Escribir Sin Saltar matriz[i,j]," ";
		FinPara
		Escribir "";
	FinPara
	Escribir "";
FinProceso
