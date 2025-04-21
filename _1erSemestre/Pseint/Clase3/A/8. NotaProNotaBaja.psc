//Ejercicio 8 (ejercicio 4 supuestamente)
//Suponga que se tiene un conjunto de calificaciones de un grupo de 10 alumnos
//Realizar un algoritmo para calcular la calificacion promedio y la 
//calificacion mas baja de todo el grupo

Proceso Principal
	Definir nota, suma Como Real;
	Definir nota_promedio,nota_baja Como Real;
	Definir i Como Entero;
	
	suma <- 0;
	nota_baja <- 99999;
	
	Para i<-1 Hasta 10 Con Paso 1 Hacer
		Escribir i, "= Ingrese la calificacion por favor: ";
		Leer nota;
		//suma iterativa de las notas
		suma <- suma + nota;
		Escribir "Esto es pa vos gil: ",suma;
		//calcular la calificacion mas baja
		Si nota < nota_baja Entonces
			nota_baja <- nota;
		FinSi
	FinPara
	
	nota_promedio <- suma/10;
	Escribir "La calificacion promedio es: ", nota_promedio;
	Escribir "La calificacion mas baja es: ", nota_baja;
FinProceso
