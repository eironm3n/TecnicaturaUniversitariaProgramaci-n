Proceso Ordenamiento_Burbuja
	Definir num,i,aux,pos Como Entero;
	Dimension num[5];
	
	Escribir "Digite el valor de los elementos del arreglo: ";
	Para i<-0 Hasta 4 Con Paso 1 Hacer
		Escribir (i+1),". Digite un numero: ";
		Leer num[i];
	FinPara
	
	//Método de inserción
	Para i<-1 Hasta 4 Con Paso 1 Hacer
		pos <- i;
		aux<-num[i];
		Mientras (pos > 0 Y num[pos-1] > aux) Hacer
			num[pos] <- num[pos-1];
			pos <- pos-1;
		FinMientras
		num[pos]<-aux;
	FinPara
	
	Escribir " ";
	Escribir "El arreglo esta ordenado";
	Para i<-0 Hasta 4 Con paso 1 Hacer
		Escribir Sin Saltar num[i];
	FinPara
	
	Escribir " ";
	Escribir "El arreglo va al reves";
	Para i<-4 Hasta 0 Con paso -1 Hacer
		Escribir Sin Saltar num[i];
	FinPara
	
	Escribir " ";
FinProceso
