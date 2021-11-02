DROP PROCEDURE IF EXISTS spCrearBahia
GO

CREATE PROCEDURE spCrearBahia
	@idParqueadero INT
	, @cantidad INT
AS
BEGIN
	DECLARE @count INT = 0;
	WHILE @count < @cantidad
	BEGIN
		INSERT INTO Bahia
			(IdParqueadero, Disponible)
		VALUES (@idParqueadero, 1)
		SET @count = @count + 1
	END
END