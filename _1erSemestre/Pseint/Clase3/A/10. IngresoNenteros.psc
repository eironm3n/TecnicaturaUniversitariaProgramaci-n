//Ejercicio 10 (supuestamente Ejercicio 7 )
//Ingresar N enteros, visualizar la suma de los n°s de la lista, cuántos n°s pares existen y cuál es el promedio de los n°s impares


Proceso principal
	Definir i, num Como Entero; 
	Definir n_elementos, suma_pares, suma_impares, conteo_pares, conteo_impares Como Entero;
	Definir promedio_i Como Real;
	
	Escribir "Digite la cantidad de elementos a ingresar: ";
	Leer n_elementos;
	
	i <- 1;
	suma_pares <- 0;
	conteo_pares <- 0;
	suma_impares <- 0;
	conteo_impares <- 0;
	
	Mientras i <= n_elementos Hacer
		Escribir i, ". Digite un número: ";
		Leer num;
		Si num mod 2 = 0 Entonces
			// El numero es par
			
			// Suma iterativa de los numeros pares
			suma_pares <- suma_pares + num;
			// contamos cuantos numeros pares se han ingresado
			conteo_pares <- conteo_pares + 1;
		SiNo
			// El numero es impar
			
			// Suma iterativa de los numeros impares
			suma_impares <- suma_impares + 1;
			// contamos cuantos numeros impares se han ingresado, y se van guardando
			conteo_impares <- conteo_impares + 1;
		FinSi
		
		//no olvidar que el iterador vayan aumentando hasta que llegue a n_elementos, caso contrario seria infinito
		i <- i + 1;
	FinMientras
	
	Si conteo_pares = 0 Entonces
		Escribir "No se han ingresado numeros pares: ";
	SiNo
		Escribir "La suma de los numeros pares es: ", suma_pares;
		Escribir "El conteo de los numeros pares es: ", conteo_pares;
	FinSi
	Si conteo_impares = 0 Entonces
		Escribir "No se han ingresado numeros impares: ";
	SiNo
		promedio_i <- suma_impares / conteo_impares;
		Escribir "El promedio de los numeros impares es: ", promedio_i;
	FinSi
FinProceso
