CREATE OR ALTER PROCEDURE spConsultarParqueaderos
	@idParqueadero INT = null
AS
BEGIN
	IF(@idParqueadero IS NULL)
		SELECT
			IdParqueadero
			, Nombre
			, Ubicacion
		FROM Parqueadero
	ELSE
		SELECT
			IdParqueadero
			, Nombre
			, Ubicacion
		FROM Parqueadero
		WHERE IdParqueadero = @idParqueadero
END