CREATE DATABASE elrapido

USE elrapido

CREATE TABLE servicios
(id_servicio int,
tipo_servicio varchar (50)
CONSTRAINT pk_id_servicio PRIMARY KEY (id_servicio)
)

CREATE TABLE distribuciones
(id_dist INT,
distribucion VARCHAR (50)
CONSTRAINT pk_id_dist PRIMARY KEY (id_dist)
)

CREATE TABLE ciudades
(id_ciudades int,
ciudades varchar (100)
CONSTRAINT id_ciudades PRIMARY KEY (id_ciudades)
)

CREATE TABLE barrios
(
    
)