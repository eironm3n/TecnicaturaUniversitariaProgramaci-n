// Ejercicio 6
// Diseñe un algoritmo que contenga el siguiente menú:
// 1. Llenar una matriz de 4*4
// 2. Mostrar la matriz
// 3. Sumar todos los elementos de la matriz
// 4. Salir
// DiagramaNS
Proceso Principal
	Definir opcion Como Entero;
	Definir matriz Como Real;
	Dimension matriz[4,4];
	Repetir
		Escribir "MENU";
		Escribir "1. Llenar una matriz de 4*4";
		Escribir "2. Mostrar la matriz";
		Escribir "3. Sumar todos los elementos de la matriz";
		Escribir "4. Salir";
		Escribir "Digite la opcion de menu: ";
		Leer opcion;
		Escribir "";
		Segun opcion Hacer
			1:
				llenarMatriz(matriz);
			2:
				mostrarMatriz(matriz);
			3:
				Escribir "La suma es: ",sumarMatriz(matriz);
			4:
			De Otro Modo:
				Escribir "Se equivoco de menu";
		FinSegun
		Escribir "";
	Hasta Que opcion = 4
FinProceso

SubProceso llenarMatriz(matriz por Referencia)
	Definir i, j Como Enteros;
	Para i<-0 Hasta 3 Con Paso 1 Hacer
		Para j<-0 Hasta 3 Con Paso 1 Hacer
			Escribir Sin Saltar "Digite un numero[",i,"][",j,"]: ";
			Leer matriz[i,j];
		FinPara
	FinPara
FinSubProceso

SubProceso mostrarMatriz(matriz)
	Definir i, j Como Enteros;
	Para i<-0 Hasta 3 Con Paso 1 Hacer
		Para j<-0 Hasta 3 Con Paso 1 Hacer
			Escribir Sin Saltar matriz[i,j], " ";
		FinPara
		Escribir Sin Saltar "";
	FinPara
FinSubProceso

SubProceso suma <- sumarMatriz(matriz)
	Definir i,j Como Enteros;
	Definir suma Como Real;
	suma <- 0;
	Para i<-0 Hasta 3 Con Paso 1 Hacer
		Para j<-0 Hasta 3 Con Paso 1 Hacer
			suma <- suma + matriz[i,j];
		FinPara
	FinPara
FinSubProceso
