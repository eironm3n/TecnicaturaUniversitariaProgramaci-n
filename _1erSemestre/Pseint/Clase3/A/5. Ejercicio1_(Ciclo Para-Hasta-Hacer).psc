//Ejercicio 1 (Ciclo Para- Hasta- Hacer)
// Calcular la suma de los "N" primeros n°s
//Ej: S = 1 + 2 + 3 ... + N

Proceso Principal
	Definir N, suma, i Como Entero;
	Escribir "Digite la cantidad de numeros a sumarse: ";
	Leer N;
	
	suma <- 0;	//asignamos el 0 para que tome un valor vacio
	
	Para i <- 1 Hasta N Con Paso 1 Hacer
		suma <- suma + i;		//suma iterativa
	FinPara
	//esto sumará los valores del 1 en adelante, hasta llegar al tope de N. Ahi frena y entrega la 'suma'
	//esto hara que se vaya avanzando de 1 en 1 hasta llegar al numero N que ingresariamos por teclado
	
	Escribir "La suma es: ", suma;
	
FinProceso
