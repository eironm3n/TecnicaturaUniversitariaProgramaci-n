Proceso Ejercicios_Arreglos
	// Ejercicio 4
	// Crear un arreglo unidimensional con N numeros
	// Leer los elementos por teclado, guardarlos en el arreglo
	// Calcula, cual de los numeros es el mayor de todos y cual el menor
	Definir mayor, menor, num Como Reales;
	Definir n_elementos, i Como Enteros;
	Dimension num[100];
	Repetir
		Escribir "Digite el numero de elementos para el arreglo: ";
		Leer n_elementos;
	Hasta Que n_elementos > 0
	Para i <-0 Hasta (n_elementos-1) Con Paso 1 Hacer
		//los arreglos se corren desde el cero en adelante, entonces, le restamo
		Escribir (i+1), ". Digite un numero: ";
		Leer num[i];
	FinPara
	mayor <- num[0];
	menor <- num[0];
	Para i<-1 Hasta (n_elementos-1) Con Paso 1 Hacer
		Si num[i] > mayor Entonces
			mayor <- num[i];
		SiNo
			Si num[i] < menor Entonces
				menor <- num[i];
			FinSi
		FinSi
	FinPara
	Escribir "El numero mayor es: ", mayor;
	Escribir "El numero menor es: ", menor;
FinProceso
