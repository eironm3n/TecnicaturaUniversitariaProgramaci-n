//Ejercicio 4
//Leer 2 numeros: si son iguales que los multiplique, si el primero es mayor que el segundo que los reste
//y si no que los sume

Proceso Principal
	Definir num1, num2, resultado Como Real;
	Escribir "Dame 2 numeros: ";
	Leer num1, num2;
	
	Si num1 == num2 Entonces
		//si son iguales multiplicamos
		resultado <- num1 * num2;
	SiNo
		Si num1 > num2 Entonces
			//si el primer numero es mayor hacemos una resta
			resultado <- num1 - num2;
		SiNo
			//en este caso no utilizamos el condicional 'Si'. Ser�a parecido a: Si num1 < num2 Entonces
			resultado <- num1 + num2;
		FinSi
	FinSi
	
	Escribir "El resultado es: ", resultado;
	
FinProceso
