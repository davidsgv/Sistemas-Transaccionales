DROP TABLE IF EXISTS Sesion;
DROP TABLE IF EXISTS Usuario;

USE Parqueadero
CREATE TABLE Usuario(
	IdUsuario INT IDENTITY(1,1),
	Correo VARCHAR(500) NOT NULL,
	Contrasena varbinary(160) NOT NULL
	CONSTRAINT pk_Usuario
		PRIMARY KEY CLUSTERED (IdUsuario),
	CONSTRAINT unique_correo UNIQUE (Correo)
);

CREATE TABLE Sesion(
	IdSesion INT IDENTITY(1,1),
	IdUsuario INT,
	Navegador VARCHAR(1000),
	Token VARCHAR(1000)
	CONSTRAINT pk_Sesion
		PRIMARY KEY CLUSTERED (IdSesion),
	CONSTRAINT fk_Sesion_Usuario
		FOREIGN KEY (IdUsuario) REFERENCES 
			Usuario (IdUsuario),
	CONSTRAINT unique_token UNIQUE (Token)
);