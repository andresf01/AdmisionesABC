-- INSERT INTO programas_programa(codigo, nombre, snies, creditos, formacion, tipo, metodologia, titulo, descripcion, image_url) 
--     VALUES('3743', 'INGENIERIA DE SISTEMAS', '584', 159, 'PROFESIONAL', 'PREGRADO', 'PRESENCIAL', 'INGENIERO(A) DE SISTEMAS', 'sin descripcion', 'assets/img/programas/sistemas.jpg');
-- INSERT INTO programas_programa(codigo, nombre, snies, creditos, formacion, tipo, metodologia, titulo, descripcion, image_url) 
--     VALUES('3140', 'BIOLOGIA', '592', 169, 'PROFESIONAL', 'PREGRADO', 'PRESENCIAL', 'BIOLOGO(A)', 'sin descripcion', 'assets/img/programas/biologia.jpg');
-- INSERT INTO programas_programa(codigo, nombre, snies, creditos, formacion, tipo, metodologia, titulo, descripcion, image_url) 
--     VALUES('3146', 'FISICA', '594', 169, 'PROFESIONAL', 'PREGRADO', 'PRESENCIAL', 'FISICO(A)', 'sin descripcion', 'assets/img/programas/fisica.jpg');
-- INSERT INTO programas_programa(codigo, nombre, snies, creditos, formacion, tipo, metodologia, titulo, descripcion, image_url) 
--     VALUES('3147', 'MATEMATICAS', '595', 158, 'PROFESIONAL', 'PREGRADO', 'PRESENCIAL', 'MATEMATICO(A)', 'sin descripcion', 'assets/img/programas/.jpg');
-- INSERT INTO programas_programa(codigo, nombre, snies, creditos, formacion, tipo, metodologia, titulo, descripcion, image_url) 
--     VALUES('3148', 'QUIMICA', '596', 168, 'PROFESIONAL', 'PREGRADO', 'PRESENCIAL', 'QUIMICO(A)');
-- INSERT INTO programas_programa(codigo, nombre, snies, creditos, formacion, tipo, metodologia, titulo, descripcion, image_url) 
--     VALUES('3340', 'ECONOMIA', '579', 149, 'PROFESIONAL', 'PREGRADO', 'PRESENCIAL', 'ECONOMISTA');
-- INSERT INTO programas_programa(codigo, nombre, snies, creditos, formacion, tipo, metodologia, titulo, descripcion, image_url) 
--     VALUES('3350', 'SOCIOLOGIA', '575', 120, 'PROFESIONAL', 'PREGRADO', 'PRESENCIAL', 'SOCIOLOGO(A)');
-- INSERT INTO programas_programa(codigo, nombre, snies, creditos, formacion, tipo, metodologia, titulo, descripcion, image_url) 
--     VALUES('3461', 'PSICOLOGIA', '573', 168, 'PROFESIONAL', 'PREGRADO', 'PRESENCIAL', 'PSICOLOGO(A)');
-- INSERT INTO programas_programa(codigo, nombre, snies, creditos, formacion, tipo, metodologia, titulo, descripcion, image_url) 
--     VALUES('3545', 'ARQUITECTURA', '591', 169, 'PROFESIONAL', 'PREGRADO', 'PRESENCIAL', 'ARQUITECTO(A)');


-- INSERT INTO admisiones_periodo(identificador, nombre, puntaje_minimo) values('2017-1', 'Febrero-Junio 2017', 170);


-- INSERT INTO admisiones_oferta(cupo, peso_lectura, peso_matematicas, peso_naturales, peso_sociales, peso_ingles, peso_prueba, periodo_id, programa_id) 
--     values(40, 20, 20, 20, 20, 20, 0, (SELECT id from admisiones_periodo WHERE identificador = '2017-1'), (SELECT id from programas_programa WHERE codigo = '3743'));

-- INSERT INTO admisiones_oferta(cupo, peso_lectura, peso_matematicas, peso_naturales, peso_sociales, peso_ingles, peso_prueba, periodo_id, programa_id) 
--     values(70, 30, 40, 15, 5, 10, 0, (SELECT id from admisiones_periodo WHERE identificador = '2017-1'), (SELECT id from programas_programa WHERE codigo = '3140'));
    
-- INSERT INTO admisiones_oferta(cupo, peso_lectura, peso_matematicas, peso_naturales, peso_sociales, peso_ingles, peso_prueba, periodo_id, programa_id) 
--     values(40, 30, 40, 20, 5, 5, 0, (SELECT id from admisiones_periodo WHERE identificador = '2017-1'), (SELECT id from programas_programa WHERE codigo = '3146'));
    
-- INSERT INTO admisiones_oferta(cupo, peso_lectura, peso_matematicas, peso_naturales, peso_sociales, peso_ingles, peso_prueba, periodo_id, programa_id) 
--     values(50, 30, 40, 20, 5, 5, 0, (SELECT id from admisiones_periodo WHERE identificador = '2017-1'), (SELECT id from programas_programa WHERE codigo = '3147'));
    
-- INSERT INTO admisiones_oferta(cupo, peso_lectura, peso_matematicas, peso_naturales, peso_sociales, peso_ingles, peso_prueba, periodo_id, programa_id) 
--     values(50, 30, 40, 15, 5, 10, 0, (SELECT id from admisiones_periodo WHERE identificador = '2017-1'), (SELECT id from programas_programa WHERE codigo = '3148'));
    
-- INSERT INTO admisiones_oferta(cupo, peso_lectura, peso_matematicas, peso_naturales, peso_sociales, peso_ingles, peso_prueba, periodo_id, programa_id) 
--     values(55, 30, 30, 15, 15, 10, 0, (SELECT id from admisiones_periodo WHERE identificador = '2017-1'), (SELECT id from programas_programa WHERE codigo = '3340'));
    
-- INSERT INTO admisiones_oferta(cupo, peso_lectura, peso_matematicas, peso_naturales, peso_sociales, peso_ingles, peso_prueba, periodo_id, programa_id) 
--     values(60, 25, 25, 15, 25, 10, 0, (SELECT id from admisiones_periodo WHERE identificador = '2017-1'), (SELECT id from programas_programa WHERE codigo = '3350'));
    
-- INSERT INTO admisiones_oferta(cupo, peso_lectura, peso_matematicas, peso_naturales, peso_sociales, peso_ingles, peso_prueba, periodo_id, programa_id) 
--     values(55, 30, 20, 25, 25, 0, 0, (SELECT id from admisiones_periodo WHERE identificador = '2017-1'), (SELECT id from programas_programa WHERE codigo = '3461'));
    
-- INSERT INTO admisiones_oferta(cupo, peso_lectura, peso_matematicas, peso_naturales, peso_sociales, peso_ingles, peso_prueba, periodo_id, programa_id) 
--     values(45, 5, 5, 5, 5, 0, 70, (SELECT id from admisiones_periodo WHERE identificador = '2017-1'), (SELECT id from programas_programa WHERE codigo = '3545'));