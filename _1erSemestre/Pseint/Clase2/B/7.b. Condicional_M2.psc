// Ejercicio 7-b
// Elaborar un programa que me muestre el significado de aniversario de cada decada hasta los 60
Proceso Condicional_M2
	Definir decada Como Entero;
	Escribir 'Digite una decada: ';
	Leer decada;
	Segun decada Hacer
		10:
			Escribir 'Bodas de Hojalata';
		20:
			Escribir 'Bodas de Porcelana';
		30:
			Escribir 'Bodas de Perlas';
		40:
			Escribir 'Bodas de Rubi';
		50:
			Escribir 'Bodas de Oro';
		60:
			Escribir 'Bodas de Diamante';
		De Otro Modo:
			Escribir 'Decada no existente';
	FinSegun
FinProceso
