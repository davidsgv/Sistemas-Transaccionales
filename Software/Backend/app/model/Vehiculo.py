from app.model.Base import selectDB, insertBD


class Vehiculo():
    @staticmethod
    def listaVehiculos(idPersona):
        data = selectDB("SELECT * FROM Vehiculo")
        return recorrerResultados(data)

    @staticmethod
    def createVehiculo(marca, idPersona, idTipo):
        query = "EXEC spCrearVehiculo @Marca = '{}', @IdPersona = {}, @IdTipo = {}".format(marca, idPersona, idTipo)
        insertBD(query)
    
def recorrerResultados(data):
    array = []
    for row in data:
        resultados = {}
        resultados.update({"IdVehiculo": row["IdVehiculo"]})
        resultados.update({"Marca": row["Marca"]})
        resultados.update({"IdPersona": row["IdPersona"]})
        resultados.update({"IdTipo": row["IdTipo"]})
        array.append(resultados)
    return array
