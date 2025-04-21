// Ejercicio 6.c
// Diseñar un programa que ingresando un año, nos devuelva por consola si es un año bisiesto o no.
// Repetir la accion hasta que el usuario lo desida
Proceso Ciclos
	Definir num, opcion Como Entero;
	Escribir 'Comprobamos que anio es bisiesto';
	Repetir
		Escribir 'Ingrese el anio: ';
		Leer num;
		Si ((num MOD 4=0) Y (num MOD 100<>0) O num MOD 400=0) Entonces
			Escribir 'El año es Bisiesto';
		SiNo
			Escribir 'El año NO es Bisiesto';
		FinSi
		Escribir 'Para seguir adelante digite la opcion 1: ';
		Leer opcion;
	Hasta Que opcion<>1
FinProceso
