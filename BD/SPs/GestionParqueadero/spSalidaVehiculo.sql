CREATE OR ALTER PROCEDURE spSalidaVehiculo
	@idVehiculo INT
AS
BEGIN
	DECLARE @idPago INT;
	DECLARE @costo INT;

	SELECT @idPago = IdPago
	FROM Pago pag
	INNER JOIN Bahia bah
		ON bah.IdBahia = pag.IdBahia
	WHERE bah.Disponible = 0
		AND pag.IdVehiculo = @idVehiculo

	SELECT @costo = costo
	FROM Tarifa tar
	INNER JOIN TipoVehiculo tip
		ON Tip.IdTipo = tar.IdTipo
	INNER JOIN Vehiculo veh
		ON veh.IdTipo = tip.IdTipo
	WHERE veh.IdVehiculo = @idVehiculo
	
	
	DECLARE @tiempo INT;
	SELECT @tiempo = DATEDIFF(minute, Fecha, GETDATE())
	FROM Pago
	WHERE IdPago = @idPago
	
	UPDATE Pago
	SET Tiempo = @tiempo, Costo =  @costo * @tiempo
	WHERE IdPago = @idPago 

END