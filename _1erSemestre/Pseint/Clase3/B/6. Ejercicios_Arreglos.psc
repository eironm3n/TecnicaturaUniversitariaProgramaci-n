Proceso Ejercicios_Arreglos
	// Ejercicio6
	// Leer por teclado una serie de numeros reales
	// El programa debe indicarnos si estan ordenados de forma creciente o si estan desordenados
	Definir i Como Entero;
	Definir creciente, decreciente Como Logico;
	Definir num Como Real;
	Dimensionar num(5);
	Para i<-0 Hasta 4 Con Paso 1 Hacer
		Escribir (i+1), '. Digite un numero: ';
		Leer num[i];
	FinPara
	creciente <- falso;
	decreciente <- falso;
	Para i<-0 Hasta 3 Con Paso 1 Hacer
		Si num[i] < num[i+1] Entonces
			creciente <- verdadero;
		SiNo
		FinSi
		Si num[i] > num[i+1] Entonces
			decreciente <- verdadero;
		FinSi
	FinPara
	Si creciente  = verdadero y decreciente = falso Entonces
		Escribir "El arreglo esta en forma creciente";
	SiNo
		Si creciente = falso y decreciente = verdadero Entonces
			Escribir "El arreglo esta en forma decreciente";
		FinSi
	FinSi
FinProceso
