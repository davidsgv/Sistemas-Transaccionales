DROP PROCEDURE IF EXISTS spConsultarTiposVehiculo
GO

CREATE PROCEDURE spConsultarTiposVehiculo
AS
BEGIN
	SELECT Clase
	FROM TipoVehiculo
END