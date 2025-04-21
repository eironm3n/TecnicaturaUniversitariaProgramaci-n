// Ejercicio 5
// Diseñar un algoritmo que pida al usuario 5 apellidos, los almacene en un arreglo
// y posteriormeten muestre los apellidos ordenados alfabeticamente
// DiagramaFlujo
Proceso Principal
	Definir apellidos Como Cadena;
	Dimension apellidos[5];
	// Primero vamos a pedir los apellidos
	pedirDatos(apellidos);
	// Ahora, ordenamos los apellidos
	ordenar(apellidos);
	// Por ultimo mostramos los apellidos
	mostrarDatos(apellidos);
	Escribir "";
FinProceso

SubProceso pedirDatos(apellidos por Referencia)
	Definir i Como Entero;
	Para i<-0 Hasta 4 Con Paso 1 Hacer
		Escribir Sin Saltar (i+1),". Digite un apellido: ";
		Leer apellidos[i];
	FinPara
FinSubProceso

SubProceso ordenar(apellidos por Referencia)
	Definir i,j Como Entero;
	Definir aux Como Cadena;
	Para i<-0 Hasta 3 Con Paso 1 Hacer
		Para j<-0 Hasta 3 Con Paso 1 Hacer
			Si apellidos[j] > apellidos[j+1] Entonces
				aux <- apellidos[j];
				apellidos[j] <- apellidos[j+1];
				apellidos[j+1] <- aux;
			FinSi
		FinPara
	FinPara
FinSubProceso

SubProceso mostrarDatos(apellidos)
	Definir i Como Entero;
	Escribir "";
	Escribir "Los apellidos ordenados alfabeticamente son: ";
	Para i<-0 Hasta 4 Con Paso 1 Hacer
		Escribir (i+1),". ",apellidos[i];
	FinPara
FinSubProceso
