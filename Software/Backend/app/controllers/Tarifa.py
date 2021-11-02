from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

#Model
from app.model.Tarifa import Tarifa
from app.model.Usuario import ManejoUsuarios



tarifa = Blueprint('tarifa', __name__, url_prefix="/tarifa/")

@tarifa.route("list", methods=["POST"])
@cross_origin()
def getTarifa():
    #se verifica si la sesion esta iniciada
    login = ManejoUsuarios.VerificarSesion()

    if(login):
        try:
            data = Tarifa.listaTarifas()
            return jsonify({"response":data,"message":"ok"})
        except:
            return jsonify({"message":"internal error"})
    
    return jsonify({"message":"invalid token"})

@tarifa.route("create", methods=["POST"])
@cross_origin()
def createPersona():
    #se verifica si la sesion esta iniciada
    login = ManejoUsuarios.VerificarSesion()

    if(login):
        try:
            costo = request.json["costo"]
            idTipo = request.json["idTipo"]
        except:
            return jsonify({"message":"Incorrec format Json"})

        try:
            Tarifa.createTarifa(costo, idTipo)
            return jsonify({"message":"ok"})
        except:
            return jsonify({"message":"internal error"})
    
    return jsonify({"message":"invalid token"})