CREATE TABLE Usuario (
	Login VARCHAR(8) NOT NULL PRIMARY KEY, 
	Nome VARCHAR(30) NOT NULL, 
	Cidade_natal VARCHAR(30) NOT NULL
);

-- CREATE TABLE Filme

CREATE TABLE Ator (
	Id VARCHAR(8) NOT NULL PRIMARY KEY, 
	Telefone VARCHAR(30) NOT NULL, 
	Endereco VARCHAR(30) NOT NULL
);

CREATE TABLE Diretor (
	Id VARCHAR(8) NOT NULL PRIMARY KEY, 
	Telefone VARCHAR(30) NOT NULL, 
	Endereco VARCHAR(30) NOT NULL
);

CREATE TABLE ArtistasMusicais (
	Id VARCHAR(8) NOT NULL PRIMARY KEY, 
	Genero_musical VARCHAR(30) NOT NULL, 
	Nome_artistico VARCHAR(30) NOT NULL,
	Pais VARCHAR(30) NOT NULL
);

CREATE TABLE Grupos (
	Id VARCHAR(8) NOT NULL PRIMARY KEY,
	FOREIGN KEY(Id) 
		REFERENCES ArtistasMusicais(Id)
);

CREATE TABLE Duplas (
	Id VARCHAR(8) NOT NULL PRIMARY KEY,
	FOREIGN KEY(Id) 
		REFERENCES ArtistasMusicais(Id)
);

CREATE TABLE Cantor (
	Id VARCHAR(8) NOT NULL PRIMARY KEY,
	FOREIGN KEY(Id) 
		REFERENCES ArtistasMusicais(Id)
);

CREATE TABLE Cantor (
	Id_musico VARCHAR(8) NOT NULL PRIMARY KEY,
	Nome_real VARCHAR(8) NOT NULL,
	Estilo_musical VARCHAR(8) NOT NULL,
	Data_nascimento DATE NOT NULL
);

CREATE TABLE UsuarioBloquearUsuario (
	Login VARCHAR(8) NOT NULL,
	Login_bloqueado VARCHAR(8) NOT NULL,
	PRIMARY KEY(Login, Login_bloqueado),
	FOREIGN KEY(Login)
		REFERENCES Usuario(Login),
	FOREIGN KEY(Login_bloqueado)
		REFERENCES Usuario(Login)
);

CREATE TABLE BloquearMotivo (
	Login VARCHAR(8) NOT NULL,
	Login_bloqueado VARCHAR(8) NOT NULL,
	Motivo VARCHAR(8) NOT NULL,
	PRIMARY KEY(Login, Login_bloqueado, Motivo),
	FOREIGN KEY(Login)
		REFERENCES Usuario(Login),
	FOREIGN KEY(Login_bloqueado)
		REFERENCES Usuario(Login)
);

CREATE TABLE UsuarioRegistraConhecidoUsuario (
	Login VARCHAR(8) NOT NULL,
	Login_registrado VARCHAR(8) NOT NULL,
	PRIMARY KEY(Login, Login_registrado),
	FOREIGN KEY(Login)
		REFERENCES Usuario(Login),
	FOREIGN KEY(Login_registrado)
		REFERENCES Usuario(Login)
);

CREATE TABLE UsuarioAvaliaArtistasMusicais (
	Login VARCHAR(8) NOT NULL,
	Id VARCHAR(8) NOT NULL,
	Nota VARCHAR(8) NOT NULL,
	PRIMARY KEY(Login, Id),
	FOREIGN KEY(Login)
		REFERENCES Usuario(Login),
	FOREIGN KEY(Id)
		REFERENCES ArtistasMusicais(Id)
);

CREATE TABLE UsuarioAvaliaFilme (
	Login VARCHAR(8) NOT NULL,
	Id VARCHAR(8) NOT NULL,
	Nota VARCHAR(8) NOT NULL,
	PRIMARY KEY(Login, Id),
	FOREIGN KEY(Login)
		REFERENCES Usuario(Login),
	FOREIGN KEY(Id)
		REFERENCES Filme(Id)
);

CREATE TABLE UsuarioGostaFilme (
	Login VARCHAR(8) NOT NULL,
	Id VARCHAR(8) NOT NULL,
	PRIMARY KEY(Login, Id),
	FOREIGN KEY(Login)
		REFERENCES Usuario(Login),
	FOREIGN KEY(Id)
		REFERENCES Filme(Id)
);

-- CREATE TABLE FilmePossuiAtor

-- CREATE TABLE AtorEhDiretor

-- CREATE TABLE DiretorDirigeFilme

-- CREATE TABLE CantorPossuiMusico

-- CREATE TABLE DuplasPossuiMusico

-- CREATE TABLE GruposPossuiMusico



