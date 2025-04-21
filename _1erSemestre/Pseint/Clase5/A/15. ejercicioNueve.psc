//Ejercicio 9
//Leer una frase y contar el numero de vocales(de cada una) que aparecen

Proceso ejercicioNueve
	Definir frase,letra Como Cadena;
	Definir i,contA,contE,contI,contO,contU Como Entero;
	
	Escribir Sin Saltar "Digite una cadena: ";
	Leer frase;
	
	frase <- Minusculas(frase);
	contA <- 0;
	contE <- 0;
	contI <- 0;
	contO <- 0;
	contU <- 0;
	
	Para i<-0 Hasta (Longitud(frase)-1) Hacer
		letra <- Subcadena(frase,i,i);
		Si letra = "a" Entonces
			contA <- contA+1;
		SiNo
			Si letra = "e" Entonces
				contE <- contE + 1;
			SiNo
				Si letra = "i" Entonces
					contI <- contI + 1;
				SiNo
					Si letra = "o" Entonces
						contO <- contO +1;
					SiNo
						Si letra = "u" Entonces
							contU <- contU + 1;
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinPara
	
	Escribir "";
	Escribir "Conteno A: ",contA;
	Escribir "Conteno E: ",contE;
	Escribir "Conteno I: ",contI;
	Escribir "Conteno O: ",contO;
	Escribir "Conteno U: ",contU;
	
FinProceso
