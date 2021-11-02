DROP PROCEDURE IF EXISTS spCrearVehiculo
GO

CREATE PROCEDURE spCrearVehiculo
	@Marca VARCHAR (50),
	@IdPersona INT,
	@IdTipo INT
AS
BEGIN
	INSERT INTO Vehiculo (Marca, IdPersona, IdTipo ) VALUES (@Marca, @IdPersona, @IdTipo)
END