//Arreglos Unidimensionales, array o vector
//Ejercicio 2
//Crear un arreglo unidimensional donde el usuario indique el tama�o por teclado luego de
//llenar el arreglo con numeros aleatorios entre 1-100 y por ultimo mostrar los elementos
//del arreglo

Proceso Array
	Definir i, num, n_elementos Como Entero;
	Dimension num[100];
	
	Escribir "Digite el numero de elementos para el arreglo: ";
	Leer n_elementos;
	
	Para i<-0 Hasta n_elementos Con Paso 1 Hacer
		num[i] <- azar(100);
	FinPara
	
	//Mostrar los elementos del arreglo
	Para i<-0 Hasta n_elementos Con Paso 1 Hacer
		Escribir num[i];
	FinPara
	
	
FinProceso
