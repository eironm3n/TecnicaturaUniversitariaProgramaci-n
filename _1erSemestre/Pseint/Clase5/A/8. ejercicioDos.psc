// Ejercicio2
// Calcular la longitud de 2 cadenas de caracteres, y mostrar la cadena con la mayor longitud
// DiagramaFlujo
Proceso ejercicioDos
	Definir frase1,frase2 Como Caracter;
	Escribir "Digite una cadena: ";
	Leer frase1;
	Escribir "Digite otra cadena: ";
	Leer frase2;
	Escribir " ";
	Si Longitud(frase1) = Longitud(frase2) Entonces
		Escribir "Ambas cadenas tienen la misma longitud";
	SiNo
		Si Longitud(frase1) > Longitud(frase2) Entonces
			Escribir "La cadena numero uno es la mas larga, contiene ",longitud(frase1)," caracteres";
			Escribir " ";
			Escribir "La frase brindada fue: ", frase1;
		SiNo
			Escribir "La cadena numero dos es la mas larga, contiene", Longitud(frase2)," caracteres";
			Escribir " " ;
			Escribir "La frase brindada fue: ",frase2;
		FinSi
	FinSi
FinProceso
