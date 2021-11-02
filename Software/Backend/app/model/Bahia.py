from app.model.Base import selectDB, insertBD


class Bahia():
    @staticmethod
    def listaBahiasParqueadero(idParqueadero):
        data = selectDB("EXEC spConsultarBahias @idParqueadero = {}".format(idParqueadero))

        return recorrerResultados(data)

    @staticmethod
    def createBahia(idParqueadero,cantidad):
        query = "EXEC spCrearBahia @idParqueadero = {}, @cantidad = {}".format(idParqueadero, cantidad)
        insertBD(query)

def recorrerResultados(data):
    array = []
    for row in data:
        resultados = {}
        resultados.update({"IdBahia": row["IdBahia"]})
        resultados.update({"IdParqueadero": row["IdParqueadero"]})
        resultados.update({"Disponible": row["Disponible"]})
        array.append(resultados)
    return array