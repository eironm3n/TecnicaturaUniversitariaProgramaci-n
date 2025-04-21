// Ejercicio 13 (supuestamente ejercicio 11)
// Imprimir la serie de los N terminos de la serie Fibonacci
// 0 1 1 2 3 5 8 13 21 ...

Proceso principal
	definir i,f,n1,n2 como entero;
    n1<-0;
    n2<-1;
    escribir sin saltar "ingrese numero: ", " ";
    leer i;
    para i<-0 hasta i-1 con paso 1 Hacer
        escribir sin saltar n1, " ";
        f<-n1+n2;
        n1<-n2;
        n2<-f;
    FinPara

FinProceso
