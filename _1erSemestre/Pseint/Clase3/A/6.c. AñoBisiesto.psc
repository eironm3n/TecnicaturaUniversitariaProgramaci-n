// Ejercicio 6.c
// Dise�ar un programa que ingresando un a�o, nos devuelva por consola si es un a�o bisiesto o no.
// Repetir la accion hasta que el usuario lo desida
Proceso Ciclos
	Definir num, opcion Como Entero;
	Escribir 'Comprobamos que anio es bisiesto';
	Repetir
		Escribir 'Ingrese el anio: ';
		Leer num;
		Si ((num MOD 4=0) Y (num MOD 100<>0) O num MOD 400=0) Entonces
			Escribir 'El a�o es Bisiesto';
		SiNo
			Escribir 'El a�o NO es Bisiesto';
		FinSi
		Escribir 'Para seguir adelante digite la opcion 1: ';
		Leer opcion;
	Hasta Que opcion<>1
FinProceso
