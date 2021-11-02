from app.model.Base import selectDB, insertBD


class GestionParqueadero():
    @staticmethod
    def ingresarVehiculo(idBahia, idVehiculo):
        data = insertBD("EXEC spRegistrarVehiculo @idBahia = {}, @idVehiculo = {}".format(idBahia, idVehiculo))

    @staticmethod
    def salidaVehiculo(idVehiculo):
        query = "EXEC spSalidaVehiculo @idVehiculo = {}".format(idVehiculo)
        insertBD(query)
