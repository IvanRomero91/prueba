CREATE DATABASE administracion_alumnos

USE administracion_alumnos

CREATE TABLE barrios
(id_barrio int IDENTITY(1,1),
nombre_barrio VARCHAR(50)
CONSTRAINT pk_id_barrio PRIMARY KEY (id_barrio)
)

CREATE TABLE alumnos
(legajo INT,
nombre varchar(50),
apellido VARCHAR(50),
calle VARCHAR(50),
nro INT,
id_barrio INT,
nro_dni int,
nro_tel bigint,
e_mail varchar (100),
fecha_nac DATETIME
CONSTRAINT pk_legajo PRIMARY KEY (legajo)
CONSTRAINT fk_id_barrio PRIMARY KEY (id_barrio)
REFERENCES barrios
)

