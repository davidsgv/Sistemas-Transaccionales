DROP PROCEDURE IF EXISTS spConsultarBahias
GO

CREATE PROCEDURE spConsultarBahias
	@idParqueadero INT
AS
BEGIN
	SELECT
		Bahia.IdBahia
		, Bahia.Disponible
		, Bahia.IdParqueadero
		, (
			select Vehiculo.IdVehiculo
			from Pago
			INNER JOIN Vehiculo
				ON Vehiculo.IdVehiculo = Pago.IdVehiculo
			where Pago.IdBahia = Bahia.IdBahia
				and pago.IdPago = (
					select max(Pago.IdPago)
					from Pago
				)
		) as IdVehiculo
	FROM Bahia
	WHERE Bahia.IdParqueadero = @idParqueadero
END