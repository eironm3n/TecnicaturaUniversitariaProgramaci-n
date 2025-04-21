// Ejercicio 4
// Hacer un algoritmo que llene una matriz de 3*4.
// Sumar las columnas e imprimir que columna tuvo la maxima suma y la suma de esa columna
Proceso Matrices
	Definir num, i, j Como Entero;
	Definir mayor, suma_col, posCol Como Entero;
	Dimensionar num(3,4);
	// Pedimos los elementos de la matriz
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 3 Hacer
			Escribir 'Digite un numero[', i, '][', j, ']: 'Sin Saltar;
			Leer num[i,j];
		FinPara
	FinPara
	Escribir '';
	// Mostramos la matriz
	Para i<-0 Hasta 2 Con Paso 1 Hacer
		Para j<-0 Hasta 3 Con Paso 1 Hacer
			Escribir num[i,j], ' 'Sin Saltar;
		FinPara
		Escribir '';
	FinPara
	// Almacenamos dentro de mayor la suma de los elementos de la primera columna
	suma_col <- 0;
	Para i<-0 Hasta 2 Con Paso 1 Hacer
		suma_col <- suma_col+num[i,0];
	FinPara
	// Por el momento la primera columna es la que tiene la mayor suma_col
	mayor <- suma_col;
	posCol <- 0;
	// Ahora, vamos a recorrer la demas columnas y sumamos
	Para j<-1 Hasta 3 Con Paso 1 Hacer
		suma_col <- 0;
		Para i<-0 Hasta 2 Con Paso 1 Hacer
			suma_col <- suma_col+num[i,j];
		FinPara
		Si suma_col>mayor Entonces
			mayor <- suma_col;
			posCol <- j;
		FinSi
	FinPara
	Escribir '';
	Escribir 'La columna con la mayor suma es: ', posCol;
	Escribir 'La suma de dicha columna es: ', mayor;
	Escribir '';
FinProceso
