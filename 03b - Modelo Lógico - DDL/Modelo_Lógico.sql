CREATE TABLE Usuario (
	Login VARCHAR(32)  NOT NULL PRIMARY KEY,
	Nome VARCHAR(30) NOT NULL, 
	Cidade_natal VARCHAR(30) NOT NULL
);

CREATE TABLE Filme(
	Id VARCHAR(32) NOT NULL PRIMARY KEY,
	Nome VARCHAR(20) NOT NULL,
	Data_lancamento DATE NOT NULL,
	Categoria VARCHAR(20) NOT NULL	
);

CREATE TABLE Ator (
	Id VARCHAR(32) NOT NULL PRIMARY KEY, 
	Telefone VARCHAR(30) NOT NULL, 
	Endereco VARCHAR(30) NOT NULL
);

CREATE TABLE Diretor (
	Id VARCHAR(32) NOT NULL PRIMARY KEY, 
	Telefone VARCHAR(30) NOT NULL, 
	Endereco VARCHAR(30) NOT NULL
);

CREATE TABLE ArtistasMusicais (
	Id VARCHAR(32) NOT NULL PRIMARY KEY, 
	Genero_musical VARCHAR(30) NOT NULL, 
	Nome_artistico VARCHAR(30) NOT NULL,
	Pais VARCHAR(30) NOT NULL
);

CREATE TABLE Grupos (
	Id VARCHAR(32) NOT NULL PRIMARY KEY,
	FOREIGN KEY(Id) 
		REFERENCES ArtistasMusicais(Id)
);

CREATE TABLE Duplas (
	Id VARCHAR(32) NOT NULL PRIMARY KEY,
	FOREIGN KEY(Id) 
		REFERENCES ArtistasMusicais(Id)
);

CREATE TABLE Cantor (
	Id VARCHAR(32) NOT NULL PRIMARY KEY,
	FOREIGN KEY(Id) 
		REFERENCES ArtistasMusicais(Id)
);

CREATE TABLE Musico (
	Id VARCHAR(1232) NOT NULL PRIMARY KEY,
	Nome_real VARCHAR(1232) NOT NULL,
	Estilo_musical VARCHAR(1232) NOT NULL,
	Data_nascimento DATE NOT NULL
);

CREATE TABLE UsuarioBloquearUsuario (
	Login VARCHAR(32) NOT NULL,
	Login_bloqueado VARCHAR(32) NOT NULL,
	PRIMARY KEY(Login, Login_bloqueado),
	FOREIGN KEY(Login)
		REFERENCES Usuario(Login),
	FOREIGN KEY(Login_bloqueado)
		REFERENCES Usuario(Login)
);

CREATE TABLE BloquearMotivo (
	Login VARCHAR(32) NOT NULL,
	Login_bloqueado VARCHAR(32) NOT NULL,
	Motivo VARCHAR(32) NOT NULL,
	PRIMARY KEY(Login, Login_bloqueado, Motivo),
	FOREIGN KEY(Login)
		REFERENCES Usuario(Login),
	FOREIGN KEY(Login_bloqueado)
		REFERENCES Usuario(Login)
);

CREATE TABLE UsuarioRegistraConhecidoUsuario (
	Login VARCHAR(32) NOT NULL,
	Login_registrado VARCHAR(32) NOT NULL,
	PRIMARY KEY(Login, Login_registrado),
	FOREIGN KEY(Login)
		REFERENCES Usuario(Login),
	FOREIGN KEY(Login_registrado)
		REFERENCES Usuario(Login)
);

CREATE TABLE UsuarioAvaliaArtistasMusicais (
	Login VARCHAR(32) NOT NULL,
	Id VARCHAR(32) NOT NULL,
	Nota INTEGER NOT NULL,
	PRIMARY KEY(Login, Id),
	FOREIGN KEY(Login)
		REFERENCES Usuario(Login),
	FOREIGN KEY(Id)
		REFERENCES ArtistasMusicais(Id)
);

CREATE TABLE UsuarioAvaliaFilme (
	Login VARCHAR(32) NOT NULL,
	Id VARCHAR(32) NOT NULL,
	Nota INTEGER NOT NULL,
	PRIMARY KEY(Login, Id),
	FOREIGN KEY(Login)
		REFERENCES Usuario(Login),
	FOREIGN KEY(Id)
		REFERENCES Filme(Id)
);

CREATE TABLE UsuarioGostaFilme (
	Login VARCHAR(32) NOT NULL,
	Id VARCHAR(32) NOT NULL,
	PRIMARY KEY(Login, Id),
	FOREIGN KEY(Login)
		REFERENCES Usuario(Login),
	FOREIGN KEY(Id)
		REFERENCES Filme(Id)
);

CREATE TABLE FilmePossuiAtor(
	Id VARCHAR(32) NOT NULL,
	Id_ator VARCHAR(32) NOT NULL,
	Salario INTEGER NOT NULL,
	PRIMARY KEY(Id, Id_ator),
	FOREIGN KEY(Id)
		REFERENCES Filme(Id),
	FOREIGN KEY(Id_ator)
		REFERENCES Ator(Id)
);


CREATE TABLE AtorEhDiretor(
	Id_ator VARCHAR(32) NOT NULL,
	Id_diretor VARCHAR(32) NOT NULL,
	PRIMARY KEY(Id_ator, Id_diretor),
	FOREIGN KEY(Id_ator)
		REFERENCES Ator(Id),
	FOREIGN KEY(Id_diretor)
		REFERENCES Diretor(Id)
);

CREATE TABLE DiretorDirigeFilme(
	Id_diretor VARCHAR(32) NOT NULL,
	Id_filme VARCHAR(32) NOT NULL,
	Salario INTEGER NOT NULL,
	PRIMARY KEY(Id_diretor, Id_filme),
	FOREIGN KEY(Id_diretor)
		REFERENCES Diretor(Id),
	FOREIGN KEY(Id_filme)
		REFERENCES Filme(Id)	
);

CREATE TABLE CantorPossuiMusico(
	Id_artistas_m VARCHAR(32) NOT NULL,
	Id_musico VARCHAR(32) NOT NULL,
	PRIMARY KEY(Id_artistas_m, Id_musico),
	FOREIGN KEY(Id_artistas_m)
		REFERENCES ArtistasMusicais(Id),
	FOREIGN KEY(Id_musico)
		REFERENCES Musico(Id)	
);

CREATE TABLE DuplasPossuiMusico(
	Id_artistas_m VARCHAR(32) NOT NULL,
	Id_musico VARCHAR(32) NOT NULL,
	PRIMARY KEY(Id_artistas_m, Id_musico),
	FOREIGN KEY(Id_artistas_m)
		REFERENCES ArtistasMusicais(Id),
	FOREIGN KEY(Id_musico)
		REFERENCES Musico(Id)	
);

CREATE TABLE GruposPossuiMusico(
	Id_artistas_m VARCHAR(32) NOT NULL,
	Id_musico VARCHAR(32) NOT NULL,
	PRIMARY KEY(Id_artistas_m, Id_musico),
	FOREIGN KEY(Id_artistas_m)
		REFERENCES ArtistasMusicais(Id),
	FOREIGN KEY(Id_musico)
		REFERENCES Musico(Id)	
);


-- Login,Nome,Cidade_natal
INSERT INTO Usuario VALUES('pedrofrancescon','Pedro Francescon','Maceió');
INSERT INTO Usuario VALUES('odvieira','Daniel Eduardo','Brasília');
INSERT INTO Usuario VALUES('gustavomfranck','Gustavo Maysonnave','Curitiba');

-- Id,Nome,Data_lancamento,Categoria
INSERT INTO Filme VALUES('00000001','Django','2015-03-11','Ação');
INSERT INTO Filme VALUES('00000002','A Origem','2016-04-22','Suspense');
INSERT INTO Filme VALUES('00000003','Sem Limites','2012-05-13','Ação');

-- Id,	Telefone,	Endereco,
INSERT INTO Ator VALUES('00000004','9999999999','Travessa Almirante Juca, 222');
INSERT INTO Ator VALUES('00000005','32323232323232323232','Rua Aiapó, 35');
INSERT INTO Ator VALUES('00000006','7777777777','Alameda Cabral, 56');

-- Id,Telefone,Endereco
INSERT INTO Diretor VALUES('00000007','5555555555','Travessa Almirante Juca, 227');
INSERT INTO Diretor VALUES('000000032','4444444444','Rua Aiapó, 37');
INSERT INTO Diretor VALUES('00000009','3333333333','Alameda Cabral, 57');

-- Id,	Genero_musical,	Nome_artistico,	Pais
INSERT INTO ArtistasMusicais VALUES('00000010','Pagode','Juquinha','Brasil');
INSERT INTO ArtistasMusicais VALUES('00000011','Rock','Axel','EUA');
INSERT INTO ArtistasMusicais VALUES('00000012','Axé','Banda Rosa','Brasil');
INSERT INTO ArtistasMusicais VALUES('00000013','Sertanejo','Henrique & Juliano','Brasil');

INSERT INTO Grupos VALUES('00000012');

INSERT INTO Duplas VALUES('00000013');

INSERT INTO Cantor VALUES('00000010');

INSERT INTO Musico VALUES('00000014','Anderson Almeida','Pagode','1994-11-22');
INSERT INTO Musico VALUES('00000015','Jorge Arae','Rock','1992-06-14');
INSERT INTO Musico VALUES('00000016','Renato Vincentin','Axé','1990-05-15');

INSERT INTO UsuarioBloquearUsuario VALUES('pedrofrancescon','odvieira');
INSERT INTO UsuarioBloquearUsuario VALUES('odvieira','gustavomfranck');
INSERT INTO UsuarioBloquearUsuario VALUES('gustavomfranck','pedrofrancescon');

INSERT INTO BloquearMotivo VALUES('pedrofrancescon','odvieira','Muitos comentários');
INSERT INTO BloquearMotivo VALUES('odvieira','gustavomfranck','Compartilha coisas politicas');
INSERT INTO BloquearMotivo VALUES('gustavomfranck','pedrofrancescon','Só posta foto do cachorro');

INSERT INTO UsuarioRegistraConhecidoUsuario VALUES('odvieira','pedrofrancescon');
INSERT INTO UsuarioRegistraConhecidoUsuario VALUES('odvieira','gustavomfranck');
INSERT INTO UsuarioRegistraConhecidoUsuario VALUES('gustavomfranck','pedrofrancescon');

INSERT INTO UsuarioAvaliaArtistasMusicais VALUES('gustavomfranck','00000010','6');
INSERT INTO UsuarioAvaliaArtistasMusicais VALUES('pedrofrancescon','00000011','32');
INSERT INTO UsuarioAvaliaArtistasMusicais VALUES('gustavomfranck','00000013','7');

INSERT INTO UsuarioAvaliaFilme VALUES('odvieira','00000001','10');
INSERT INTO UsuarioAvaliaFilme VALUES('pedrofrancescon','00000002','4');
INSERT INTO UsuarioAvaliaFilme VALUES('gustavomfranck','00000003','2');

INSERT INTO UsuarioGostaFilme VALUES('odvieira','00000001');
INSERT INTO UsuarioGostaFilme VALUES('pedrofrancescon','00000001');
INSERT INTO UsuarioGostaFilme VALUES('gustavomfranck','00000002');

INSERT INTO FilmePossuiAtor VALUES('00000001','00000004',50000);
INSERT INTO FilmePossuiAtor VALUES('00000002','00000005',14000);
INSERT INTO FilmePossuiAtor VALUES('00000003','00000006',7500);

INSERT INTO AtorEhDiretor VALUES('00000004','00000007');
INSERT INTO AtorEhDiretor VALUES('00000005','000000032');

INSERT INTO DiretorDirigeFilme VALUES('00000007','00000001',24000);
INSERT INTO DiretorDirigeFilme VALUES('000000032','00000003',19000);

INSERT INTO CantorPossuiMusico VALUES('00000010','00000014');

INSERT INTO DuplasPossuiMusico VALUES('00000013','00000015');

INSERT INTO GruposPossuiMusico VALUES('00000012','00000016');