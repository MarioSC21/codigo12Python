--?PROCEDURE 

DELIMITER $$
CREATE PROCEDURE listar_alumnos()
BEGIN
    SELECT * FROM tbl_alumno;

END
$$
DELIMITER;

--!llamar al proc alamacenado 
-- CALL listar_alumnos();

--------------------------------------------------------*
CREATE PROCEDURE sp_matricular_alumno(
    IN alu_id INT,
    IN niv_id INT,
    IN mod_id INT
)
BEGIN
    --variables
    DECLARE matId INT;
    DECLARE curId INT;
    DECLARE totalCursos INT;
    SET matId = 0;
    SET curId = 1;
    set totalCursos = 0;
    --regsitrar matricula
    INSERT INTO tbl_matricula(alumno_id,nivel_id,modulo_id)
    VALUES(alu_id,niv_id,mod_id);

    select max(matricula_id) INTO matID from tbl_matricula;

    SELECT COUNT(*) INTO totalCursos from tbl_curso;
    
    WHILE curId <= totalCursos DO
        INSERT INTO tbl_matricula_curso(matricula_id,curso_id)
        VALUES (matId,curId);

        SET curId = curId + 1;
    END WHILE;
END
$$
DELIMITER;
CALL sp_matricular_alumno(2,1,1);

SELECT * FROM tbl_matricula;

select * from tbl_matricula_curso;

-- DELETE FROM tbl_matricula;
-- DELETE FROM tbl_matricula_curso;
