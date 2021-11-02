DROP PROCEDURE IF EXISTS spConsultarBahias
GO

CREATE PROCEDURE spConsultarBahias
	@idParqueadero INT
AS
BEGIN
	SELECT * 
	FROM Bahia
	WHERE Bahia.IdParqueadero = @idParqueadero
END