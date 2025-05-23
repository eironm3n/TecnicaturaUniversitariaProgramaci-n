// Ejercicio 7
// Leer 10 numeros e imprimir cuantos son positivos, cuantos negativos y cuantos neutros
Proceso Ejercicio3
	// 0 es neutro -^- 1 es positivo -^- (-1) es negativo
	Definir num, i Como Entero;
	Definir conteo_positivos, conteo_negativos, conteo_neutros Como Entero;
	conteo_positivos <- 0;
	conteo_negativos <- 0;
	conteo_neutros <- 0;
	// Se utiliza el ciclo 'PARA' ya que necesitamos que revise todos los valores de c/u
	Para i<-1 Hasta 10 Con Paso 1 Hacer
		Escribir i, " Digite un numero: ";
		Leer num;
		Si num = 0 Entonces
			conteo_neutros <- conteo_neutros + 1;
		SiNo
			Si num > 0  Entonces
				conteo_positivos <- conteo_positivos + 1;
			SiNo
				conteo_negativos <- conteo_negativos + 1;
			FinSi
		FinSi
	FinPara
	Escribir "La cantidad de positivos es: ", conteo_positivos;
	Escribir "La cantidad de negativos es: ", conteo_negativos;
	Escribir "La cantidad de neutros es: ", conteo_neutros;
FinProceso
