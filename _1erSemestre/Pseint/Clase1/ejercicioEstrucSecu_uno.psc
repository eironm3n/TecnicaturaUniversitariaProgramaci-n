Proceso Ejercicios

	//Ejercicio 1 de Estructuras Secuenciales
	//Calcular la cantidad de segundos que estan incluidos en el numero de horas, minutos, y segundos ingresados por el usuario
	
	Definir resultado, h, m, hr, sumaDeMin Como Real;
	
	
	Escribir "Vamos a jugar un pequeño juego de tiempo";
	Escribir "En cuanto tiempo crees que llegas desde tu casa hasta tu trabajo en colectivo?";
	Escribir "De seguro te subis a varios colectivos";
	Escribir "Dame el tiempo en Horas, Minutos. Ok?";
	
	Escribir "Hora";
	Leer h;
	Escribir "Minutos";
	Leer m;
	
	hr <- h*60;		//aqui pasamos la hora a minutos, multiplicando el numero por 60 (siendo los minutos 1h=60m)
	sumaDeMin <- hr + m;		//aqui hacemos la suma de el primer numero en minutos ingresado, mas el resultado de 'hr'
	resultado <- (sumaDeMin*60);		//aqui usamos el total de la suma anterior, y multiplicamos por 60, siendo los segundos (1m=60s)
	
	Escribir "Aunque no lo creas, has viajado una cantidad de ", resultado," segundos";
		
	
	Escribir "Muchas gracias vuelvas prontos";
FinProceso
