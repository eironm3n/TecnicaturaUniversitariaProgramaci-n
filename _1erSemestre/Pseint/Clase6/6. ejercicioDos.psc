// Ejercicio 2
// Diseñe un algoritmo que muestre un menu al usuario con las siguientes opciones:
// potenciación,raiz cuadrada y terminar, que cada opción la realice una funcion o procedimiento
// Diagrama Flujo
Proceso Principal
	menu();
	Escribir "";
FinProceso

SubProceso menu
	Definir opcion Como Entero;
	Definir num,exponente Como Reales;
	Repetir
		Escribir "MENU";
		Escribir "1. Potenciación";
		Escribir "2. Raiz cuadrada";
		Escribir "3. Salir";
		Escribir Sin Saltar "Digite una opcion: ";
		Leer opcion;
		Escribir "";
		Segun opcion Hacer
			1:
				Escribir Sin Saltar "Digite un numero: ";
				Leer num;
				Escribir Sin Saltar "Digite un exponente: ";
				Leer exponente;
				Escribir "La potencia es: ",potencia(num,exponente);
			2:
				Escribir Sin Saltar "Digite un numero: ";
				Leer num;
				Escribir "La raiz cuadrada es: ",raizCuadrada(num);
			3:
			De Otro Modo:
				Escribir "Se equivoco de opcion de menu";
		FinSegun
		Escribir "";
	Hasta Que opcion = 3
FinSubProceso

SubProceso pot <- potencia(num,exponente)
	Definir pot Como Real;
	pot <- num^exponente;
FinSubProceso

SubProceso raiz_C <- raizCuadrada(num)
	Definir raiz_C Como Real;
	raiz_C <- rc(num);
FinSubProceso
