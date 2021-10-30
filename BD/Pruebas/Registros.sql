--DELETE FROM Persona;
--DELETE FROM TipoVehiculo;

INSERT INTO Persona 
		(Nombre) 
	VALUES 
		('David');


INSERT INTO TipoVehiculo 
		(Clase) 
	VALUES 
		('A');
INSERT INTO Tarifa 
		(Costo, idTipo) 
	Values
		(1000, 1);
INSERT INTO Vehiculo
		(Marca, idPersona, idTipo)
	Values
		('Audi',1,1);
INSERT INTO Parqueadero
		(Nombre, Ubicacion)
	VALUES
		('Centro plaza','Calle 128 #7-58');
INSERT INTO Bahia
		(idParqueadero, disponible)
	VALUES
		(1,0);
INSERT INTO Pago
		(idBahia, idVehiculo, Tiempo, Costo, Fecha)
	VALUES (1,1,10,10000,'2021-10-25')


SELECT * 
FROM Persona;
SELECT * 
FROM TipoVehiculo;
SELECT * 
FROM Tarifa;
SELECT * 
FROM Vehiculo;
SELECT * 
FROM Parqueadero;
SELECT * 
FROM Bahia;
SELECT * 
FROM Pago;