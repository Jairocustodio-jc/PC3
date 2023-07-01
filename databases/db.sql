drop database PC3;

create database PC3;

use PC3;

CREATE TABLE alumnos (
  username VARCHAR(50) PRIMARY KEY,
  nombre VARCHAR(50),
  apellidos VARCHAR(50),
  clave VARCHAR(50)
);
INSERT INTO alumnos (username, nombre, apellidos, clave)
VALUES
  ('alumno1', 'Violeta', 'Perez', '123456'),
  ('alumno2', 'Angela', 'Perez', '123456'),
  ('alumno3', 'Katherine', 'Perez', '123456');