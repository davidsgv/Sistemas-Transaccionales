DROP PROCEDURE IF EXISTS spVerificarSesionToken
GO

CREATE PROCEDURE spVerificarSesionToken
	@token VARCHAR(max)
AS
BEGIN
	SET NOCOUNT ON;

	SELECT Token
	FROM Sesion
	WHERE Token = @token
END