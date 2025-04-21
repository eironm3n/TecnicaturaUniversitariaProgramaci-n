//Recursividad
Funcion retorno <- factorial(num)		//Parametro
	Definir retorno Como Entero;
	
	//Caso base
	Si num = 0 Entonces
		retorno <- 1;
		
	SiNo	//Caso recursivo
		retorno <- num * factorial(num-1);
	FinSi
FinFuncion

Proceso Principal
	Definir num Como Entero;
	
	Escribir Sin Saltar "Digite un numero: ";
	Leer num;
	
	Escribir "El factorial del numero es: ", factorial(num);		//Argumento
FinProceso
