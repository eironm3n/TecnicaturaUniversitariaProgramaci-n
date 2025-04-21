//Ejercicio 9 (supuestamente Ejercicio 5 de Ciclos, u orden 35)
//Calcular el factorial de un numero mayor o igual a 0.


//La función factorial se representa con un signo de exclamación (!) detrás de un número. Por ejemplo, 6! se llama generalmente "6 factorial"
//Ej: si decimos 5!(se lee 5 factorial) su calculo serian todos los numeros entre el 0 y 5.
//Es decir, se calcula asi: 5! = 1.2.3.4.5 = 120. Entonces, el 5! = 120
Proceso Ciclos
	Definir num, i Como Entero;
	Definir factorial Como Entero;
	
	//utilizamos esta condicion para que ingrese un numero mayor o igual a 0
	Repetir
		Escribir "Digite un numero: ";
		Leer num;
		
	Hasta Que num >= 0;
	i <- 1;
	factorial <- 1;
	
	// N! = 1 * 2 * 3 * ...* N 
	Mientras i <= num Hacer
		factorial <- factorial*i;
		i <- i +1;
		Escribir "El iterador aca es: ", i," El factorial entonces aca seria: ", factorial;
	FinMientras
	
	Escribir "El factorial es: ", factorial, ". Entonces el iterador quedo en: ", i;
FinProceso
