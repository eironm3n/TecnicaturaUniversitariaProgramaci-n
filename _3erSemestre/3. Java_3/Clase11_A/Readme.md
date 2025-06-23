## Practicas realizadas con MySQL de la clase 11A de Java3

1. Se realiza la descarga e instalación de MySQL, y se instala la versión Comunnity.
2. Se realiza la instalación y se ingresa a la base de prueba creada, le asignamos el nombre "Estudiantes"
CREATE SCHEMA `estudiantes` ;
3. Dentro de la tabla, se crea una nueva tabla y se renombra a 'estudiantes2025'. Se agrega la primer columna: 'id'
CREATE TABLE `estudiantes`.`estudiantes2025` (
  `idestudiantes2025` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idestudiantes2025`));
4. Se crean las columnas: nombre, apellido, telefono, email
ALTER TABLE `estudiantes`.`estudiantes2025` 
ADD COLUMN `nombre` VARCHAR(45) NULL AFTER `idestudiantes2025`,
ADD COLUMN `apellido` VARCHAR(45) NULL AFTER `nombre`,
ADD COLUMN `telefono` VARCHAR(45) NULL AFTER `apellido`,
ADD COLUMN `email` VARCHAR(45) NULL AFTER `telefono`;
5. Luego iremos a la opción "Select Rows - Limit 1000"
SELECT * FROM estudiantes.estudiantes2025;
6. Se almacenan los scripts practicados dentro de MySQL Workbench y se crea el archivo scriptsEjecutados.sql y se dejan los comentarios allí
