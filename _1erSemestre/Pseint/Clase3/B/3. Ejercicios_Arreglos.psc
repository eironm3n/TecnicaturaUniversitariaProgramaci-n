Proceso Ejercicios_Arreglos
	//revisar el codigo atentamente, no coincide con el video
	// Ejercicio3
	// Crear un arreglo con unidimensional con N caracteres, leer
	// los elementos por teclado, guardarlos en el arreglo y mostrarlos
	// en el orden inverso al introducido
	Definir letras como caracter;
	Dimension letras[100];
	Definir n_elementos,i como enteros;
	// Desde el diagrama N/S asi se visualiza el 'Repetir'
	Repetir
		Escribir "Digite el numero de elementos para el arreglo: ";
		Leer n_elementos;
	Hasta Que n_elementos > 0
	Para i<-0 Hasta (n_elementos-1) Hacer
		Escribir (i+1), "Digite un numero: ";
		Leer letras[i];
	FinPara
	Para i<-(n_elementos-1) Hasta 0 Con Paso -1 Hacer
		Escribir letras[i];
	FinPara
FinProceso
