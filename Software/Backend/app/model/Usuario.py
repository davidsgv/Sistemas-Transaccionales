from app.model.Base import selectDB, insertBD
from uuid import uuid4
from flask import request

class ManejoUsuarios():
    @staticmethod
    def IniciarSesion(correo, contrasena, navegador):
        #Verificar datos de usuario 
        query = "EXEC dbo.spVerificarDatosUsuario @correo = '{}', @clave = '{}'".format(correo, contrasena)
        data = selectDB(query)

        results = recorrerDatos(data)

        if len(results) <= 0:
            return 0

        
        #generar token
        token = uuid4()
        query = "EXEC dbo.spCrearSesion @correo = '{}', @navegador = '{}', @token = '{}'".format(correo,navegador, token)
        insertBD(query)
        
        return token

    def VerificarSesion():
        try:
            token = request.json["token"]
        except:
            return False
        #verificar token de usuario
        query = "EXEC spVerificarSesionToken @token = '{}'".format(token)
        data = selectDB(query)
        
        results = recorrerDatos(data)
        
        if len(results) <= 0:
            return False
        
        return True

def recorrerDatos(data):
    results = []
    for row in data:
        results.append(row)
    return results
