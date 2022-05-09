--?FUNCIONES

DELIMITER $$


CREATE FUNCTION fn_contar_curso()
    RETURNS INT 
    DETERMINISTIC
BEGIN

    DECLARE total INT ;

    SELECT count(*) into total from tbl_curso;

    RETURN total;
END
$$

DELIMITER;

SELECT fn_contar_curso() from tbl_curso

