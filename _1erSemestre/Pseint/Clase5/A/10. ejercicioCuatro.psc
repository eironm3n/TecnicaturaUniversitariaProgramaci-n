//Ejercicio 4
//Diseñe un algoritmo que elimine los espacios en blanco de un texto
Proceso ejercicioCuatro
	Definir frase, frase1 Como Cadena;
	Definir i Como Entero;
	
	Escribir Sin Saltar "Digite una cadena: ";
	Leer frase;
	
	i<-0;
	frase1<- "";
	Mientras (i<Longitud(frase)) Hacer
		//Si el elemento de la cadena es espacio, avanzamos
		Si Subcadena(frase,i,i) = ' ' Entonces
			i <- i+1;
		SiNo	//Si no concatenamos el elemento
			frase1 <- Concatenar(frase1,Subcadena(frase,i,i));
			i <- i+1;
		FinSi
	FinMientras
	
	frase <- frase1;
	Escribir "La cadena sin espacios es: ", frase;
FinProceso
