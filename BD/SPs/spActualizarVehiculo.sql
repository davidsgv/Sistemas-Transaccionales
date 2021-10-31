DROP PROCEDURE spActualizarVehiculo
GO

CREATE PROCEDURE spActualizarVehiculo
	@idVehiculo INT
	, @marca VARCHAR(50) = NULL
	, @idPersona INT = NULL
	, @idTipo INT = NULL
AS
BEGIN
	PRINT @marca

	SELECT * 
	INTO #vehiculo
	FROM Vehiculo ve
	WHERE ve.IdVehiculo = @idVehiculo;

	IF(@marca IS NULL)
		SET @marca = (SELECT Marca FROM #vehiculo);
	IF(@idPersona IS NULL)
		SET @idPersona = (SELECT IdPersona FROM #vehiculo);
	IF(@idTipo IS NULL)
		SET @idTipo = (SELECT IdTipo FROM #vehiculo);

	UPDATE Vehiculo
	SET marca = @marca, IdPersona = @idPersona, idTipo = @idTipo
	WHERE idVehiculo = @idVehiculo;
END