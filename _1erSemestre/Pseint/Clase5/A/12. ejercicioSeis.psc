//Ejercicio 6
//Dise�ar un algoritmo que tomando como entrada una cadena de texto nos devuelva si es o no un pal�ndromo.
//Se conoce que se denomina pal�ndromo a una palabra o frase que, ignorando los blancos, se lee igual de 
//izquierda a derecha que se de derecha a izquierda
Proceso ejercicioSeis
	Definir i Como Entero;
	Definir frase, frase2, fraseReves Como Cadena;
	
	Escribir "Digite una cadena: ";
	Leer frase;
	
	i <- 0;
	frase2 <- "";
	
	//Eliminamos los espacios en blanco de la cadena
	Mientras i<Longitud(frase) Hacer
		Si Subcadena(frase,i,i) <> " " Entonces
			frase2 <- Concatenar(frase2,Subcadena(frase,i,i));
			i <- i+1;
		SiNo
			i <- i+1;
		FinSi
	FinMientras
	
	frase <- frase2;
	//Hallar la frase al reves
	fraseReves <- "";
	Para i<-(Longitud(frase)-1) Hasta 0 Con Paso -1 Hacer
		fraseReves <- Concatenar(fraseReves, Subcadena(frase,i,i));
	FinPara
	
	//Por ultimo, comparamos ambas cadenas
	Si frase = fraseReves Entonces
		Escribir "La cadena es un palidromo: ",frase;
	SiNo
		Escribir "La cadena NO es un palindromo: ",frase;
	FinSi
FinProceso
