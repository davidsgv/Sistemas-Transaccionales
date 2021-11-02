from app.model.Base import selectDB, insertBD


class Parqueadero():
    @staticmethod
    def listaParqueaderos():
        data = selectDB("EXEC spConsultarParqueaderos")

        return recorrerResultados(data)

    @staticmethod
    def GetParqueaderoById(idParqueadero):
        query = "EXEC spConsultarParqueaderos @idParqueadero = {}".format(idParqueadero)
        data = selectDB(query)
        return recorrerResultados(data)

    @staticmethod
    def GetParqueaderoByDireccion(direccion):
        query = "EXEC spConsultarParqueaderoByDireccion @direccion = '{}'".format(direccion)
        data = selectDB(query)
        return recorrerResultados(data)

    @staticmethod
    def createParqueadero(nombre, ubicacion):
        insertBD("EXEC spCrearParqueadero @nombre = '{}', @ubicacion = '{}'".format(nombre,ubicacion))

def recorrerResultados(data):
    array = []
    for row in data:
        resultados = {}
        resultados.update({"IdParqueadero": row["IdParqueadero"]})
        resultados.update({"Nombre": row["Nombre"]})
        resultados.update({"Ubicacion": row["Ubicacion"]})
        array.append(resultados)
    return array