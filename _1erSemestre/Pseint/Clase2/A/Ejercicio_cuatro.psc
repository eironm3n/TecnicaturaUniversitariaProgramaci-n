//Ejercicio 4
//Un profesor prepara tres cuestionarios para una evaluación final: A, B y C.
//Se sabe que se tarda 5min en revisar el cuestionario A, 8min en revisar el cuestionario B y 6min en el C
//La cantidad de examenes de c/tipo se entran por teclado.
//¿Cuantas horas y cuantos minutos se tardara en revisar todas las evaluaciones?
Proceso Ejercicio_cuatro
	Definir cantA, cantB, cantC Como Entero;
	Definir tiempoA, tiempoB, tiempoC, tiempo_total, horas, minutos Como Entero;
	
	Escribir "Dame la cantidad de cuestionarios de tipo A: ";
	Leer cantA;
	Escribir "Dame la cantidad de cuestionarios de tipo B: ";
	Leer cantB;
	Escribir "Dame la cantidad de cuestionarios de tipo C: ";
	Leer cantC;
	
	//calcular la cant de tiempo que gastara en c/cuestionario
	tiempoA <- cantA * 5;		//Coloqué 5
	tiempoB <- cantB * 8;		//Coloqué 8
	tiempoC <- cantC * 6;		//Coloqué 6
	
	//tiempo total de todos los cuestionarios
	tiempo_total <- tiempoA + tiempoB + tiempoC;		//Deberia ser 25+64+36 = 125
	
	//calculamos las horas y minutos
	
	horas <- trunc (tiempo_total / 60);			//Deberia ser 125/60 = 2,0833.. ó 
	//La función trunc elimina todos los n°s después del punto decimal para dejar como resultado sólo al n° entero
	minutos <- tiempo_total mod 60;
	//La función MOD( ) esta función para probar si dos n°s pueden dividirse de manera exacta o aislar el resto de un cálculo de división. Esta función divide un n° entre otro y devuelve el resto.
	
	Escribir "Se tardará ", horas, " horas y ", minutos, " minutos";
	
FinProceso
