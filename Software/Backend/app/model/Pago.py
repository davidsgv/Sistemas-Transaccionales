from app.model.Base import selectDB, insertBD


class Pago():
    @staticmethod
    def listaPagos():
        data = selectDB("SELECT * FROM Pago")
        return recorrerResultados(data)

def recorrerResultados(data):
    array = []
    for row in data:
        resultados = {}
        resultados.update({"IdPago": row["IdPago"]})
        resultados.update({"IdBahia": row["IdBahia"]})
        resultados.update({"IdVehiculo": row["IdVehiculo"]})
        resultados.update({"Tiempo": row["Tiempo"]})
        resultados.update({"Costo": int(row["Costo"])})
        resultados.update({"Fecha": row["Fecha"]})
        array.append(resultados)
    return array