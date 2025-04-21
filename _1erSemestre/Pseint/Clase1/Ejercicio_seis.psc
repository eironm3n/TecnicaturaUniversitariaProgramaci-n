//Ejercicio 6
//Un alumno desea saber cuál será su calificación final en la materia de Algoritmos.
//Dicha calificación se compone de los siguientes porcentajes:
//55% del promedio de sus tres calificaciones parciales
//30% de la calificacion del examen final 
//15% de las calificacion de un trabajo final
//este fue hecho por mi, sin ver video
Proceso Ejercicio_seis
	Definir examFinal, trabajFinal,totalParcial,porcenTotal  Como Real;	
	Definir parcial1, parcial2, parcial3, califTotal Como Real;
	Definir porcenParciales, porcenExamen, porcenTrabajo Como Real;
	
	//Solicitamos las notas de las tres calificaciones parciales
	Escribir "Dame tu puntuación de los 3 parciales ";
	Leer parcial1, parcial2, parcial3;

	califTotal <- (parcial1 + parcial2 + parcial3) / 3;	//sumamos el total del 55%
	
	//Solicitamos el valor del Examen Final
	Escribir "Dame tu puntuación en el Examen Final: ";
	Leer examFinal;
	//Solicitamos el valor del Trabajo Final
	Escribir "Dame tu puntuación en el Trabajo Final: ";
	Leer trabajFinal;
	
	porcenParciales <- califTotal * 0.55;
	porcenExamen <- examFinal * 0.3;
	porcenTrabajo <- trabajFinal * 0.15;

	porcenTotal <- trunc(porcenParciales + porcenExamen + porcenTrabajo);
	
	Escribir "Tu nota total sería de: ", porcenTotal, " %";
FinProceso