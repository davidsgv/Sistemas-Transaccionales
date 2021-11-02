from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

#Model
from app.model.Bahia import Bahia
from app.model.Usuario import ManejoUsuarios


bahia = Blueprint('Bahia', __name__, url_prefix="/bahia/")

@bahia.route("list", methods=["POST"])
@cross_origin()
def getBahias():
    #se verifica si la sesion esta iniciada
    login = ManejoUsuarios.VerificarSesion()

    if(login):
        try:
            idParqueadero = request.json["idParqueadero"]
        except:
            return jsonify({"message":"Incorrec format Json"})

        #se obetiene la lista de la personas
        data = Bahia.listaBahiasParqueadero(idParqueadero)
        return jsonify({"response":data,"message":"ok"})
    
    return jsonify({"message":"invalid token"})


@bahia.route("create", methods=["POST"])
@cross_origin()
def createBahia():
    #se verifica si la sesion esta iniciada
    login = ManejoUsuarios.VerificarSesion()

    if(login):
        try:
            idParqueadero = request.json["idParqueadero"]
        except: 
            return jsonify({"message":"Incorrec format Json"})
        
        try:
            cantidad = request.json["cantidad"]
            Bahia.createBahia(idParqueadero, cantidad)    
        except:
            Bahia.createBahia(idParqueadero, 1)

        return jsonify({"message":"ok"})
    
    return jsonify({"message":"invalid token"})