CREATE PROCEDURE spConsultarComprobantePago
	@idPersona INT = NULL
	, @idVehiculo INT = NULL
AS
BEGIN
	IF(@idPersona IS NOT NULL)
		BEGIN
			SELECT 
				par.Nombre AS Parqueadero
				, par.Ubicacion AS Ubicacion
				, per.Nombre AS NombreDueño
				, pag.Tiempo
				, pag.Fecha
				, pag.Costo AS TotalPago
				, ba.IdBahia AS Bahia
				, veh.Marca
				, veh.IdTipo
			INTO #temp
			FROM Persona per
			INNER JOIN Vehiculo veh
				ON per.IdPersona = veh.IdPersona
			INNER JOIN Pago pag
				ON pag.IdVehiculo = veh.IdVehiculo
			INNER JOIN Bahia ba
				ON ba.IdBahia = pag.IdBahia
			INNER JOIN Parqueadero par
				ON par.IdParqueadero = ba.IdParqueadero
			WHERE per.IdPersona = @idPersona

			SELECT 
				Parqueadero
				, Ubicacion
				, NombreDueño
				, Tiempo
				, Fecha
				, TotalPago
				, Bahia
				, Marca
				, tip.Clase AS 'Clase vehiculo'
				, taf.Costo
			FROM #temp temp
			INNER JOIN TipoVehiculo tip
				ON tip.IdTipo = temp.IdTipo
			INNER JOIN Tarifa taf
				ON taf.IdTipo = tip.IdTipo
		END
	ELSE
		BEGIN
			IF(@idVehiculo IS NOT NULL)
				SELECT 
					par.Nombre AS Parqueadero
					, par.Ubicacion AS Ubicacion
					, per.Nombre AS NombreDueño
					, pag.Tiempo
					, pag.Fecha
					, pag.Costo AS TotalPago
					, ba.IdBahia AS Bahia
					, veh.Marca
					, veh.IdTipo
				INTO #temporal
				FROM Persona per
				INNER JOIN Vehiculo veh
					ON per.IdPersona = veh.IdPersona
				INNER JOIN Pago pag
					ON pag.IdVehiculo = veh.IdVehiculo
				INNER JOIN Bahia ba
					ON ba.IdBahia = pag.IdBahia
				INNER JOIN Parqueadero par
					ON par.IdParqueadero = ba.IdParqueadero
				WHERE veh.IdVehiculo = @idVehiculo

				SELECT 
					Parqueadero
					, Ubicacion
					, NombreDueño
					, Tiempo
					, Fecha
					, TotalPago
					, Bahia
					, Marca
					, tip.Clase AS 'Clase vehiculo'
					, taf.Costo
				FROM #temporal temp
				INNER JOIN TipoVehiculo tip
					ON tip.IdTipo = temp.IdTipo
				INNER JOIN Tarifa taf
					ON taf.IdTipo = tip.IdTipo
		END
		
END