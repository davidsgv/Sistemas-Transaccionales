DROP PROCEDURE IF EXISTS spVerificarDatosUsuario
GO

CREATE PROCEDURE spVerificarDatosUsuario
	@correo VARCHAR(500),
	@clave VARCHAR(160)
AS
BEGIN
	SET NOCOUNT ON;


	CREATE TABLE #UsuariosTemporal(
		correo VARCHAR(max),
		clave VARCHAR(max)
	);


	INSERT INTO #UsuariosTemporal
	SELECT 
		correo,
		CONVERT(VARCHAR(MAX),
			DECRYPTBYPASSPHRASE('i*NzwG47e6GX*C$TqTW2ebe^!CWgJ*Dn^HJESX@fpK8bN7eHDMnYCjr@nR&xJWYj#$zH^cW9!A2E%7#'
			, Contrasena
			)
		) AS clave
	FROM Usuario
	WHERE Correo = @correo;


	SELECT TOP 1 
		correo
		, clave
	FROM #UsuariosTemporal
	WHERE clave = @clave;
END