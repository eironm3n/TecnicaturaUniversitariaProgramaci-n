Proceso Ejercicios_Arreglos
	// Ejercicio5
	// Leer 8 numeros enteros dentro de un arreglo
	// Debemos mostrarlo en el siguiente orden: primero, ultimo, segundo, penultimo, tercero, etc
	Definir num,i Como Entero;
	Dimension num[8];
	Para i<-0 Hasta 7 Hacer
		Escribir (i+1),". Digite un numero: ";
		Leer num[i];
	FinPara
	Para i<-0 Hasta 3 Hacer
		Escribir num[i];
		Escribir num[7-i];
	FinPara
FinProceso
