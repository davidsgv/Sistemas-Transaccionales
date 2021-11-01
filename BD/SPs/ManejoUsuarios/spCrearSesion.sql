DROP PROCEDURE IF EXISTS spCrearSesion
GO

CREATE PROCEDURE spCrearSesion
	@correo VARCHAR(500)
	, @navegador VARCHAR(MAX)
	, @token VARCHAR(MAX)
AS
BEGIN
	SET NOCOUNT ON;

	SELECT TOP 1
		IdUsuario
		, Correo
	INTO #temporalUsuario
	FROM Usuario
	WHERE Correo = @correo

	INSERT INTO Sesion
	SELECT 
		IdUsuario
		, @navegador
		, @token
	FROM #temporalUsuario

END