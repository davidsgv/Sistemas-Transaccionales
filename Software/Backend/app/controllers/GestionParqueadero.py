from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

#Model
from app.model.GestionParqueadero import GestionParqueadero
from app.model.Usuario import ManejoUsuarios


gestionParqueadero = Blueprint('gestionParqueadero', __name__, url_prefix="/gestionParqueadero/")

@gestionParqueadero.route("ingresarvehiculo", methods=["POST"])
@cross_origin()
def ingresarVehiculo():
    #se verifica si la sesion esta iniciada
    login = ManejoUsuarios.VerificarSesion()

    if(login):
        try:
            idBahia = request.json["idBahia"]
            idVehiculo = request.json["idVehiculo"]
        except:
            return jsonify({"message":"Incorrec format Json"})
        
        try:
            #se obetiene la lista de la personas
            GestionParqueadero.ingresarVehiculo(idBahia, idVehiculo)
            return jsonify({"message":"ok"})
        except:
            return jsonify({"message":"internal error"})

    return jsonify({"message":"invalid token"})

@gestionParqueadero.route("salidavehiculo", methods=["POST"])
@cross_origin()
def salidaVehiculo():
    #se verifica si la sesion esta iniciada
    login = ManejoUsuarios.VerificarSesion()

    if(login):
        try:
            idVehiculo = request.json["idVehiculo"]
        except:
            return jsonify({"message":"Incorrec format Json"})
        
        try:
            #se obetiene la lista de la personas
            GestionParqueadero.salidaVehiculo(idVehiculo)
            return jsonify({"message":"ok"})
        except:
            return jsonify({"message":"internal error"})

    return jsonify({"message":"invalid token"})