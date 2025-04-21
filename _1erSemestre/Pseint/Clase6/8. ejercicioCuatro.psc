//Ejercicio 4
//Escriba un subprograma nombrado cambio() que tenga un parametro en numero entero y
//seis parametros de referencia en numero entero nombrados cien, cincuenta, veinte, diez, cinco
//y uno, respectivamente.
//La funcion tiene que considerar el valor entero transmitido como una cantidad en dolares y 
//convertir el valor en el numero menor de billetes equivalentes
SubProceso pedirDatos(dolares Por Referencia)
	Escribir Sin Saltar "Digite la cantidad de dolares: ";
	Leer dolares;
FinSubProceso

SubProceso	cambio(dolares, cien Por Referencia, cincuenta Por Referencia, veinte Por Referencia, diez Por Referencia, cinco Por Referencia,uno Por Referencia)	//Parametros
	cien <- trunc(dolares/100);	//716 = 7 de 100 dolares
	dolares <- dolares mod 100;
	cincuenta <- trunc(dolares/50);
	dolares <- dolares mod 50;
	veinte <- trunc(dolares/20);
	dolares <- dolares mod 20;
	diez <- trunc(dolares/10);
	dolares <- dolares mod 10;
	cinco <- trunc(dolares/5);
	uno <- dolares mod 5;
	
FinSubProceso

SubProceso mostrarDatos(cien, cincuenta, veinte, diez, cinco, uno)
	Escribir "";
	Escribir "La cantidad de billetes necesarios es: ";
	Escribir "Cien: ", cien;
	Escribir "Cincuenta: ",cincuenta;
	Escribir "Veinte: ", veinte;
	Escribir "Diez: ", diez;
	Escribir "Cinco: ",cinco;
	Escribir "Uno: ", uno;
	
FinSubProceso

Proceso Principal
	Definir dolares Como Real;
	Definir cien, cincuenta, veinte, diez, cinco, uno Como Enteros;
	
	//Primero pedimos la cantidad de dolares al usuario
	pedirDatos(dolares);		//Argumento
	
	//Ahora, convertimos a billetes
	cambio(dolares, cien, cincuenta, veinte, diez, cinco, uno);	//Argumentos
	
	//Por ultimo mostramos los datos
	mostrarDatos(cien, cincuenta, veinte, diez, cinco, uno);	//Argumentos
FinProceso
