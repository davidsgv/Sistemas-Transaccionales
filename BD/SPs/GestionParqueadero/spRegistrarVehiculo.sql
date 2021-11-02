CREATE OR ALTER PROCEDURE spRegistrarVehiculo
	@idBahia INT
	, @idVehiculo INT
AS
BEGIN
	DECLARE @disponible BIT;
	SELECT @disponible = Disponible
	FROM Bahia
	WHERE IdBahia = @idBahia

	IF(@disponible = 1)
		INSERT INTO Pago (IdBahia, IdVehiculo, Fecha) VALUES (@idBahia, @idVehiculo, GETDATE())
		UPDATE Bahia SET Disponible = 0 WHERE IdBahia = @idBahia
END