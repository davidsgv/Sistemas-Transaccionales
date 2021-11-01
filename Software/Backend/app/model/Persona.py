from app.model.Base import selectDB, insertBD


class Persona():
    @staticmethod
    def listaPersonas():
        data = selectDB("SELECT * FROM Persona")

        return recorrerResultados(data)

    @staticmethod
    def GetPersonaById(idPersona):
        query = "SELECT * FROM Persona WHERE IdPersona = {}".format(idPersona)
        data = selectDB(query)
        return recorrerResultados(data)

    @staticmethod
    def createPersona(nombre):
        insertBD("INSERT INTO Persona (Nombre) VALUES ('{}')".format(nombre))

def recorrerResultados(data):
    array = []
    for row in data:
        resultados = {}
        resultados.update({"IdPersona": row["IdPersona"]})
        resultados.update({"Nombre": row["Nombre"]})
        array.append(resultados)
    return array