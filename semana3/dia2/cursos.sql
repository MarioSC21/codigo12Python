CREATE TABLE IF NOT EXISTS alumno (
  id int(11) NOT NULL AUTO_INCREMENT,
  nombres varchar(100) NOT NULL,
  apellidos varchar(100) NOT NULL,
  email varchar(100) NOT NULL,
  pais varchar(100) DEFAULT 'Perú',
  nota int(11) DEFAULT '0',
  PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS alumno_nota(
  id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  alumno_id int(11) NOT NULL,
  curso varchar(100) NOT NULL,
  nota int(11) NOT NULL,
  FOREIGN KEY (alumno_id) REFERENCES alumno(id)
);
SELECT
  *
FROM
  alumno;
--?poblando tabla alumno_nota
  TRUNCATE TABLE alumno_nota;
INSERT INTO
  alumno_nota(alumno_id, curso, nota)
VALUES
  (1, 'html y css', 20),
  (1, 'JS', 15),
  (1, 'REACT', 11),
  (1, 'PYTHON', 12),
  (1, 'MYSQL', 17),
  (2, 'html y css', 15),
  (2, 'JS', 19),
  (2, 'REACT', 18),
  (2, 'PYTHON', 20),
  (2, 'MYSQL', 16),
  (3, 'html y css', 12),
  (3, 'JS', 08),
  (3, 'REACT', 05),
  (3, 'PYTHON', 11),
  (3, 'MYSQL', 09);
SELECT a.nombres,an.nota,AVG(an.nota) promedio FROM alumno a JOIN alumno_nota an ON  a.id = an.alumno_id GROUP BY a.nombres;