CREATE TABLE Usuario (
	Login VARCHAR(8) NOT NULL PRIMARY KEY, 
	Nome VARCHAR(30) NOT NULL, 
	Cidade_natal VARCHAR(30) NOT NULL
);

CREATE TABLE Filme(
	Id VARCHAR(8) NOT NULL PRIMARY KEY,
	Nome VARCHAR(20) NOT NULL,
	Data_lancamento DATE NOT NULL,
	Categoria VARCHAR(20) NOT NULL,	
);

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

CREATE TABLE Musico(
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

CREATE TABLE FilmePossuiAtor(
	Id VARCHAR(8) NOT NULL,
	Id_ator VARCHAR(8) NOT NULL,
	Salario INTEGER NOT NULL,
	PRIMARY KEY(Id, Id_ator),
	FOREIGN KEY(Id)
		REFERENCES Filme(Id),
	FOREIGN KEY(Id_ator)
		REFERENCES Ator(Id)
);


CREATE TABLE AtorEhDiretor(
	Id_ator VARCHAR(8) NOT NULL,
	Id_diretor VARCHAR(8) NOT NULL,
	PRIMARY KEY(Id_ator, Id_diretor),
	FOREIGN KEY(Id_ator)
		REFERENCES Ator(Id),
	FOREIGN KEY(Id_diretor)
		REFERENCES Diretor(Id)
);

CREATE TABLE DiretorDirigeFilme(
	Id_diretor VARCHAR(8) NOT NULL,
	Id_filme VARCHAR(8) NOT NULL,
	Salario INTEGER NOT NULL,
	PRIMARY KEY(Id_diretor, Id_filme),
	FOREIGN KEY(Id_diretor)
		REFERENCES Diretor(Id),
	FOREIGN KEY(Id_filme)
		REFERENCES Filme(Id)	
);

CREATE TABLE CantorPossuiMusico(
	Id_artistas_m VARCHAR(8) NOT NULL,
	Id_musico VARCHAR(8) NOT NULL,
	PRIMARY KEY(Id_artistas_m, Id_musico),
	FOREIGN KEY(Id_artistas_m)
		REFERENCES ArtistasMusicais(Id),
	FOREIGN KEY(Id_musico)
		REFERENCES Musico(Id)	
);

CREATE TABLE DuplasPossuiMusico(
	Id_duplas VARCHAR(8) NOT NULL,
	Id_musico VARCHAR(8) NOT NULL,
	PRIMARY KEY(Id_duplas, Id_musico),
	FOREIGN KEY(Id_duplas)
		REFERENCES Duplas(Id),
	FOREIGN KEY(Id_musico)
		REFERENCES Musico(Id)	
);

CREATE TABLE GruposPossuiMusico(
	Id_grupos VARCHAR(8) NOT NULL,
	Id_musico VARCHAR(8) NOT NULL,
	PRIMARY KEY(Id_grupos, Id_musico),
	FOREIGN KEY(Id_grupos)
		REFERENCES Grupos(Id),
	FOREIGN KEY(Id_musico)
		REFERENCES Musico(Id)	
);


-- Login,Nome,Cidade_natal
INSERT INTO Usuario VALUES('pedrofrancescon','Pedro Francescon','Maceió');
INSERT INTO Usuario VALUES('odvieira','Daniel Eduardo','Brasília');
INSERT INTO Usuario VALUES('gustavomfranck','Gustavo Maysonnave','Curitiba');

-- Id,Nome,Data_lancamento,Categoria
INSERT INTO Filme VALUES('','','','');
INSERT INTO Filme VALUES('','','','');
INSERT INTO Filme VALUES('','','','');

-- Id,	Telefone,	Endereco,
INSERT INTO Ator VALUES('','','');
INSERT INTO Ator VALUES('','','');
INSERT INTO Ator VALUES('','','');

-- Id,Telefone,Endereco
INSERT INTO Diretor VALUES();
INSERT INTO Diretor VALUES();
INSERT INTO Diretor VALUES();

-- Id,	Genero_musical,	Nome_artistico,	Pais
INSERT INTO ArtistasMusicais VALUES();
INSERT INTO ArtistasMusicais VALUES();
INSERT INTO ArtistasMusicais VALUES();

INSERT INTO Grupos VALUES();
INSERT INTO Grupos VALUES();
INSERT INTO Grupos VALUES();

INSERT INTO Duplas VALUES();
INSERT INTO Duplas VALUES();
INSERT INTO Duplas VALUES();

INSERT INTO Cantor VALUES();
INSERT INTO Cantor VALUES();
INSERT INTO Cantor VALUES();

INSERT INTO Musico VALUES();
INSERT INTO Musico VALUES();
INSERT INTO Musico VALUES();

INSERT INTO UsuarioBloquearUsuario VALUES();
INSERT INTO UsuarioBloquearUsuario VALUES();
INSERT INTO UsuarioBloquearUsuario VALUES();

INSERT INTO BloquearMotivo VALUES();
INSERT INTO BloquearMotivo VALUES();
INSERT INTO BloquearMotivo VALUES();

INSERT INTO UsuarioRegistraConhecidoUsuario VALUES();
INSERT INTO UsuarioRegistraConhecidoUsuario VALUES();
INSERT INTO UsuarioRegistraConhecidoUsuario VALUES();

INSERT INTO UsuarioAvaliaArtistasMusicais VALUES();
INSERT INTO UsuarioAvaliaArtistasMusicais VALUES();
INSERT INTO UsuarioAvaliaArtistasMusicais VALUES();

INSERT INTO UsuarioAvaliaFilme VALUES();
INSERT INTO UsuarioAvaliaFilme VALUES();
INSERT INTO UsuarioAvaliaFilme VALUES();

INSERT INTO UsuarioGostaFilme VALUES();
INSERT INTO UsuarioGostaFilme VALUES();
INSERT INTO UsuarioGostaFilme VALUES();

INSERT INTO FilmePossuiAtor VALUES();
INSERT INTO FilmePossuiAtor VALUES();
INSERT INTO FilmePossuiAtor VALUES();

INSERT INTO AtorEhDiretor VALUES();
INSERT INTO AtorEhDiretor VALUES();
INSERT INTO AtorEhDiretor VALUES();

INSERT INTO DiretorDirigeFilme VALUES();
INSERT INTO DiretorDirigeFilme VALUES();
INSERT INTO DiretorDirigeFilme VALUES();

INSERT INTO CantorPossuiMusico VALUES();
INSERT INTO CantorPossuiMusico VALUES();
INSERT INTO CantorPossuiMusico VALUES();

INSERT INTO DuplasPossuiMusico VALUES();
INSERT INTO DuplasPossuiMusico VALUES();
INSERT INTO DuplasPossuiMusico VALUES();

INSERT INTO GruposPossuiMusico VALUES();
INSERT INTO GruposPossuiMusico VALUES();
INSERT INTO GruposPossuiMusico VALUES();
