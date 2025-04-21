//Ejercicio 14 (supuestamente ejercicio 12)
//Hacer un programa donde el usuario ingrese un numero N, luego le vamos a pedir otro n°
//para calcular la potencia de los N n°s recorridos, los cuales dividiremos con la 
//multiplicación del factorial y al mismo tiempo sumamos en cada recorrido, imprimir el 
//resultado de la suma


Proceso principal
	Definir N, i, j, factorial, base, potencia Como Entero;
    Definir sumatoria, aux Como Real;
    Escribir "Ingrese la cantidad de veces que desea sumar el factorial del exponente (?: ";
    Leer N;
    Escribir "Ingrese el número de base que quiere elevar al exponente (?:";
    Leer base;
    sumatoria <- 1;
    factorial <- 1;
    Para i <- 1 Hasta N Hacer
        factorial <- factorial * i;
        potencia <- base ^ i;
        sumatoria <- sumatoria + potencia / factorial;
    FinPara
    Escribir "La sumatoria de todos los números es: ", sumatoria;
FinProceso
