Proceso Ejercicios
	//Ejercicio 1
	Definir a, b, c, resultadoUno, resultadoDos Como Real;
	Escribir "Digite el valor de A: ";		//digitamos 2
	Leer a;
	Escribir "Digite el valor de B: ";		//digitamos 10
	Leer b;
	Escribir "Digite el valor de C: ";		//digitamos 3
	Leer c;
	
	resultadoUno <- (-b + rc(b^2 - 4 * a * c)) / (2*a);
	resultadoDos <- (-b - rc(b^2 - 4 * a * c)) / (2*a);
	//rc(número) o raiz(número) : devuelve la raíz cuadrada del número
	
	Escribir "El resultado de la suma en la ecuación es: ", resultadoUno; //El resultado: -0.320550..
	Escribir "El resultado de la resta en la ecuación es: ", resultadoDos; //El resultado: -4.67944..
	
	Escribir "Muchas gracias vuelvas prontos";
FinProceso
