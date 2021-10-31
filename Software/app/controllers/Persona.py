from flask import Blueprint, jsonify, request

#Model
from app.model.Persona import Persona


persona = Blueprint('persona', __name__, url_prefix="/persona/")

#listar todas las ciudades Personas
@persona.route("list")
def getPersona():
    data = Persona.listaPersonas()
    return jsonify({"reponse":data,"message":"ok"})

#Obtener persona
@persona.route("")
def getPersonaById():
    try:
        personaId = request.json["idPersona"]
        data = Persona.GetPersonaById(personaId)
        return jsonify({"reponse":data,"message":"ok"})
    except:
        return jsonify({"message":"error"})

#Crear persona
@persona.route("create", methods=["POST"])
def createPersona():
    try:
        Persona.createPersona(request.json["nombre"])
        print("------------------------------------------")
        return jsonify({"message":"ok"})
    except:
        return jsonify({"message":"error"})