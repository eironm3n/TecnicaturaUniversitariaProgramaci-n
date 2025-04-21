// Ejercicio 8
// Implementar un subprograma recursivo que realice la serie Fibonacci
// 0 1 1 2 3 5 8 13 21 ... hasta N elementos
// Diagrama de Flujo
Proceso Principal
	Definir nElementos Como Entero;
	// Primero, pedimos los elementos
	pedirDatos(nElementos);
	// Ahora, mostramos la serie
	mostrarSerie(nElementos);
FinProceso

SubProceso pedirDatos(nElementos por Referencia)
	Escribir Sin Saltar "Digite el numero de elementos: ";
	Leer nElementos;
FinSubProceso

SubProceso mostrarSerie(nElementos)
	Definir i Como Entero;
	Escribir "";
	Escribir "La serie fibonacci es: ";
	Escribir Sin Saltar "0 ";
	Para i<-1 Hasta nElementos-1 Hacer
		Escribir Sin Saltar fibonacci(i), " ";
	FinPara
FinSubProceso

SubProceso retorno <- fibonacci(num)
	Definir retorno Como Entero;
	Si num = 1 O num = 2 Entonces
		// Caso base
		retorno <- 1;
	SiNo
		// Caso recursivo
		retorno <- fibonacci(num-1) + fibonacci(num-2);
	FinSi
FinSubProceso
