DROP PROCEDURE IF EXISTS spConsultarDisponibilidadParqueadero
GO

CREATE PROCEDURE spConsultarDisponibilidadParqueadero
	@idParqueadero INT
AS
BEGIN
	SELECT
		COUNT(*) AS 'Bahias Disponibles'
	FROM Parqueadero par
	INNER JOIN Bahia ba
		ON ba.IdParqueadero = par.IdParqueadero
	WHERE par.IdParqueadero = @idParqueadero
		AND ba.Disponible = 1;
END