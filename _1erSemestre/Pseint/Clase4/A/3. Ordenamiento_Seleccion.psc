Proceso Ordenamiento_Seleccion
	Definir i,j,min,aux,num Como Entero;
	Dimension num[5];
	
	Escribir "Digite el valor de los elementos del arreglo: ";
	Para i<-0 Hasta 4 Con Paso 1 Hacer
		Escribir (i+1),". Digite un numero: ";
		Leer num[i];
	FinPara
	
	//Método de Selección
	Para i<-0 Hasta 3 Con Paso 1 Hacer
		min <- i;
		Para j <- i+1 Hasta 4 Con Paso 1 Hacer
			Si num[j]<num[min] Entonces
				min<-j;
			FinSi
		FinPara
		aux <- num[i];
		num[i] <- num[min];
		num[min] <- aux;
	FinPara
	
	Escribir " ";
	Escribir "El arreglo esta ordenado";
	Para i<-0 Hasta 4 Con paso 1 Hacer
		Escribir Sin Saltar num[i];
	FinPara
	
	Escribir " ";
	Escribir "El arreglo va al reves";
	Para i<-0 Hasta 4 Con paso -1 Hacer
		Escribir Sin Saltar num[i];
	FinPara
	
	Escribir " ";
FinProceso
