from app.model.Base import select_db


class Persona():
    @staticmethod
    def listaPersonas():
        data = select_db("SELECT * FROM Persona")

        return recorrerResultados(data)

    @staticmethod
    def GetPersonaById(idPersona):
        query = "SELECT * FROM Persona WHERE IdPersona = {}".format(idPersona)
        data = select_db(query)
        return recorrerResultados(data)

    @staticmethod
    def createPersona(nombre):
        select_db("INSERT INTO Persona (Nombre) VALUES ('{}')".format(nombre))

def recorrerResultados(data):
    array = []
    for row in data:
        resultados = {}
        resultados.update({"IdPersona": row["IdPersona"]})
        resultados.update({"Nombre": row["Nombre"]})
        array.append(resultados)
    return array