CREATE DATABASE IF NOT EXISTS master_python;

USE master_python;

CREATE TABLE IF NOT EXISTS users(
    id int(10) auto_increment not null,
    nombre varchar(100) not null,
    apellido varchar(100) not null,
    email varchar(100) not null,
    password varchar(255) not null,
    fecha datetime not null,
    CONSTRAINT pk_users PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)

)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS notas(
    id int(10) auto_increment not null,
    usuario_id int(10) not null,
    titulo varchar(100) not null,
    descripcion MEDIUMTEXT not null,
    fecha datetime not null,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_notas_users FOREIGN KEY(usuario_id) REFERENCES users(id)

)ENGINE=InnoDB;


