-- Comenzamos con CRUD: create(insertar), read(leer), update(actualizar), delete(eliminar)

-- Listar los estudiantes (leer)
SELECT * FROM estudiantes2025;

-- Insertar estudiante
INSERT INTO estudiantes2025 (nombre, apellido, telefono, email) VALUES ("Juan","Perez","261787899","jperez@mail.com");

-- Actualizar estudiante
UPDATE estudiantes2025 SET nombre="Juan Carlos", apellido="GARCIA" WHERE idestudiantes2025=1;

-- Eliminar estudiante
DELETE FROM estudiantes2025 WHERE idestudiantes2025=1;

-- Para modificar el id manualmente y hacerlo que comience en 1
ALTER TABLE estudiantes2025 AUTO_INCREMENT=1;
-- Revisar comando por que no ejecuta

-- Se continua con IntelliJ