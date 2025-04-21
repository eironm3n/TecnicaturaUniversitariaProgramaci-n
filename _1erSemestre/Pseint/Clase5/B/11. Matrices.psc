//Ejercicio 10: LLenando una matriz de  numeros aleatorios
//Hacer una matriz preguntando al usuario el numero de filas y columnas
//LLenar con numeros aleatorios, copiar el contenido a otra matriz y por ultimo mostrarla en pantalla
Proceso Matrices

	Definir matriz1,matriz2,i,j,filas,columnas Como Entero;
	Dimension matriz1[100,100],matriz2[100,100];
	
	Escribir Sin Saltar "Digite la cantidad de filas para la matriz: ";
	Leer filas;
	Escribir Sin Saltar "Digite la cantidad de columnas para la matriz: ";
	Leer columnas;
	//Llenamos la matriz con numeros aleatorios, copiamos y mostramos
	Para i<-0 Hasta 1 Con Paso 1 Hacer
		Para j<-0 Hasta 1 Con Paso 1 Hacer
			matriz1[i,j] <- azar(999);
			matriz2[i,j] <- matriz1[i,j];
			Escribir Sin Saltar matriz2[i,j]," ";
		FinPara
		Escribir "";
	FinPara
	Escribir "";
FinProceso
