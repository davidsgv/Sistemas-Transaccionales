DROP PROCEDURE IF EXISTS spCrearUsuario
GO

CREATE PROCEDURE spCrearUsuario
	@correo VARCHAR(500),
	@clave VARCHAR(160)
AS
BEGIN
	INSERT INTO Usuario
		(Correo, Contrasena)
	VALUES
		(
			@correo,
			ENCRYPTBYPASSPHRASE('i*NzwG47e6GX*C$TqTW2ebe^!CWgJ*Dn^HJESX@fpK8bN7eHDMnYCjr@nR&xJWYj#$zH^cW9!A2E%7#',
			@clave)
		);
END