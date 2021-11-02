DROP PROCEDURE IF EXISTS spCrearTiposVehiculo
GO

CREATE PROCEDURE spCrearTiposVehiculo
	@clase VARCHAR(1000)
AS
BEGIN
	DECLARE @registros INT;

	SELECT @registros = COUNT(*)
	FROM TipoVehiculo
	WHERE Clase = @clase

	IF(@registros > 0)
		SELECT 'La clase ya existe'
	ELSE
		INSERT INTO TipoVehiculo (Clase) VALUES (@clase)
END