--CREATE LOGIN transaccionales   
--    WITH PASSWORD = '340$Uuxwp7Mcxo7Khy';
CREATE USER transaccionalesUser for login transaccionales;
GO

USE Parqueadero
GO
exec sp_addrolemember 'db_owner', 'transaccionalesUser'