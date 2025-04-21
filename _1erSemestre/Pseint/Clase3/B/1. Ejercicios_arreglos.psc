//Ejercicio 1
//Crea un arreglo unidimensional con un tamaño de 5 numeros reales, preguntale al usuario
//los valores y calcula la suma y promedio de todos ellos

Proceso Ejercicios_arreglos
	Definir i Como Entero;
	Definir numReales, suma, promedio Como Real;
	Dimension numReales[5];
	
	suma <- 0;
	//no olvidar de darle el valor de cero a suma, para luego ir sumando los nuevos valores
	
	Para i <- 0 Hasta 4 Con Paso 1 Hacer
		Escribir i, ". Dame un valor por favor: ";
		//No olvidar usar el mismo iterador para 'marcar' el lugar de inicio
		Leer numReales[i];
		suma <- suma + numReales[i];
		
	FinPara
	
	promedio <- suma /5;
	
	Escribir "La suma es ", suma, " y el promedio es ", promedio;
	
	
FinProceso
