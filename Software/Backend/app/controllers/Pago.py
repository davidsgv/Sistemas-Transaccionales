from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

#Model
from app.model.Pago import Pago
from app.model.Usuario import ManejoUsuarios


pago = Blueprint('pago', __name__, url_prefix="/pago/")

@pago.route("list", methods=["POST"])
@cross_origin()
def getPagos():
    #se verifica si la sesion esta iniciada
    login = ManejoUsuarios.VerificarSesion()

    if(login):
        try:
            #se obetiene la lista de la personas
            data = Pago.listaPagos()
            return jsonify({"response": data,"message":"ok"})
        except:
            return jsonify({"message":"internal error"})
    
    return jsonify({"message":"invalid token"})