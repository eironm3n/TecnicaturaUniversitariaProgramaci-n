Proceso Principal
	Definir i Como Entero;
	
	i <- 1;
	// condición dentro del ciclo, hasta que no llegue a 10 no finaliza
	Mientras i  <= 10 Hacer
		Escribir i;
		i <- i + 1;	//agregando esta variable, aumentaria en 1 cada vez que recorra el ciclo hasta que finalice
	FinMientras
	// este ciclo nunca terminaria ya que contaria 1, 1, 1, 1, 1 ,1 ,1
	// pero esta indeterminado, ya que no hay nada que aumente el 1..
	// es necesario agregar la nueva variable de i, y que la vaya aumentando..
	Escribir "";	//salto de linea
	
FinProceso
