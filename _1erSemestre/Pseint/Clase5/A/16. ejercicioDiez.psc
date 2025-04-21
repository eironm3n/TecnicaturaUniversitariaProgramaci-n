//Ejercicio 10
//Realizar un programa que permita contabilizar cuantas veces una subcadena se repite dentro de una frase
Proceso ejercicioDiez
	Definir i, contador Como Entero;
	Definir frase, subfrase,palabra Como Cadena;
	
	Escribir Sin Saltar "Digite una cadena: ";
	Leer frase;
	Escribir Sin Saltar "Digite una palabra a buscar en la frase: ";
	Leer subfrase;
	
	i <- 0;
	contador <- 0;
	//Si puedes imaginarlo, puedes programarlo
	Mientras i<Longitud(frase) Hacer
		palabra <- "";
		Si Subcadena(frase,i,i) <> " " Entonces
			//Almcacenar la palabra completa dentro de la variable palabra 
			Mientras Subcadena(frase,i,i) <> " " Y i<Longitud(frase) Hacer
				palabra <- Concatenar(palabra,Subcadena(frase,i,i));
				i <- i+1;
			FinMientras
			
			Si palabra = subfrase Entonces
				contador <- contador +1;
			FinSi
		SiNo
			//Es un espacio
			Mientras Subcadena(frase,i,i) = " " Y i<Longitud(frase) Hacer
				i <- i +1;
			FinMientras
		FinSi
	FinMientras
	
	Escribir "";
	Escribir "La palabra: ", subfrase, " se repite ", contador, " veces";
	
FinProceso
