EXEC spCrearUsuario @correo = 'davidsgv98@gmail.com', @clave = '123'

SELECT
	Correo,
	CONVERT(VARCHAR(MAX),
		DECRYPTBYPASSPHRASE('i*NzwG47e6GX*C$TqTW2ebe^!CWgJ*Dn^HJESX@fpK8bN7eHDMnYCjr@nR&xJWYj#$zH^cW9!A2E%7#'
		, Contrasena
		)
	)
FROM Usuario