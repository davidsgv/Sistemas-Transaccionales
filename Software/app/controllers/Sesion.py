from flask import Blueprint, jsonify, request
from app.model.Usuario import ManejoUsuarios

sesion = Blueprint('sesion', __name__, url_prefix="/sesion/")

@sesion.route("login", methods=["POST"])
def login():
    try:
        correo = request.json["correo"]
        contrasena = request.json["password"]
        cliente = request.json["cliente"]
    except:
        return jsonify({"message":"Incorrec format Json"})

    try:
        data = ManejoUsuarios.IniciarSesion(correo, contrasena, cliente)
        return jsonify({"response":data,"message":"ok"})
    except:
        return jsonify({"message":"Internal error"})