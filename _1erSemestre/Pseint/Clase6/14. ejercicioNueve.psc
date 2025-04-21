// Ejercicio 9
// Implementar un subprograma recursivo que permita sumar los digitos de un numero
// Ejemplo: Entrada =123 Salida= 6
// Diagrama NS
Proceso Principal
	Definir num Como Entero;
	// Primero, pedimos el numero al usuario
	pedirDatos(num);
	// Ahora, sumamos los digitos del numero
	Escribir "La suma es: ", sumarDigitos(num);
FinProceso

SubProceso pedirDatos(num por Referencia)
	Escribir Sin Saltar "Digite un numero: ";
	Leer num;
FinSubProceso

SubProceso retorno <- sumarDigitos(num)
	Definir retorno Como Entero;
	Si num = 0 Entonces
		// Caso base
		retorno <- num;
	SiNo
		// Caso recursivo
		retorno <- sumarDigitos(trunc(num/10)) + (num mod 10);
	FinSi
FinSubProceso
