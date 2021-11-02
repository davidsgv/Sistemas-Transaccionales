from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

#Model
from app.model.TipoVehiculo import TipoVehiculo
from app.model.Usuario import ManejoUsuarios


tipo = Blueprint('Tipo', __name__, url_prefix="/tipo/")

@tipo.route("list", methods=["POST"])
@cross_origin()
def gettipos():
    #se verifica si la sesion esta iniciada
    login = ManejoUsuarios.VerificarSesion()

    if(login):
        try:
            #se obetiene la lista de la personas
            data = TipoVehiculo.listaTipos()
            return jsonify({"response":data,"message":"ok"})
        except:
            return jsonify({"message":"internal error"})
    
    return jsonify({"message":"invalid token"})

@tipo.route("create", methods=["POST"])
@cross_origin()
def createTipo():
    #se verifica si la sesion esta iniciada
    login = ManejoUsuarios.VerificarSesion()

    if(login):
        try:
            clase = request.json["clase"]
        except: 
            return jsonify({"message":"Incorrec format Json"})
        
        try:
            TipoVehiculo.createTipo(clase)
        except:
            return jsonify({"message":"internal error"})

        return jsonify({"message":"ok"})
    
    return jsonify({"message":"invalid token"})