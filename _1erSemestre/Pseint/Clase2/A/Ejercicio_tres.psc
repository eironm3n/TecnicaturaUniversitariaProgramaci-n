Proceso Ejercicio_tres
	//Ejercicio 3 
	//Un maestro desea saber que porcentaje de hombes y que porcentaje de mujeres hay en un grupo de estudiantes
	
	Definir num_h, num_m Como Entero;
	Definir total_estudiantes Como Entero;
	Definir porcentajeH, porcentajeM Como Real;
	
	Escribir "Digite un numero de hombres: ";
	Leer num_h;
	
	Escribir "Digite un numero de mujeres: ";
	Leer num_m;
	
	total_estudiantes <- num_h + num_m;
	porcentajeH <- num_h/total_estudiantes * 100;
	porcentajeM <- num_m/total_estudiantes * 100;
	
	Escribir "El porcentaje de Hombres es: ", porcentajeH,"%";
	Escribir "El porcentaje de Mujeres es: ", porcentajeM,"%";
	
FinProceso
