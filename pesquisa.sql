CREATE DATABASE pesquisa;
USE pesquisa;

CREATE TABLE perguntas(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    carnaval BOOLEAN NOT NULL,
    acai BOOLEAN NOT NULL,
    alcool BOOLEAN NOT NULL,
    id_estilo INT NOT NULL,
	FOREIGN KEY (id) REFERENCES estilos_musicais(id),
    sugestao TEXT
    );

CREATE TABLE estilos_musicais(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL,
    descricao TEXT
    );

select * from perguntas;
select * from estilos_musicais;
