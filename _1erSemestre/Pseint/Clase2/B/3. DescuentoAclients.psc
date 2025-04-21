// Ejercicio 3
// En un almacen se hace un 20 MOD  de descuento a los clientes cuya compra supere los $100
// ¿Cual sera la cantidad que pagara una persona por su compra?
Proceso Principal
	Definir compra, descuento, precio_final Como Reales;
	Escribir "Digite la cantidad a pagar: ";
	Leer compra;
	Si compra > 100 Entonces
		descuento <- compra * 0.20;
	SiNo
		descuento <- 0;
	FinSi
	precio_final <- compra - descuento;
	Escribir "El precio a pagar es: ", precio_final;
FinProceso
