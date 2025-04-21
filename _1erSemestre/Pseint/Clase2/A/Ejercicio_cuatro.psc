//Ejercicio 4
//Un profesor prepara tres cuestionarios para una evaluaci�n final: A, B y C.
//Se sabe que se tarda 5min en revisar el cuestionario A, 8min en revisar el cuestionario B y 6min en el C
//La cantidad de examenes de c/tipo se entran por teclado.
//�Cuantas horas y cuantos minutos se tardara en revisar todas las evaluaciones?
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
	tiempoA <- cantA * 5;		//Coloqu� 5
	tiempoB <- cantB * 8;		//Coloqu� 8
	tiempoC <- cantC * 6;		//Coloqu� 6
	
	//tiempo total de todos los cuestionarios
	tiempo_total <- tiempoA + tiempoB + tiempoC;		//Deberia ser 25+64+36 = 125
	
	//calculamos las horas y minutos
	
	horas <- trunc (tiempo_total / 60);			//Deberia ser 125/60 = 2,0833.. � 
	//La funci�n trunc elimina todos los n�s despu�s del punto decimal para dejar como resultado s�lo al n� entero
	minutos <- tiempo_total mod 60;
	//La funci�n MOD( ) esta funci�n para probar si dos n�s pueden dividirse de manera exacta o aislar el resto de un c�lculo de divisi�n. Esta funci�n divide un n� entre otro y devuelve el resto.
	
	Escribir "Se tardar� ", horas, " horas y ", minutos, " minutos";
	
FinProceso
