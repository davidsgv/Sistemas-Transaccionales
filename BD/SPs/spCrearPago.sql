DROP PROCEDURE IF EXISTS spCrearPago
GO

CREATE PROCEDURE spCrearPago
	@idBahia INT
	, @idVehiculo INT
	, @tiempo INT
	, @costo MONEY
	, @Fecha DATETIME
AS
BEGIN
	INSERT INTO Pago
			(IdBahia, IdVehiculo, Tiempo, Costo, Fecha)
		VALUES 
			(@idBahia, @idVehiculo, @tiempo, @costo, @Fecha);	
END