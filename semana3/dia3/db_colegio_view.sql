--?VISTAS
SELECT * FROM tbl_matricula_curso;

CREATE VIEW vw_matricula_notas AS
SELECT 
m.matricula_fecha_registro as fecha,
a.alumno_nombre as alumo,
c.curso_nombre as curso,
mc.curso_nota as nota
FROM tbl_matricula_curso mc
join tbl_matricula m ON mc.matricula_id = m.matricula_id
join tbl_alumno a ON a.alumno_id = m.alumno_id
join tbl_curso c ON c.curso_id = mc.curso_id;

--?LLAMANDO A LA VISTA
SELECT alumo,curso FROM vw_matricula_notas