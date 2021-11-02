from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

#Model
from app.model.Parqueadero import Parqueadero
from app.model.Usuario import ManejoUsuarios


parqueadero = Blueprint('parqueadero', __name__, url_prefix="/parqueadero/")

@parqueadero.route("list", methods=["POST"])
@cross_origin()
def getParqueaderos():
    #se verifica si la sesion esta iniciada
    login = ManejoUsuarios.VerificarSesion()

    if(login):
        #se obetiene la lista de la personas
        data = Parqueadero.listaParqueaderos()
        return jsonify({"response":data,"message":"ok"})
    
    return jsonify({"message":"invalid token"})


@parqueadero.route("", methods=["POST"])
@cross_origin()
def getParqueaderoById():
    #se verifica si la sesion esta iniciada
    login = ManejoUsuarios.VerificarSesion()

    if(login):
        try:
            parqueaderoId = request.json["idParqueadero"]
        except:
            return jsonify({"message":"Incorrec format Json"})

        try:
            #se obetiene la lista de la personas
            data = Parqueadero.GetParqueaderoById(parqueaderoId)
            return jsonify({"response":data,"message":"ok"})
        except:
            return jsonify({"message":"internal error"})
    
    return jsonify({"message":"invalid token"})


@parqueadero.route("direccion", methods=["POST"])
@cross_origin()
def getParqueaderoByDireccion():
    #se verifica si la sesion esta iniciada
    login = ManejoUsuarios.VerificarSesion()

    if(login):
        try:
            parqueaderoDireccion = request.json["direccion"]
        except:
            return jsonify({"message":"Incorrec format Json"})

        try:
            #se obetiene la lista de la personas
            data = Parqueadero.GetParqueaderoByDireccion(parqueaderoDireccion)
            return jsonify({"response":data,"message":"ok"})
        except:
            return jsonify({"message":"internal error"})
    
    return jsonify({"message":"invalid token"})

@parqueadero.route("create", methods=["POST"])
@cross_origin()
def createParqueadero():
    #se verifica si la sesion esta iniciada
    login = ManejoUsuarios.VerificarSesion()

    if(login):
        try:
            nombre = request.json["nombre"]
            direccion = request.json["direccion"]
        except:
            return jsonify({"message":"Incorrec format Json"})

        try:
            #se obetiene la lista de la personas
            Parqueadero.createParqueadero(nombre, direccion)
            return jsonify({"message":"ok"})
        except:
            return jsonify({"message":"internal error"})
    
    return jsonify({"message":"invalid token"})