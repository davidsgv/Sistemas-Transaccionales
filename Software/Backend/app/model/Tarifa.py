from app.model.Base import selectDB, insertBD


class Tarifa():
    @staticmethod
    def listaTarifas():
        data = selectDB("SELECT * FROM Tarifa")
        return recorrerResultados(data)

    @staticmethod
    def createTarifa(costo, idTipo):
        query = "INSERT INTO Tarifa (Costo, IdTipo) VALUES ({},{})".format(costo, idTipo)
        insertBD(query)

def recorrerResultados(data):
    array = []
    for row in data:
        resultados = {}
        resultados.update({"IdTarifa": row["IdTarifa"]})
        resultados.update({"Costo": int(row["Costo"]) })
        resultados.update({"IdTipo": row["IdTipo"]})
        array.append(resultados)
    return array