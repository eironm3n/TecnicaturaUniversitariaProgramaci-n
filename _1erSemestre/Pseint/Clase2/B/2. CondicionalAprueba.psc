// Ejercicio 2
// Determinar si un alumno aprueba o no un curso.
// Sabiendo que aprobará si su promedio de tres claificaciones es mayor o igual a 70.
// Caso contrario, reprueba
Proceso Principal
	Definir nota1, nota2, nota3 Como Reales;
	Definir promedio Como Real;
	Escribir "Digite las 3 calificaciones: ";
	Leer nota1, nota2, nota3;
	promedio <- (nota1 + nota2 + nota3) /3;
	Si promedio >= 70 Entonces
		Escribir "Aprobaste mi rey, tu nota fue de: ", promedio;
	SiNo
		Escribir "A seguir estudiando mi rey, falta mas culosilla en tu vida. Tu nota fue de: ", promedio70;
	FinSi
FinProceso
