// Ejercicio 6 (?)
// Una fruteria ofrece las manzanas con descuentos segun la siguiente tabla:
// 0-2 = 0 MOD  descuento
// 2.01 - 5 = 10 MOD  descuento
// 5.01 - 10 = 15 MOD  descuento
// 10.01 en adelante = 20 MOD  de descuento
// Determinar cuanto pagara una persona que compre manzanas en esta fruteria

Proceso Principal
	Definir precioK, kilos, precioI Como Reales;
	Definir descuento, precio_final Como Reales;
	Escribir "Cuanto cuesta el kilo de manzanas mi rey?: ";
	Leer precioK;
	Escribir "Cuantos kilos compraste?: ";
	Leer kilos;
	precioI <- precioK * kilos;
	Si kilos >= 0 Y kilos <= 2 Entonces
		descuento <- 0;
	SiNo
		Si kilos >= 2.01 Y kilos <= 5 Entonces
			descuento <- precioI * 0.1;
		SiNo
			Si kilos >= 5.01 Y kilos <= 10 Entonces
				descuento <- precioI * 0.15;
			SiNo
				descuento <- precioI * 0.20;
			FinSi
		FinSi
	FinSi
	
	precio_final <- precioI - descuento;
	
	Escribir "El precio a pagar es: $", precio_final;
FinProceso
