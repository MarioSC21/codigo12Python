--?probando tabla
--?alumno

INSERT INTO tbl_alumno(alumno_nombre,alumno_email,alumno_celular,alumno_github)
VALUES
('mario ','mario@gmail.com','9999999','https://github.com/MarioSC21'),
('mario2 ','mario2@gmail.com','9999998','https://github.com/MarioSC21'),
('mario3 ','mario3@gmail.com','9999997','https://github.com/MarioSC21'),
('mario4 ','mario4@gmail.com','9999996','https://github.com/MarioSC21'),
('mario5 ','mario5@gmail.com','9999995','https://github.com/MarioSC21');

INSERT INTO tbl_curso(curso_nombre)
VALUES
('html y css'),('javaScript'),('react'),('python'),('flask');

INSERT INTO tbl_modulo(modulo_nombre,modulo_fecha_inicio,modulo_nro_sesiones)
VALUES
('front','2022-01-01',15),
('back','2022-03-01',15);

INSERT INTO tbl_nivel(nivel_nombre)
VALUES
('basico'),('avanzado');

SELECT * from tbl_alumno