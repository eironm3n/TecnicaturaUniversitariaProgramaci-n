Proceso Ejercicio_uno
	//Ejercicio 1 - Realizado en la clase 1
	//Calcular la cantidad de segundos que están incluidos en el n° de hs, m y s ingresados por el usuario
	
	Definir horas, minutos, seg Como Entero;
	Definir horas_seg, minutos_seg, total_seg Como Entero;
	
	Escribir "Digite las horas: ";
	Leer horas;
	
	Escribir "Digite los minutos: ";
	Leer minutos;
	
	Escribir "Digite los segundos: ";
	Leer seg;
	
	//Calcular el equivalente en segundos
	horas_seg <- horas * 3600;
	minutos_seg <- minutos * 60;
	total_seg <- horas_seg + minutos_seg + seg;
	
	Escribir "Los segundos equivalentes son: ", total_seg;
	
FinProceso
