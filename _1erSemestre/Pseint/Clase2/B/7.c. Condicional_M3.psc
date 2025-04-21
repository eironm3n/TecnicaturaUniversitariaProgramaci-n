// Ejercicio 7.c
// Hacer un programa que tenga un menu con las siguientes opciones:
// Opcion 1: Elevar un número a una potencia x
// Opcion 2: Sacar la raiz cuadrada de un numero
// Opcion 3: Salir
Proceso Condicional_M3
	Definir opcion Como Entero;
	Escribir "MENU";
	Escribir "1. Elevar un numero a una potencia x";
	Escribir "2. Sacar la raiz cuadrada de un numero";
	Escribir "3. Salir";
	Escribir "Digite una opción: ";
	Leer  opcion;
	Segun opcion Hacer
		1:
			Definir num, potencia, resultado Como Reales;
			Escribir "Digite un numero: ";
			Leer num;
			Escribir "Digite la potencia: ";
			Leer potencia;
			resultado <- num^potencia;
			Escribir "El resultado es: ", resultado;
		2:
			Definir num, resultado Como Reales;
			Escribir "Digite un numero ";
			Leer num;
			resultado <- rc(num);
			// rc() es una variable interna de PSeint, significa Raiz Cuadrada
			Escribir "El resultado es: ", resultado;
		De Otro Modo:
			Escribir "Se equivoco de menu";
			Escribir "Hasta luego joven padawan";
	FinSegun
FinProceso
