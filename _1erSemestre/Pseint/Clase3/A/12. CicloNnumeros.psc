//Ejercicio 12 (supuestamente n°11) 
//Ingresar N n°s, calcular el maximo y minimo de ellos

Proceso principal
	Definir i, n_elementos Como Entero;
	Definir mayor, menor, num Como Real;
	
	
	Repetir
		//Cantidad de 'elementos' o numeros
		Escribir "Digite un numero de elementos mayor a dos, sino no existiria una comparativa: ";
		Leer n_elementos;
		
	Hasta Que n_elementos  > 1
	//aqui significa que el usuario no puede ingresar un numero menor-igual a cero o 1, ya que deberia haber un menor y un mayor
	
	Escribir "1. Digite un numero: ";
	Leer num;
	mayor <- num;
	menor <- num;
	
	i <- 2;
	Repetir
		Escribir i, ". Digite un numero: ";
		Leer num;
		Si num > mayor Entonces
			mayor <- num;
		SiNo
			Si num < menor Entonces
				menor <- num;
			FinSi
		FinSi
		i <- i + 1;
	Hasta Que i > n_elementos
	
	Escribir "El numero mayor es: ", mayor;
	Escribir "El numero menor es: ", menor;
	
FinProceso
