Proceso Busqueda_Secuencial
	Definir encontrado Como Logico;
	Definir num,i,posicion, dato Como Entero;
	Dimension num[5];
	
	Escribir "Digite los elementos del arreglo";
	
	Para i<-0 Hasta 4 Con Paso 1 Hacer
		Escribir Sin Saltar i, ". Digite un numero: ";
		Leer num[i];
	FinPara
	
	Escribir " ";
	Escribir "Digite un elemento a buscar: ";
	Leer dato;
	
	encontrado <- falso;
	i<-0;
	
	//Busqueda Secuencial
	Mientras (i<5 Y encontrado = falso) Hacer
		Si (num[i] = dato) Entonces
			encontrado <- Verdadero;
			posicion <- i;
		FinSi
		i <- i + 1;
	FinMientras
	
	Si encontrado = Verdadero Entonces
		Escribir "El elemento ",dato," SI existe en el arreglo, posicion: ",posicion;
	SiNo
		Escribir "El elemento no existe.";
	FinSi
	
	
FinProceso