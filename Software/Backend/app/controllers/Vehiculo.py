from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

#Model
from app.model.Vehiculo import Vehiculo
from app.model.Usuario import ManejoUsuarios



vehiculo = Blueprint('vehiculo', __name__, url_prefix="/vehiculo/")

@vehiculo.route("list", methods=["POST"])
@cross_origin()
def getVehiculo():
    #se verifica si la sesion esta iniciada
    login = ManejoUsuarios.VerificarSesion()

    if(login):
        try:
            idPersona = request.json["idPersona"]
        except:
            return jsonify({"message":"Incorrec format Json"})

        try:
            data = Vehiculo.listaVehiculos(idPersona)
            return jsonify({"response":data,"message":"ok"})
        except:
            return jsonify({"message":"internal error"})
    
    return jsonify({"message":"invalid token"})

@vehiculo.route("create", methods=["POST"])
@cross_origin()
def createVehiculo():
    #se verifica si la sesion esta iniciada
    login = ManejoUsuarios.VerificarSesion()

    if(login):
        try:
            marca = request.json["marca"]
            idPersona = request.json["idPersona"]
            idTipo = request.json["idTipo"]
        except:
            return jsonify({"message":"Incorrec format Json"})

        try:
            Vehiculo.createVehiculo(marca, idPersona, idTipo)
            return jsonify({"message":"ok"})
        except:
            return jsonify({"message":"internal error"})
    
    return jsonify({"message":"invalid token"})