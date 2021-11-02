DROP PROCEDURE IF EXISTS spConsultarParqueaderoByDireccion
GO

CREATE PROCEDURE spConsultarParqueaderoByDireccion
	@direccion VARCHAR(500)
AS
BEGIN
	SELECT *
	FROM Parqueadero par
	WHERE par.Ubicacion = @direccion;
END