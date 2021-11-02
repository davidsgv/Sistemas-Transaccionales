DROP PROCEDURE IF EXISTS spCrearParqueadero
GO

CREATE PROCEDURE spCrearParqueadero
	@nombre VARCHAR(MAX)
	, @ubicacion VARCHAR(MAX)
AS
BEGIN
	INSERT INTO Parqueadero
			(Nombre, Ubicacion)
		VALUES
			(@nombre, @ubicacion)
END