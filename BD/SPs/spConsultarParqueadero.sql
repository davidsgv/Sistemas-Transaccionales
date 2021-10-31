DROP PROCEDURE IF EXISTS spConsultarParqueadero
GO

CREATE PROCEDURE spConsultarParqueadero
	@direccion VARCHAR(500)
AS
BEGIN
	SELECT *
	FROM Parqueadero par
	WHERE par.Ubicacion = @direccion;
END