from app.model.Base import selectDB, insertBD


class TipoVehiculo():
    @staticmethod
    def listaTipos():
        data = selectDB("EXEC spConsultarTiposVehiculo")
        return recorrerResultados(data)

    @staticmethod
    def createTipo(nombre):
        query = "EXEC spCrearTiposVehiculo @clase = '{}'".format(nombre)
        insertBD(query)

def recorrerResultados(data):
    array = []
    for row in data:
        resultados = {}
        resultados.update({"IdTipo": row["IdTipo"]})
        resultados.update({"Clase": row["Clase"]})
        array.append(resultados)
    return array