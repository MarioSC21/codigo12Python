--?TRIGGER DISPARADORES

SELECT alumno_nombre,
CONCAT(REPLACE(lower(alumno_nombre),' ',''),'@tecsup.edu.pe')
FROM tbl_alumno;

DELIMITER $$

CREATE TRIGGER tg_correo_alumno
BEFORE INSERT
ON tbl_alumno FOR EACH ROW
BEGIN
    SET NEW.alumno_email = CONCAT(REPLACE(lower(NEW.alumno_nombre),' ',''),'@tecsup.edu.pe');
END
$$

DELIMITER;

--PROBANDO
SELECT * FROM tbl_alumno;
INSERT INTO tbl_alumno(alumno_nombre,alumno_celular,alumno_github)
VALUES('mario cs','321313131','https://github.com/cesarmayta')