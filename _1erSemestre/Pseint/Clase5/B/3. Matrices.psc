//Matrices, ejercicio 2
//Hacer un algoritmo que llene un matriz de 4*4 y determine la posicion [fila,columa] del numero mayor almacenado en la matriz

Proceso Matrices
	Definir num,i,j,mayor,posfila,posCol Como Entero;
	Dimension num[4,4];
	
	//Pedimos los elementos de la matriz
	Para i<-0 Hasta 3 Hacer
		//LLenando las columnas
		Para j<-0 Hasta 3 Hacer
			Escribir Sin Saltar "Digite un numero [",i,"] [",j,"]: ";
			Leer num[i,j];
		FinPara
	FinPara
	
	//Mostrar la matriz en pantalla
	Escribir "";
	Para i<-0 Hasta 3 Hacer
		Para j<-0 Hasta 3 Hacer
			Escribir Sin Saltar num[i,j], " ";
		FinPara
		Escribir "";
	FinPara
	
	mayor <- 0;
	Para i<-0 Hasta 3 Hacer
		Para j<-0 Hasta 3 Hacer
			Si num[i,j] > mayor Entonces
				mayor <- num[i,j];
				posfila <- i;
				posCol <- j;
			FinSi
		FinPara
	FinPara
	
	Escribir "";
	Escribir "La posicion del numero es: ",posfila," Columna: ",posCol;
	Escribir "El numero mayor es: ",mayor;
	
FinProceso
