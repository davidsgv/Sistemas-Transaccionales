from flask import Blueprint, jsonify, request

#Model
from app.model.Persona import Persona
from app.model.Usuario import ManejoUsuarios



persona = Blueprint('persona', __name__, url_prefix="/persona/")

#listar todas las Personas
@persona.route("list")
def getPersona():
    #se verifica si la sesion esta iniciada
    login = ManejoUsuarios.VerificarSesion()

    if(login):
        #se obetiene la lista de la personas
        data = Persona.listaPersonas()
        return jsonify({"response":data,"message":"ok"})
    
    return jsonify({"message":"invalid token"})

#Obtener persona
@persona.route("")
def getPersonaById():
    #se verifica si la sesion esta iniciada
    login = ManejoUsuarios.VerificarSesion()

    if(login):
        try:
            personaId = request.json["idPersona"]
        except:
            return jsonify({"message":"invalid token"})

        try:
            data = Persona.GetPersonaById(personaId)
            return jsonify({"response":data,"message":"ok"})
        except:
            return jsonify({"message":"error"})
    
    return jsonify({"message":"invalid token"})

#Crear persona
@persona.route("create", methods=["POST"])
def createPersona():
    #se verifica si la sesion esta iniciada
    login = ManejoUsuarios.VerificarSesion()

    if(login):
        try:
            nombre = request.json["nombre"]
        except:
            return jsonify({"message":"invalid token"})

        try:
            Persona.createPersona(nombre)
            return jsonify({"message":"ok"})
        except:
            return jsonify({"message":"error"})
    
    return jsonify({"message":"invalid token"})